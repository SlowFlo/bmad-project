"""La recherche exacte : égalité stricte de niveau, exclusions, clé de sport (CAP-5).

Les règles s'éprouvent contre un **faux port en mémoire** : c'est ce que gagne un port
qui rétrécit sans filtrer — aucune base n'est nécessaire pour prouver qu'un niveau
inconnu ou un profil sorti du vivier n'est jamais rendu. Les repères de mise au point
— « Tennis, mardi, débutant » rend Emma Leroy — s'éprouvent, eux, contre le vivier
d'amorçage réel, seul endroit où ces noms veulent dire quelque chose.
"""

from __future__ import annotations

import ast
import datetime as dt
import inspect
import textwrap
from collections.abc import Mapping, Sequence
from pathlib import Path
from uuid import UUID

import pytest
from sqlalchemy import Engine, event, text
from sqlalchemy.orm import Session

from exaequo.adaptateurs.secondaires.persistance.depots import DepotSports, DepotVivier
from exaequo.adaptateurs.secondaires.persistance.modeles import (
    JourDisponibleORM,
    ProfilORM,
    SportORM,
)
from exaequo.domaine import recherche
from exaequo.domaine.identifiants import nouvel_identifiant
from exaequo.domaine.ports import PortVivier
from exaequo.domaine.recherche import ResultatRecherche, chercher_candidats_exacts
from exaequo.domaine.vivier import JourSemaine, Niveau, Population, Profil

RACINE_DU_PROJET = Path(__file__).resolve().parents[1]

#: Ce qu'aucun chemin de **lecture** n'a le droit d'appeler. Les trois consultent la
#: table de synonymes, qui ne redirige qu'à l'écriture (AD-5) : `synonymes()` est
#: elle-même une lecture, mais une lecture *de cette table-là*, et c'est cette
#: consultation qui est interdite ici — pas l'écriture en général.
CONSULTATIONS_DE_SYNONYMES_INTERDITES = (
    "synonymes",
    "resoudre_libelle",
    "resoudre_a_l_ecriture",
)


class VivierEnMemoire:
    """Un faux `PortVivier` : il rétrécit par la clé de sport, et ne filtre rien.

    Il porte sa **propre correspondance clé → profils**, comme la base porte la
    sienne par la table `sport` : un profil garde donc son `libelle_sport` d'origine
    — « Tennis », tel que la personne l'a dit — et le faux ne s'en sert jamais pour
    rétrécir. C'est l'invariant AD-5 que ces tests protègent : un faux qui
    apparierait sur le libellé le contredirait au moment même de le vérifier.

    Il rend les profils dans l'ordre où on les lui a donnés — l'ordre du vivier — et
    n'écarte ni le niveau inconnu, ni la sortie du vivier : c'est le contrat du port,
    et c'est ce qui met les exclusions à la charge du domaine.
    """

    def __init__(self, profils_par_cle: Mapping[str, Sequence[Profil]]) -> None:
        self._par_cle = {
            cle: list(profils) for cle, profils in profils_par_cle.items()
        }
        self.cles_demandees: list[str] = []

    def profils_du_sport(self, cle_sport: str) -> Sequence[Profil]:
        self.cles_demandees.append(cle_sport)
        return list(self._par_cle.get(cle_sport, []))


def _vivier_de_tennis(*profils: Profil) -> VivierEnMemoire:
    """Un faux vivier dont la seule clé est `tennis`, libellée « Tennis »."""
    return VivierEnMemoire({"tennis": profils})


def _profil(
    *,
    prenom: str,
    libelle_sport: str = "Tennis",
    jours: Sequence[JourSemaine] = (JourSemaine.MARDI,),
    niveau: Niveau | None = Niveau.DEBUTANT,
    sortie_vivier_le: dt.datetime | None = None,
    identifiant: UUID | None = None,
) -> Profil:
    """Un profil de test.

    `libelle_sport` porte le **libellé d'affichage**, distinct de la clé : c'est ce
    que la base porte réellement, et rien du chemin de recherche n'a le droit de s'en
    servir pour apparier.
    """
    return Profil(
        id=identifiant or nouvel_identifiant(),
        prenom=prenom,
        population=Population.AMORCAGE,
        sport_id=nouvel_identifiant(),
        libelle_sport=libelle_sport,
        jours_disponibles=frozenset(jours),
        niveau=niveau,
        sortie_vivier_le=sortie_vivier_le,
    )


def _prenoms(resultat: ResultatRecherche) -> list[str]:
    return [candidat.prenom for candidat in resultat.candidats]


