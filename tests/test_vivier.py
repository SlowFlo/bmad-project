"""Le vocabulaire du vivier, et ce que le schéma refuse de porter."""

from __future__ import annotations

import dataclasses
import datetime as dt
from uuid import UUID

import pytest
from sqlalchemy import Engine, inspect, text
from sqlalchemy.exc import IntegrityError, StatementError

from exaequo.adaptateurs.secondaires.persistance.depots import DepotSports, DepotVivier
from exaequo.adaptateurs.secondaires.persistance.modeles import JourDisponibleORM
from exaequo.domaine.identifiants import nouvel_identifiant
from exaequo.domaine.vivier import (
    JourSemaine,
    Niveau,
    Population,
    Profil,
    ProvenanceNumero,
)

#: Les tables des lots suivants. Aucune ne doit exister dans le socle.
TABLES_DES_LOTS_SUIVANTS = (
    "rencontre",
    "jeton",
    "envoi",
    "alerte",
    "conversation",
    "tour",
    "etape",
)

#: Colonnes que rien ne doit poser : deux états dérivés (AD-6) et toute calibration
#: du niveau.
COLONNES_INTERDITES = (
    "bloque",
    "jour_bloque",
    "recherche_active",
    "mu",
    "sigma",
    "historique",
)


def test_le_niveau_n_a_que_trois_valeurs() -> None:
    """Le *niveau inconnu* est une absence, pas une quatrième valeur."""
    assert [membre.value for membre in Niveau] == [
        "debutant",
        "intermediaire",
        "avance",
    ]


def test_les_jours_sont_une_enumeration_de_sept_membres() -> None:
    assert len(list(JourSemaine)) == 7
    assert JourSemaine.depuis_libelle("Mardi") is JourSemaine.MARDI
    assert JourSemaine.depuis_libelle("  MARDI ") is JourSemaine.MARDI


def test_un_libelle_de_jour_inconnu_leve() -> None:
    with pytest.raises(ValueError):
        JourSemaine.depuis_libelle("Marsdi")


def test_les_deux_populations_et_les_deux_provenances_existent() -> None:
    assert {membre.value for membre in Population} == {"amorcage", "inscrit"}
    assert len(list(ProvenanceNumero)) == 2
    assert ProvenanceNumero.DONNEE_AMORCAGE.value == "donnee d'amorcage"
    assert (
        ProvenanceNumero.SAISIE_PAR_UTILISATEUR_INSCRIT.value
        == "saisie par un utilisateur inscrit"
    )


def test_un_profil_du_domaine_est_immuable() -> None:
    profil = Profil(
        id=nouvel_identifiant(),
        prenom="Emma",
        population=Population.AMORCAGE,
        sport_id=nouvel_identifiant(),
        libelle_sport="Tennis",
    )
    assert profil.niveau is None
    assert profil.jours_disponibles == frozenset()
    with pytest.raises(dataclasses.FrozenInstanceError):
        profil.prenom = "Iris"  # type: ignore[misc]


def test_le_schema_porte_les_cinq_tables_du_socle(moteur: Engine) -> None:
    tables = set(inspect(moteur).get_table_names())
    assert {"compte", "profil", "jour_disponible", "sport", "synonyme"} <= tables


def test_le_schema_ne_porte_aucune_table_des_lots_suivants(moteur: Engine) -> None:
    tables = set(inspect(moteur).get_table_names())
    assert tables & set(TABLES_DES_LOTS_SUIVANTS) == set()


def test_aucune_colonne_derivee_ni_de_calibration(moteur: Engine) -> None:
    inspecteur = inspect(moteur)
    for table in inspecteur.get_table_names():
        noms = {colonne["name"] for colonne in inspecteur.get_columns(table)}
        assert noms & set(COLONNES_INTERDITES) == set(), table


