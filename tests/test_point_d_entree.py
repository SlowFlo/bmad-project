"""Le point d'entrée `python -m exaequo` et la variable qui nomme la base.

Sans ces cas, renommer `EXAEQUO_BASE` ou casser `principal()` laisserait la suite
verte alors que la commande de vérification de la spec ne fonctionnerait plus.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from exaequo.__main__ import principal
from exaequo.adaptateurs.secondaires.persistance.base import (
    BASE_PAR_DEFAUT,
    creer_fabrique_de_sessions,
    creer_moteur,
    url_de_base,
)
from exaequo.adaptateurs.secondaires.persistance.depots import DepotSports, DepotVivier


def test_url_de_base_lit_la_variable_d_environnement(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("EXAEQUO_BASE", "sqlite:///ailleurs.db")
    assert url_de_base() == "sqlite:///ailleurs.db"


def test_url_de_base_retombe_sur_le_fichier_local(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv("EXAEQUO_BASE", raising=False)
    assert url_de_base() == BASE_PAR_DEFAUT
    assert BASE_PAR_DEFAUT == "sqlite:///exaequo.db"


def test_une_variable_vide_retombe_sur_le_fichier_local(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("EXAEQUO_BASE", "")
    assert url_de_base() == BASE_PAR_DEFAUT


def _decompte(url: str) -> tuple[int, int]:
    moteur = creer_moteur(url)
    try:
        with creer_fabrique_de_sessions(moteur)() as session:
            return DepotVivier(session).compter(), DepotSports(session).compter()
    finally:
        moteur.dispose()


def test_amorcer_seulement_charge_le_vivier_et_rend_la_main(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    url = f"sqlite:///{tmp_path / 'vivier.db'}"
    monkeypatch.setenv("EXAEQUO_BASE", url)

    assert principal(["--amorcer-seulement"]) == 0

    assert _decompte(url) == (86, 11)


def test_amorcer_seulement_est_rejouable(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Deux passages de suite : 86 profils et 11 sports aux deux."""
    url = f"sqlite:///{tmp_path / 'vivier.db'}"
    monkeypatch.setenv("EXAEQUO_BASE", url)

    assert principal(["--amorcer-seulement"]) == 0
    premier = _decompte(url)
    assert principal(["--amorcer-seulement"]) == 0
    second = _decompte(url)

    assert premier == (86, 11)
    assert second == premier


def test_une_option_inconnue_est_refusee() -> None:
    with pytest.raises(SystemExit):
        principal(["--inconnue"])