def _instructions_de(session: Session, appel) -> list[tuple[str, object]]:
    """Le SQL réellement envoyé au pilote pendant `appel`.

    On écoute le moteur plutôt que de recomposer la requête dans le test : c'est la
    requête de production qui est éprouvée, et non une copie qui dériverait d'elle.
    """
    instructions: list[tuple[str, object]] = []

    def enregistrer(conn, cursor, statement, parameters, context, executemany):
        instructions.append((statement, parameters))

    event.listen(Engine, "before_cursor_execute", enregistrer)
    try:
        appel()
    finally:
        event.remove(Engine, "before_cursor_execute", enregistrer)
    return instructions


def _requete_des_profils_du_sport(
    session: Session, cle: str = "tennis"
) -> tuple[str, object]:
    """La requête que `profils_du_sport` envoie pour joindre `profil` à `sport`.

    `_vers_profil` en déclenche d'autres — une par profil, pour ses jours — dont on
    ne veut pas ici.
    """
    instructions = _instructions_de(
        session, lambda: DepotVivier(session).profils_du_sport(cle)
    )
    jointures = [
        (sql, parametres)
        for sql, parametres in instructions
        if "FROM profil" in sql and "JOIN sport" in sql
    ]
    assert len(jointures) == 1, f"attendu une seule jointure, vu {len(jointures)}"
    return jointures[0]


def _plan_de(session: Session, sql: str, parametres: object) -> str:
    """Le `EXPLAIN QUERY PLAN` de SQLite, en une seule chaîne lisible."""
    brut = session.connection().connection.driver_connection
    lignes = brut.execute("EXPLAIN QUERY PLAN " + sql, parametres).fetchall()
    return " | ".join(ligne[3] for ligne in lignes)


# --- Les règles, contre un faux port -----------------------------------------------


def test_seul_le_niveau_demande_est_rendu() -> None:
    vivier = _vivier_de_tennis(
        _profil(prenom="Debutante", niveau=Niveau.DEBUTANT),
        _profil(prenom="Intermediaire", niveau=Niveau.INTERMEDIAIRE),
        _profil(prenom="Avancee", niveau=Niveau.AVANCE),
    )

    resultat = chercher_candidats_exacts(
        vivier,
        libelle_sport="Tennis",
        jour=JourSemaine.MARDI,
        niveau=Niveau.DEBUTANT,
    )

    assert _prenoms(resultat) == ["Debutante"]
    assert all(candidat.niveau is Niveau.DEBUTANT for candidat in resultat.candidats)


def test_un_niveau_inconnu_n_est_jamais_rendu() -> None:
    """Le niveau inconnu est une **absence**, jamais une quatrième valeur."""
    vivier = _vivier_de_tennis(
        _profil(prenom="Sans niveau", niveau=None),
        _profil(prenom="Emma", niveau=Niveau.DEBUTANT),
    )

    resultat = chercher_candidats_exacts(
        vivier,
        libelle_sport="Tennis",
        jour=JourSemaine.MARDI,
        niveau=Niveau.DEBUTANT,
    )

    assert _prenoms(resultat) == ["Emma"]


def test_un_profil_sorti_du_vivier_n_est_jamais_rendu() -> None:
    vivier = _vivier_de_tennis(
        _profil(
            prenom="Partie",
            sortie_vivier_le=dt.datetime(2026, 8, 30, 12, 0, tzinfo=dt.UTC),
        ),
        _profil(prenom="Emma"),
    )

    resultat = chercher_candidats_exacts(
        vivier,
        libelle_sport="Tennis",
        jour=JourSemaine.MARDI,
        niveau=Niveau.DEBUTANT,
    )

    assert _prenoms(resultat) == ["Emma"]


def test_le_demandeur_n_est_jamais_son_propre_partenaire() -> None:
    demandeur = _profil(prenom="Moi")
    vivier = _vivier_de_tennis(demandeur, _profil(prenom="Emma"))

    resultat = chercher_candidats_exacts(
        vivier,
        libelle_sport="Tennis",
        jour=JourSemaine.MARDI,
        niveau=Niveau.DEBUTANT,
        demandeur_id=demandeur.id,
    )

    assert _prenoms(resultat) == ["Emma"]


def test_sans_demandeur_aucun_profil_n_est_ecarte_a_ce_titre() -> None:
    """`demandeur_id=None` n'écarte personne : un visiteur sans profil cherche aussi."""
    vivier = _vivier_de_tennis(_profil(prenom="Emma"), _profil(prenom="Margot"))

    resultat = chercher_candidats_exacts(
        vivier,
        libelle_sport="Tennis",
        jour=JourSemaine.MARDI,
        niveau=Niveau.DEBUTANT,
    )

    assert _prenoms(resultat) == ["Emma", "Margot"]