def test_un_utilisateur_inscrit_se_distingue_d_un_profil_d_amorcage(
    depot_vivier: DepotVivier, depot_sports: DepotSports, session
) -> None:
    sport, _ = depot_sports.resoudre_a_l_ecriture("Tennis")
    inscrit = depot_vivier.inserer_profil(
        prenom="Iris",
        population=Population.INSCRIT,
        sport_id=sport.id,
        libelle_sport="Tennis",
        jours_disponibles=[JourSemaine.MARDI],
        niveau=Niveau.AVANCE,
        courriel="iris@exemple.test",
        secteur="Croix-Rousse",
        telephone="+33612345678",
        provenance_numero=ProvenanceNumero.SAISIE_PAR_UTILISATEUR_INSCRIT,
    )
    session.commit()

    assert inscrit.population is Population.INSCRIT
    assert inscrit.cle_amorcage is None
    assert (
        inscrit.provenance_numero is ProvenanceNumero.SAISIE_PAR_UTILISATEUR_INSCRIT
    )
    assert isinstance(inscrit.id, UUID)
    assert inscrit.cree_le is not None and inscrit.cree_le.tzinfo is not None


def test_un_niveau_absent_reste_nul_en_base(
    depot_vivier: DepotVivier, depot_sports: DepotSports, session
) -> None:
    """Le *niveau inconnu* traverse la persistance : la colonne reste `NULL`."""
    sport, _ = depot_sports.resoudre_a_l_ecriture("Tennis")
    profil = depot_vivier.inserer_profil(
        prenom="Iris",
        population=Population.INSCRIT,
        sport_id=sport.id,
        libelle_sport="Tennis",
        jours_disponibles=[JourSemaine.MARDI],
    )
    session.commit()

    nuls = session.execute(
        text("SELECT count(*) FROM profil WHERE niveau IS NULL")
    ).scalar_one()
    assert nuls == 1
    assert depot_vivier.par_identifiant(profil.id).niveau is None


def test_les_jours_disponibles_ne_se_dupliquent_pas(
    depot_vivier: DepotVivier, depot_sports: DepotSports, session
) -> None:
    """Deux gardes, pas une : la déduplication du dépôt **et** celle du schéma."""
    sport, _ = depot_sports.resoudre_a_l_ecriture("Tennis")
    profil = depot_vivier.inserer_profil(
        prenom="Iris",
        population=Population.INSCRIT,
        sport_id=sport.id,
        libelle_sport="Tennis",
        jours_disponibles=[JourSemaine.MARDI, JourSemaine.MARDI, JourSemaine.JEUDI],
    )
    session.commit()
    assert depot_vivier.compter_jours_disponibles() == 2

    # Le schéma refuse le doublon même écrit directement, sans passer par le dépôt.
    session.add(
        JourDisponibleORM(
            id=nouvel_identifiant(), profil_id=profil.id, jour=JourSemaine.MARDI
        )
    )
    with pytest.raises(IntegrityError):
        session.flush()
    session.rollback()
    assert depot_vivier.compter_jours_disponibles() == 2


def test_un_horodatage_sans_fuseau_est_refuse(
    depot_vivier: DepotVivier, depot_sports: DepotSports, session
) -> None:
    """Les horodatages sont en UTC : une heure locale muette n'entre pas en base."""
    sport, _ = depot_sports.resoudre_a_l_ecriture("Tennis")
    with pytest.raises(StatementError, match="fuseau"):
        depot_vivier.inserer_profil(
            prenom="Iris",
            population=Population.INSCRIT,
            sport_id=sport.id,
            libelle_sport="Tennis",
            jours_disponibles=[JourSemaine.MARDI],
            maintenant=dt.datetime(2026, 8, 30, 12, 0),
        )


def test_un_numero_sans_provenance_est_refuse(
    depot_vivier: DepotVivier, depot_sports: DepotSports, session
) -> None:
    """AD-11 : chaque numéro porte sa provenance, enregistrée dans le modèle."""
    sport, _ = depot_sports.resoudre_a_l_ecriture("Tennis")
    with pytest.raises(IntegrityError, match="ck_profil_provenance_avec_numero"):
        depot_vivier.inserer_profil(
            prenom="Iris",
            population=Population.INSCRIT,
            sport_id=sport.id,
            libelle_sport="Tennis",
            jours_disponibles=[JourSemaine.MARDI],
            telephone="+33612345678",
            provenance_numero=None,
        )


