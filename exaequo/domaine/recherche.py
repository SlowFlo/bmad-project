"""La recherche : même sport, **même niveau** (FR-5, CAP-5), et le jour seul élargi.

L'égalité de niveau est **structurelle** et non conventionnelle : `niveau` est
obligatoire, aucune signature de ce module n'expose de tolérance, d'adjacence ni de
repli, et il n'existe aucune fonction à appeler pour obtenir un candidat d'un autre
niveau. C'est l'interdit d'élargissement de niveau rendu impossible à contourner,
plutôt que confié à la relecture.

Module pur : le vivier arrive par un port (`domaine.ports.PortVivier`), qui ne sait
que rétrécir par la clé de sport. **Toutes** les exclusions sont appliquées ici, donc
éprouvables avec un faux port et sans base.

Deux points d'entrée, jamais un drapeau. `chercher_candidats_exacts` rend la
correspondance **exacte** et n'élargit jamais d'elle-même : E9 en a besoin telle
quelle, une alerte différée ne se déclenchant que sur un exact. `chercher_candidats`
est le point d'entrée produit : l'exact d'abord, puis — **si et seulement si** il n'a
rien rendu — le même appariement en relâchant le jour, et lui seul. Le sport et le
niveau restent identiques, et les cinq exclusions de CAP-5 s'appliquent encore.

Ce module ne connaît ni le délai d'attente, ni le tri, ni le plafond de trois
candidats (2.3), ni le parcours des 231 combinaisons (2.4).
"""

from __future__ import annotations

from collections.abc import Set
from dataclasses import dataclass, field
from enum import Enum
from typing import TYPE_CHECKING
from uuid import UUID

from exaequo.domaine.ports import PortVivier
from exaequo.domaine.sports import cle_sport
from exaequo.domaine.vivier import JourSemaine, Niveau, Profil

if TYPE_CHECKING:  # pragma: no cover - annotations seules
    # `Set` reste importé à l'exécution : `_exiger_jours_indisponibles` l'emploie dans
    # un `isinstance`. `Sequence`, elle, ne sert qu'en annotation, et le module porte
    # `from __future__ import annotations` : même choix que `ports.py`, pour que les
    # deux modules du domaine ne divergent pas sur la même question.
    from collections.abc import Sequence

__all__ = [
    "JourIndisponible",
    "ResultatRecherche",
    "chercher_candidats",
    "chercher_candidats_exacts",
]

#: Un couple *(profil, jour)* qu'une rencontre immobilise. Le blocage porte sur ce
#: jour seul : un profil bloqué mardi reste rendu le jeudi (CAP-14, AD-6).
JourIndisponible = tuple[UUID, JourSemaine]


