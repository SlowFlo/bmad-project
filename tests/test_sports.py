"""La clé de sport normalisée et la résolution d'un libellé (AD-5).

Couvre les six premières lignes de la matrice d'E/S du lot.
"""

from __future__ import annotations

import pytest

from exaequo.amorcage.lecture import lire_donnees_amorcage
from exaequo.domaine.sports import cle_sport, resoudre_libelle


@pytest.mark.parametrize("libelle", ["Tennis", "tennis", "  TENNIS  ", "TeNNiS"])
def test_la_casse_et_les_espaces_ne_font_qu_une_seule_cle(libelle: str) -> None:
    assert cle_sport(libelle) == "tennis"


def test_les_espaces_internes_sont_reduits() -> None:
    assert cle_sport("Course   à\tpied") == "course a pied"


@pytest.mark.parametrize(
    ("libelle", "attendue"),
    [
        ("Course à pied", "course a pied"),
        ("Basket-ball", "basket-ball"),
        ("Volley-ball", "volley-ball"),
        ("PILATES", "pilates"),
    ],
)
def test_les_accents_sont_retires_et_le_trait_d_union_conserve(
    libelle: str, attendue: str
) -> None:
    assert cle_sport(libelle) == attendue


def test_les_onze_libelles_du_fichier_donnent_onze_cles(chemin_donnees_amorcage) -> None:
    """Onze clés, pas douze : la normalisation ne pulvérise pas le vivier."""
    libelles = {profil.libelle_sport for profil in lire_donnees_amorcage()}
    assert len(libelles) == 11
    assert len({cle_sport(libelle) for libelle in libelles}) == 11


def test_un_synonyme_redirige_a_l_ecriture() -> None:
    resolution = resoudre_libelle(
        "Ping-Pong",
        cles_connues={"tennis de table"},
        synonymes={"ping-pong": "tennis de table"},
    )
    assert resolution.cle == "tennis de table"
    assert resolution.fondation is False
    # Le libellé affiché est conservé tel que la personne l'a dit.
    assert resolution.libelle_affiche == "Ping-Pong"


def test_un_libelle_connu_ne_fonde_rien() -> None:
    resolution = resoudre_libelle("tennis", cles_connues={"tennis"}, synonymes={})
    assert resolution == type(resolution)(
        cle="tennis", libelle_affiche="tennis", fondation=False
    )


def test_un_libelle_inconnu_fonde_un_sport_et_ne_refuse_jamais() -> None:
    resolution = resoudre_libelle("Squash", cles_connues={"tennis"}, synonymes={})
    assert resolution.cle == "squash"
    assert resolution.fondation is True
    assert resolution.libelle_affiche == "Squash"


def test_le_synonyme_est_consulte_avant_le_sport_existant() -> None:
    """L'ordre est : synonyme, puis sport existant, puis fondation."""
    resolution = resoudre_libelle(
        "Ping-Pong",
        cles_connues={"ping-pong", "tennis de table"},
        synonymes={"ping-pong": "tennis de table"},
    )
    assert resolution.cle == "tennis de table"