def test_un_profil_sans_aucun_jour_declare_n_est_jamais_rendu() -> None:
    vivier = _vivier_de_tennis(
        _profil(prenom="Sans jour", jours=()), _profil(prenom="Emma")
    )

    resultat = chercher_candidats_exacts(
        vivier,
        libelle_sport="Tennis",
        jour=JourSemaine.MARDI,
        niveau=Niveau.DEBUTANT,
    )

    assert _prenoms(resultat) == ["Emma"]


def test_le_jour_demande_doit_etre_declare_disponible() -> None:
    vivier = _vivier_de_tennis(
        _profil(prenom="Emma", jours=(JourSemaine.MARDI, JourSemaine.JEUDI)),
        _profil(prenom="Margot", jours=(JourSemaine.LUNDI, JourSemaine.VENDREDI)),
    )

    resultat = chercher_candidats_exacts(
        vivier,
        libelle_sport="Tennis",
        jour=JourSemaine.MARDI,
        niveau=Niveau.DEBUTANT,
    )

    assert _prenoms(resultat) == ["Emma"]


def test_un_jour_indisponible_ecarte_ce_jour_la_et_lui_seul() -> None:
    """Le blocage porte sur un couple *(profil, jour)*, jamais sur le profil entier."""
    emma = _profil(prenom="Emma", jours=(JourSemaine.MARDI, JourSemaine.JEUDI))
    vivier = _vivier_de_tennis(emma)
    bloque_le_mardi = frozenset({(emma.id, JourSemaine.MARDI)})

    mardi = chercher_candidats_exacts(
        vivier,
        libelle_sport="Tennis",
        jour=JourSemaine.MARDI,
        niveau=Niveau.DEBUTANT,
        jours_indisponibles=bloque_le_mardi,
    )
    jeudi = chercher_candidats_exacts(
        vivier,
        libelle_sport="Tennis",
        jour=JourSemaine.JEUDI,
        niveau=Niveau.DEBUTANT,
        jours_indisponibles=bloque_le_mardi,
    )

    assert _prenoms(mardi) == []
    assert _prenoms(jeudi) == ["Emma"]


def test_le_blocage_ne_deborde_pas_sur_un_autre_profil() -> None:
    """Le couple porte l'identifiant : bloquer Emma ne bloque pas Margot."""
    emma = _profil(prenom="Emma")
    margot = _profil(prenom="Margot")
    vivier = _vivier_de_tennis(emma, margot)

    resultat = chercher_candidats_exacts(
        vivier,
        libelle_sport="Tennis",
        jour=JourSemaine.MARDI,
        niveau=Niveau.DEBUTANT,
        jours_indisponibles=frozenset({(emma.id, JourSemaine.MARDI)}),
    )

    assert _prenoms(resultat) == ["Margot"]


def test_les_jours_indisponibles_sont_vides_par_defaut() -> None:
    """Le paramètre est inerte tant qu'E5 n'y branche pas la dérivation (AD-6).

    Le défaut est un `frozenset` et **non** un `set` : `set() == frozenset()` est
    vrai, si bien qu'une égalité seule laisserait passer le défaut mutable — partagé
    entre tous les appels, et qu'un appelant pourrait peupler pour tout le processus.
    """
    defaut = inspect.signature(chercher_candidats_exacts).parameters[
        "jours_indisponibles"
    ].default

    assert defaut == frozenset()
    assert type(defaut) is frozenset


def test_l_ordre_du_vivier_est_preserve_tel_quel() -> None:
    """Le domaine ne retrie rien : il ne fait que retrancher."""
    vivier = _vivier_de_tennis(
        *(_profil(prenom=prenom) for prenom in ("Un", "Deux", "Trois", "Quatre"))
    )

    resultat = chercher_candidats_exacts(
        vivier,
        libelle_sport="Tennis",
        jour=JourSemaine.MARDI,
        niveau=Niveau.DEBUTANT,
    )

    assert _prenoms(resultat) == ["Un", "Deux", "Trois", "Quatre"]


@pytest.mark.parametrize("libelle", ["tennis", "Tennis", "  TENNIS  ", "TÉNNIS"])
def test_la_comparaison_porte_sur_la_cle_de_sport_normalisee(libelle: str) -> None:
    """Trois graphies d'un même sport rendent le même ensemble (AD-5)."""
    vivier = _vivier_de_tennis(_profil(prenom="Emma"))

    resultat = chercher_candidats_exacts(
        vivier,
        libelle_sport=libelle,
        jour=JourSemaine.MARDI,
        niveau=Niveau.DEBUTANT,
    )

    assert vivier.cles_demandees == ["tennis"]
    assert resultat.cle_sport == "tennis"
    assert _prenoms(resultat) == ["Emma"]


