---
title: 'Outillage de vérification statique — ruff et mypy strict'
type: 'chore'
created: '2026-08-31'
status: 'done'
baseline_commit: '494d4c0aa94bbe6d667187aa4a0e9a14658a0c31'
review_loop_iteration: 0
context:
  - '{project-root}/documentation/implementation-artifacts/deferred-work.md'
---

<frozen-after-approval reason="human-owned intent — do not modify unless human renegotiates">

## Intent

**Problème :** Le dépôt n'a ni linter ni vérificateur de types. Les huit `# type: ignore[...]` qu'il
porte ne sont vérifiés par rien, et les gardes `TypeError` écrites à la main en 2.1 et 2.2
compensent à l'exécution exactement la classe de défaut qu'un vérificateur attrape à l'écriture.
C'est l'entrée de `deferred-work.md` que ce lot ferme.

**Approche :** Ajouter `ruff` (lint seul) et `mypy --strict` sur `exaequo/` et `tests/`, les
configurer dans `pyproject.toml`, et amener le dépôt à zéro erreur. Mesuré avant d'écrire :
**41 erreurs ruff** et **67 erreurs mypy**, dont **6 seulement dans `exaequo/`** — toutes dans
l'adaptateur de persistance, et aucune n'est un défaut de comportement.

## Boundaries & Constraints

**Always :**
- Une règle désactivée porte sa **raison**, en une ligne, dans `pyproject.toml`. Une désactivation
  muette ne vaut pas mieux que pas de linter.
- Les versions sont **épinglées à l'exact**, comme `pytest==8.4.2` l'est déjà.
- La suite reste verte et son décompte inchangé : ce lot ne change aucun comportement.

**Ask First :**
- Toute correction qui changerait un comportement, une signature publique ou un nom du glossaire
  pour faire taire un outil.
- Tout relâchement de `--strict` (`disallow_untyped_defs`, `warn_unused_ignores`…) sur `exaequo/`.

**Never :**
- Faire tourner ruff ou mypy sur `_bmad/` : c'est le framework installé, pas notre code.
- `ruff format` : le formatage est hors périmètre, le diff mécanique noierait la revue.
- Élargir la limite de 88 colonnes pour faire disparaître les `E501` : ce sont 14 lignes à replier.
- Ajouter une intégration continue — c'est l'entrée **suivante** de `deferred-work.md`, distincte.
- Toucher à `domaine/`, à la recherche ou aux tests de 2.1 et 2.2 autrement que par des annotations.

## I/O & Edge-Case Matrix

| Scénario | Entrée / État | Sortie / Comportement attendu | Traitement d'erreur |
|----------|---------------|-------------------------------|---------------------|
| Lint propre | `uv run ruff check .` | Zéro erreur ; `_bmad/` jamais visité | N/A |
| Types propres | `uv run mypy` | Zéro erreur sur `exaequo/` **et** `tests/` | N/A |
| Ignore devenu faux | Un `# type: ignore[...]` qui ne masque plus rien | `warn_unused_ignores` le signale | Erreur mypy |
| Régression de types | `niveau: Niveau = Niveau.DEBUTANT` réintroduit | Détecté par les tests de 2.2, pas par mypy | N/A — connu |
| Comportement | `uv run pytest` | 180 passés, décompte inchangé | N/A |

</frozen-after-approval>

## Code Map

Mesures faites à la planification, avec `uv run --with` — rien n'est encore installé.

- `pyproject.toml:13` — `[dependency-groups] dev` ne porte que `pytest==8.4.2` ; `:22`
  `[tool.pytest.ini_options]` est la seule section d'outil. Reçoit `[tool.ruff]` et `[tool.mypy]`.
- **ruff, 41 erreurs sur `exaequo/` + `tests/`** (847 à la racine — dont `_bmad/`, à exclure) :
  `E501` ×14 (89 colonnes, à replier), `ARG001` ×12 (fixtures pytest demandées pour leur effet de
  bord), `RUF022` ×4 (`__all__` en ordre **sémantique**, voir `vivier.py:22`), `ARG005` ×3,
  `ARG002` ×2, `I001` ×2, `N818` ×2 (`SchemaObsolete` — le suffixe `Error` est une convention
  anglaise, le dépôt nomme en français), `C416` ×1, `RUF002` ×1 (typographie française « » et
  insécables, délibérée partout).
