---
title: 'E1 — Socle du vivier'
type: 'feature'
created: '2026-08-30'
status: 'done'
baseline_commit: '661e1be720140444e0317225b23828b16ddab941'
review_loop_iteration: 0
context:
  - '{project-root}/documentation/specs/spec-ex-aequo/SPEC.md'
  - '{project-root}/documentation/specs/spec-ex-aequo/glossaire.md'
  - '{project-root}/documentation/specs/spec-ex-aequo/donnees-amorcage.md'
  - '{project-root}/documentation/planning-artifacts/architecture/architecture-bmad-2026-08-28/ARCHITECTURE-SPINE.md'
---

<frozen-after-approval reason="human-owned intent — do not modify unless human renegotiates">

## Intent

**Problem :** Le dépôt ne contient aucun code. Rien ne peut être construit — ni la recherche d'E2, ni le fil d'E3 — tant que le vivier n'existe pas : les entités, le schéma, la clé de sport normalisée et sa table de synonymes, la distinction des deux populations, la provenance des numéros, et les 86 profils d'amorçage en base.

**Approach :** Poser le squelette du projet (Python 3.13, uv, FastAPI, SQLAlchemy, SQLite fichier) et, dans l'arbre source de la spine, les trois couches d'E1 : un domaine pur (`domaine/vivier.py`, `domaine/sports.py`), un adaptateur de persistance qui les mappe en tables, et un chargement d'amorçage idempotent déclenché au démarrage de l'application.

## Boundaries & Constraints

