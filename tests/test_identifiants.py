"""UUIDv7 monotone : la version, la variante, et l'ordre qu'il porte."""

from __future__ import annotations

import pytest

from exaequo.domaine import identifiants
from exaequo.domaine.identifiants import nouvel_identifiant


@pytest.fixture
def etat_du_generateur_restaure():
    """Le générateur porte un état de processus : on le rend tel qu'on l'a trouvé.

    Sans cela, figer l'horloge dans le futur laisserait les identifiants tirés
    ensuite ancrés sur cette milliseconde-là.
    """
    horodatage = identifiants._dernier_horodatage_ms
    compteur = identifiants._compteur
    try:
        yield
    finally:
        identifiants._dernier_horodatage_ms = horodatage
        identifiants._compteur = compteur


def _horodatage_de(identifiant) -> int:
    return int.from_bytes(identifiant.bytes[0:6])


def test_la_version_et_la_variante_sont_celles_de_la_rfc_9562() -> None:
    identifiant = nouvel_identifiant()
    assert identifiant.version == 7
    assert identifiant.variant == "specified in RFC 4122"


def test_les_identifiants_sont_strictement_croissants() -> None:
    """Y compris tirés dans la même milliseconde : c'est ce qui porte l'ordre du vivier."""
    identifiants = [nouvel_identifiant() for _ in range(5_000)]
    assert identifiants == sorted(identifiants)
    assert len(set(identifiants)) == len(identifiants)


def test_l_ordre_lexicographique_du_texte_est_l_ordre_des_identifiants() -> None:
    """La base trie des chaînes : les deux ordres doivent coïncider."""
    identifiants = [nouvel_identifiant() for _ in range(500)]
    assert [str(un) for un in identifiants] == sorted(str(un) for un in identifiants)
    assert [un.hex for un in identifiants] == sorted(un.hex for un in identifiants)


def test_l_horodatage_est_celui_du_moment() -> None:
    import time

    avant = time.time_ns() // 1_000_000
    identifiant = nouvel_identifiant()
    apres = time.time_ns() // 1_000_000
    assert avant <= _horodatage_de(identifiant) <= apres + 1


def test_le_compteur_epuise_emprunte_la_milliseconde_suivante(
    monkeypatch, etat_du_generateur_restaure
) -> None:
    """Horloge figée, plus de 4096 tirages : la branche d'emprunt est traversée.

    C'est elle qui garantit l'ordre du vivier quand une milliseconde ne suffit plus.
    Une horloge réelle ne l'atteint pratiquement jamais — figer le temps est le seul
    moyen de l'éprouver.
    """
    instant_fige = (identifiants._dernier_horodatage_ms) + 1_000_000
    monkeypatch.setattr(
        identifiants, "_maintenant_en_millisecondes", lambda: instant_fige
    )

    tirages = 4_500  # > 4096, quel que soit le point de départ du compteur
    identifiants_tires = [nouvel_identifiant() for _ in range(tirages)]

    assert identifiants_tires == sorted(identifiants_tires)
    assert len(set(identifiants_tires)) == tirages
    assert _horodatage_de(identifiants_tires[0]) == instant_fige
    # Le compteur a débordé : la fin de la série a emprunté au moins une milliseconde.
    assert _horodatage_de(identifiants_tires[-1]) > instant_fige
    assert all(un.version == 7 for un in identifiants_tires)


def test_l_horloge_qui_recule_ne_casse_pas_l_ordre(
    monkeypatch, etat_du_generateur_restaure
) -> None:
    """Un ajustement d'horloge vers l'arrière ne doit pas rendre deux identifiants
    dans le désordre."""
    instant = identifiants._dernier_horodatage_ms + 1_000_000
    monkeypatch.setattr(identifiants, "_maintenant_en_millisecondes", lambda: instant)
    avant = nouvel_identifiant()

    monkeypatch.setattr(
        identifiants, "_maintenant_en_millisecondes", lambda: instant - 5_000
    )
    apres = [nouvel_identifiant() for _ in range(50)]

    assert avant < apres[0]
    assert apres == sorted(apres)