- **mypy `--strict`, 6 erreurs dans `exaequo/`**, toutes de la persistance :
  - `modeles.py:32` `TypeDecorator` sans paramètre de type · `:42` `process_bind_param` et `:49`
    `process_result_value` non annotées.
  - `depots.py:106` — `ligne` reçoit `SportORM | None` là où la branche précédente l'a fixé à
    `SportORM`. La garde `if ligne is None: raise LookupError` (`:109`) existe : **pas un défaut**,
    un rétrécissement invisible au vérificateur.
  - `depots.py:126` — `set(Sequence[str | None])` pour une fonction qui rend `set[str]`. Le
    `.where(cle_amorcage.is_not(None))` le garantit, SQLAlchemy ne sait pas l'exprimer.
  - `base.py:46` — l'écouteur `_activer_les_cles_etrangeres` non annoté.
- **mypy, 61 erreurs dans `tests/`** : massivement `no-untyped-def` sur les fixtures et les tests
  paramétrés (`test_chargement_amorcage.py` ×12, `test_vivier.py` ×11, `test_recherche.py` ×11…),
  plus `test_domaine_sans_dependance.py:96-97` (`str | None` passé à un paramètre `str`),
  `test_chargement_amorcage.py:126,150` (`FromClause.update`) et **un `unused-ignore` réel** à
  `test_recherche.py:1500`.
- `documentation/implementation-artifacts/deferred-work.md` — l'entrée « Aucun vérificateur de types
  ni linter » ; 2.1 a établi le motif de clôture par une ligne `resolution:`.

## Tasks & Acceptance

**Execution :**
- [ ] `pyproject.toml` — ajouter `ruff==0.14.5` et `mypy==1.18.2` au groupe `dev`. `[tool.ruff]` :
  `line-length = 88`, `target-version = "py313"`, `extend-exclude = ["_bmad"]`. Sélection
  `E,W,F,I,N,UP,B,C4,SIM,RUF,ARG,RET,TID`, et pour chaque règle écartée — `N818`, `RUF001`/`RUF002`/
  `RUF003`, `RUF022` — une ligne disant pourquoi. `ARG001` ignoré sous `tests/` seulement, par
  `per-file-ignores` : une fixture pytest demandée pour son effet de bord n'est pas un paramètre
  mort. `[tool.mypy]` : `strict = true`, `files = ["exaequo", "tests"]`, `python_version = "3.13"`.
- [ ] `exaequo/adaptateurs/secondaires/persistance/` — les 6 erreurs. Annoter `TypeDecorator` et ses
  deux méthodes, annoter l'écouteur de `base.py`, et **rendre visibles au vérificateur** les deux
  rétrécissements de `depots.py` — par une variable distincte ou une compréhension qui écarte
  `None`, jamais par un `# type: ignore`, qui masquerait la garde au lieu de l'exprimer.
- [ ] `tests/` — annoter fixtures et tests jusqu'à zéro erreur mypy ; corriger les deux `arg-type`
  de `test_domaine_sans_dependance.py` et les deux `FromClause.update` ; **retirer** l'ignore
  inutile de `test_recherche.py:1500`.
- [ ] `exaequo/` et `tests/` — les 41 erreurs ruff : replier les 14 lignes à 88 colonnes, trier les
  imports, et le reste. Le repliage ne réécrit pas les phrases, il les coupe.
- [ ] `documentation/implementation-artifacts/deferred-work.md` — clore l'entrée « Aucun
  vérificateur de types ni linter » par une ligne `resolution:` nommant cette spec, les deux outils
  et leurs versions. Ne toucher à aucune autre entrée.

**Acceptance Criteria :**
- Étant donné le dépôt, quand on lance `uv run ruff check .` et `uv run mypy`, alors les deux rendent
  zéro erreur et `_bmad/` n'est pas analysé.
- Étant donné `pyproject.toml`, quand on lit sa configuration ruff, alors chaque règle écartée porte
  sa raison en clair.
- Étant donné `uv run pytest`, quand la suite s'exécute, alors 180 tests passent — le même décompte
  qu'avant ce lot.

## Spec Change Log

- **2026-08-31 — l'exclusion ne vise pas `_bmad/` seul.** La Code Map ne nommait que `_bmad/`. À
  l'implémentation, `.claude/skills/` et `.agents/skills/` se sont révélés en être des copies
  conformes — 716 des 738 constats ruff restants venaient de là. L'exclusion les couvre désormais,
  fidèlement au `Never` qui parle du « framework installé, pas notre code ». La revue a corrigé la
  première tentative, qui excluait les deux arbres **entiers** : un `.claude/hooks/*.py` écrit par
  le projet aurait échappé au lint en silence. Le motif porte les répertoires `skills`, et eux
  seuls.