def test_un_profil_d_amorcage_sans_cle_naturelle_est_refuse(
    depot_vivier: DepotVivier, depot_sports: DepotSports, session
) -> None:
    """AD-16 : l'idempotence porte sur une clé naturelle stable."""
    sport, _ = depot_sports.resoudre_a_l_ecriture("Tennis")
    with pytest.raises(IntegrityError, match="ck_profil_amorcage_porte_sa_cle"):
        depot_vivier.inserer_profil(
            prenom="Emma",
            population=Population.AMORCAGE,
            sport_id=sport.id,
            libelle_sport="Tennis",
            jours_disponibles=[JourSemaine.MARDI],
            cle_amorcage=None,
        )


def test_deux_profils_ne_partagent_pas_une_cle_d_amorcage(
    depot_vivier: DepotVivier, depot_sports: DepotSports, session
) -> None:
    sport, _ = depot_sports.resoudre_a_l_ecriture("Tennis")
    depot_vivier.inserer_profil(
        prenom="Emma",
        population=Population.AMORCAGE,
        sport_id=sport.id,
        libelle_sport="Tennis",
        jours_disponibles=[JourSemaine.MARDI],
        telephone="+33639980002",
        provenance_numero=ProvenanceNumero.DONNEE_AMORCAGE,
        cle_amorcage="+33639980002",
    )
    session.commit()
    with pytest.raises(IntegrityError, match="UNIQUE"):
        depot_vivier.inserer_profil(
            prenom="Iris",
            population=Population.AMORCAGE,
            sport_id=sport.id,
            libelle_sport="Tennis",
            jours_disponibles=[JourSemaine.JEUDI],
            telephone="+33639980002",
            provenance_numero=ProvenanceNumero.DONNEE_AMORCAGE,
            cle_amorcage="+33639980002",
        )


def test_un_sport_jamais_fonde_est_refuse_par_la_base(
    depot_vivier: DepotVivier, session
) -> None:
    """Le `PRAGMA foreign_keys=ON` est observé : SQLite le laisse à OFF par défaut,
    et sans lui un profil pourrait pointer vers un sport qui n'existe pas."""
    with pytest.raises(IntegrityError, match="FOREIGN KEY"):
        depot_vivier.inserer_profil(
            prenom="Iris",
            population=Population.INSCRIT,
            sport_id=nouvel_identifiant(),  # jamais fondé
            libelle_sport="Tennis",
            jours_disponibles=[JourSemaine.MARDI],
        )


def test_un_jour_disponible_orphelin_est_refuse_par_la_base(session) -> None:
    session.add(
        JourDisponibleORM(
            id=nouvel_identifiant(),
            profil_id=nouvel_identifiant(),  # aucun profil
            jour=JourSemaine.MARDI,
        )
    )
    with pytest.raises(IntegrityError, match="FOREIGN KEY"):
        session.flush()
    session.rollback()


def test_un_horodatage_decale_est_stocke_en_utc(
    depot_vivier: DepotVivier, depot_sports: DepotSports, session
) -> None:
    """Un instant donné en `+02:00` revient en UTC, sans avoir bougé.

    C'est la conversion de `HorodatageUTC` : la stocker telle quelle écrirait une
    heure locale muette, que rien ne permettrait de relire correctement.
    """
    paris = dt.timezone(dt.timedelta(hours=2))
    instant_decale = dt.datetime(2026, 8, 30, 14, 30, tzinfo=paris)
    meme_instant_en_utc = dt.datetime(2026, 8, 30, 12, 30, tzinfo=dt.UTC)

    sport, _ = depot_sports.resoudre_a_l_ecriture("Tennis", maintenant=instant_decale)
    profil = depot_vivier.inserer_profil(
        prenom="Iris",
        population=Population.INSCRIT,
        sport_id=sport.id,
        libelle_sport="Tennis",
        jours_disponibles=[JourSemaine.MARDI],
        maintenant=instant_decale,
    )
    session.commit()
    session.expunge_all()

    relu = depot_vivier.par_identifiant(profil.id)
    assert relu is not None
    assert relu.cree_le == instant_decale  # le même instant
    assert relu.cree_le == meme_instant_en_utc
    assert relu.cree_le.tzinfo is dt.UTC
    assert relu.cree_le.hour == 12  # exprimé en UTC, pas en heure locale

    # Ce que la base porte vraiment : le décalage a été appliqué avant l'écriture.
    brut = session.execute(text("SELECT cree_le FROM profil")).scalar_one()
    assert brut.startswith("2026-08-30 12:30")
