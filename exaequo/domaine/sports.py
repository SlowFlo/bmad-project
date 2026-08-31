"""Sports : clé normalisée, synonymes, fondation (AD-5).

Toute comparaison, jointure, alerte et agrégation porte sur la **clé de sport
normalisée**, jamais sur le libellé : sans elle, « tennis » et « Tennis » sont deux
sports qui ne se rencontrent jamais et le vivier se pulvérise en silence.

Module pur : aucune persistance, aucune dépendance sortante.
"""

from __future__ import annotations

import unicodedata
from collections.abc import Mapping, Set
from dataclasses import dataclass

__all__ = ["replier_texte", "cle_sport", "ResolutionSport", "resoudre_libelle"]


def replier_texte(texte: str) -> str:
    """Replie un texte : casse repliée, accents retirés, espaces réduits.

    Primitive de comparaison du domaine. Le trait d'union est un caractère du texte
    et il est conservé : « Basket-ball » se replie en `basket-ball`.
    """
    sans_accent = "".join(
        caractere
        for caractere in unicodedata.normalize("NFD", texte)
        if not unicodedata.combining(caractere)
    )
    return " ".join(sans_accent.casefold().split())


def cle_sport(libelle: str) -> str:
    """Rend la **clé de sport normalisée** d'un libellé (AD-5).

    C'est elle, et jamais le libellé, que portent les comparaisons, les jointures,
    les alertes et les agrégations.
    """
    return replier_texte(libelle)


@dataclass(frozen=True, slots=True)
class ResolutionSport:
    """Le sport auquel rattacher un libellé, et s'il faut le fonder.

    `libelle_affiche` est le libellé tel que la personne l'a dit : il est conservé
    sur le profil même lorsque la table de synonymes a redirigé la clé.
    """

    cle: str
    libelle_affiche: str
    fondation: bool


def resoudre_libelle(
    libelle: str,
    cles_connues: Set[str],
    synonymes: Mapping[str, str],
) -> ResolutionSport:
    """Résout un libellé **à l'écriture**.

    Synonyme, puis sport existant, puis fondation.

    `synonymes` va d'une clé de synonyme vers la clé du sport qu'elle désigne. Elle
    n'est consultée qu'ici, c'est-à-dire à l'écriture : **la lecture ne la consulte
    jamais** (AD-5). Un libellé qu'aucune des deux ne connaît **fonde** un sport ; ce
    n'est jamais un refus.
    """
    cle = cle_sport(libelle)
    cle_cible = synonymes.get(cle, cle)
    return ResolutionSport(
        cle=cle_cible,
        libelle_affiche=libelle,
        fondation=cle_cible not in cles_connues,
    )