**Always :**
- **AD-5** — toute comparaison porte sur la **clé de sport normalisée** (casse repliée, accents retirés, espaces réduits) ; la table de synonymes redirige **à l'écriture uniquement** ; un libellé inconnu **fonde** un sport. Le libellé affiché est conservé tel que la personne l'a dit.
- **AD-11** — chaque profil porte sa **population** (*amorçage* / *inscrit*) et chaque numéro sa **provenance** (*donnée d'amorçage* / *saisie par un utilisateur inscrit*), enregistrées dans le modèle. Aucun code ne déduit l'une ou l'autre d'un préfixe.
- **AD-16** — le chargement se rejoue **sans duplication**, sur une clé naturelle stable ; après lui, la base est la source de vérité.
- **AD-1** — le domaine n'a **aucune dépendance sortante** : aucun module de `exaequo/domaine/` n'importe SQLAlchemy, FastAPI, le SDK Anthropic ni les adaptateurs.
- Le vocabulaire de `glossaire.md` est employé **littéralement**, jusque dans les noms de types, de champs, de fonctions et de tables. Jamais `match`, `rendez_vous`, `booking`, `slot`.
- Identifiants **UUIDv7** pour toute entité. Jours de la semaine : **énumération**, jamais une chaîne. Horodatages en UTC.
- **Nullabilité plutôt que valeurs par défaut trompeuses.** Le *niveau inconnu* est `NULL`, pas une quatrième valeur d'énumération.

**Ask First :**
- Ajouter une dépendance hors de la table *Stack* de la spine.
- Poser une colonne pour une entité hors du périmètre (rencontre, alerte, envoi, jeton, conversation, tour, étape).

**Never :**
- Créer les tables des lots suivants — `RENCONTRE`, `JETON`, `ENVOI`, `ALERTE`, `CONVERSATION`, `TOUR`, `ETAPE` — elles arrivent avec E5, E6, E9 et E3.
- Un champ `bloque` ou `recherche_active` : ces deux états sont **dérivés** (AD-6), et leur dérivation appartient à E2 et E5.
- Toute colonne anticipant une calibration du niveau : ni `mu`, ni `sigma`, ni historique de résultats.
- Inventer du contenu de données : aucun synonyme de sport fabriqué, aucun profil hors du CSV, aucun numéro hors de la plage ARCEP.
- Écrire des routes web, des gabarits HTML ou un appel au modèle — E3.

## I/O & Edge-Case Matrix

| Scenario | Input / State | Expected Output / Behavior | Error Handling |
|---|---|---|---|
| Normalisation | « Tennis », « tennis », «  TENNIS  » | une seule et même clé `tennis` | N/A |
| Accents et traits d'union | « Course à pied », « Basket-ball » | `course a pied`, `basket-ball` — le trait d'union est conservé | N/A |
| Les 11 libellés du CSV | les 11 sports des données d'amorçage | **11 clés, pas 12** | N/A |
| Synonyme à l'écriture | table portant `ping-pong` → sport `tennis de table`, écriture de « Ping-Pong » | rattaché au sport `tennis de table` ; libellé affiché conservé | N/A |
| Synonyme à la lecture | même table, recherche sur la clé `ping-pong` | **aucune redirection** : la lecture ne consulte jamais la table | N/A |
| Libellé inconnu | écriture de « Squash » | **fonde** un nouveau sport de clé `squash` | jamais un refus |
| Amorçage, 1re exécution | base vide | 86 profils, population *amorçage*, provenance de numéro *donnée d'amorçage* | ligne CSV invalide → échec bruyant, transaction annulée |
| Amorçage, N-ième exécution | 86 profils déjà chargés | **aucune insertion, aucune mise à jour, aucun doublon** | N/A |
| Profil d'amorçage modifié depuis | un profil sorti du vivier | il n'est **ni ressuscité ni réécrit** par un rechargement | N/A |
| Niveau absent | profil sans niveau déclaré | `niveau IS NULL` — *niveau inconnu* | N/A |
| Colonnes que le CSV n'a pas | profil d'amorçage | `courriel`, `secteur`, `compte_id` à `NULL` | jamais de valeur par défaut |

</frozen-after-approval>

## Code Map

Dépôt sans code : **tout est à créer**. Les chemins suivent l'arbre source de `ARCHITECTURE-SPINE.md`, section *Structural Seed*.

- `documentation/planning-artifacts/prds/prd-bmad-2026-08-26/SportsProfiles.csv` — **lecture seule**, source d'amorçage. UTF-8, fins de ligne CRLF, en-tête `Prénom,Nom,Numéro de téléphone,Sports pratiqués,Jours disponibles,Niveau`, 86 lignes de données, jours séparés par `;`. Vérifié sur le fichier : 86 numéros uniques de `+33639980001` à `+33639980086` dans l'ordre du fichier, 86 couples prénom+nom uniques, 11 libellés de sport, 3 niveaux (`Débutant` / `Intermédiaire` / `Avancé`), 7 jours en français capitalisés.
- `ARCHITECTURE-SPINE.md` — *Structural Seed* (arbre source, ERD, cardinalités), *Consistency Conventions* (nommage, identifiants, dates, nullabilité, erreurs), *Stack* (versions épinglées).
- `donnees-amorcage.md`, section *Conséquences pour le modèle de données* — les cinq propriétés que le schéma doit tenir.
- `glossaire.md` — vocabulaire contraignant des types et des champs.

## Tasks & Acceptance

**Execution :**
- [x] `pyproject.toml` — projet `exaequo` géré par uv, `requires-python = "==3.13.*"`, dépendances épinglées aux versions de la spine (`fastapi`, `uvicorn`, `sqlalchemy`), `pytest` en groupe de développement. Le socle n'a besoin ni d'`anthropic` (E3) ni d'un client HTTP (E7).
- [x] `.env.example` et `.gitignore` — documenter les clés nommées par la spine (Anthropic, ATMO, OAuth Google et Microsoft) **sans valeurs**, plus `EXAEQUO_BASE` ; ignorer `.venv/`, `__pycache__/`, `*.db`, `.env`.
- [x] `exaequo/domaine/identifiants.py` — `nouvel_identifiant()` : UUIDv7 **monotone**, absent de la stdlib 3.13 ; sa monotonie porte l'ordre du vivier (voir *Design Notes*).
- [x] `exaequo/domaine/sports.py` — `cle_sport(libelle)` (casse repliée, accents retirés, espaces réduits) et la logique de résolution d'un libellé : synonyme, puis sport existant, puis fondation. Pur, sans persistance.
- [x] `exaequo/domaine/vivier.py` — énumérations `Niveau`, `JourSemaine`, `Population`, `ProvenanceNumero` et les types `Profil`, `Compte`, `Sport`, `Synonyme`. Pur, sans dépendance sortante.
- [x] `exaequo/adaptateurs/secondaires/persistance/{base,modeles,depots}.py` — moteur et session SQLite, tables `compte`, `profil`, `jour_disponible`, `sport`, `synonyme`, et les dépôts `DepotVivier` et `DepotSports`, qui écrivent la résolution d'un sport en une seule transaction.
- [x] `exaequo/amorcage/{lecture,chargement}.py` — lecture du CSV vers les types du domaine, puis chargement idempotent sur `cle_amorcage`, **en insertion seule**, dans une transaction.
- [x] `exaequo/application.py` et `exaequo/__main__.py` — racine de composition : un `lifespan` qui crée le schéma puis déclenche l'amorçage. **Aucune route** : E3 remplit l'adaptateur web.
- [x] `tests/` — couvre chaque ligne de la matrice d'E/S, plus les critères d'acceptation ci-dessous.

**Acceptance Criteria :**
- Étant donné une base vide, quand l'application démarre deux fois de suite, alors le vivier compte **86 profils** aux deux passages et aucun jour disponible n'est dupliqué.
- Étant donné les 86 profils chargés, quand on compte les sports, alors il y en a **11**, chacun portant une clé distincte et son libellé d'origine.
- Étant donné le domaine, quand on inspecte ses imports, alors aucun module de `exaequo/domaine/` n'importe `sqlalchemy`, `fastapi`, `anthropic` ni `exaequo.adaptateurs` — vérifié par un test.
- Étant donné les profils chargés dans l'ordre du fichier, quand on les trie par identifiant, alors l'ordre du fichier est restitué : c'est l'*ordre du vivier* dont CAP-6 a besoin pour départager les ex æquo.

## Spec Change Log

## Design Notes

**L'idempotence est une insertion, jamais une réécriture.** Rejouer un `UPSERT` au démarrage ressusciterait un profil d'amorçage sorti du vivier (CAP-13) et écraserait ce que les lots suivants auront écrit sur lui. Le chargement n'insère donc que les `cle_amorcage` absentes et ne met jamais à jour une ligne existante. C'est la lecture stricte d'AD-16 : *après lui, la base est la source de vérité*.

**`cle_amorcage` porte la clé naturelle.** Colonne nullable et unique sur `profil`, valuée par le numéro du CSV pour les seuls profils d'amorçage. Elle rend la règle d'AD-16 explicite dans le modèle et ne contraint jamais un utilisateur inscrit.

**L'ordre du vivier est l'ordre de création.** UUIDv7 étant préfixé d'un horodatage, un générateur monotone rend `ORDER BY profil.id` égal à l'ordre d'insertion. CAP-6 exige que deux recherches identiques rendent le même trio dans le même ordre ; le tenir par l'identifiant évite une colonne de rang à maintenir.

**La table de synonymes naît vide.** Aucun contenu n'est contractuel, et le bot n'invente rien : c'est le mécanisme qui est livré, pas des données.

**Deux colonnes posées et jamais lues en v1**, conformément à la spine : `derniere_activite` (QO-6) et `sortie_vivier_le`, que E6 franchit et que E2 filtrera.

**Pas d'outil de migration.** Enveloppe locale à un seul environnement : le schéma est créé au démarrage. Alembic serait de l'appareillage sans usage.

## Verification

**Commands :**
- `uv run pytest` — attendu : tous les tests passent, dont ceux de la matrice d'E/S et le test d'imports du domaine.
- `uv run python -m exaequo` lancé deux fois de suite, puis un décompte en base — attendu : **86 profils** et **11 sports** aux deux passages.

## Suggested Review Order

**Racine de composition — ce que le démarrage promet**

- Le point d'entrée du lot : créer le schéma, puis amorcer, dans une transaction unique.
  [`application.py:29`](../../exaequo/application.py#L29)
- Le `lifespan` qui déclenche cette préparation, et l'absence assumée de toute route.
  [`application.py:50`](../../exaequo/application.py#L50)
- La commande de l'opérateur, dont `--amorcer-seulement`, qui rend le contrôle d'idempotence exécutable.
  [`__main__.py:24`](../../exaequo/__main__.py#L24)

**Domaine pur — le vocabulaire du glossaire, sans dépendance sortante (AD-1)**

- Les quatre énumérations et les quatre types du vivier ; le niveau inconnu est une absence.
  [`vivier.py:48`](../../exaequo/domaine/vivier.py#L48)
- Population et provenance portées par le modèle, jamais déduites d'un préfixe (AD-11).
  [`vivier.py:72`](../../exaequo/domaine/vivier.py#L72)
- La clé de sport normalisée : casse repliée, accents retirés, espaces réduits (AD-5).
  [`sports.py:33`](../../exaequo/domaine/sports.py#L33)
- La résolution d'un libellé : synonyme, puis sport existant, puis fondation — jamais un refus.
  [`sports.py:55`](../../exaequo/domaine/sports.py#L55)
- UUIDv7 monotone : c'est lui qui porte l'ordre du vivier dont CAP-6 a besoin.
  [`identifiants.py:38`](../../exaequo/domaine/identifiants.py#L38)

**Persistance — ce que le schéma refuse de porter**

- Le profil : `cle_amorcage` unique et nullable, et les contraintes qui tiennent AD-11 et AD-16.
  [`modeles.py:110`](../../exaequo/adaptateurs/secondaires/persistance/modeles.py#L110)
- La contrainte d'amorçage dérivée de l'énumération, pour qu'un renommage ne la désactive pas.
  [`modeles.py:54`](../../exaequo/adaptateurs/secondaires/persistance/modeles.py#L54)
- Les horodatages : tout décalage est converti en UTC à l'écriture, une heure naïve est refusée.
  [`modeles.py:31`](../../exaequo/adaptateurs/secondaires/persistance/modeles.py#L31)
- La résolution d'un sport écrite en une seule transaction, fondation comprise.
  [`depots.py:85`](../../exaequo/adaptateurs/secondaires/persistance/depots.py#L85)
- L'insertion d'un profil : insertion seule, jours dédupliqués, jamais de réécriture.
  [`depots.py:161`](../../exaequo/adaptateurs/secondaires/persistance/depots.py#L161)
- Le moteur SQLite et l'activation des clés étrangères, que SQLite laisse désactivées.
  [`base.py:32`](../../exaequo/adaptateurs/secondaires/persistance/base.py#L32)

**Amorçage — 86 profils, rejouables sans duplication**

- Le chargement idempotent : les seules clés absentes sont insérées, aucune n'est mise à jour (AD-16).
  [`chargement.py:42`](../../exaequo/amorcage/chargement.py#L42)
- La lecture du CSV : tout le fichier est validé avant la moindre écriture, l'échec est bruyant.
  [`lecture.py:112`](../../exaequo/amorcage/lecture.py#L112)
- La clé naturelle stable : le numéro du CSV, et lui seul, porte l'idempotence.
  [`lecture.py:68`](../../exaequo/amorcage/lecture.py#L68)

**Vérification — la matrice d'E/S, ligne par ligne**

- AD-1 vérifié par l'AST, imports relatifs résolus : le domaine n'atteint aucun adaptateur.
  [`test_domaine_sans_dependance.py:1`](../../tests/test_domaine_sans_dependance.py#L1)
- Les refus du schéma, chacun sur son type d'exception précis.
  [`test_vivier.py:1`](../../tests/test_vivier.py#L1)
- Idempotence, ordre du vivier, et l'annulation de transaction sur le chemin de production.
  [`test_chargement_amorcage.py:1`](../../tests/test_chargement_amorcage.py#L1)
- Normalisation, synonymes à l'écriture seule, fondation d'un libellé inconnu.
  [`test_sports.py:1`](../../tests/test_sports.py#L1)
- La commande de l'opérateur et `EXAEQUO_BASE`, seule porte de configuration.
  [`test_point_d_entree.py:1`](../../tests/test_point_d_entree.py#L1)

**Périphérie**

- Dépendances épinglées aux versions de la spine ; ni `anthropic` ni client HTTP dans le socle.
  [`pyproject.toml:1`](../../pyproject.toml#L1)
- Les clés nommées par la spine, documentées sans valeurs.
  [`.env.example:1`](../../.env.example#L1)
