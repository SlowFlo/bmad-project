"""AD-1 : le domaine n'a aucune dépendance sortante.

Le test lit les modules de `exaequo/domaine/` avec `ast` plutôt que de les importer :
un import réussi ne prouverait rien, l'adaptateur pouvant déjà être chargé.
"""

from __future__ import annotations

import ast
from pathlib import Path

import pytest

RACINE_DU_PROJET = Path(__file__).resolve().parents[1]
RACINE_DU_DOMAINE = RACINE_DU_PROJET / "exaequo" / "domaine"

#: Ce qu'un module du domaine ne peut pas importer, à aucune profondeur.
INTERDITS = ("sqlalchemy", "fastapi", "anthropic", "uvicorn", "exaequo.adaptateurs")


def _modules_du_domaine() -> list[Path]:
    return sorted(RACINE_DU_DOMAINE.rglob("*.py"))


def _paquet_de(module: Path) -> str:
    """Le nom de paquet pointé du module, p. ex. `exaequo.domaine`."""
    relatif = module.relative_to(RACINE_DU_PROJET).with_suffix("")
    parties = list(relatif.parts)
    if parties[-1] == "__init__":
        parties.pop()
    else:
        parties.pop()  # le paquet est celui qui contient le module
    return ".".join(parties)


def _resoudre(nom: str | None, niveau: int, module: Path) -> str | None:
    """Rend le nom absolu d'un `from ... import`, relatif comme absolu.

    Un import relatif n'est pas réputé rester dans le paquet : `from ..adaptateurs
    import ...` sort du domaine et doit être vu comme tel.
    """
    if not niveau:
        return nom
    parties = _paquet_de(module).split(".")
    remontee = niveau - 1
    if remontee:
        parties = parties[:-remontee] if remontee < len(parties) else []
    return ".".join([*parties, nom]) if nom else ".".join(parties)


def _imports(module: Path) -> set[str]:
    arbre = ast.parse(module.read_text(encoding="utf-8"), filename=str(module))
    noms: set[str] = set()
    for noeud in ast.walk(arbre):
        if isinstance(noeud, ast.Import):
            noms.update(alias.name for alias in noeud.names)
        elif isinstance(noeud, ast.ImportFrom):
            resolu = _resoudre(noeud.module, noeud.level, module)
            if resolu:
                noms.add(resolu)
    return noms


def test_le_domaine_a_bien_des_modules() -> None:
    assert _modules_du_domaine(), "aucun module de domaine trouvé"


def _est_interdit(nom: str) -> bool:
    return any(
        nom == interdit or nom.startswith(interdit + ".") for interdit in INTERDITS
    )


@pytest.mark.parametrize(
    "module", _modules_du_domaine(), ids=lambda chemin: chemin.name
)
def test_aucun_module_du_domaine_n_importe_un_adaptateur(module: Path) -> None:
    for importe in _imports(module):
        assert not _est_interdit(importe), f"{module.name} importe {importe}"


def test_un_import_relatif_est_resolu_en_nom_absolu() -> None:
    """Sans résolution, `from ..adaptateurs import ...` passerait sous le radar."""
    module = RACINE_DU_DOMAINE / "vivier.py"
    assert _resoudre("sports", 1, module) == "exaequo.domaine.sports"
    assert _resoudre(None, 1, module) == "exaequo.domaine"
    assert (
        _resoudre("adaptateurs.secondaires", 2, module)
        == "exaequo.adaptateurs.secondaires"
    )


def test_un_import_relatif_vers_un_adaptateur_serait_refuse() -> None:
    """Garde-fou : le nom résolu doit bien tomber sous l'interdiction d'AD-1."""
    module = RACINE_DU_DOMAINE / "vivier.py"
    # `_resoudre` peut rendre `None` — pour un `from . import x` sans module. Ici
    # les deux noms sont donnés : la résolution rend toujours une chaîne, et
    # l'affirmer le dit au vérificateur autant qu'au lecteur.
    sortant = _resoudre("adaptateurs.secondaires.persistance", 2, module)
    interne = _resoudre("sports", 1, module)
    assert sortant is not None
    assert interne is not None
    assert _est_interdit(sortant)
    assert not _est_interdit(interne)


@pytest.mark.parametrize(
    "module", _modules_du_domaine(), ids=lambda chemin: chemin.name
)
def test_le_domaine_ne_sort_pas_de_lui_meme(module: Path) -> None:
    """Un module du domaine n'importe du projet que le domaine lui-même."""
    for importe in _imports(module):
        if importe.startswith("exaequo"):
            assert importe.startswith("exaequo.domaine"), (
                f"{module.name} importe {importe}"
            )
