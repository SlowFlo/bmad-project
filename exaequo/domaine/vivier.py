"""Le vivier : profils, populations, provenance des numéros.

Le vivier est l'ensemble des profils parmi lesquels le bot cherche. Il contient des
*profils d'amorçage* et des *utilisateurs inscrits* ; il grossit à chaque compte créé
et ne diminue que par une sortie définitive.

Module pur : aucune dépendance sortante (AD-1). Aucun champ `bloque` ni
`recherche_active` : les deux sont dérivés (AD-6) et leur dérivation n'appartient pas
à ce lot.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import StrEnum
from typing import Self
from uuid import UUID

from exaequo.domaine.sports import replier_texte

__all__ = [
    "Niveau",
    "JourSemaine",
    "Population",
    "ProvenanceNumero",
    "Compte",
    "Sport",
    "Synonyme",
    "Profil",
]


class _EnumLibelle(StrEnum):
    """Énumération dont les membres se retrouvent depuis leur libellé français."""

    @classmethod
    def depuis_libelle(cls, libelle: str) -> Self:
        """Rend le membre désigné par un libellé français, quelles que soient la
        casse et les accents. Lève `ValueError` sur un libellé inconnu."""
        replie = replier_texte(libelle)
        for membre in cls:
            if membre.value == replie:
                return membre
        raise ValueError(f"{cls.__name__} : libellé inconnu {libelle!r}")


class Niveau(_EnumLibelle):
    """Le niveau déclaré par la personne, demandé une fois, jamais vérifié.

    Le *niveau inconnu* n'est **pas** une quatrième valeur : c'est une absence,
    portée par `Profil.niveau is None`.
    """

    DEBUTANT = "debutant"
    INTERMEDIAIRE = "intermediaire"
    AVANCE = "avance"


class JourSemaine(_EnumLibelle):
    """Un jour de la semaine, sans heure. Le vivier ne connaît que des jours."""

    LUNDI = "lundi"
    MARDI = "mardi"
    MERCREDI = "mercredi"
    JEUDI = "jeudi"
    VENDREDI = "vendredi"
    SAMEDI = "samedi"
    DIMANCHE = "dimanche"


class Population(StrEnum):
    """La population dont relève un profil. Portée dans le modèle, jamais déduite
    d'un préfixe ni d'une colonne vide (AD-11)."""

    AMORCAGE = "amorcage"
    INSCRIT = "inscrit"


class ProvenanceNumero(StrEnum):
    """La provenance d'un numéro de téléphone (AD-11).

    Le filtre de destinataire d'AD-12 lira cette valeur, jamais le préfixe du numéro.
    """

    DONNEE_AMORCAGE = "donnee d'amorcage"
    SAISIE_PAR_UTILISATEUR_INSCRIT = "saisie par un utilisateur inscrit"


@dataclass(frozen=True, slots=True)
class Compte:
    """Le compte d'un utilisateur inscrit : la clé d'identité de son profil.

    Optionnel des deux côtés — un profil d'amorçage n'en a pas.
    """

    id: UUID
    courriel: str
    cree_le: datetime


@dataclass(frozen=True, slots=True)
class Sport:
    """Un sport du vivier : une **clé** normalisée et un libellé d'origine.

    `SPORT` est une entité et non une colonne, pour que la fusion de deux libellés
    reste une opération et non une reprise de données.
    """

    id: UUID
    cle: str
    libelle: str


@dataclass(frozen=True, slots=True)
class Synonyme:
    """Une clé qui en désigne une autre. Redirige **à l'écriture uniquement** (AD-5).

    La table naît vide : c'est le mécanisme qui est livré, pas des données.
    """

    id: UUID
    cle: str
    sport_id: UUID


@dataclass(frozen=True, slots=True)
class Profil:
    """Un profil du vivier, quelle que soit sa population.

    `libelle_sport` est le libellé tel que la personne l'a dit ; l'appariement, lui,
    passe par `sport_id` et la clé du sport (AD-5). `niveau` à `None` est le *niveau
    inconnu* : le profil ne sort d'aucune recherche et ne peut pas non plus chercher.
    """

    id: UUID
    prenom: str
    population: Population
    sport_id: UUID
    libelle_sport: str
    jours_disponibles: frozenset[JourSemaine] = field(default_factory=frozenset)
    niveau: Niveau | None = None
    nom: str | None = None
    telephone: str | None = None
    provenance_numero: ProvenanceNumero | None = None
    courriel: str | None = None
    secteur: str | None = None
    compte_id: UUID | None = None
    cle_amorcage: str | None = None
    cree_le: datetime | None = None
    derniere_activite: datetime | None = None
    sortie_vivier_le: datetime | None = None