def test_le_libelle_d_affichage_ne_sert_jamais_a_apparier() -> None:
    """Le profil porte « Tennis » ; c'est la clé `tennis` qui l'a trouvé (AD-5)."""
    emma = _profil(prenom="Emma", libelle_sport="Tennis")
    vivier = _vivier_de_tennis(emma)

    resultat = chercher_candidats_exacts(
        vivier,
        libelle_sport="TENNIS",
        jour=JourSemaine.MARDI,
        niveau=Niveau.DEBUTANT,
    )

    assert emma.libelle_sport != resultat.cle_sport
    assert _prenoms(resultat) == ["Emma"]


def test_un_sport_inconnu_rend_un_resultat_vide_et_non_un_refus() -> None:
    vivier = _vivier_de_tennis(_profil(prenom="Emma"))

    resultat = chercher_candidats_exacts(
        vivier,
        libelle_sport="Squash",
        jour=JourSemaine.MARDI,
        niveau=Niveau.DEBUTANT,
    )

    assert resultat.candidats == ()
    assert resultat.cle_sport == "squash"


@pytest.mark.parametrize("libelle", ["", "   ", "\t\n"])
def test_un_libelle_vide_rend_un_resultat_vide_et_non_un_refus(libelle: str) -> None:
    """Un libellé vide ou blanc se replie en clé vide, qu'aucun sport ne porte.

    Le comportement voulu est celui d'un sport inconnu : un **vide**, jamais une
    exception — la conséquence conversationnelle appartient à E3.
    """
    vivier = _vivier_de_tennis(_profil(prenom="Emma"))

    resultat = chercher_candidats_exacts(
        vivier,
        libelle_sport=libelle,
        jour=JourSemaine.MARDI,
        niveau=Niveau.DEBUTANT,
    )

    assert resultat.cle_sport == ""
    assert resultat.candidats == ()
    assert vivier.cles_demandees == [""]


def test_le_resultat_porte_la_demande_a_laquelle_il_repond() -> None:
    """E3 y lit le niveau commun du groupe, dit une fois et jamais par candidat."""
    vivier = _vivier_de_tennis(_profil(prenom="Emma"))

    resultat = chercher_candidats_exacts(
        vivier,
        libelle_sport="  TENNIS  ",
        jour=JourSemaine.MARDI,
        niveau=Niveau.DEBUTANT,
    )

    assert (resultat.cle_sport, resultat.jour, resultat.niveau) == (
        "tennis",
        JourSemaine.MARDI,
        Niveau.DEBUTANT,
    )


def test_le_resultat_est_gele() -> None:
    resultat = chercher_candidats_exacts(
        VivierEnMemoire({}),
        libelle_sport="Tennis",
        jour=JourSemaine.MARDI,
        niveau=Niveau.DEBUTANT,
    )
    with pytest.raises(AttributeError):
        resultat.candidats = ()  # type: ignore[misc]


# --- Le refus des libellés à la place des membres d'énumération --------------------


def test_un_niveau_donne_en_chaine_est_refuse_bruyamment() -> None:
    """`"debutant"` rendrait **zéro candidat sans erreur** : un vide indiscernable.

    `Niveau` est un `StrEnum` : la chaîne se glisserait sans bruit, et l'égalité
    stricte — la promesse qui fonde le produit — deviendrait un silence.
    """
    vivier = _vivier_de_tennis(_profil(prenom="Emma"))

    with pytest.raises(TypeError, match="niveau"):
        chercher_candidats_exacts(
            vivier,
            libelle_sport="Tennis",
            jour=JourSemaine.MARDI,
            niveau="debutant",  # type: ignore[arg-type]
        )


def test_un_jour_donne_en_chaine_est_refuse_bruyamment() -> None:
    """`"mardi"` comparerait *juste par accident*, `JourSemaine` étant un `StrEnum`."""
    vivier = _vivier_de_tennis(_profil(prenom="Emma"))

    with pytest.raises(TypeError, match="jour"):
        chercher_candidats_exacts(
            vivier,
            libelle_sport="Tennis",
            jour="mardi",  # type: ignore[arg-type]
            niveau=Niveau.DEBUTANT,
        )


def test_le_refus_ne_convertit_rien_et_n_interroge_pas_le_vivier() -> None:
    """On refuse, on ne rattrape pas : le port n'est même pas appelé."""
    vivier = _vivier_de_tennis(_profil(prenom="Emma"))

    with pytest.raises(TypeError):
        chercher_candidats_exacts(
            vivier,
            libelle_sport="Tennis",
            jour=JourSemaine.MARDI,
            niveau="debutant",  # type: ignore[arg-type]
        )

    assert vivier.cles_demandees == []


