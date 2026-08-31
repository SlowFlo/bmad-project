"""La recherche : égalité stricte de niveau, exclusions, clé de sport, jour élargi.

Les règles s'éprouvent contre un **faux port en mémoire** : c'est ce que gagne un port
qui rétrécit sans filtrer — aucune base n'est nécessaire pour prouver qu'un niveau
inconnu ou un profil sorti du vivier n'est jamais rendu. Les repères de mise au point
— « Tennis, mardi, débutant » rend Emma Leroy, la même demande en intermédiaire rend
Anna, Iris et Tessa après élargissement — s'éprouvent, eux, contre le vivier d'amorçage
réel, seul endroit où ces noms veulent dire quelque chose.
"""

from __future__ import annotations

import ast
import datetime as dt
import inspect
import textwrap
from collections.abc import Callable, Mapping, Sequence, Set
from pathlib import Path
from typing import Any, Protocol
from uuid import UUID

import pytest
from conftest import TABLE_PROFIL
from sqlalchemy import Connection, Engine, event, text, update
from sqlalchemy.engine.interfaces import DBAPICursor, ExecutionContext
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
from exaequo.domaine.recherche import (
    JourIndisponible,
    ResultatRecherche,
    chercher_candidats,
    chercher_candidats_exacts,
)
from exaequo.domaine.sports import cle_sport, replier_texte
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

#: Les deux points d'entrée publics de `recherche.py`. Tout ce qui porte sur la
#: **forme** de la signature — le niveau obligatoire, le défaut inerte des jours
#: indisponibles, la liste blanche des paramètres — les parcourt tous les deux :
#: `chercher_candidats` (2.2) hérite des gardes de l'exact, et une garde qui ne
#: vaudrait que pour `chercher_candidats_exacts` laisserait la porte ouverte sur
#: le point d'entrée que le produit appelle réellement.
POINTS_D_ENTREE_DE_LA_RECHERCHE = (chercher_candidats_exacts, chercher_candidats)


class PointDEntreeDeRecherche(Protocol):
    """La signature que les deux points d'entrée partagent, mot pour mot.

    Les tests paramétrés ci-dessous en appellent un sans lui donner `niveau`, et
    affirment que c'est une erreur. Typer le paramètre par un `Callable` permissif
    — ou par `FunctionType`, dont le `__call__` accepte n'importe quoi — rendrait
    cet appel acceptable au vérificateur : la garde qu'on éprouve à l'exécution
    serait éteinte à l'écriture, là où elle devrait l'être en premier.
    """

    __name__: str

    def __call__(
        self,
        vivier: PortVivier,
        *,
        libelle_sport: str,
        jour: JourSemaine,
        niveau: Niveau,
        demandeur_id: UUID | None = None,
        jours_indisponibles: Set[JourIndisponible] = frozenset(),
    ) -> ResultatRecherche: ...


#: Le protocole doit décrire la **vraie** signature, sinon il ne protège rien : ces
#: deux affectations le prouvent statiquement, et `pytest.mark.parametrize` étant
#: non typé, elles sont le seul endroit qui puisse le faire.
_EXACT_EST_UN_POINT_D_ENTREE: PointDEntreeDeRecherche = chercher_candidats_exacts
_PRODUIT_EST_UN_POINT_D_ENTREE: PointDEntreeDeRecherche = chercher_candidats


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


def _instructions_de(
    session: Session, appel: Callable[[], object]
) -> list[tuple[str, object]]:
    """Le SQL réellement envoyé au pilote pendant `appel`.

    On écoute le moteur plutôt que de recomposer la requête dans le test : c'est la
    requête de production qui est éprouvée, et non une copie qui dériverait d'elle.
    """
    instructions: list[tuple[str, object]] = []

    def enregistrer(
        conn: Connection,
        cursor: DBAPICursor,
        statement: str,
        # `parameters` reste `Any` : SQLAlchemy le déclare
        # `_DBAPIAnyExecuteParams`, un nom privé qu'il n'expose pas.
        parameters: Any,
        context: ExecutionContext | None,
        executemany: bool,
    ) -> None:
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
    assert brut is not None
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