@dataclass(frozen=True, slots=True)
class ResultatRecherche:
    """Ce qu'une recherche a trouvé, et ce qu'elle cherchait.

    Le résultat porte la **clé de sport normalisée** effectivement interrogée, jamais
    le libellé dit par la personne : c'est elle qui a servi la comparaison (AD-5).
    Le `niveau` est celui du groupe entier — dit une fois, jamais répété par candidat.

    `jour_demande_indisponible` qualifie des **candidats**, jamais un vide : vrai, il
    dit « ceux-ci ne sont pas disponibles le jour demandé » — nécessairement vrai,
    sinon l'exact les aurait rendus. Sur un résultat vide il reste faux : le résultat
    ne prétend pas que le jour était en cause. `chercher_candidats_exacts` le laisse
    toujours faux, puisqu'elle n'élargit jamais.
    """

    cle_sport: str
    jour: JourSemaine
    niveau: Niveau
    candidats: tuple[Profil, ...] = field(default_factory=tuple)
    jour_demande_indisponible: bool = False


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

    Lève `TypeError` si `niveau` ou `jour` n'est pas un membre de son énumération, si
    `libelle_sport` n'est pas une chaîne, si `demandeur_id` n'est ni absent ni un
    `UUID`, ou si `jours_indisponibles` ne porte pas des couples
    `(UUID, JourSemaine)`. Les cinq entrées sont gardées, et pour la même raison : ici
    une entrée mal typée ne casse pas, elle **se tait**.
    """
    cle, profils = _garder_puis_charger(
        vivier,
        libelle_sport=libelle_sport,
        jour=jour,
        niveau=niveau,
        demandeur_id=demandeur_id,
        jours_indisponibles=jours_indisponibles,
    )
    candidats = _appariement_exact(
        profils,
        jour=jour,
        niveau=niveau,
        demandeur_id=demandeur_id,
        jours_indisponibles=jours_indisponibles,
    )
    return ResultatRecherche(
        cle_sport=cle, jour=jour, niveau=niveau, candidats=candidats
    )


def chercher_candidats(
    vivier: PortVivier,
    *,
    libelle_sport: str,
    jour: JourSemaine,
    niveau: Niveau,
    demandeur_id: UUID | None = None,
    jours_indisponibles: Set[JourIndisponible] = frozenset(),
) -> ResultatRecherche:
    """Le point d'entrée produit : l'exact d'abord, le jour relâché ensuite.

    Signature identique à `chercher_candidats_exacts` — mêmes cinq gardes, même
    normalisation, **un seul** appel au port : les profils du sport, chargés une fois,
    se filtrent deux fois.

    L'appariement exact s'applique d'abord. S'il rend au moins un candidat, c'est lui
    le résultat, à l'identique — y compris là où relâcher le jour en aurait rendu
    davantage. **Si et seulement si** il rend vide, le même appariement recommence en
    relâchant le jour, **et lui seul** : la clé de sport et le niveau sont inchangés,
    et les exclusions de CAP-5 — niveau inconnu, sortie du vivier, demandeur lui-même
    — s'appliquent encore. Un profil dont *tous* les jours déclarés sont immobilisés
    n'est jamais rendu : il n'a aucun jour à proposer.

    `jour_demande_indisponible` n'est vrai que si cet élargissement a produit des
    candidats. Sur un vivier vide, un sport inconnu, ou une paire sport × niveau sans
    personne, il reste faux : le résultat ne prétend alors pas que le jour était en
    cause.

    Il n'y a **aucun élargissement de niveau**, à aucune étape, et aucun paramètre
    n'en ouvre la possibilité (CAP-5, CAP-6).

    Lève les mêmes `TypeError` que la recherche exacte, pour la même raison : ici une
    entrée mal typée ne casse pas, elle **se tait**.
    """
    cle, profils = _garder_puis_charger(
        vivier,
        libelle_sport=libelle_sport,
        jour=jour,
        niveau=niveau,
        demandeur_id=demandeur_id,
        jours_indisponibles=jours_indisponibles,
    )
    candidats = _appariement_exact(
        profils,
        jour=jour,
        niveau=niveau,
        demandeur_id=demandeur_id,
        jours_indisponibles=jours_indisponibles,
    )
    if candidats:
        return ResultatRecherche(
            cle_sport=cle, jour=jour, niveau=niveau, candidats=candidats
        )

    candidats = _elargir_sur_le_jour(
        profils,
        niveau=niveau,
        demandeur_id=demandeur_id,
        jours_indisponibles=jours_indisponibles,
    )
    return ResultatRecherche(
        cle_sport=cle,
        jour=jour,
        niveau=niveau,
        candidats=candidats,
        jour_demande_indisponible=bool(candidats),
    )


def _garder_puis_charger(
    vivier: PortVivier,
    *,
    libelle_sport: str,
    jour: JourSemaine,
    niveau: Niveau,
    demandeur_id: UUID | None,
    jours_indisponibles: Set[JourIndisponible],
) -> tuple[str, tuple[Profil, ...]]:
    """Les cinq gardes, la normalisation, et l'**unique** appel au port.

    Partagé par les deux points d'entrée plutôt que recopié : les gardes ne peuvent
    pas diverger entre l'exact et le point d'entrée produit, et le port n'est appelé
    qu'une fois quoi qu'il advienne ensuite. Le port ne connaît que la clé de sport
    (AD-5) : élargir sur le jour ne le rappelle pas, puisqu'il rend déjà **tous** les
    profils de cette clé, sans filtrer.

    Ce qu'il rend est **matérialisé** en `tuple` : `chercher_candidats` parcourt les
    profils deux fois — l'exact, puis l'élargissement — et le contrat de `PortVivier`
    ne promet qu'une `Sequence`. Un adaptateur qui rendrait un itérateur à usage
    unique donnerait alors un élargissement silencieusement vide, au moment même où
    il compte.
    """
    _exiger_membre(niveau, Niveau, "niveau")
    _exiger_membre(jour, JourSemaine, "jour")
    _exiger_libelle_de_sport(libelle_sport)
    _exiger_demandeur(demandeur_id)
    _exiger_jours_indisponibles(jours_indisponibles)

    cle = cle_sport(libelle_sport)
    return cle, tuple(vivier.profils_du_sport(cle))


def _appariement_exact(
    profils: Sequence[Profil],
    *,
    jour: JourSemaine,
    niveau: Niveau,
    demandeur_id: UUID | None,
    jours_indisponibles: Set[JourIndisponible],
) -> tuple[Profil, ...]:
    """Les profils de ce niveau disponibles **ce jour-là**, dans l'ordre du vivier."""
    return tuple(
        profil
        for profil in profils
        if _est_candidat(
            profil,
            jour=jour,
            niveau=niveau,
            demandeur_id=demandeur_id,
            jours_indisponibles=jours_indisponibles,
        )
    )