def test_un_niveau_absent_est_refuse_comme_un_libelle() -> None:
    """`None` n'est pas « tous les niveaux » : c'est une absence, et elle est refusée."""
    with pytest.raises(TypeError, match="niveau"):
        chercher_candidats_exacts(
            VivierEnMemoire({}),
            libelle_sport="Tennis",
            jour=JourSemaine.MARDI,
            niveau=None,  # type: ignore[arg-type]
        )


# --- Les repères, contre le vivier d'amorçage --------------------------------------


def test_tennis_mardi_debutant_rend_emma_leroy(vivier_amorce: Session) -> None:
    """Le repère de CAP-5, sur les données d'amorçage réelles."""
    resultat = chercher_candidats_exacts(
        DepotVivier(vivier_amorce),
        libelle_sport="Tennis",
        jour=JourSemaine.MARDI,
        niveau=Niveau.DEBUTANT,
    )

    assert [(c.prenom, c.nom) for c in resultat.candidats] == [("Emma", "Leroy")]


def test_la_meme_demande_en_intermediaire_ne_rend_rien(vivier_amorce: Session) -> None:
    """La recherche exacte rend vide et **n'élargit jamais d'elle-même** (2.2)."""
    resultat = chercher_candidats_exacts(
        DepotVivier(vivier_amorce),
        libelle_sport="Tennis",
        jour=JourSemaine.MARDI,
        niveau=Niveau.INTERMEDIAIRE,
    )

    assert resultat.candidats == ()
    # Anna, Iris et Tessa existent bien : elles ne jouent simplement pas le mardi.
    # Les rendre serait l'élargissement de 2.2, qui n'appartient pas à ce lot.
    autres_jours = {
        candidat.prenom
        for jour in JourSemaine
        for candidat in chercher_candidats_exacts(
            DepotVivier(vivier_amorce),
            libelle_sport="Tennis",
            jour=jour,
            niveau=Niveau.INTERMEDIAIRE,
        ).candidats
    }
    assert {"Anna", "Iris", "Tessa"} <= autres_jours


@pytest.mark.parametrize("libelle", ["tennis", "Tennis", "  TENNIS  "])
def test_les_trois_graphies_rendent_le_meme_ensemble(
    vivier_amorce: Session, libelle: str
) -> None:
    resultat = chercher_candidats_exacts(
        DepotVivier(vivier_amorce),
        libelle_sport=libelle,
        jour=JourSemaine.MARDI,
        niveau=Niveau.DEBUTANT,
    )
    assert [candidat.prenom for candidat in resultat.candidats] == ["Emma"]


def test_un_sport_absent_du_vivier_rend_vide_sans_rien_ecrire(
    vivier_amorce: Session,
) -> None:
    """« Squash » n'est pas un refus, et ne **fonde** surtout aucun sport."""
    depot_sports = DepotSports(vivier_amorce)
    avant = depot_sports.compter()

    resultat = chercher_candidats_exacts(
        DepotVivier(vivier_amorce),
        libelle_sport="squash",
        jour=JourSemaine.MARDI,
        niveau=Niveau.DEBUTANT,
    )

    assert resultat.candidats == ()
    assert depot_sports.compter() == avant == 11
    assert depot_sports.par_cle("squash") is None


def test_un_profil_sorti_du_vivier_disparait_de_la_recherche(
    vivier_amorce: Session,
) -> None:
    """Bout en bout : la sortie du vivier est écartée par le domaine, pas par le SQL."""
    depot = DepotVivier(vivier_amorce)
    emma = depot.par_cle_amorcage("+33639980002")
    assert emma is not None

    vivier_amorce.execute(
        ProfilORM.__table__.update()
        .where(ProfilORM.id == emma.id)
        .values(sortie_vivier_le=dt.datetime(2026, 8, 30, 12, 0, tzinfo=dt.UTC))
    )
    vivier_amorce.commit()
    vivier_amorce.expire_all()

    # Le port rétrécit sans filtrer : Emma est toujours là, côté dépôt…
    assert emma.id in {p.id for p in depot.profils_du_sport("tennis")}
    # …et c'est le domaine qui l'écarte.
    resultat = chercher_candidats_exacts(
        depot,
        libelle_sport="Tennis",
        jour=JourSemaine.MARDI,
        niveau=Niveau.DEBUTANT,
    )
    assert resultat.candidats == ()


def test_la_recherche_ne_consulte_jamais_la_table_de_synonymes(
    vivier_amorce: Session,
) -> None:
    """Un synonyme posé vers le tennis ne fait rien rendre : il ne redirige qu'à
    l'écriture (AD-5)."""
    depot_sports = DepotSports(vivier_amorce)
    tennis = depot_sports.par_cle("tennis")
    assert tennis is not None
    depot_sports.poser_synonyme("tenis", tennis.id)
    vivier_amorce.commit()

    resultat = chercher_candidats_exacts(
        DepotVivier(vivier_amorce),
        libelle_sport="tenis",
        jour=JourSemaine.MARDI,
        niveau=Niveau.DEBUTANT,
    )

    assert resultat.candidats == ()


