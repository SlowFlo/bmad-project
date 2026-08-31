"""La recherche exacte : même sport, même jour, **même niveau** (FR-5, CAP-5).

L'égalité de niveau est **structurelle** et non conventionnelle : `niveau` est
obligatoire, aucune signature de ce module n'expose de tolérance, d'adjacence ni de
repli, et il n'existe aucune fonction à appeler pour obtenir un candidat d'un autre
niveau. C'est l'interdit d'élargissement de niveau rendu impossible à contourner,
plutôt que confié à la relecture.

Module pur : le vivier arrive par un port (`domaine.ports.PortVivier`), qui ne sait
que rétrécir par la clé de sport. **Toutes** les exclusions sont appliquées ici, donc
éprouvables avec un faux port et sans base.

Ce module ne connaît pas l'élargissement sur le jour (2.2), ni le délai d'attente, le
tri ou le plafond de trois candidats (2.3) : la recherche exacte rend vide et
n'élargit jamais d'elle-même.
"""

from __future__ import annotations

from collections.abc import Set
from dataclasses import dataclass, field
from enum import Enum
from uuid import UUID

from exaequo.domaine.ports import PortVivier
from exaequo.domaine.sports import cle_sport
from exaequo.domaine.vivier import JourSemaine, Niveau, Profil

__all__ = ["ResultatRecherche", "chercher_candidats_exacts"]

#: Un couple *(profil, jour)* qu'une rencontre immobilise. Le blocage porte sur ce
#: jour seul : un profil bloqué mardi reste rendu le jeudi (CAP-14, AD-6).
JourIndisponible = tuple[UUID, JourSemaine]


@dataclass(frozen=True, slots=True)
class ResultatRecherche:
    """Ce qu'une recherche exacte a trouvé, et ce qu'elle cherchait.

    Le résultat porte la **clé de sport normalisée** effectivement interrogée, jamais
    le libellé dit par la personne : c'est elle qui a servi la comparaison (AD-5).
    Le `niveau` est celui du groupe entier — dit une fois, jamais répété par candidat.
    """

    cle_sport: str
    jour: JourSemaine
    niveau: Niveau
    candidats: tuple[Profil, ...] = field(default_factory=tuple)


def chercher_candidats_exacts(
    vivier: PortVivier,
    *,
    libelle_sport: str,
    jour: JourSemaine,
    niveau: Niveau,
    demandeur_id: UUID | None = None,
    jours_indisponibles: Set[JourIndisponible] = frozenset(),
) -> ResultatRecherche:
    """Rend les profils du vivier **exactement** de ce niveau, ce sport, ce jour.

    Le libellé est normalisé en clé de sport ; le port rend les profils de cette clé
    dans l'ordre du vivier, et cet ordre est préservé tel quel. Une clé que le vivier
    ne connaît pas rend un résultat vide, **jamais un refus**.

    Sont écartés, tous ici et non par le port :

    - le *niveau inconnu* (`profil.niveau is None`) — une absence, pas une quatrième
      valeur — et tout niveau autre que celui demandé ;
    - un profil sorti du vivier (`sortie_vivier_le` valué) ;
    - le demandeur lui-même, jamais son propre partenaire ;
    - un profil qui n'a pas déclaré ce jour disponible ;
    - un profil dont ce jour est immobilisé, désigné par le couple
      `(profil.id, jour)` dans `jours_indisponibles`.

    `jours_indisponibles` est vide par défaut, donc inerte : la dérivation du jour
    bloqué par une rencontre appartient à E5 (AD-6) et se branchera ici sans que
    cette signature soit réécrite.

    Lève `TypeError` si `niveau` ou `jour` n'est pas un membre de son énumération.
    """
    _exiger_membre(niveau, Niveau, "niveau")
    _exiger_membre(jour, JourSemaine, "jour")

    cle = cle_sport(libelle_sport)
    candidats = tuple(
        profil
        for profil in vivier.profils_du_sport(cle)
        if _est_candidat(
            profil,
            jour=jour,
            niveau=niveau,
            demandeur_id=demandeur_id,
            jours_indisponibles=jours_indisponibles,
        )
    )
    return ResultatRecherche(
        cle_sport=cle, jour=jour, niveau=niveau, candidats=candidats
    )


def _exiger_membre(valeur: object, enumeration: type[Enum], parametre: str) -> None:
    """Refuse une valeur qui n'est pas un membre de son énumération.

    `Niveau` et `JourSemaine` sont des `StrEnum` : `"debutant"` et `"mardi"` se
    glisseraient sans bruit à la place de `Niveau.DEBUTANT` et `JourSemaine.MARDI`.
    Le premier rendrait **zéro candidat sans la moindre erreur** — un vide
    indiscernable d'un vivier réellement vide, sur la promesse qui fonde le produit ;
    le second comparerait juste par accident. Le dépôt n'ayant pas de vérificateur de
    types, la garde est portée à l'exécution.

    On **refuse**, on ne convertit pas : rattraper une chaîne reviendrait à accepter
    deux façons de nommer un niveau, et la seconde échapperait au test négatif qui
    interdit d'en obtenir un autre.
    """
    if not isinstance(valeur, enumeration):
        raise TypeError(
            f"{parametre} : {enumeration.__name__} attendu, reçu "
            f"{type(valeur).__name__} ({valeur!r}). Passer le membre de "
            f"l'énumération, jamais son libellé."
        )


def _est_candidat(
    profil: Profil,
    *,
    jour: JourSemaine,
    niveau: Niveau,
    demandeur_id: UUID | None,
    jours_indisponibles: Set[JourIndisponible],
) -> bool:
    """Les exclusions de CAP-5, dans l'ordre où elles se lisent."""
    if profil.niveau is None or profil.niveau is not niveau:
        return False
    if profil.sortie_vivier_le is not None:
        return False
    if demandeur_id is not None and profil.id == demandeur_id:
        return False
    if jour not in profil.jours_disponibles:
        return False
    return (profil.id, jour) not in jours_indisponibles