@pytest.mark.parametrize(
    "point_d_entree", POINTS_D_ENTREE_DE_LA_RECHERCHE, ids=lambda f: f.__name__
)
def test_les_jours_indisponibles_sont_vides_par_defaut(
    point_d_entree: PointDEntreeDeRecherche,
) -> None:
    """Le paramètre est inerte tant qu'E5 n'y branche pas la dérivation (AD-6).

    Le défaut est un `frozenset` et **non** un `set` : `set() == frozenset()` est
    vrai, si bien qu'une égalité seule laisserait passer le défaut mutable — partagé
    entre tous les appels, et qu'un appelant pourrait peupler pour tout le processus.

    Éprouvé sur les **deux** points d'entrée : un défaut mutable posé sur le seul
    `chercher_candidats` serait le plus dangereux des deux, puisque c'est lui que le
    produit appelle.
    """
    defaut = inspect.signature(point_d_entree).parameters[
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
    """`None` n'est pas « tous les niveaux ».

    C'est une absence, et elle est refusée.
    """
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
    # L'exact n'élargit jamais, donc ne le signale jamais : Emma est bien disponible
    # le mardi, et le drapeau de 2.2 dirait le contraire.
    assert resultat.jour_demande_indisponible is False


def test_la_meme_demande_en_intermediaire_ne_rend_rien(vivier_amorce: Session) -> None:
    """La recherche exacte rend vide et **n'élargit jamais d'elle-même** (2.2)."""
    resultat = chercher_candidats_exacts(
        DepotVivier(vivier_amorce),
        libelle_sport="Tennis",
        jour=JourSemaine.MARDI,
        niveau=Niveau.INTERMEDIAIRE,
    )

    assert resultat.candidats == ()
    # Le drapeau de 2.2 reste faux là où il serait le plus tentant : c'est
    # exactement la demande sur laquelle `chercher_candidats` rendra trois
    # candidates en le levant. L'exact, lui, n'élargit pas — il n'a donc rien à
    # signaler, et ne prétend pas que le jour était en cause.
    assert resultat.jour_demande_indisponible is False
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
        update(TABLE_PROFIL)
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


# --- L'élargissement sur le jour, et sur lui seul -----------------------------------


def test_l_elargissement_rend_anna_iris_et_tessa(vivier_amorce: Session) -> None:
    """Le repère de 2.2, sur les données d'amorçage réelles.

    « Tennis, mardi, intermédiaire » ne rend personne en exact — Anna, Iris et Tessa
    jouent d'autres jours, exactement à ce niveau. Elles sont rendues dans **l'ordre
    du vivier**, chacune avec ses jours déclarés, et le résultat porte que le jour
    demandé n'était pas disponible.
    """
    depot = DepotVivier(vivier_amorce)

    assert (
        chercher_candidats_exacts(
            depot,
            libelle_sport="Tennis",
            jour=JourSemaine.MARDI,
            niveau=Niveau.INTERMEDIAIRE,
        ).candidats
        == ()
    )

    resultat = chercher_candidats(
        depot,
        libelle_sport="Tennis",
        jour=JourSemaine.MARDI,
        niveau=Niveau.INTERMEDIAIRE,
    )

    assert [(c.prenom, c.nom) for c in resultat.candidats] == [
        ("Anna", "Perrot"),
        ("Iris", "Payet"),
        ("Tessa", "Armand"),
    ]
    assert [sorted(c.jours_disponibles) for c in resultat.candidats] == [
        sorted({JourSemaine.MERCREDI, JourSemaine.SAMEDI}),
        sorted({JourSemaine.LUNDI, JourSemaine.MERCREDI}),
        sorted({JourSemaine.LUNDI, JourSemaine.SAMEDI}),
    ]
    assert resultat.jour_demande_indisponible is True
    assert resultat.cle_sport == "tennis"
    assert resultat.jour is JourSemaine.MARDI
    assert resultat.niveau is Niveau.INTERMEDIAIRE


def test_un_exact_non_vide_n_est_jamais_elargi(vivier_amorce: Session) -> None:
    """« Tennis, mardi, débutant » rend Emma seule, et le drapeau reste faux.

    Margot et Mélina sont débutantes au tennis, mais lundi et vendredi : les rendre
    serait élargir un exact qui n'était pas vide.
    """
    resultat = chercher_candidats(
        DepotVivier(vivier_amorce),
        libelle_sport="Tennis",
        jour=JourSemaine.MARDI,
        niveau=Niveau.DEBUTANT,
    )

    assert [(c.prenom, c.nom) for c in resultat.candidats] == [("Emma", "Leroy")]
    assert resultat.jour_demande_indisponible is False


def test_un_seul_candidat_exact_suffit_a_interdire_l_elargissement() -> None:
    """Le cas le plus tentant : l'élargissement aurait rendu bien davantage."""
    vivier = _vivier_de_tennis(
        _profil(prenom="Exacte", jours=(JourSemaine.MARDI,)),
        _profil(prenom="Jeudi", jours=(JourSemaine.JEUDI,)),
        _profil(prenom="Samedi", jours=(JourSemaine.SAMEDI,)),
    )

    resultat = chercher_candidats(
        vivier,
        libelle_sport="Tennis",
        jour=JourSemaine.MARDI,
        niveau=Niveau.DEBUTANT,
    )

    assert _prenoms(resultat) == ["Exacte"]
    assert resultat.jour_demande_indisponible is False


def test_l_elargissement_ne_relache_ni_le_sport_ni_le_niveau() -> None:
    """Le jour est le **seul** axe : un autre sport ou un autre niveau reste dehors."""
    vivier = VivierEnMemoire(
        {
            "tennis": (
                _profil(
                    prenom="Autre niveau",
                    jours=(JourSemaine.JEUDI,),
                    niveau=Niveau.AVANCE,
                ),
            ),
            "padel": (
                _profil(
                    prenom="Autre sport",
                    libelle_sport="Padel",
                    jours=(JourSemaine.JEUDI,),
                    niveau=Niveau.DEBUTANT,
                ),
            ),
        }
    )

    resultat = chercher_candidats(
        vivier,
        libelle_sport="Tennis",
        jour=JourSemaine.MARDI,
        niveau=Niveau.DEBUTANT,
    )

    assert resultat.candidats == ()
    assert resultat.jour_demande_indisponible is False
    # Le port n'a été interrogé que sur la clé demandée : élargir ne va pas
    # chercher un autre sport.
    assert vivier.cles_demandees == ["tennis"]


#: Les quatre exclusions de CAP-5 que le jour ne concerne pas, chacune fabriquée à
#: part. Une seule assertion de liste les agrégerait : si « soi-même » cassait après
#: élargissement — le cas que `_exiger_demandeur` documente précisément comme muet —
#: l'échec ne dirait que « la liste diffère ». Séparées, il nomme l'exclusion.
#: Toutes ces profils sont disponibles le **jeudi**, donc à portée de l'élargissement
#: d'une demande du mardi : c'est bien l'exclusion qui les écarte, pas le jour.
EXCLUSIONS_DE_CAP_5_APRES_ELARGISSEMENT = (
    pytest.param(
        lambda _demandeur: _profil(
            prenom="Exclue", jours=(JourSemaine.JEUDI,), niveau=None
        ),
        id="niveau-inconnu",
    ),
    pytest.param(
        lambda _demandeur: _profil(
            prenom="Exclue",
            jours=(JourSemaine.JEUDI,),
            sortie_vivier_le=dt.datetime(2026, 8, 30, 12, 0, tzinfo=dt.UTC),
        ),
        id="sortie-du-vivier",
    ),
    pytest.param(
        lambda demandeur: _profil(
            prenom="Exclue", jours=(JourSemaine.JEUDI,), identifiant=demandeur
        ),
        id="demandeur-lui-meme",
    ),
    pytest.param(
        lambda _demandeur: _profil(prenom="Exclue", jours=()),
        id="aucun-jour-declare",
    ),
)


@pytest.mark.parametrize("fabriquer_exclue", EXCLUSIONS_DE_CAP_5_APRES_ELARGISSEMENT)
def test_une_exclusion_de_cap_5_survit_a_l_elargissement(
    fabriquer_exclue: Callable[[UUID], Profil],
) -> None:
    """Relâcher le jour ne relâche aucune des quatre autres exclusions.

    Le témoin « Retenue » est là pour que l'assertion prouve quelque chose : sans
    lui, un élargissement cassé rendrait vide et le test passerait pour la mauvaise
    raison.
    """
    demandeur = nouvel_identifiant()
    temoin = _profil(prenom="Retenue", jours=(JourSemaine.JEUDI,))
    vivier = _vivier_de_tennis(fabriquer_exclue(demandeur), temoin)

    resultat = chercher_candidats(
        vivier,
        libelle_sport="Tennis",
        jour=JourSemaine.MARDI,
        niveau=Niveau.DEBUTANT,
        demandeur_id=demandeur,
    )

    assert "Exclue" not in _prenoms(resultat)
    # Le garde-fou du garde-fou : l'élargissement a bien eu lieu.
    assert _prenoms(resultat) == ["Retenue"]
    assert resultat.jour_demande_indisponible is True


def test_l_elargissement_garde_le_bon_niveau_et_ecarte_l_autre() -> None:
    """Le pendant du témoin : un profil du bon niveau passe l'élargissement."""
    vivier = _vivier_de_tennis(
        _profil(prenom="Bon niveau", jours=(JourSemaine.JEUDI,)),
        _profil(
            prenom="Autre niveau", jours=(JourSemaine.JEUDI,), niveau=Niveau.AVANCE
        ),
    )

    resultat = chercher_candidats(
        vivier,
        libelle_sport="Tennis",
        jour=JourSemaine.MARDI,
        niveau=Niveau.DEBUTANT,
    )

    assert _prenoms(resultat) == ["Bon niveau"]


def test_un_blocage_partiel_laisse_le_profil_rendu_par_l_elargissement() -> None:
    """Bloqué mardi, libre jeudi : c'est exactement ce que l'élargissement récupère."""
    bloquee = _profil(
        prenom="Bloquee mardi", jours=(JourSemaine.MARDI, JourSemaine.JEUDI)
    )
    vivier = _vivier_de_tennis(bloquee)

    resultat = chercher_candidats(
        vivier,
        libelle_sport="Tennis",
        jour=JourSemaine.MARDI,
        niveau=Niveau.DEBUTANT,
        jours_indisponibles=frozenset({(bloquee.id, JourSemaine.MARDI)}),
    )

    assert _prenoms(resultat) == ["Bloquee mardi"]
    assert resultat.jour_demande_indisponible is True


def test_un_blocage_total_n_est_jamais_rendu() -> None:
    """Tous ses jours déclarés immobilisés : il n'a aucun jour à proposer (CAP-14)."""
    immobilisee = _profil(
        prenom="Immobilisee", jours=(JourSemaine.MARDI, JourSemaine.JEUDI)
    )
    vivier = _vivier_de_tennis(immobilisee)

    resultat = chercher_candidats(
        vivier,
        libelle_sport="Tennis",
        jour=JourSemaine.MARDI,
        niveau=Niveau.DEBUTANT,
        jours_indisponibles=frozenset(
            {
                (immobilisee.id, JourSemaine.MARDI),
                (immobilisee.id, JourSemaine.JEUDI),
            }
        ),
    )

    assert resultat.candidats == ()
    assert resultat.jour_demande_indisponible is False


def test_un_vivier_vraiment_vide_ne_met_pas_le_jour_en_cause(
    vivier_amorce: Session,
) -> None:
    """« Pilates, avancé » : personne, aucun jour. Le drapeau qualifie des candidats.

    Vrai, il dirait « ceux-ci ne sont pas disponibles le jour demandé » — il n'y a
    personne dont le dire.
    """
    resultat = chercher_candidats(
        DepotVivier(vivier_amorce),
        libelle_sport="Pilates",
        jour=JourSemaine.MARDI,
        niveau=Niveau.AVANCE,
    )

    assert resultat.candidats == ()
    assert resultat.jour_demande_indisponible is False


def test_un_sport_absent_rend_vide_sans_rien_ecrire_ni_lever(
    vivier_amorce: Session,
) -> None:
    """« Squash » n'est pas un refus, même sur le point d'entrée qui élargit."""
    depot_sports = DepotSports(vivier_amorce)
    avant = depot_sports.compter()

    resultat = chercher_candidats(
        DepotVivier(vivier_amorce),
        libelle_sport="squash",
        jour=JourSemaine.MARDI,
        niveau=Niveau.DEBUTANT,
    )

    assert resultat.candidats == ()
    assert resultat.jour_demande_indisponible is False
    assert depot_sports.compter() == avant == 11
    assert depot_sports.par_cle("squash") is None


def test_l_ordre_du_vivier_est_preserve_par_l_elargissement() -> None:
    """Le second filtre ne retrie rien non plus : il ne fait, lui aussi, que retrancher.

    2.1 avait pris soin de l'écrire pour l'exact ; l'élargissement passe par un autre
    filtre et mérite le même test. 2.3 s'appuiera sur cet ordre — l'ordre du vivier,
    identifiant croissant — pour départager les ex æquo du tri par délai d'attente,
    qui est le cas le plus fréquent sur les données d'amorçage.
    """
    vivier = _vivier_de_tennis(
        *(
            _profil(prenom=prenom, jours=(JourSemaine.JEUDI,))
            for prenom in ("Un", "Deux", "Trois", "Quatre")
        )
    )

    resultat = chercher_candidats(
        vivier,
        libelle_sport="Tennis",
        jour=JourSemaine.MARDI,
        niveau=Niveau.DEBUTANT,
    )

    assert _prenoms(resultat) == ["Un", "Deux", "Trois", "Quatre"]
    assert resultat.jour_demande_indisponible is True


def test_l_elargissement_n_appelle_le_port_qu_une_seule_fois() -> None:
    """Les profils chargés une fois se filtrent deux fois (AD-1, coût de 2.4)."""
    vivier = _vivier_de_tennis(_profil(prenom="Jeudi", jours=(JourSemaine.JEUDI,)))

    chercher_candidats(
        vivier,
        libelle_sport="Tennis",
        jour=JourSemaine.MARDI,
        niveau=Niveau.DEBUTANT,
    )

    assert vivier.cles_demandees == ["tennis"]


@pytest.mark.parametrize(
    ("parametre", "arguments"),
    [
        ("niveau", {"niveau": "debutant"}),
        ("jour", {"jour": "mardi"}),
        ("libelle_sport", {"libelle_sport": None}),
        ("demandeur_id", {"demandeur_id": "pas-un-uuid"}),
        ("jours_indisponibles", {"jours_indisponibles": frozenset({"mardi"})}),
    ],
)
def test_les_cinq_gardes_valent_aussi_pour_le_point_d_entree_produit(
    parametre: str, arguments: dict[str, object]
) -> None:
    """Jamais de vide muet : les gardes sont partagées, jamais recopiées.

    Un vide muet serait ici pire encore que sur l'exact : il ressemblerait à « aucun
    candidat, même en élargissant », le résultat le plus décourageant du produit.
    """
    vivier = _vivier_de_tennis(_profil(prenom="Jeudi", jours=(JourSemaine.JEUDI,)))
    appel = {
        "libelle_sport": "Tennis",
        "jour": JourSemaine.MARDI,
        "niveau": Niveau.DEBUTANT,
        **arguments,
    }

    with pytest.raises(TypeError, match=parametre):
        chercher_candidats(vivier, **appel)  # type: ignore[arg-type]

    # On refuse, on ne rattrape pas : le port n'est même pas appelé.
    assert vivier.cles_demandees == []


def test_aucun_candidat_elargi_n_est_d_un_autre_niveau(vivier_amorce: Session) -> None:
    """Le test **négatif** de la règle de niveau de 2.2, sur toute la grille réelle.

    Le risque propre à 2.2 est de relâcher une contrainte de trop. On parcourt donc
    les sports, les jours et les niveaux du vivier d'amorçage, et on affirme une
    **absence** : quel que soit le résultat — exact ou élargi — aucun candidat rendu
    n'est d'un autre niveau que celui demandé, et l'élargissement n'est jamais
    signalé sur un résultat vide.

    Ce n'est **pas** la mesure de SM-3. Les chiffres contractuels de la grille — les
    combinaisons sans candidat exact, la part que l'élargissement récupère, le plafond
    atteignable au-delà duquel il faudrait soupçonner une fuite de niveau —
    appartiennent à 2.4, qui les mesure et les assume. Les asserter ici les figerait
    à deux endroits, dont l'un ne les explique pas.
    """
    depot = DepotVivier(vivier_amorce)
    libelles = {
        libelle
        for (libelle,) in vivier_amorce.execute(
            ProfilORM.__table__.select().with_only_columns(ProfilORM.libelle_sport)
        )
    }
    assert len(libelles) == 11

    elargissements = 0
    for libelle in sorted(libelles):
        for jour in JourSemaine:
            for niveau in Niveau:
                resultat = chercher_candidats(
                    depot, libelle_sport=libelle, jour=jour, niveau=niveau
                )
                for candidat in resultat.candidats:
                    assert candidat.niveau is niveau, (
                        f"{libelle}/{jour}/{niveau} rend {candidat.prenom} "
                        f"de niveau {candidat.niveau}"
                    )
                    assert candidat.sortie_vivier_le is None
                    assert candidat.jours_disponibles
                if not resultat.candidats:
                    assert resultat.jour_demande_indisponible is False
                if resultat.jour_demande_indisponible:
                    elargissements += 1
                    # Ce que cette assertion prouve, et ce qu'elle ne prouve pas :
                    # la boucle ne passe **aucun** `jours_indisponibles`, si bien que
                    # « jours déclarés » et « jours effectivement disponibles » se
                    # confondent ici. Sous cette hypothèse seule, un candidat élargi
                    # ne peut pas avoir déclaré le jour demandé — sinon l'exact
                    # l'aurait rendu, et il n'y aurait pas eu d'élargissement.
                    # Dès qu'un blocage entre en jeu, l'implication tombe. Le
                    # contre-exemple immédiat — drapeau vrai, et MARDI toujours
                    # parmi les jours *déclarés* de la bloquée — est le test
                    # test_un_blocage_partiel_laisse_le_profil_rendu_par_l_elargissement
                    for candidat in resultat.candidats:
                        assert jour not in candidat.jours_disponibles

    # Le garde-fou du garde-fou : la grille doit bien contenir des élargissements,
    # sans quoi la boucle ne prouverait rien.
    assert elargissements > 0


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
    """Sans lui, SQLite balaie `profil` à chaque recherche — et 2.4 en fait 231.

    Report d'E1 « aucun index sur `profil.sport_id` », clos par cette histoire.
    """
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
        # `sports.py` est sur le chemin — `chercher_candidats_exacts` y appelle
        # `cle_sport` — et c'est le module qui **définit** `resoudre_libelle` : le
        # lieu le plus probable d'une reconsultation de la table de synonymes. On
        # n'ajoute que les deux fonctions de lecture, pas le fichier entier, qui
        # contiendrait `resoudre_libelle` par définition et non par appel.
        "sports.cle_sport": inspect.getsource(cle_sport),
        "sports.replier_texte": inspect.getsource(replier_texte),
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


#: La surface publique admise de `recherche.py`, et les paramètres admis de la
#: recherche. La liste noire ci-dessus n'attrape que le vocabulaire auquel on a pensé :
#: `niveau_max=`, `strict=False` ou `marge=` la traversent sans la déclencher. Cette
#: liste-ci prend le problème par l'autre bout — **tout** ce qui n'y est pas inscrit
#: fait échouer le test, y compris un paramètre inerte par défaut.
#: `chercher_candidats` (2.2) y est inscrite **délibérément** : le point d'entrée
#: produit élargit sur le jour, et sur lui seul. Son nom ne porte pas `elargi` — la
#: liste noire ci-dessus le refuse justement pour interdire `elargir_le_niveau`, et on
#: ne l'affaiblit pas pour se faire de la place : le geste est privé
#: (`_elargir_sur_le_jour`).
SURFACE_PUBLIQUE_ADMISE = frozenset(
    {"chercher_candidats", "chercher_candidats_exacts", "ResultatRecherche"}
)
PARAMETRES_ADMIS_DE_LA_RECHERCHE = frozenset(
    {
        "vivier",
        "libelle_sport",
        "jour",
        "niveau",
        "demandeur_id",
        "jours_indisponibles",
    }
)


@pytest.mark.parametrize(
    "point_d_entree", POINTS_D_ENTREE_DE_LA_RECHERCHE, ids=lambda f: f.__name__
)
def test_la_recherche_ne_porte_que_les_parametres_admis(
    point_d_entree: PointDEntreeDeRecherche,
) -> None:
    """L'interdit d'élargissement est vérifié par liste blanche, pas par liste noire.

    Une liste noire ne protège que contre les noms que son auteur a imaginés. Ici,
    ajouter `niveau_max`, `strict` ou `assouplir` à l'un des deux points d'entrée fait
    échouer ce test tant que personne ne l'a délibérément inscrit — ce qui est
    exactement le geste qu'AC-3 veut rendre impossible par inadvertance.
    """
    parametres = set(inspect.signature(point_d_entree).parameters)
    ajouts = parametres - PARAMETRES_ADMIS_DE_LA_RECHERCHE

    assert not ajouts, (
        f"paramètre non admis sur {point_d_entree.__name__} : {sorted(ajouts)}"
    )
    # Le garde-fou du garde-fou : la liste blanche doit décrire la vraie signature.
    assert PARAMETRES_ADMIS_DE_LA_RECHERCHE - parametres == set()


def test_la_surface_publique_de_recherche_est_exactement_celle_attendue() -> None:
    """Sans liste noire : une classe `RechercheElargie` ajoutée échouerait ici."""
    noms = {nom for nom, _ in _surface_publique_de_recherche()}
    ajouts = noms - SURFACE_PUBLIQUE_ADMISE

    assert not ajouts, f"surface publique non admise : {sorted(ajouts)}"
    assert SURFACE_PUBLIQUE_ADMISE - noms == set()


def test_l_export_public_de_recherche_est_exactement_celui_attendu() -> None:
    """`__all__` échappe aux deux gardes de surface : il faut le fixer à part.

    `_surface_publique_de_recherche` lit `vars(recherche)` et ne retient que ce dont
    le `__module__` est celui de `recherche.py`. `JourIndisponible` est un **alias de
    type** — `tuple[UUID, JourSemaine]` — dont le `__module__` vaut `builtins` : il
    n'apparaît ni dans la liste noire, ni dans la liste blanche. Un futur
    `NiveauxVoisins = tuple[Niveau, Niveau]`, exporté et documenté, les traverserait
    donc toutes les deux sans un test rouge. Celui-ci ferme la porte par le nom
    exporté, qui est ce qu'un appelant importe réellement.
    """
    assert recherche.__all__ == [
        "JourIndisponible",
        "ResultatRecherche",
        "chercher_candidats",
        "chercher_candidats_exacts",
    ]
    # Un nom exporté qui ne résout pas est un `ImportError` chez l'appelant, pas ici.
    for nom in recherche.__all__:
        assert hasattr(recherche, nom), nom
        assert not any(fuite in nom.casefold() for fuite in FUITES_DE_NIVEAU), nom


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


@pytest.mark.parametrize(
    "point_d_entree", POINTS_D_ENTREE_DE_LA_RECHERCHE, ids=lambda f: f.__name__
)
def test_le_niveau_est_obligatoire_et_ne_peut_pas_etre_absent(
    point_d_entree: PointDEntreeDeRecherche,
) -> None:
    """`niveau: Niveau`, sans défaut et sans `None` : jamais « tous les niveaux ».

    Un défaut posé sur `chercher_candidats` seul — `niveau: Niveau = Niveau.DEBUTANT`
    — rendrait le niveau facultatif sur le point d'entrée que le produit appelle, et
    l'omettre ne lèverait plus rien : c'est l'égalité stricte devenue silencieuse.
    """
    niveau = inspect.signature(point_d_entree).parameters["niveau"]

    assert niveau.default is inspect.Parameter.empty
    assert niveau.annotation == "Niveau"
    assert niveau.kind is inspect.Parameter.KEYWORD_ONLY

    with pytest.raises(TypeError):
        # L'ignore est **vivant** : omettre `niveau` est refusé à l'écriture par
        # le protocole, et le test prouve qu'il l'est aussi à l'exécution.
        point_d_entree(  # type: ignore[call-arg]
            VivierEnMemoire({}),
            libelle_sport="Tennis",
            jour=JourSemaine.MARDI,
        )


def test_les_deux_points_d_entree_ont_exactement_la_meme_signature() -> None:
    """La docstring de `chercher_candidats` promet « signature identique » à l'exact.

    Rien ne l'éprouvait. Or c'est cette identité qui fait porter à l'élargissement
    **toutes** les gardes de 2.1 : le jour dérive d'un paramètre ajouté, d'un défaut
    posé ou d'une annotation relâchée sur un seul des deux, et la liste blanche des
    paramètres ne verrait qu'une signature sur deux. Une égalité de `Signature`
    compare les noms, l'ordre, les genres, les défauts et les annotations.
    """
    assert inspect.signature(chercher_candidats) == inspect.signature(
        chercher_candidats_exacts
    )