# --- Le contrat du port, contre la base --------------------------------------------


def test_le_depot_satisfait_le_port_du_vivier(vivier_amorce: Session) -> None:
    depot = DepotVivier(vivier_amorce)
    assert isinstance(depot, PortVivier)


def test_le_depot_rend_tous_les_profils_du_sport_sans_filtrer(
    vivier_amorce: Session,
) -> None:
    """Le port **rétrécit** : les neuf profils de tennis, tous niveaux confondus."""
    depot = DepotVivier(vivier_amorce)
    profils = depot.profils_du_sport("tennis")

    assert [profil.prenom for profil in profils] == [
        "Emma",
        "Jules",
        "Anna",
        "Lina",
        "Margot",
        "Iris",
        "Raphaël",
        "Mélina",
        "Tessa",
    ]
    # Les trois niveaux sont présents — sans exiger qu'il n'y ait *que* ceux-là : un
    # profil de niveau inconnu est lui aussi rendu par le port, comme l'éprouve
    # `test_le_port_rend_un_niveau_inconnu_que_le_domaine_ecarte`.
    assert {profil.niveau for profil in profils} >= set(Niveau)
    # Le profil porte le **libellé** d'affichage, jamais la clé qui l'a trouvé (AD-5).
    assert {profil.libelle_sport for profil in profils} == {"Tennis"}


def _poser_profil(
    session: Session,
    *,
    identifiant: UUID,
    prenom: str,
    sport_id: UUID,
    niveau: Niveau | None,
    jours: Sequence[JourSemaine] = (JourSemaine.MARDI,),
) -> None:
    """Écrit un profil directement, identifiant imposé.

    `DepotVivier.inserer_profil` tire lui-même un UUIDv7 : il ne permet donc pas de
    faire diverger l'ordre d'insertion de l'ordre des identifiants.
    """
    session.add(
        ProfilORM(
            id=identifiant,
            prenom=prenom,
            nom=None,
            population=Population.INSCRIT,
            sport_id=sport_id,
            libelle_sport="Tennis",
            niveau=niveau,
            telephone=None,
            provenance_numero=None,
            courriel=None,
            secteur=None,
            compte_id=None,
            cle_amorcage=None,
            cree_le=dt.datetime(2026, 8, 31, 9, 0, tzinfo=dt.UTC),
            derniere_activite=None,
            sortie_vivier_le=None,
        )
    )
    session.flush()
    for jour in jours:
        session.add(
            JourDisponibleORM(
                id=nouvel_identifiant(), profil_id=identifiant, jour=jour
            )
        )
    session.flush()


def test_le_port_rend_un_niveau_inconnu_que_le_domaine_ecarte(
    vivier_amorce: Session,
) -> None:
    """La frontière du contrat, éprouvée contre la **base** et non contre le faux.

    Aucun des 86 profils d'amorçage ne porte de niveau inconnu : sans ce profil posé
    ici, « le port ne filtre pas » ne serait vérifié que là où c'est le plus facile.
    """
    depot = DepotVivier(vivier_amorce)
    tennis = DepotSports(vivier_amorce).par_cle("tennis")
    assert tennis is not None

    sans_niveau = UUID("ffffffff-ffff-7fff-8fff-ffffffffffff")
    _poser_profil(
        vivier_amorce,
        identifiant=sans_niveau,
        prenom="Inconnue",
        sport_id=tennis.id,
        niveau=None,
    )
    vivier_amorce.commit()

    # Le port rétrécit et ne filtre pas : il la rend.
    rendus = depot.profils_du_sport("tennis")
    assert sans_niveau in {profil.id for profil in rendus}
    assert None in {profil.niveau for profil in rendus}

    # Le domaine, lui, l'écarte — à chacun des trois niveaux.
    for niveau in Niveau:
        resultat = chercher_candidats_exacts(
            depot,
            libelle_sport="Tennis",
            jour=JourSemaine.MARDI,
            niveau=niveau,
        )
        assert sans_niveau not in {candidat.id for candidat in resultat.candidats}


def test_le_depot_rend_les_profils_dans_l_ordre_du_vivier(
    vivier_amorce: Session,
) -> None:
    depot = DepotVivier(vivier_amorce)
    identifiants = [profil.id for profil in depot.profils_du_sport("tennis")]
    assert identifiants == sorted(identifiants)


