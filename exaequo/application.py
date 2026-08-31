"""Racine de composition.

Le `lifespan` crée le schéma puis déclenche l'amorçage. **Aucune route** : l'adaptateur
web — le fil, le flux SSE, la page d'acceptation — arrive avec E3.
"""

from __future__ import annotations

import logging
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from sqlalchemy import Engine

from exaequo.adaptateurs.secondaires.persistance.base import (
    creer_fabrique_de_sessions,
    creer_moteur,
    creer_schema,
)
from exaequo.amorcage.chargement import ResultatAmorcage, charger_donnees_amorcage

__all__ = ["preparer_le_vivier", "creer_application"]

journal = logging.getLogger("exaequo")


def preparer_le_vivier(
    moteur: Engine, chemin_donnees: Path | None = None
) -> ResultatAmorcage:
    """Crée le schéma puis charge les données d'amorçage, en une seule transaction.

    Rejouable sans effet : la deuxième exécution n'insère rien. Une donnée invalide
    annule la transaction et remonte — un échec bruyant, jamais un vivier à moitié
    peuplé.
    """
    creer_schema(moteur)
    fabrique = creer_fabrique_de_sessions(moteur)
    with fabrique() as session:
        try:
            resultat = charger_donnees_amorcage(session, chemin_donnees)
            session.commit()
        except Exception:
            session.rollback()
            raise
    return resultat


def creer_application(
    url_base: str | None = None, chemin_donnees: Path | None = None
) -> FastAPI:
    """Compose l'application : moteur, schéma, amorçage. Sans aucune route."""

    @asynccontextmanager
    async def cycle_de_vie(application: FastAPI) -> AsyncIterator[None]:
        moteur = creer_moteur(url_base)
        application.state.moteur = moteur
        application.state.fabrique_de_sessions = creer_fabrique_de_sessions(moteur)
        resultat = preparer_le_vivier(moteur, chemin_donnees)
        application.state.amorcage = resultat
        journal.info(
            "vivier prêt : %d profils lus, %d insérés, %d déjà présents",
            resultat.lus,
            resultat.inseres,
            resultat.deja_presents,
        )
        try:
            yield
        finally:
            moteur.dispose()

    return FastAPI(title="Ex Aequo", lifespan=cycle_de_vie)


application = creer_application()
