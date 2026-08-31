"""Lecture des données d'amorçage : ce que le fichier contient, et ce qu'il refuse."""

from __future__ import annotations

import pytest

from exaequo.amorcage.lecture import (
    ErreurDonneesAmorcage,
    lire_donnees_amorcage,
)
from exaequo.domaine.vivier import JourSemaine, Niveau

_EN_TETE = (
    "Prénom,Nom,Numéro de téléphone,Sports pratiqués,Jours disponibles,Niveau\n"
)


def _fichier(tmp_path, corps: str, fin_de_ligne: str = "\n"):
    chemin = tmp_path / "amorcage.csv"
    contenu = (_EN_TETE + corps).replace("\n", fin_de_ligne)
    chemin.write_bytes(contenu.encode("utf-8"))
    return chemin


def test_le_fichier_porte_quatre_vingt_six_profils() -> None:
    profils = lire_donnees_amorcage()
    assert len(profils) == 86


def test_les_numeros_sont_uniques_et_dans_la_plage_de_fiction_arcep() -> None:
    profils = lire_donnees_amorcage()
    numeros = [profil.telephone for profil in profils]
    assert len(set(numeros)) == 86
    assert all(numero.startswith("+336399800") for numero in numeros)
    assert numeros[0] == "+33639980001"
    assert numeros[-1] == "+33639980086"


def test_les_jours_et_les_niveaux_sont_des_valeurs_du_domaine() -> None:
    profils = lire_donnees_amorcage()
    assert all(profil.niveau in set(Niveau) for profil in profils)
    for profil in profils:
        assert profil.jours_disponibles
        assert profil.jours_disponibles <= set(JourSemaine)


def test_le_premier_profil_est_lu_tel_quel() -> None:
    premier = lire_donnees_amorcage()[0]
    assert premier.prenom == "Lucas"
    assert premier.nom == "Moreau"
    assert premier.libelle_sport == "Football"
    assert premier.niveau is Niveau.INTERMEDIAIRE
    assert premier.jours_disponibles == frozenset(
        {JourSemaine.LUNDI, JourSemaine.MERCREDI, JourSemaine.VENDREDI}
    )
    assert premier.cle_amorcage == premier.telephone


@pytest.mark.parametrize("fin_de_ligne", ["\n", "\r\n"])
def test_les_deux_fins_de_ligne_sont_lues(tmp_path, fin_de_ligne: str) -> None:
    chemin = _fichier(
        tmp_path, "Emma,Leroy,+33639980002,Tennis,Mardi;Jeudi,Débutant\n", fin_de_ligne
    )
    profils = lire_donnees_amorcage(chemin)
    assert len(profils) == 1
    assert profils[0].niveau is Niveau.DEBUTANT


def test_un_niveau_absent_est_le_niveau_inconnu(tmp_path) -> None:
    """Le niveau inconnu est une absence, pas une quatrième valeur d'énumération."""
    chemin = _fichier(tmp_path, "Emma,Leroy,+33639980002,Tennis,Mardi;Jeudi,\n")
    assert lire_donnees_amorcage(chemin)[0].niveau is None


@pytest.mark.parametrize(
    "ligne",
    [
        "Emma,Leroy,+33639980002,Tennis,Mardi;Jeudi,Expert\n",  # niveau inconnu
        "Emma,Leroy,+33639980002,Tennis,Marsdi,Débutant\n",  # jour inconnu
        "Emma,Leroy,+33639980002,Tennis,,Débutant\n",  # aucun jour
        "Emma,Leroy,,Tennis,Mardi,Débutant\n",  # pas de numéro
        ",Leroy,+33639980002,Tennis,Mardi,Débutant\n",  # pas de prénom
        "Emma,Leroy,+33639980002,,Mardi,Débutant\n",  # pas de sport
        "Emma,Leroy,+33639980002,Tennis,Mardi\n",  # colonne manquante
    ],
)
def test_une_ligne_invalide_echoue_bruyamment(tmp_path, ligne: str) -> None:
    chemin = _fichier(tmp_path, ligne)
    with pytest.raises(ErreurDonneesAmorcage):
        lire_donnees_amorcage(chemin)


def test_un_numero_en_double_echoue_bruyamment(tmp_path) -> None:
    chemin = _fichier(
        tmp_path,
        "Emma,Leroy,+33639980002,Tennis,Mardi,Débutant\n"
        "Iris,Petit,+33639980002,Tennis,Jeudi,Avancé\n",
    )
    with pytest.raises(ErreurDonneesAmorcage):
        lire_donnees_amorcage(chemin)


def test_un_en_tete_inattendu_echoue_bruyamment(tmp_path) -> None:
    chemin = tmp_path / "amorcage.csv"
    chemin.write_text("Prenom,Nom\nEmma,Leroy\n", encoding="utf-8")
    with pytest.raises(ErreurDonneesAmorcage):
        lire_donnees_amorcage(chemin)


def test_un_fichier_absent_echoue_bruyamment(tmp_path) -> None:
    with pytest.raises(ErreurDonneesAmorcage):
        lire_donnees_amorcage(tmp_path / "absent.csv")