- **2026-08-31 — « le repliage coupe, il ne réécrit pas » ne valait pas pour les résumés.** La
  consigne était juste pour le corps des docstrings, et fausse pour leur **première ligne** : PEP 257
  veut un résumé d'une seule ligne, et c'est elle que rendent `help()` et les éditeurs. Appliquée
  telle quelle, elle a coupé huit résumés en plein milieu de phrase — `SchemaObsolete` s'annonçait
  comme « Une base antérieure à une modification de schéma, que `create_all` n'atteint ». Les lignes
  de résumé sont **raccourcies**, le détail passant au paragraphe suivant ; le corps des docstrings,
  lui, reste coupé sans réécriture, ce qui était le bon geste et doit le rester.

## Design Notes

**Pourquoi mypy et pas `ty`.** Les huit `# type: ignore[arg-type]` du dépôt portent déjà des codes
d'erreur au format mypy. Avec `warn_unused_ignores`, ils cessent d'être décoratifs : un ignore qui ne
masque plus rien devient une erreur — et il y en a déjà un, à `test_recherche.py:1500`.

**Les tests sont vérifiés, pas seulement le code.** C'est là que vivent tous les ignores, et là que
2.1 et 2.2 ont posé leurs gardes de type. Un vérificateur qui ne lirait que `exaequo/` laisserait
sans surveillance précisément les fichiers qui documentent l'invariant.

**Ce que l'outillage ne remplace pas.** Les gardes `TypeError` de `recherche.py` restent : mypy ne
voit pas un appelant qui n'existe pas encore — un adaptateur primaire d'E3, une entrée venue du
langage naturel. Le vérificateur ferme la porte à l'écriture, la garde la ferme à l'exécution.

## Verification

**Commands :**
- `uv run ruff check .` — attendu : `All checks passed!`
- `uv run mypy` — attendu : `Success: no issues found`
- `uv run pytest` — attendu : 180 passés, aucun changement de décompte.

## Suggested Review Order

**La configuration — c'est là que sont les décisions, pas dans le code**

- Le jeu de règles, et surtout les quatre écartées : chacune porte sa raison en clair.
  [`pyproject.toml:39`](../../pyproject.toml#L39)
- L'exclusion du framework installé, rétrécie aux `skills/` : un `.claude/hooks/*.py` du projet est linté.
  [`pyproject.toml:29`](../../pyproject.toml#L29)
- `ARG001` levée sous `tests/` seulement : une fixture demandée pour son effet de bord n'est pas morte.
  [`pyproject.toml:61`](../../pyproject.toml#L61)
- `strict` sur le code **et** les tests, plus l'exigence qu'un ignore dise ce qu'il masque.
  [`pyproject.toml:66`](../../pyproject.toml#L66)

**Les six erreurs de la persistance — annoter sans masquer**

- La garde d'intégrité rendue visible au vérificateur par une variable distincte, jamais par un ignore.
  [`depots.py:115`](../../exaequo/adaptateurs/secondaires/persistance/depots.py#L115)
- Le `None` écarté là où le vérificateur peut le voir, pour une fonction qui promet `set[str]`.
  [`depots.py:133`](../../exaequo/adaptateurs/secondaires/persistance/depots.py#L133)
- `TypeDecorator` paramétré, et `dialect` gardé sous son nom : la signature est celle de SQLAlchemy.
  [`modeles.py:33`](../../exaequo/adaptateurs/secondaires/persistance/modeles.py#L33)
- L'écouteur `PRAGMA foreign_keys` annoté depuis les types que SQLAlchemy expose.
  [`base.py:52`](../../exaequo/adaptateurs/secondaires/persistance/base.py#L52)

**Ce que la revue a redressé dans les tests**

- Le protocole qui rend aux deux points d'entrée leur vraie signature — sans lui, mypy ne vérifiait plus rien.
  [`test_recherche.py:67`](../../tests/test_recherche.py#L67)
- Les deux affectations statiques qui épinglent le protocole sur les fonctions réelles.
  [`test_recherche.py:94`](../../tests/test_recherche.py#L94)
- La table du profil définie une seule fois, depuis `__table__` et non par un lookup faillible.
  [`conftest.py:31`](../../tests/conftest.py#L31)

**Le journal — deux consignes de la spec corrigées en cours de route**

- Pourquoi l'exclusion a grandi, puis rétréci ; et pourquoi « couper sans réécrire » ne valait pas pour les résumés.
  [`spec:117`](spec-outillage-verification-statique.md#L117)

