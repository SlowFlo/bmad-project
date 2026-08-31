"""Le chargement d'amorçage : idempotence, populations, provenance, ordre du vivier."""

from __future__ import annotations

import datetime as dt

import pytest
from sqlalchemy import Engine, select
from sqlalchemy.orm import Session

from exaequo.adaptateurs.secondaires.persistance.base import (
    creer_fabrique_de_sessions,
    creer_moteur,
)
from exaequo.adaptateurs.secondaires.persistance.depots import DepotSports, DepotVivier
from exaequo.adaptateurs.secondaires.persistance.modeles import ProfilORM
from exaequo.amorcage.chargement import charger_donnees_amorcage
from exaequo.amorcage.lecture import ErreurDonneesAmorcage, lire_donnees_amorcage
from exaequo.application import preparer_le_vivier
from exaequo.domaine.vivier import Population, ProvenanceNumero


def _charger(session: Session, chemin=None):
    resultat = charger_donnees_amorcage(session, chemin)
    session.commit()
    return resultat


def test_premiere_execution_charge_quatre_vingt_six_profils(session: Session) -> None:
    resultat = _charger(session)
    assert resultat.inseres == 86
    assert DepotVivier(session).compter() == 86


def test_les_profils_charges_portent_leur_population_et_leur_provenance(
    session: Session,
) -> None:
    _charger(session)
    profils = DepotVivier(session).profils_ordonnes()
    assert all(profil.population is Population.AMORCAGE for profil in profils)
    assert all(
        profil.provenance_numero is ProvenanceNumero.DONNEE_AMORCAGE
        for profil in profils
    )


def test_les_colonnes_absentes_du_fichier_restent_nulles(session: Session) -> None:
    _charger(session)
    for profil in DepotVivier(session).profils_ordonnes():
        assert profil.courriel is None
        assert profil.secteur is None
        assert profil.compte_id is None
        assert profil.sortie_vivier_le is None
        assert profil.derniere_activite is None


def test_le_vivier_compte_onze_sports_a_cles_distinctes(session: Session) -> None:
    _charger(session)
    sports = DepotSports(session).tous()
    assert len(sports) == 11
    assert len({sport.cle for sport in sports}) == 11
    # Chacun porte son libellé d'origine, tel qu'il est écrit dans le fichier.
    libelles_du_fichier = {
        profil.libelle_sport for profil in lire_donnees_amorcage()
    }
    assert {sport.libelle for sport in sports} == libelles_du_fichier


def test_le_chargement_se_rejoue_sans_duplication(session: Session) -> None:
    _charger(session)
    jours_apres_le_premier = DepotVivier(session).compter_jours_disponibles()

    second = _charger(session)

    assert second.inseres == 0
    assert second.deja_presents == 86
    assert DepotVivier(session).compter() == 86
    assert DepotSports(session).compter() == 11
    assert (
        DepotVivier(session).compter_jours_disponibles() == jours_apres_le_premier
    )


def test_le_decompte_des_deja_presents_est_l_intersection_avec_le_fichier(
    session: Session, tmp_path
) -> None:
    """`deja_presents` est compté, pas déduit de `lus - inseres`.

    Le premier fichier laisse en base une clé que le second n'a pas : elle ne doit
    pas compter comme « déjà présente », n'étant pas du second chargement.
    """
    en_tete = (
        "Prénom,Nom,Numéro de téléphone,Sports pratiqués,Jours disponibles,Niveau\n"
    )
    partagee = "Emma,Leroy,+33639980002,Tennis,Mardi;Jeudi,Débutant\n"

    premier = tmp_path / "premier.csv"
    premier.write_text(
        en_tete + partagee + "Lucas,Moreau,+33639980001,Football,Lundi,Avancé\n",
        encoding="utf-8",
    )
    second = tmp_path / "second.csv"
    second.write_text(
        en_tete
        + partagee
        + "Hugo,Martin,+33639980003,Basket-ball,Lundi,Avancé\n"
        + "Chloé,Garcia,+33639980004,Natation,Samedi,Débutant\n",
        encoding="utf-8",
    )

    assert _charger(session, premier).inseres == 2

    resultat = _charger(session, second)
    assert (resultat.lus, resultat.inseres, resultat.deja_presents) == (3, 2, 1)
    assert DepotVivier(session).compter() == 4


def test_un_rechargement_ne_reecrit_pas_un_profil_existant(session: Session) -> None:
    """L'idempotence est une insertion, jamais une réécriture."""
    _charger(session)
    depot = DepotVivier(session)
    avant = depot.par_cle_amorcage("+33639980002")
    assert avant is not None

    session.execute(
        ProfilORM.__table__.update()
        .where(ProfilORM.id == avant.id)
        .values(secteur="Croix-Rousse")
    )
    session.commit()

    _charger(session)

    apres = depot.par_cle_amorcage("+33639980002")
    assert apres is not None
    assert apres.id == avant.id
    assert apres.secteur == "Croix-Rousse"


