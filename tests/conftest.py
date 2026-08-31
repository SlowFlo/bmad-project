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


#: Le nombre de profils que porte le CSV d'amorçage. Les repères de mise au point ne
#: valent que sur ce jeu-là : s'il change, ils doivent être relus, pas rattrapés.
PROFILS_D_AMORCAGE = 86


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
    resultat = charger_donnees_amorcage(session)
    assert resultat.inseres == PROFILS_D_AMORCAGE, (
        f"le vivier d'amorçage a inséré {resultat.inseres} profils au lieu de "
        f"{PROFILS_D_AMORCAGE} : les repères qui en dépendent — « Tennis, mardi, "
        f"débutant » rend Emma Leroy — ne veulent alors plus rien dire."
    )
    session.commit()
    return session
