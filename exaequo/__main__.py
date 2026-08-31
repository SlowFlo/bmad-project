"""Point d'entrée : `python -m exaequo`.

Un seul processus, exécuté en local. Le démarrage crée le schéma puis déclenche
l'amorçage, par le `lifespan` de l'application. E1 ne pose aucune route : le serveur
est là parce que la racine de composition l'est, pas parce qu'il sert quelque chose.

`--amorcer-seulement` fait le même travail de démarrage et rend la main aussitôt, sans
retenir un port — c'est la forme commode pour vérifier que le chargement est bien
idempotent.
"""

from __future__ import annotations

import argparse
import logging
import sys

import uvicorn

from exaequo.adaptateurs.secondaires.persistance.base import creer_moteur, url_de_base
from exaequo.application import creer_application, preparer_le_vivier


def principal(arguments: list[str] | None = None) -> int:
    analyseur = argparse.ArgumentParser(
        prog="exaequo", description="Ex Aequo — socle du vivier"
    )
    analyseur.add_argument(
        "--amorcer-seulement",
        action="store_true",
        help="créer le schéma et charger les données d'amorçage, puis rendre la main",
    )
    analyseur.add_argument("--hote", default="127.0.0.1")
    analyseur.add_argument("--port", type=int, default=8000)
    options = analyseur.parse_args(arguments)

    logging.basicConfig(level=logging.INFO, format="%(message)s")
    journal = logging.getLogger("exaequo")

    if options.amorcer_seulement:
        moteur = creer_moteur()
        try:
            resultat = preparer_le_vivier(moteur)
        finally:
            moteur.dispose()
        journal.info(
            "vivier prêt sur %s : %d profils lus, %d insérés, %d déjà présents",
            url_de_base(),
            resultat.lus,
            resultat.inseres,
            resultat.deja_presents,
        )
        return 0

    uvicorn.run(creer_application(), host=options.hote, port=options.port)
    return 0


if __name__ == "__main__":
    sys.exit(principal())