def test_un_profil_sorti_du_vivier_n_est_ni_ressuscite_ni_reecrit(
    session: Session,
) -> None:
    _charger(session)
    depot = DepotVivier(session)
    profil = depot.par_cle_amorcage("+33639980002")
    assert profil is not None
    sortie = dt.datetime(2026, 8, 30, 12, 0, tzinfo=dt.UTC)

    session.execute(
        ProfilORM.__table__.update()
        .where(ProfilORM.id == profil.id)
        .values(sortie_vivier_le=sortie)
    )
    session.commit()

    _charger(session)

    apres = depot.par_cle_amorcage("+33639980002")
    assert apres is not None
    assert apres.sortie_vivier_le == sortie
    assert depot.compter() == 86


def test_l_ordre_des_identifiants_restitue_l_ordre_du_fichier(session: Session) -> None:
    """C'est *l'ordre du vivier* dont CAP-6 a besoin pour départager les ex æquo."""
    _charger(session)
    depot = DepotVivier(session)
    profils = depot.profils_ordonnes()

    ordre_du_vivier = [profil.cle_amorcage for profil in profils]
    ordre_du_fichier = [profil.cle_amorcage for profil in lire_donnees_amorcage()]
    assert ordre_du_vivier == ordre_du_fichier

    # Les deux lectures d'ordre du dépôt disent la même chose.
    assert depot.identifiants_ordonnes() == [profil.id for profil in profils]
    assert depot.identifiants_ordonnes() == sorted(depot.identifiants_ordonnes())


def test_l_ordre_par_identifiant_est_celui_de_la_base(session: Session) -> None:
    """Le tri est fait par SQLite, pas en Python : c'est `ORDER BY profil.id`."""
    _charger(session)
    cles = list(
        session.scalars(select(ProfilORM.cle_amorcage).order_by(ProfilORM.id))
    )
    assert cles == [profil.cle_amorcage for profil in lire_donnees_amorcage()]


def _fichier_a_ligne_invalide(tmp_path):
    """Deux lignes, la seconde portant un niveau que le domaine ne connaît pas."""
    fichier = tmp_path / "amorcage.csv"
    fichier.write_text(
        "Prénom,Nom,Numéro de téléphone,Sports pratiqués,Jours disponibles,Niveau\n"
        "Emma,Leroy,+33639980002,Tennis,Mardi;Jeudi,Débutant\n"
        "Hugo,Martin,+33639980003,Basket-ball,Lundi,Expert\n",
        encoding="utf-8",
    )
    return fichier


def test_une_ligne_invalide_annule_la_transaction_au_demarrage(tmp_path) -> None:
    """« Ligne CSV invalide → échec bruyant, transaction annulée ».

    Le rollback éprouvé est celui de `preparer_le_vivier` — le chemin qu'emprunte le
    démarrage de l'application — et non un rollback écrit dans le test.
    """
    url = f"sqlite:///{tmp_path / 'vivier.db'}"
    fichier = _fichier_a_ligne_invalide(tmp_path)

    moteur = creer_moteur(url)
    try:
        with pytest.raises(ErreurDonneesAmorcage):
            preparer_le_vivier(moteur, fichier)
    finally:
        moteur.dispose()

    # Moteur rouvert : ce que la base contient vraiment, pas ce qu'une session garde.
    moteur = creer_moteur(url)
    try:
        with creer_fabrique_de_sessions(moteur)() as session:
            assert DepotVivier(session).compter() == 0
            assert DepotVivier(session).compter_jours_disponibles() == 0
            assert DepotSports(session).compter() == 0
    finally:
        moteur.dispose()


def test_un_echec_en_cours_d_ecriture_annule_les_profils_deja_inseres(
    tmp_path, monkeypatch
) -> None:
    """La transaction est annulée même quand des profils sont déjà écrits.

    La lecture précédant toute écriture, une ligne invalide seule ne prouverait pas
    l'annulation : rien n'aurait encore été inséré. On fait donc échouer l'insertion
    elle-même, après deux profils déjà posés.
    """
    url = f"sqlite:///{tmp_path / 'vivier.db'}"

    inserer = DepotVivier.inserer_profil
    appels = {"n": 0}

    def inserer_puis_echouer(self, **arguments):
        appels["n"] += 1
        if appels["n"] > 2:
            raise RuntimeError("panne d'écriture simulée")
        return inserer(self, **arguments)

    monkeypatch.setattr(DepotVivier, "inserer_profil", inserer_puis_echouer)

    moteur = creer_moteur(url)
    try:
        with pytest.raises(RuntimeError, match="panne d'écriture simulée"):
            preparer_le_vivier(moteur)
    finally:
        moteur.dispose()

    monkeypatch.undo()

    moteur = creer_moteur(url)
    try:
        with creer_fabrique_de_sessions(moteur)() as session:
            assert DepotVivier(session).compter() == 0
            assert DepotVivier(session).compter_jours_disponibles() == 0
            assert DepotSports(session).compter() == 0
    finally:
        moteur.dispose()


def test_une_ligne_invalide_leve_avant_toute_ecriture(
    moteur: Engine, tmp_path
) -> None:
    """La lecture est complète avant la première insertion : rien n'est écrit."""
    fichier = _fichier_a_ligne_invalide(tmp_path)

    fabrique = creer_fabrique_de_sessions(moteur)
    with fabrique() as session:
        with pytest.raises(ErreurDonneesAmorcage):
            charger_donnees_amorcage(session, fichier)
        session.rollback()

    with fabrique() as session:
        assert DepotVivier(session).compter() == 0
        assert DepotSports(session).compter() == 0