def test_l_ordre_du_vivier_ne_depend_pas_de_l_ordre_d_insertion(
    session: Session,
) -> None:
    """L'ordre rendu est celui des **identifiants**, pas celui des lignes écrites.

    Sur les données d'amorçage les deux coïncident — les UUIDv7 sont monotones — et
    la coïncidence masquerait le retrait du `ORDER BY`. On écrit donc trois profils
    d'identifiants **décroissants**, de sorte que l'ordre physique des lignes soit
    l'inverse de l'ordre attendu.

    L'assertion sur le SQL émis accompagne celle sur le résultat, et c'est elle qui
    discrimine : l'index composite `(sport_id, id)` fait remonter les lignes déjà
    triées, si bien que le résultat seul ne distinguerait pas une requête privée de
    sa clause `ORDER BY`. La clause reste ce qui garantit l'ordre quel que soit le
    plan que SQLite retiendra demain — un index perdu, une table analysée.
    """
    sport_id = UUID("00000000-0000-7000-8000-00000000aaaa")
    session.add(
        SportORM(
            id=sport_id,
            cle="tennis",
            libelle="Tennis",
            cree_le=dt.datetime(2026, 8, 31, 9, 0, tzinfo=dt.UTC),
        )
    )
    session.flush()

    croissants = [
        UUID("00000000-0000-7000-8000-000000000001"),
        UUID("00000000-0000-7000-8000-000000000002"),
        UUID("00000000-0000-7000-8000-000000000003"),
    ]
    # Écriture à rebours : la ligne physiquement première porte le plus grand id.
    for rang, identifiant in enumerate(reversed(croissants), start=1):
        _poser_profil(
            session,
            identifiant=identifiant,
            prenom=f"Ecrite en {rang}",
            sport_id=sport_id,
            niveau=Niveau.DEBUTANT,
        )
    session.commit()

    rendus = [profil.id for profil in DepotVivier(session).profils_du_sport("tennis")]
    assert rendus == croissants

    sql, _ = _requete_des_profils_du_sport(session)
    assert "ORDER BY profil.id" in sql


def test_le_depot_rend_vide_sur_une_cle_inconnue(vivier_amorce: Session) -> None:
    assert DepotVivier(vivier_amorce).profils_du_sport("squash") == []


# --- Les trois critères d'acceptation ----------------------------------------------


def test_l_index_sur_la_cle_de_sport_existe_apres_creation_du_schema(
    moteur: Engine,
) -> None:
    """DW-1 : sans lui, SQLite balaie `profil` à chaque recherche — et 2.4 en fait 231."""
    with moteur.connect() as connexion:
        index = {
            ligne[1] for ligne in connexion.execute(text("PRAGMA index_list(profil)"))
        }
    assert "ix_profil_sport_id" in index


def test_l_index_porte_la_cle_de_sport_puis_l_identifiant(moteur: Engine) -> None:
    """Composite et dans cet ordre : `sport_id` pour la jointure, `id` pour le tri."""
    with moteur.connect() as connexion:
        colonnes = [
            ligne[2]
            for ligne in connexion.execute(
                text("PRAGMA index_info(ix_profil_sport_id)")
            )
        ]
    assert colonnes == ["sport_id", "id"]


def test_le_plan_de_la_requete_reelle_emprunte_l_index(vivier_amorce: Session) -> None:
    """L'existence de l'index ne prouve rien : c'est le **plan** qui le prouve.

    On demande à SQLite ce qu'il fait de la requête que `profils_du_sport` envoie
    vraiment — pas d'une copie écrite dans le test. Trois choses à y lire : l'index
    est nommé, `profil` n'est pas balayé, et le `ORDER BY` ne coûte pas un tri
    supplémentaire — c'est ce que l'index composite achète.
    """
    sql, parametres = _requete_des_profils_du_sport(vivier_amorce)
    plan = _plan_de(vivier_amorce, sql, parametres)

    assert "ix_profil_sport_id" in plan, plan
    assert "SCAN profil" not in plan, plan
    assert "USE TEMP B-TREE" not in plan, plan


def _sources_du_chemin_de_recherche() -> dict[str, str]:
    """Le chemin qu'emprunte une recherche : le domaine, et l'accès qu'il appelle."""
    return {
        "domaine/recherche.py": (
            RACINE_DU_PROJET / "exaequo" / "domaine" / "recherche.py"
        ).read_text(encoding="utf-8"),
        "domaine/ports.py": (
            RACINE_DU_PROJET / "exaequo" / "domaine" / "ports.py"
        ).read_text(encoding="utf-8"),
        "DepotVivier.profils_du_sport": inspect.getsource(
            DepotVivier.profils_du_sport
        ),
        "DepotVivier._vers_profil": inspect.getsource(DepotVivier._vers_profil),
        "DepotVivier._jours_de": inspect.getsource(DepotVivier._jours_de),
    }


