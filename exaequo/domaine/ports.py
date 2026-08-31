"""Protocoles des adaptateurs secondaires.

Le domaine n'a aucune dépendance sortante (AD-1) : il déclare ici ce qu'il attend
d'un adaptateur, et l'adaptateur vient s'y conformer. Un port **rétrécit**, il ne
filtre pas : les règles — le niveau, la sortie du vivier, le demandeur, les jours
indisponibles — appartiennent au domaine, ce qui les rend éprouvables sans base.

`typing` seul : aucune autre dépendance, à aucune profondeur.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol, runtime_checkable

if TYPE_CHECKING:  # pragma: no cover - annotations seules
    from collections.abc import Sequence

    from exaequo.domaine.vivier import Profil

__all__ = ["PortVivier"]


@runtime_checkable
class PortVivier(Protocol):
    """L'accès en lecture au vivier dont la recherche a besoin."""

    def profils_du_sport(self, cle_sport: str) -> Sequence[Profil]:
        """Rend **tous** les profils rattachés à cette clé de sport.

        Contrat :

        - la sélection porte sur la **clé de sport normalisée** (AD-5), jamais sur
          le libellé, et la table de synonymes n'est **jamais** consultée ici ;
        - l'ordre est celui du vivier — l'ordre des identifiants — et il est
          préservé de bout en bout ;
        - **aucun filtre** : ni le *niveau inconnu*, ni la sortie du vivier, ni le
          demandeur, ni un jour indisponible n'écartent quoi que ce soit. Ces
          exclusions appartiennent au domaine ;
        - une clé que le vivier ne connaît pas rend une séquence vide, jamais une
          exception.
        """
        ...
