"""Moteur et session SQLite.

Enveloppe locale à un seul environnement : la base est un fichier à côté du dépôt et
le schéma est créé au démarrage. **Pas d'outil de migration** — Alembic serait de
l'appareillage sans usage. En contrepartie, `creer_schema` vérifie que la base en
place porte bien le schéma déclaré, et refuse de démarrer sinon : sans migration, la
seule chose qu'on ne peut pas se permettre est de dériver en silence.
"""

from __future__ import annotations

import os
from pathlib import Path

from sqlalchemy import Engine, create_engine, event, inspect as inspecter
from sqlalchemy.orm import Session, sessionmaker

__all__ = [
    "BASE_PAR_DEFAUT",
    "SchemaObsolete",
    "url_de_base",
    "creer_moteur",
    "creer_fabrique_de_sessions",
    "creer_schema",
]


class SchemaObsolete(RuntimeError):
    """Une base antérieure à une modification de schéma, que `create_all` n'atteint pas."""


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
    """Crée les tables absentes, puis exige que le schéma en place soit celui déclaré.

    Rejouable sans effet — mais **pas** rattrapant : `create_all` ne touche jamais à
    une table qui existe déjà, index compris. Une base née avant l'ajout d'un index ne
    le recevra donc jamais, et rien ne le dit : la recherche continue de rendre les
    bons profils, simplement en balayant la table. Faute d'outil de migration (voir
    `deferred-work.md`), la garde ci-dessous transforme cette dérive muette en échec
    bruyant au démarrage — c'est le seul endroit que traversent tous les points
    d'entrée.
    """
    from exaequo.adaptateurs.secondaires.persistance.modeles import Base

    if moteur.url.database and moteur.url.get_backend_name() == "sqlite":
        Path(moteur.url.database).parent.mkdir(parents=True, exist_ok=True)
    Base.metadata.create_all(moteur)
    _exiger_les_index_declares(moteur)


def _exiger_les_index_declares(moteur: Engine) -> None:
    """Refuse une base à laquelle il manque un index déclaré dans les modèles."""
    from exaequo.adaptateurs.secondaires.persistance.modeles import Base

    inspecteur = inspecter(moteur)
    manquants = sorted(
        f"{table.name}.{index.name}"
        for table in Base.metadata.tables.values()
        for index in table.indexes
        if index.name
        not in {pose["name"] for pose in inspecteur.get_indexes(table.name)}
    )
    if manquants:
        raise SchemaObsolete(
            "Base antérieure à une modification de schéma : index manquants — "
            f"{', '.join(manquants)}. `create_all` ne modifie pas une table déjà "
            "présente. Supprimer le fichier de base (ou pointer `EXAEQUO_BASE` "
            "ailleurs) pour le faire recréer ; les données d'amorçage se rechargent "
            "seules."
        )