@pytest.mark.parametrize("nom", sorted(_sources_du_chemin_de_recherche()))
def test_la_table_de_synonymes_n_est_pas_consultee_sur_le_chemin_de_lecture(
    nom: str,
) -> None:
    """La lecture ne consulte jamais la table de synonymes ni ne fonde de sport (AD-5).

    Le test lit les appels avec `ast` : une mention en commentaire ou en docstring ne
    doit pas le faire échouer, et un appel indirect ne doit pas lui échapper.
    """
    source = _sources_du_chemin_de_recherche()[nom]
    arbre = ast.parse(textwrap.dedent(source))

    appeles: set[str] = set()
    for noeud in ast.walk(arbre):
        if isinstance(noeud, ast.Call):
            cible = noeud.func
            if isinstance(cible, ast.Attribute):
                appeles.add(cible.attr)
            elif isinstance(cible, ast.Name):
                appeles.add(cible.id)

    interdits = appeles.intersection(CONSULTATIONS_DE_SYNONYMES_INTERDITES)
    assert not interdits, f"{nom} appelle {sorted(interdits)}"


#: Les formes que prendrait une porte de sortie vers un autre niveau.
FUITES_DE_NIVEAU = (
    "toleran",
    "adjacen",
    "voisin",
    "proche",
    "repli",
    "elargi",
    "niveaux",
)


def _surface_publique_de_recherche() -> list[tuple[str, inspect.Signature]]:
    """Toute la surface publique de `recherche.py` : fonctions, classes et méthodes.

    Ne regarder que `inspect.isfunction` laisserait passer une classe publique dont
    une méthode ouvrirait la porte — `RechercheElargie(...).avec_niveaux_voisins()`.
    """
    surface: list[tuple[str, inspect.Signature]] = []
    for nom, objet in vars(recherche).items():
        if nom.startswith("_"):
            continue
        if getattr(objet, "__module__", None) != recherche.__name__:
            continue
        if inspect.isfunction(objet):
            surface.append((nom, inspect.signature(objet)))
        elif inspect.isclass(objet):
            surface.append((nom, inspect.signature(objet)))
            for nom_membre, membre in vars(objet).items():
                if nom_membre.startswith("_") or not callable(membre):
                    continue
                surface.append((f"{nom}.{nom_membre}", inspect.signature(membre)))
    return surface


def test_aucune_signature_publique_n_ouvre_sur_un_autre_niveau() -> None:
    """L'égalité de niveau est **structurelle** : rien à passer, rien à appeler.

    Le test parcourt toute la surface publique de `recherche.py` — fonctions, classes
    et méthodes : une porte de sortie ajoutée plus tard, `tolerance`, `niveaux`,
    `adjacent` ou `elargir_niveau`, la ferait échouer, au lieu de dépendre d'une
    relecture.
    """
    surface = _surface_publique_de_recherche()
    noms = {nom for nom, _ in surface}
    # Le garde-fou du garde-fou : la fonction et la classe doivent bien être vues.
    assert "chercher_candidats_exacts" in noms
    assert "ResultatRecherche" in noms

    for nom, signature in surface:
        assert not any(fuite in nom.casefold() for fuite in FUITES_DE_NIVEAU), nom
        for parametre in signature.parameters.values():
            assert not any(
                fuite in parametre.name.casefold() for fuite in FUITES_DE_NIVEAU
            ), f"{nom}({parametre.name})"


def test_le_detecteur_de_fuite_reconnait_bien_une_porte_de_sortie() -> None:
    """Sans lui, un détecteur qui n'attrape plus rien passerait pour une protection."""
    for porte in (
        "elargir_le_niveau",
        "chercher_avec_tolerance",
        "niveaux_adjacents",
        "candidats_de_niveau_voisin",
        "repli_sur_le_niveau_proche",
    ):
        assert any(fuite in porte for fuite in FUITES_DE_NIVEAU), porte


def test_le_niveau_est_obligatoire_et_ne_peut_pas_etre_absent() -> None:
    """`niveau: Niveau`, sans défaut et sans `None` : jamais « tous les niveaux »."""
    niveau = inspect.signature(chercher_candidats_exacts).parameters["niveau"]

    assert niveau.default is inspect.Parameter.empty
    assert niveau.annotation == "Niveau"
    assert niveau.kind is inspect.Parameter.KEYWORD_ONLY

    with pytest.raises(TypeError):
        chercher_candidats_exacts(  # type: ignore[call-arg]
            VivierEnMemoire({}),
            libelle_sport="Tennis",
            jour=JourSemaine.MARDI,
        )