def _elargir_sur_le_jour(
    profils: Sequence[Profil],
    *,
    niveau: Niveau,
    demandeur_id: UUID | None,
    jours_indisponibles: Set[JourIndisponible],
) -> tuple[Profil, ...]:
    """Le même appariement, sans la contrainte de jour — et sans autre relâchement.

    Le geste reste **privé** : le nom public ne dit pas « élargir », précisément pour
    que la liste noire d'AC-3 puisse interdire `elargi` dans toute surface publique de
    ce module, et donc interdire `elargir_le_niveau`. On ne l'affaiblit pas pour se
    faire de la place.

    `niveau` et le sport sont ceux de l'exact, à la lettre : cette fonction ne reçoit
    même pas de quoi les relâcher. Ne change que l'exigence de disponibilité — non
    plus « ce jour-là », mais « au moins un jour ». Un profil dont tous les jours
    déclarés sont immobilisés a un ensemble vide, et n'est donc jamais rendu.
    """
    return tuple(
        profil
        for profil in profils
        if _correspond_au_groupe(profil, niveau=niveau, demandeur_id=demandeur_id)
        and _jours_effectivement_disponibles(profil, jours_indisponibles)
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


def _exiger_libelle_de_sport(valeur: object) -> None:
    """Refuse un libellé de sport qui n'est pas une chaîne.

    Sans elle, `None` échoue au fond de `unicodedata.normalize`, avec un message qui
    parle d'encodage plutôt que du paramètre fautif. Le module répond de ses entrées
    lui-même, plutôt que de laisser fuiter l'erreur d'une dépendance de `sports.py`.
    """
    if not isinstance(valeur, str):
        raise TypeError(
            f"libelle_sport : str attendu, reçu {type(valeur).__name__} ({valeur!r})."
        )


def _exiger_demandeur(valeur: object) -> None:
    """Refuse un demandeur qui n'est ni absent, ni un `UUID`.

    Le cas dangereux est muet : `str(profil.id)` n'est jamais égal à `profil.id`, donc
    l'exclusion « soi-même » de CAP-5 ne s'appliquerait pas et le demandeur **serait
    rendu comme son propre partenaire**. Un défaut de ce genre ne lève rien, ne casse
    aucun test d'appel, et ne se voit qu'en lisant le résultat.
    """
    if valeur is not None and not isinstance(valeur, UUID):
        raise TypeError(
            f"demandeur_id : UUID ou None attendu, reçu {type(valeur).__name__} "
            f"({valeur!r})."
        )


def _exiger_jours_indisponibles(valeur: object) -> None:
    """Refuse autre chose qu'un ensemble de couples `(UUID, JourSemaine)`.

    E5 branchera ici la dérivation des jours qu'une rencontre immobilise (AD-6). Un
    `JourSemaine` nu, ou un couple `(str, str)`, n'écarterait **rien** sans lever : le
    blocage serait silencieusement inerte le jour même où il compte. La garde est
    posée avant qu'un appelant existe, pour que ce jour-là l'erreur soit bruyante.
    """
    if not isinstance(valeur, Set):
        raise TypeError(
            f"jours_indisponibles : ensemble attendu, reçu {type(valeur).__name__} "
            f"({valeur!r})."
        )
    for element in valeur:
        if (
            not isinstance(element, tuple)
            or len(element) != 2
            or not isinstance(element[0], UUID)
            or not isinstance(element[1], JourSemaine)
        ):
            raise TypeError(
                "jours_indisponibles : couples (UUID, JourSemaine) attendus, reçu "
                f"{element!r}."
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
    if not _correspond_au_groupe(profil, niveau=niveau, demandeur_id=demandeur_id):
        return False
    return jour in _jours_effectivement_disponibles(profil, jours_indisponibles)


def _correspond_au_groupe(
    profil: Profil, *, niveau: Niveau, demandeur_id: UUID | None
) -> bool:
    """Les trois exclusions de CAP-5 que le jour ne concerne pas.

    Elles valent donc **à l'identique** après élargissement : le *niveau inconnu*
    (une absence, jamais une quatrième valeur) et tout autre niveau, un profil sorti
    du vivier, et le demandeur lui-même — jamais son propre partenaire.

    L'égalité de niveau est ici, et nulle part ailleurs : `is not niveau`, sans marge
    ni voisinage. C'est le seul endroit à relire pour s'en convaincre.
    """
    if profil.niveau is None or profil.niveau is not niveau:
        return False
    if profil.sortie_vivier_le is not None:
        return False
    return demandeur_id is None or profil.id != demandeur_id


def _jours_effectivement_disponibles(
    profil: Profil, jours_indisponibles: Set[JourIndisponible]
) -> frozenset[JourSemaine]:
    """Les jours que le profil a déclarés, moins ceux qu'une rencontre immobilise.

    Le seul point où l'exact et l'élargissement diffèrent, et la raison pour laquelle
    ils le partagent : l'exact demande que le jour **demandé** y soit, l'élargissement
    seulement que l'ensemble soit **non vide**. « Bloqué mardi, libre jeudi » est ainsi
    rendu par l'élargissement, et « tous ses jours immobilisés » ne l'est par aucun des
    deux — un candidat sans aucun jour disponible n'est jamais proposé (CAP-14).

    Attention : les candidats rendus portent leurs jours **déclarés**, pas ceux-ci. La
    projection appartient à 2.3, qui en a besoin pour le délai d'attente.
    """
    return frozenset(
        jour
        for jour in profil.jours_disponibles
        if (profil.id, jour) not in jours_indisponibles
    )
