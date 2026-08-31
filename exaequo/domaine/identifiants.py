"""Identifiants du domaine : UUIDv7 monotone.

La stdlib de Python 3.13 ne fournit pas UUIDv7 (`uuid.uuid7` n'arrive qu'en 3.14).
La génération est donc écrite ici, conformément à la RFC 9562 §5.7.

**La monotonie porte l'ordre du vivier.** UUIDv7 étant préfixé d'un horodatage
milliseconde, un générateur strictement croissant rend `ORDER BY profil.id` égal à
l'ordre d'insertion — c'est *l'ordre du vivier* dont CAP-6 a besoin pour départager
les ex æquo. Deux identifiants tirés dans la même milliseconde doivent donc rester
ordonnés : le champ `rand_a` de 12 bits sert de compteur intra-milliseconde
(RFC 9562 §6.2, « fixed bit-length dedicated counter »), et déborde sur la
milliseconde suivante s'il est épuisé.
"""

from __future__ import annotations

import os
import threading
import time
from uuid import UUID

_VERROU = threading.Lock()
_COMPTEUR_MAX = 0xFFF  # rand_a : 12 bits
_dernier_horodatage_ms = -1
_compteur = 0


def _maintenant_en_millisecondes() -> int:
    """L'horloge du générateur, isolée en une fonction.

    C'est le seul point où le temps entre : le figer suffit à éprouver le
    débordement du compteur, qu'une horloge réelle ne fait pratiquement jamais
    atteindre.
    """
    return time.time_ns() // 1_000_000


def nouvel_identifiant() -> UUID:
    """Rend un UUIDv7 strictement supérieur à tous ceux déjà rendus par ce processus."""
    global _dernier_horodatage_ms, _compteur

    with _VERROU:
        horodatage_ms = _maintenant_en_millisecondes()

        if horodatage_ms > _dernier_horodatage_ms:
            _dernier_horodatage_ms = horodatage_ms
            _compteur = int.from_bytes(os.urandom(2)) & 0x3FF  # marge de débordement
        elif _compteur < _COMPTEUR_MAX:
            _compteur += 1
        else:
            # Compteur épuisé : on emprunte la milliseconde suivante plutôt que de
            # rendre deux identifiants dans le désordre.
            _dernier_horodatage_ms += 1
            _compteur = 0

        horodatage = _dernier_horodatage_ms
        compteur = _compteur

    octets = bytearray(16)
    octets[0:6] = horodatage.to_bytes(6)
    # 4 bits de version (7) puis les 12 bits de rand_a.
    octets[6] = 0x70 | (compteur >> 8)
    octets[7] = compteur & 0xFF
    aleatoire = os.urandom(8)
    # 2 bits de variant (0b10) puis les 62 bits de rand_b.
    octets[8] = 0x80 | (aleatoire[0] & 0x3F)
    octets[9:16] = aleatoire[1:8]

    return UUID(bytes=bytes(octets))
