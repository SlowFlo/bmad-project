"""Moteur et session SQLite.

Enveloppe locale à un seul environnement : la base est un fichier à côté du dépôt et
le schéma est créé au démarrage. **Pas d'outil de migration** — Alembic serait de
l'appareillage sans usage.
"""

from __future__ import annotations

import os
from pathlib import Path

from sqlalchemy import Engine, create_engine, event
from sqlalchemy.orm import Session, sessionmaker

__all__ = [
    "BASE_PAR_DEFAUT",
    "url_de_base",
    "creer_moteur",
    "creer_fabrique_de_sessions",
    "creer_schema",
]

BASE_PAR_DEFAUT = "sqlite:///exaequo.db"


def url_de_base() -> str:
    """Rend l'URL de la base, prise de `EXAEQUO_BASE` ou, à défaut, du fichier local."""
    return os.environ.get("EXAEQUO_BASE") or BASE_PAR_DEFAUT


def creer_moteur(url: str | None = None) -> Engine:
    """Crée le moteur SQLite et active l'intégrité référentielle, que SQLite laisse
    désactivée par défaut."""
    moteur = create_engine(url or url_de_base())

    @event.listens_for(moteur, "connect")
    def _activer_les_cles_etrangeres(connexion, _record):
        curseur = connexion.cursor()
        curseur.execute("PRAGMA foreign_keys=ON")
        curseur.close()

    return moteur


def creer_fabrique_de_sessions(moteur: Engine) -> sessionmaker[Session]:
    return sessionmaker(bind=moteur, expire_on_commit=False)


def creer_schema(moteur: Engine) -> None:
    """Crée les tables absentes. Rejouable sans effet."""
    from exaequo.adaptateurs.secondaires.persistance.modeles import Base

    if moteur.url.database and moteur.url.get_backend_name() == "sqlite":
        Path(moteur.url.database).parent.mkdir(parents=True, exist_ok=True)
    Base.metadata.create_all(moteur)
