"""Chargement idempotent des données d'amorçage (AD-16).

**L'idempotence est une insertion, jamais une réécriture.** Rejouer un `UPSERT` au
démarrage ressusciterait un profil d'amorçage sorti du vivier et écraserait ce que les
lots suivants auront écrit sur lui. Le chargement n'insère donc que les
`cle_amorcage` absentes et ne met **jamais** à jour une ligne existante : après lui,
la base est la source de vérité et le fichier n'est plus lu.

Tout se joue dans une seule transaction : une ligne invalide annule le chargement
entier plutôt que de laisser un vivier à moitié peuplé.
"""

from __future__ import annotations

import datetime as dt
from dataclasses import dataclass
from pathlib import Path

from sqlalchemy.orm import Session

from exaequo.adaptateurs.secondaires.persistance.depots import DepotSports, DepotVivier
from exaequo.amorcage.lecture import lire_donnees_amorcage
from exaequo.domaine.vivier import Population, ProvenanceNumero

__all__ = ["ResultatAmorcage", "charger_donnees_amorcage"]


@dataclass(frozen=True, slots=True)
class ResultatAmorcage:
    """Ce qu'un passage de chargement a fait, et ce qu'il a laissé en place.

    `deja_presents` est **compté**, jamais déduit de `lus - inseres` : une ligne
    sautée pour une autre raison que sa présence en base ne doit pas se faire passer
    pour un profil déjà chargé.
    """

    lus: int
    inseres: int
    deja_presents: int


def charger_donnees_amorcage(
    session: Session,
    chemin: Path | None = None,
    maintenant: dt.datetime | None = None,
) -> ResultatAmorcage:
    """Charge les profils d'amorçage absents du vivier, en insertion seule.

    L'appelant est propriétaire de la transaction : cette fonction ne valide ni
    n'annule. Elle lève sur une donnée invalide, ce qui laisse l'appelant annuler.
    """
    profils = lire_donnees_amorcage(chemin)
    depot_vivier = DepotVivier(session)
    depot_sports = DepotSports(session)
    instant = maintenant or dt.datetime.now(dt.UTC)

    deja_presentes = depot_vivier.cles_amorcage_presentes()
    cles_du_fichier = {profil.cle_amorcage for profil in profils}
    deja_presents = len(cles_du_fichier & deja_presentes)
    inseres = 0

    for profil in profils:
        if profil.cle_amorcage in deja_presentes:
            continue

        sport, resolution = depot_sports.resoudre_a_l_ecriture(
            profil.libelle_sport, maintenant=instant
        )
        depot_vivier.inserer_profil(
            prenom=profil.prenom,
            nom=profil.nom,
            population=Population.AMORCAGE,
            sport_id=sport.id,
            libelle_sport=resolution.libelle_affiche,
            jours_disponibles=profil.jours_disponibles,
            niveau=profil.niveau,
            telephone=profil.telephone,
            provenance_numero=ProvenanceNumero.DONNEE_AMORCAGE,
            # Les colonnes que le fichier n'a pas restent nulles : un profil
            # d'amorçage n'a ni compte, ni adresse électronique, ni secteur.
            courriel=None,
            secteur=None,
            compte_id=None,
            cle_amorcage=profil.cle_amorcage,
            maintenant=instant,
        )
        inseres += 1

    return ResultatAmorcage(
        lus=len(profils),
        inseres=inseres,
        deja_presents=deja_presents,
    )
