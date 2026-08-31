"""Les critères d'acceptation du lot, joués sur la racine de composition."""

from __future__ import annotations

from pathlib import Path

import pytest
from sqlalchemy import text

from exaequo.adaptateurs.secondaires.persistance.base import (
    SchemaObsolete,
    creer_fabrique_de_sessions,
    creer_moteur,
)
from exaequo.adaptateurs.secondaires.persistance.depots import DepotSports, DepotVivier
from exaequo.application import creer_application, preparer_le_vivier


def test_deux_demarrages_de_suite_laissent_quatre_vingt_six_profils(
    tmp_path: Path,
) -> None:
    url = f"sqlite:///{tmp_path / 'vivier.db'}"
    decomptes = []

    for _ in range(2):
        moteur = creer_moteur(url)
        try:
            preparer_le_vivier(moteur)
            fabrique = creer_fabrique_de_sessions(moteur)
            with fabrique() as session:
                decomptes.append(
                    (
                        DepotVivier(session).compter(),
                        DepotSports(session).compter(),
                        DepotVivier(session).compter_jours_disponibles(),
                    )
                )
        finally:
            moteur.dispose()

    assert decomptes[0][0] == 86
    assert decomptes[0][1] == 11
    # Aucun jour disponible n'est dupliqué : le second passage n'ajoute rien.
    assert decomptes[0] == decomptes[1]


def test_une_base_privee_de_son_index_refuse_de_demarrer(tmp_path: Path) -> None:
    """`create_all` n'atteint pas une table déjà là : la dérive doit être bruyante.

    Le cas réel est celui d'un `exaequo.db` né avant 2.1 : il porte déjà `profil`,
    donc `create_all` le laisse tel quel et `ix_profil_sport_id` n'y arrive jamais.
    On le reproduit en privant une base saine de son index — c'est le seul test qui
    emprunte ce chemin, toutes les fixtures fabriquant par ailleurs des bases neuves,
    où le défaut est par construction invisible.
    """
    url = f"sqlite:///{tmp_path / 'vivier.db'}"
    moteur = creer_moteur(url)
    try:
        preparer_le_vivier(moteur)
        with moteur.begin() as connexion:
            connexion.execute(text("DROP INDEX ix_profil_sport_id"))
    finally:
        moteur.dispose()

    moteur = creer_moteur(url)
    try:
        with pytest.raises(SchemaObsolete, match="ix_profil_sport_id"):
            preparer_le_vivier(moteur)
    finally:
        moteur.dispose()


#: Ce que FastAPI installe de lui-même, sans qu'on lui demande rien. Toute autre
#: route serait une route du produit — et le produit n'en pose aucune en E1.
ROUTES_PAR_DEFAUT_DE_FASTAPI = {
    "/openapi.json",
    "/docs",
    "/docs/oauth2-redirect",
    "/redoc",
}


def test_l_application_ne_pose_aucune_route(tmp_path: Path) -> None:
    """E1 est la racine de composition ; l'adaptateur web arrive avec E3.

    Toutes les routes sont comparées, y compris hors schéma, WebSocket et montages :
    filtrer sur `include_in_schema` rendrait le test tautologique, les routes par
    défaut de FastAPI portant précisément cet attribut à faux.
    """
    application = creer_application(f"sqlite:///{tmp_path / 'vivier.db'}")
    chemins = {getattr(route, "path", None) for route in application.routes}
    assert chemins == ROUTES_PAR_DEFAUT_DE_FASTAPI


def test_le_test_de_route_verrait_une_route_ajoutee(tmp_path: Path) -> None:
    """Garde-fou du test précédent : il doit échouer dès qu'une route apparaît."""
    application = creer_application(f"sqlite:///{tmp_path / 'vivier.db'}")

    @application.get("/temoin", include_in_schema=False)
    def _temoin() -> dict[str, str]:  # pragma: no cover - jamais appelée
        return {}

    chemins = {getattr(route, "path", None) for route in application.routes}
    assert chemins != ROUTES_PAR_DEFAUT_DE_FASTAPI
    assert "/temoin" in chemins


def test_le_cycle_de_vie_amorce_le_vivier(tmp_path: Path) -> None:
    """Le `lifespan` crée le schéma puis déclenche l'amorçage.

    Il est joué directement plutôt que par un client de test : le socle n'a pas de
    client HTTP, et il n'a rien à servir.
    """
    import asyncio

    application = creer_application(f"sqlite:///{tmp_path / 'vivier.db'}")

    async def demarrer_puis_verifier() -> None:
        async with application.router.lifespan_context(application):
            assert application.state.amorcage.inseres == 86
            with creer_fabrique_de_sessions(application.state.moteur)() as session:
                assert DepotVivier(session).compter() == 86
                assert DepotSports(session).compter() == 11

    asyncio.run(demarrer_puis_verifier())
