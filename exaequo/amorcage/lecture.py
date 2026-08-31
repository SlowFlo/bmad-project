"""Lecture des données d'amorçage : le CSV vers les types du domaine.

Le fichier porte 86 profils, un en-tête, des jours séparés par `;` et des numéros de
la plage de fiction ARCEP `+336 39 98 XX XX`. Une ligne invalide **échoue bruyamment**
— aucune valeur par défaut n'est substituée, rien n'est inventé.
"""

from __future__ import annotations

import csv
from collections.abc import Iterator
from dataclasses import dataclass
from pathlib import Path

from exaequo.domaine.vivier import JourSemaine, Niveau

__all__ = [
    "CHEMIN_DONNEES_AMORCAGE",
    "ErreurDonneesAmorcage",
    "ProfilAmorcage",
    "lire_donnees_amorcage",
]

#: Le fichier des données d'amorçage. Seule étiquette employée pour ce fichier.
CHEMIN_DONNEES_AMORCAGE = (
    Path(__file__).resolve().parents[2]
    / "documentation"
    / "planning-artifacts"
    / "prds"
    / "prd-bmad-2026-08-26"
    / "SportsProfiles.csv"
)

_EN_TETE = (
    "Prénom",
    "Nom",
    "Numéro de téléphone",
    "Sports pratiqués",
    "Jours disponibles",
    "Niveau",
)


class ErreurDonneesAmorcage(Exception):
    """Une ligne des données d'amorçage est inexploitable.

    Elle interrompt le chargement : la transaction est annulée et rien n'est chargé
    à moitié.
    """


@dataclass(frozen=True, slots=True)
class ProfilAmorcage:
    """Une ligne des données d'amorçage, portée par les types du domaine.

    `cle_amorcage` est la clé naturelle stable sur laquelle porte l'idempotence : le
    numéro de téléphone, unique dans le fichier.
    """

    prenom: str
    nom: str
    telephone: str
    libelle_sport: str
    jours_disponibles: frozenset[JourSemaine]
    niveau: Niveau | None

    @property
    def cle_amorcage(self) -> str:
        return self.telephone


def _exiger(valeur: str | None, colonne: str, numero_de_ligne: int) -> str:
    if valeur is None or not valeur.strip():
        raise ErreurDonneesAmorcage(
            f"ligne {numero_de_ligne} : colonne « {colonne} » vide"
        )
    return valeur.strip()


def _lire_jours(brut: str, numero_de_ligne: int) -> frozenset[JourSemaine]:
    jours: set[JourSemaine] = set()
    for morceau in brut.split(";"):
        libelle = morceau.strip()
        if not libelle:
            continue
        try:
            jours.add(JourSemaine.depuis_libelle(libelle))
        except ValueError as cause:
            raise ErreurDonneesAmorcage(
                f"ligne {numero_de_ligne} : jour inconnu « {libelle} »"
            ) from cause
    if not jours:
        raise ErreurDonneesAmorcage(
            f"ligne {numero_de_ligne} : aucun jour disponible"
        )
    return frozenset(jours)


def _lire_niveau(brut: str, numero_de_ligne: int) -> Niveau | None:
    """Un niveau absent est le *niveau inconnu* : `None`, jamais une quatrième valeur."""
    libelle = brut.strip()
    if not libelle:
        return None
    try:
        return Niveau.depuis_libelle(libelle)
    except ValueError as cause:
        raise ErreurDonneesAmorcage(
            f"ligne {numero_de_ligne} : niveau inconnu « {libelle} »"
        ) from cause


def lire_donnees_amorcage(
    chemin: Path | None = None,
) -> list[ProfilAmorcage]:
    """Lit le fichier en entier et rend ses profils dans **l'ordre du fichier**.

    L'ordre est significatif : il devient l'ordre du vivier une fois les profils
    insérés (CAP-6).
    """
    return list(_lire(chemin or CHEMIN_DONNEES_AMORCAGE))


def _lire(chemin: Path) -> Iterator[ProfilAmorcage]:
    if not chemin.is_file():
        raise ErreurDonneesAmorcage(f"données d'amorçage introuvables : {chemin}")

    # `newline=""` laisse le module csv gérer les fins de ligne, CRLF comme LF.
    with chemin.open("r", encoding="utf-8-sig", newline="") as fichier:
        lecteur = csv.reader(fichier)
        try:
            en_tete = next(lecteur)
        except StopIteration as cause:
            raise ErreurDonneesAmorcage("données d'amorçage vides") from cause

        if tuple(colonne.strip() for colonne in en_tete) != _EN_TETE:
            raise ErreurDonneesAmorcage(
                f"en-tête inattendu : {en_tete!r}, attendu {list(_EN_TETE)!r}"
            )

        cles_vues: set[str] = set()
        for numero_de_ligne, ligne in enumerate(lecteur, start=2):
            if not any(champ.strip() for champ in ligne):
                continue
            if len(ligne) != len(_EN_TETE):
                raise ErreurDonneesAmorcage(
                    f"ligne {numero_de_ligne} : {len(ligne)} colonnes, "
                    f"{len(_EN_TETE)} attendues"
                )

            telephone = _exiger(ligne[2], _EN_TETE[2], numero_de_ligne)
            if telephone in cles_vues:
                raise ErreurDonneesAmorcage(
                    f"ligne {numero_de_ligne} : numéro en double « {telephone} »"
                )
            cles_vues.add(telephone)

            yield ProfilAmorcage(
                prenom=_exiger(ligne[0], _EN_TETE[0], numero_de_ligne),
                nom=_exiger(ligne[1], _EN_TETE[1], numero_de_ligne),
                telephone=telephone,
                libelle_sport=_exiger(ligne[3], _EN_TETE[3], numero_de_ligne),
                jours_disponibles=_lire_jours(ligne[4], numero_de_ligne),
                niveau=_lire_niveau(ligne[5], numero_de_ligne),
            )
