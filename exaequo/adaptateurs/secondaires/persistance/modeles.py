"""Tables du vivier : `compte`, `profil`, `jour_disponible`, `sport`, `synonyme`.

Les noms de tables et de colonnes reprennent **littéralement** le vocabulaire du
glossaire. Aucune table de rencontre, de jeton, d'envoi, d'alerte, de conversation, de
tour ni d'étape : elles arrivent avec les lots suivants.

Aucune colonne `bloque` ni `recherche_active` (AD-6), aucune colonne anticipant une
calibration du niveau — ni `mu`, ni `sigma`, ni historique de résultats.
"""

from __future__ import annotations

import datetime as dt
import uuid

from sqlalchemy import (
    CheckConstraint,
    DateTime,
    Enum,
    ForeignKey,
    Index,
    String,
    TypeDecorator,
    UniqueConstraint,
    Uuid,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from exaequo.domaine.vivier import JourSemaine, Niveau, Population, ProvenanceNumero


class HorodatageUTC(TypeDecorator):
    """Horodatage conscient du fuseau, stocké en UTC.

    SQLite ne porte pas de fuseau : le décalage est appliqué à l'écriture et l'UTC
    remis à la lecture, plutôt que d'écrire une heure locale muette.
    """

    impl = DateTime
    cache_ok = True

    def process_bind_param(self, value, dialect):
        if value is None:
            return None
        if value.tzinfo is None:
            raise ValueError("un horodatage doit porter son fuseau")
        return value.astimezone(dt.UTC).replace(tzinfo=None)

    def process_result_value(self, value, dialect):
        if value is None:
            return None
        return value.replace(tzinfo=dt.UTC)


def _litteral_sql(valeur: str) -> str:
    """Rend une chaîne SQL littérale, apostrophes échappées.

    Les contraintes de vérification sont du SQL brut : la valeur d'une énumération y
    est **dérivée du domaine**, jamais recopiée. Un renommage casse alors le schéma
    au lieu de désactiver la contrainte en silence.
    """
    return "'" + valeur.replace("'", "''") + "'"


def _enum(enumeration: type) -> Enum:
    """Énumération stockée par sa valeur, avec sa contrainte de vérification."""
    return Enum(
        enumeration,
        native_enum=False,
        values_callable=lambda membres: [membre.value for membre in membres],
        name=f"enum_{enumeration.__name__.lower()}",
        validate_strings=True,
    )


class Base(DeclarativeBase):
    pass


class CompteORM(Base):
    __tablename__ = "compte"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    courriel: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    cree_le: Mapped[dt.datetime] = mapped_column(HorodatageUTC, nullable=False)


class SportORM(Base):
    """Un sport : sa **clé normalisée**, unique, et son libellé d'origine (AD-5)."""

    __tablename__ = "sport"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    cle: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    libelle: Mapped[str] = mapped_column(String, nullable=False)
    cree_le: Mapped[dt.datetime] = mapped_column(HorodatageUTC, nullable=False)


class SynonymeORM(Base):
    """Une clé qui en désigne une autre. Consultée **à l'écriture uniquement**."""

    __tablename__ = "synonyme"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    cle: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    sport_id: Mapped[uuid.UUID] = mapped_column(
        Uuid, ForeignKey("sport.id"), nullable=False
    )


class ProfilORM(Base):
    __tablename__ = "profil"
    __table_args__ = (
        CheckConstraint(
            "(telephone IS NULL) = (provenance_numero IS NULL)",
            name="ck_profil_provenance_avec_numero",
        ),
        CheckConstraint(
            f"(population <> {_litteral_sql(Population.AMORCAGE.value)}) "
            "OR (cle_amorcage IS NOT NULL)",
            name="ck_profil_amorcage_porte_sa_cle",
        ),
        #: « Chercher les profils d'un sport » est l'accès central de la recherche
        #: (DW-1) : SQLite n'indexe pas les clés étrangères, et sans cet index il
        #: balaie `profil` à chaque recherche.
        #:
        #: **Composite, et dans cet ordre** : `sport_id` sert la jointure, `id` sert
        #: le `ORDER BY profil.id` qui la suit — l'*ordre du vivier*, dont 2.3 a
        #: besoin pour départager les ex æquo. Sur le seul `sport_id`, SQLite
        #: retrouve bien les lignes mais les retrie dans un `USE TEMP B-TREE`.
        Index("ix_profil_sport_id", "sport_id", "id"),
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    prenom: Mapped[str] = mapped_column(String, nullable=False)
    nom: Mapped[str | None] = mapped_column(String, nullable=True)
    population: Mapped[Population] = mapped_column(_enum(Population), nullable=False)

    sport_id: Mapped[uuid.UUID] = mapped_column(Uuid, ForeignKey("sport.id"), nullable=False)
    #: Le libellé tel que la personne l'a dit ; l'appariement passe par `sport_id`.
    libelle_sport: Mapped[str] = mapped_column(String, nullable=False)
    #: `NULL` est le *niveau inconnu* — une absence, pas une quatrième valeur.
    niveau: Mapped[Niveau | None] = mapped_column(_enum(Niveau), nullable=True)

    telephone: Mapped[str | None] = mapped_column(String, nullable=True)
    provenance_numero: Mapped[ProvenanceNumero | None] = mapped_column(
        _enum(ProvenanceNumero), nullable=True
    )
    courriel: Mapped[str | None] = mapped_column(String, nullable=True)
    secteur: Mapped[str | None] = mapped_column(String, nullable=True)
    compte_id: Mapped[uuid.UUID | None] = mapped_column(
        Uuid, ForeignKey("compte.id"), nullable=True, unique=True
    )

    #: Clé naturelle stable de l'amorçage : le numéro du fichier, pour les seuls
    #: profils d'amorçage. Elle ne contraint jamais un utilisateur inscrit (AD-16).
    cle_amorcage: Mapped[str | None] = mapped_column(String, nullable=True, unique=True)

    cree_le: Mapped[dt.datetime] = mapped_column(HorodatageUTC, nullable=False)
    #: Posée et jamais lue en v1 (QO-6).
    derniere_activite: Mapped[dt.datetime | None] = mapped_column(
        HorodatageUTC, nullable=True
    )
    #: Posée et jamais lue en v1 : E6 la franchit, E2 la filtrera.
    sortie_vivier_le: Mapped[dt.datetime | None] = mapped_column(
        HorodatageUTC, nullable=True
    )


class JourDisponibleORM(Base):
    """Un jour de la semaine, sans heure. L'heure appartient à la rencontre."""

    __tablename__ = "jour_disponible"
    __table_args__ = (
        UniqueConstraint("profil_id", "jour", name="uq_jour_disponible_profil_jour"),
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    profil_id: Mapped[uuid.UUID] = mapped_column(
        Uuid, ForeignKey("profil.id"), nullable=False
    )
    jour: Mapped[JourSemaine] = mapped_column(_enum(JourSemaine), nullable=False)
