"""Fixtures partagées : un vivier vide, un vivier amorcé, et le chemin des données."""

from __future__ import annotations

from collections.abc import Iterator

import pytest
from sqlalchemy import Engine
from sqlalchemy.orm import Session

from exaequo.adaptateurs.secondaires.persistance.base import (
    creer_fabrique_de_sessions,
    creer_moteur,
    creer_schema,
)
from exaequo.adaptateurs.secondaires.persistance.depots import DepotSports, DepotVivier
from exaequo.amorcage.chargement import charger_donnees_amorcage
from exaequo.amorcage.lecture import CHEMIN_DONNEES_AMORCAGE


@pytest.fixture
def chemin_donnees_amorcage():
    return CHEMIN_DONNEES_AMORCAGE


@pytest.fixture
def moteur(tmp_path) -> Iterator[Engine]:
    """Une base fichier neuve par test : la même forme qu'en exécution réelle."""
    moteur = creer_moteur(f"sqlite:///{tmp_path / 'vivier.db'}")
    creer_schema(moteur)
    try:
        yield moteur
    finally:
        moteur.dispose()


@pytest.fixture
def session(moteur: Engine) -> Iterator[Session]:
    fabrique = creer_fabrique_de_sessions(moteur)
    with fabrique() as ouverte:
        yield ouverte


@pytest.fixture
def depot_sports(session: Session) -> DepotSports:
    return DepotSports(session)


@pytest.fixture
def depot_vivier(session: Session) -> DepotVivier:
    return DepotVivier(session)


@pytest.fixture
def vivier_amorce(session: Session) -> Session:
    """Une session dont le vivier porte les 86 profils d'amorçage, commités.

    Les repères de mise au point — « Tennis, mardi, débutant » rend Emma Leroy — ne
    valent que sur ces données-là : la fixture les charge par le chemin réel du
    produit, jamais par un jeu d'essai réécrit à côté.
    """
    charger_donnees_amorcage(session)
    session.commit()
    return session
