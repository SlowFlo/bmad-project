"""La résolution d'un sport écrite en base : fondation, synonyme, lecture."""

from __future__ import annotations

from exaequo.adaptateurs.secondaires.persistance.depots import DepotSports


def test_un_libelle_inconnu_fonde_un_sport(depot_sports: DepotSports) -> None:
    sport, resolution = depot_sports.resoudre_a_l_ecriture("Squash")
    assert resolution.fondation is True
    assert sport.cle == "squash"
    assert sport.libelle == "Squash"
    assert depot_sports.compter() == 1


def test_deux_ecritures_du_meme_libelle_ne_fondent_qu_un_sport(
    depot_sports: DepotSports,
) -> None:
    premier, _ = depot_sports.resoudre_a_l_ecriture("Tennis")
    second, resolution = depot_sports.resoudre_a_l_ecriture("  tennis ")
    assert second.id == premier.id
    assert resolution.fondation is False
    assert depot_sports.compter() == 1
    # Le libellé d'origine du sport est celui de sa fondation.
    assert second.libelle == "Tennis"


def test_un_synonyme_rattache_a_l_ecriture(depot_sports: DepotSports) -> None:
    tennis_de_table, _ = depot_sports.resoudre_a_l_ecriture("Tennis de table")
    depot_sports.poser_synonyme("ping-pong", tennis_de_table.id)

    sport, resolution = depot_sports.resoudre_a_l_ecriture("Ping-Pong")
    assert sport.id == tennis_de_table.id
    assert resolution.libelle_affiche == "Ping-Pong"
    assert depot_sports.compter() == 1


def test_la_lecture_ne_consulte_jamais_la_table_de_synonymes(
    depot_sports: DepotSports,
) -> None:
    """« Synonyme à la lecture » : aucune redirection, la clé est prise telle quelle."""
    tennis_de_table, _ = depot_sports.resoudre_a_l_ecriture("Tennis de table")
    depot_sports.poser_synonyme("ping-pong", tennis_de_table.id)

    assert depot_sports.par_cle("ping-pong") is None
    assert depot_sports.par_cle("tennis de table") is not None


def test_la_table_de_synonymes_nait_vide(depot_sports: DepotSports) -> None:
    """Le mécanisme est livré, pas des données : aucun synonyme n'est fabriqué."""
    assert depot_sports.synonymes() == {}
