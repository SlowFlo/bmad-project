"""Dépôts : `DepotSports` et `DepotVivier`.

Un dépôt lit et écrit ce que le domaine lui demande ; il ne décide jamais d'une règle.
La résolution d'un libellé de sport est calculée par `domaine.sports` et **écrite ici
en une seule transaction** : lecture des clés connues et des synonymes, puis fondation
si le libellé est inconnu.
"""

from __future__ import annotations

import datetime as dt
from collections.abc import Iterable
from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from exaequo.adaptateurs.secondaires.persistance.modeles import (
    JourDisponibleORM,
    ProfilORM,
    SportORM,
    SynonymeORM,
)
from exaequo.domaine.identifiants import nouvel_identifiant
from exaequo.domaine.sports import ResolutionSport, cle_sport, resoudre_libelle
from exaequo.domaine.vivier import (
    JourSemaine,
    Niveau,
    Population,
    Profil,
    ProvenanceNumero,
    Sport,
    Synonyme,
)

__all__ = ["DepotSports", "DepotVivier"]


def _vers_sport(ligne: SportORM) -> Sport:
    return Sport(id=ligne.id, cle=ligne.cle, libelle=ligne.libelle)


class DepotSports:
    """Accès aux sports et à leur table de synonymes."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def par_cle(self, cle: str) -> Sport | None:
        """Lecture par clé. **Ne consulte jamais la table de synonymes** (AD-5)."""
        ligne = self._session.scalar(select(SportORM).where(SportORM.cle == cle))
        return _vers_sport(ligne) if ligne is not None else None

    def tous(self) -> list[Sport]:
        lignes = self._session.scalars(select(SportORM).order_by(SportORM.id)).all()
        return [_vers_sport(ligne) for ligne in lignes]

    def compter(self) -> int:
        return self._session.scalar(select(func.count()).select_from(SportORM)) or 0

    def synonymes(self) -> dict[str, str]:
        """Rend la table de synonymes sous la forme *clé de synonyme -> clé du sport*."""
        lignes = self._session.execute(
            select(SynonymeORM.cle, SportORM.cle).join(
                SportORM, SportORM.id == SynonymeORM.sport_id
            )
        ).all()
        return {synonyme: sport for synonyme, sport in lignes}

    def poser_synonyme(self, cle_du_synonyme: str, sport_id: UUID) -> Synonyme:
        """Inscrit une redirection d'écriture.

        La table naît vide : aucun contenu n'est contractuel, seul le mécanisme est
        livré.
        """
        synonyme = SynonymeORM(
            id=nouvel_identifiant(),
            cle=cle_sport(cle_du_synonyme),
            sport_id=sport_id,
        )
        self._session.add(synonyme)
        self._session.flush()
        return Synonyme(id=synonyme.id, cle=synonyme.cle, sport_id=synonyme.sport_id)

    def resoudre_a_l_ecriture(
        self, libelle: str, maintenant: dt.datetime | None = None
    ) -> tuple[Sport, ResolutionSport]:
        """Résout un libellé à l'écriture et fonde le sport s'il est inconnu.

        Rend le sport rattaché et la résolution qui y a mené — dont le
        `libelle_affiche`, à conserver tel que la personne a dit le libellé.
        """
        cles_connues = set(self._session.scalars(select(SportORM.cle)).all())
        resolution = resoudre_libelle(libelle, cles_connues, self.synonymes())

        if resolution.fondation:
            ligne = SportORM(
                id=nouvel_identifiant(),
                cle=resolution.cle,
                libelle=resolution.libelle_affiche,
                cree_le=maintenant or dt.datetime.now(dt.UTC),
            )
            self._session.add(ligne)
            self._session.flush()
        else:
            ligne = self._session.scalar(
                select(SportORM).where(SportORM.cle == resolution.cle)
            )
            if ligne is None:  # pragma: no cover - garde d'intégrité
                raise LookupError(
                    f"synonyme orphelin : aucun sport de clé {resolution.cle!r}"
                )

        return _vers_sport(ligne), resolution


class DepotVivier:
    """Accès aux profils du vivier et à leurs jours disponibles."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def cles_amorcage_presentes(self) -> set[str]:
        """Les clés naturelles déjà chargées. C'est sur elles que porte l'idempotence."""
        return set(
            self._session.scalars(
                select(ProfilORM.cle_amorcage).where(
                    ProfilORM.cle_amorcage.is_not(None)
                )
            ).all()
        )

    def compter(self) -> int:
        return self._session.scalar(select(func.count()).select_from(ProfilORM)) or 0

    def compter_jours_disponibles(self) -> int:
        return (
            self._session.scalar(select(func.count()).select_from(JourDisponibleORM))
            or 0
        )

    def identifiants_ordonnes(self) -> list[UUID]:
        """Les profils dans l'ordre du vivier : l'ordre de leurs identifiants."""
        return list(self._session.scalars(select(ProfilORM.id).order_by(ProfilORM.id)))

    def par_cle_amorcage(self, cle: str) -> Profil | None:
        ligne = self._session.scalar(
            select(ProfilORM).where(ProfilORM.cle_amorcage == cle)
        )
        return self._vers_profil(ligne) if ligne is not None else None

    def par_identifiant(self, identifiant: UUID) -> Profil | None:
        ligne = self._session.get(ProfilORM, identifiant)
        return self._vers_profil(ligne) if ligne is not None else None

    def profils_ordonnes(self) -> list[Profil]:
        """Les profils du vivier dans l'ordre du vivier (CAP-6)."""
        lignes = self._session.scalars(select(ProfilORM).order_by(ProfilORM.id)).all()
        return [self._vers_profil(ligne) for ligne in lignes]

    def profils_du_sport(self, cle_sport: str) -> list[Profil]:
        """Tous les profils d'une **clé de sport**, dans l'ordre du vivier (`PortVivier`).

        Le dépôt **rétrécit, il ne filtre pas** : ni le niveau inconnu, ni la sortie du
        vivier, ni le demandeur n'écartent quoi que ce soit ici — ces exclusions sont
        des règles, et elles vivent dans `domaine.recherche`.

        La jointure porte sur `sport.cle`, jamais sur le libellé, et la table de
        synonymes n'est **pas** consultée : elle ne redirige qu'à l'écriture (AD-5).
        Une clé inconnue rend une liste vide, jamais une exception.
        """
        lignes = self._session.scalars(
            select(ProfilORM)
            .join(SportORM, SportORM.id == ProfilORM.sport_id)
            .where(SportORM.cle == cle_sport)
            .order_by(ProfilORM.id)
        ).all()
        return [self._vers_profil(ligne) for ligne in lignes]

    def inserer_profil(
        self,
        *,
        prenom: str,
        population: Population,
        sport_id: UUID,
        libelle_sport: str,
        jours_disponibles: Iterable[JourSemaine],
        niveau: Niveau | None = None,
        nom: str | None = None,
        telephone: str | None = None,
        provenance_numero: ProvenanceNumero | None = None,
        courriel: str | None = None,
        secteur: str | None = None,
        compte_id: UUID | None = None,
        cle_amorcage: str | None = None,
        maintenant: dt.datetime | None = None,
    ) -> Profil:
        """Insère un profil et ses jours disponibles.

        **Insertion seule** : ce dépôt ne réécrit jamais un profil existant.
        """
        identifiant = nouvel_identifiant()
        ligne = ProfilORM(
            id=identifiant,
            prenom=prenom,
            nom=nom,
            population=population,
            sport_id=sport_id,
            libelle_sport=libelle_sport,
            niveau=niveau,
            telephone=telephone,
            provenance_numero=provenance_numero,
            courriel=courriel,
            secteur=secteur,
            compte_id=compte_id,
            cle_amorcage=cle_amorcage,
            cree_le=maintenant or dt.datetime.now(dt.UTC),
            derniere_activite=None,
            sortie_vivier_le=None,
        )
        self._session.add(ligne)
        # Le profil est écrit avant ses jours : `jour_disponible` porte une clé
        # étrangère vers lui, et rien ne déclare de relation ORM pour l'ordonner.
        self._session.flush()
        for jour in sorted(set(jours_disponibles), key=lambda membre: membre.value):
            self._session.add(
                JourDisponibleORM(
                    id=nouvel_identifiant(), profil_id=identifiant, jour=jour
                )
            )
        self._session.flush()
        return self._vers_profil(ligne)

    def _jours_de(self, profil_id: UUID) -> frozenset[JourSemaine]:
        return frozenset(
            self._session.scalars(
                select(JourDisponibleORM.jour).where(
                    JourDisponibleORM.profil_id == profil_id
                )
            )
        )

    def _vers_profil(self, ligne: ProfilORM) -> Profil:
        return Profil(
            id=ligne.id,
            prenom=ligne.prenom,
            population=ligne.population,
            sport_id=ligne.sport_id,
            libelle_sport=ligne.libelle_sport,
            jours_disponibles=self._jours_de(ligne.id),
            niveau=ligne.niveau,
            nom=ligne.nom,
            telephone=ligne.telephone,
            provenance_numero=ligne.provenance_numero,
            courriel=ligne.courriel,
            secteur=ligne.secteur,
            compte_id=ligne.compte_id,
            cle_amorcage=ligne.cle_amorcage,
            cree_le=ligne.cree_le,
            derniere_activite=ligne.derniere_activite,
            sortie_vivier_le=ligne.sortie_vivier_le,
        )
