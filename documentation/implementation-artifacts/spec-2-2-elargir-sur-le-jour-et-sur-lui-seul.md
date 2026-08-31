---
title: '2.2 — Élargir sur le jour, et sur lui seul'
type: 'feature'
created: '2026-08-31'
status: 'done'
baseline_commit: 'd59df30d58fbef41babba926d728756c11b7bc54'
review_loop_iteration: 0
context:
  - '{project-root}/documentation/implementation-artifacts/epic-2-context.md'
  - '{project-root}/documentation/implementation-artifacts/spec-2-1-chercher-des-candidats-du-niveau-exact.md'
  - '{project-root}/documentation/specs/spec-ex-aequo/criteres-acceptation.md'
  - '{project-root}/documentation/specs/spec-ex-aequo/glossaire.md'
---

<frozen-after-approval reason="human-owned intent — do not modify unless human renegotiates">

## Intent

**Problème :** La recherche exacte rend vide sur 127 des 231 combinaisons d'amorçage, et rien ne
prend le relais : « Tennis, mardi, intermédiaire » ne rend personne alors qu'Anna, Iris et Tessa sont
disponibles d'autres jours, exactement à ce niveau.

**Approche :** Ajouter à `domaine/recherche.py` le point d'entrée produit : l'exact d'abord, puis —
**si et seulement si** il n'a rien rendu — le même appariement en relâchant le jour, et lui seul. Le
résultat porte, comme donnée, que le jour demandé n'était pas disponible.

## Boundaries & Constraints

**Always :**
- Le jour est la **seule** contrainte relâchée : clé de sport et niveau identiques, et toutes les
  exclusions de CAP-5 s'appliquent encore après élargissement.
- L'élargissement n'est tenté **que** sur un exact vide, et se voit dans le résultat.
- Un candidat dont tous les jours déclarés sont immobilisés par `jours_indisponibles` n'est jamais
  rendu.
- Les cinq gardes de type d'entrée de l'exact valent aussi pour le nouveau point d'entrée.
- Vocabulaire du glossaire : *candidat*, *élargissement*, *vivier*, *niveau*, *jour disponible*.

**Ask First :**
- Toute dépendance nouvelle, toute modification du schéma, tout changement à `PortVivier`.
- Tout affaiblissement des gardes d'AC-3 de 2.1 (`FUITES_DE_NIVEAU`, listes blanches de surface et de
  paramètres) au-delà de l'inscription délibérée du nouveau point d'entrée.

**Never :**
- Délai d'attente, tri, plafond de trois (2.3) ; parcours des 231 combinaisons (2.4).
- Élargir sur autre chose que le jour — ni sport, ni niveau — même par un paramètre inerte.
- Toucher à la persistance, aux modèles ou aux dépôts : ce lot est du domaine pur.
- Consulter la table de synonymes sur le chemin de lecture (AD-5).

## I/O & Edge-Case Matrix

| Scénario | Entrée / État | Sortie / Comportement attendu | Traitement d'erreur |
|----------|---------------|-------------------------------|---------------------|
| Élargissement nominal | Vivier d'amorçage ; « Tennis », mardi, intermédiaire | Anna, Iris, Tessa dans l'ordre du vivier, chacune avec ses jours ; le résultat porte que le jour demandé n'était pas disponible | N/A |
| Exact non vide | « Tennis », mardi, débutant | Emma Leroy seule ; aucun élargissement, le drapeau reste faux | N/A |
| Le jour, et lui seul | Autre sport ou autre niveau, disponibles d'autres jours | Jamais rendus | N/A |
| Exclusions maintenues | Niveau inconnu, sorti du vivier, demandeur lui-même, aucun jour déclaré | Jamais rendus, même après élargissement | N/A |
| Blocage partiel | Profil bloqué mardi, libre jeudi | Rendu par l'élargissement | N/A |
| Blocage total | Tous ses jours déclarés immobilisés | Jamais rendu | N/A |
| Vivier vraiment vide | « Pilates », avancé | Aucun candidat ; le drapeau reste faux | N/A |
| Sport inconnu | « squash », absent du vivier | Résultat vide, aucune écriture | Aucune exception |
| Entrée mal typée | `niveau`, `jour`, `libelle_sport`, `demandeur_id` ou `jours_indisponibles` mal typés | Jamais de vide muet | `TypeError` nommant le paramètre |

</frozen-after-approval>

## Code Map

- `exaequo/domaine/recherche.py` — `:51` `chercher_candidats_exacts` : ses cinq gardes (`:86`) et sa
  normalisation puis appel au port (`:92`) sont à **réutiliser**, non à recopier. `:36`
  `ResultatRecherche` (`frozen`, `slots`) reçoit le nouveau champ, avec défaut. `:185`
  `_est_candidat` porte les exclusions de CAP-5 ; `:200` teste le jour — la seule ligne relâchée.
  `:29` `__all__`.
- `exaequo/domaine/ports.py:29` `PortVivier.profils_du_sport` — **inchangé** : un seul appel, les
  profils chargés une fois se filtrent deux fois.
- `exaequo/domaine/vivier.py:141` `Profil.jours_disponibles: frozenset[JourSemaine]` — les jours
  déclarés, déjà portés par candidat.
- `tests/test_recherche.py` — `:50` `VivierEnMemoire`, `:80` `_profil`, `:107` `_prenoms` à
  réutiliser. `:896` `FUITES_DE_NIVEAU` contient `"elargi"` : **aucun symbole public de
  `recherche.py` ne doit porter ce mot**. `:958` `SURFACE_PUBLIQUE_ADMISE` et `:959`
  `PARAMETRES_ADMIS_DE_LA_RECHERCHE` sont des listes blanches exactes : tout ajout non inscrit fait
  échouer `test_la_surface_publique_de_recherche_est_exactement_celle_attendue`.
- `tests/conftest.py:60` `vivier_amorce` — les 86 profils par le chemin réel. Données : Anna Perrot
  (mercredi, samedi), Iris Payet (lundi, mercredi), Tessa Armand (lundi, samedi) — les trois seules
  intermédiaires de Tennis, dans cet ordre de vivier.

## Tasks & Acceptance

**Execution :**
- [x] `exaequo/domaine/recherche.py` — champ `jour_demande_indisponible: bool = False` sur
  `ResultatRecherche`, **vrai seulement** quand l'élargissement a produit des candidats. Le nom évite
  `elargi`, réservé à la liste noire d'AC-3.
- [x] `exaequo/domaine/recherche.py` — `chercher_candidats(...)`, de signature identique à l'exact :
  un seul appel au port, filtre exact, puis si vide un second filtre qui relâche le jour. Extraire un
  `_jours_effectivement_disponibles(profil, jours_indisponibles)` partagé — l'exact demande que le
  jour demandé y soit, l'élargi que l'ensemble soit non vide. Le geste d'élargissement reste privé.
  Inscrire dans `__all__`.
- [x] `tests/test_recherche.py` — une section couvrant chaque ligne de la matrice ; inscrire
  délibérément `chercher_candidats` et ses paramètres dans les deux listes blanches ; test négatif :
  sur le vivier amorcé, aucun candidat rendu après élargissement n'est d'un autre niveau.
- [x] `documentation/implementation-artifacts/deferred-work.md` — une entrée : les candidats sont
  rendus avec leurs jours **déclarés**, non effectivement disponibles ; un jour immobilisé resterait
  affiché par E3. La projection appartient à 2.3, qui en a besoin pour le délai d'attente. Ne toucher
  à aucune entrée existante.

**Acceptance Criteria :**
- Étant donné un exact non vide, quand `chercher_candidats` s'exécute, alors elle rend exactement les
  candidats de l'exact, y compris là où l'élargissement en aurait rendu davantage.
- Étant donné la surface publique de `recherche.py`, quand on l'inspecte, alors aucun nom ni
  paramètre ne porte un mot de `FUITES_DE_NIVEAU`, et les deux listes blanches la décrivent
  exactement.
- Étant donné `uv run pytest`, quand la suite s'exécute, alors aucun test de 2.1 ne régresse.

## Spec Change Log

## Design Notes

**Deux points d'entrée, pas un drapeau.** `chercher_candidats_exacts` reste inchangée : E9 en a
besoin telle quelle, une alerte se déclenchant sur une correspondance **exacte**. Un paramètre
`elargir=True` aurait rendu optionnel ce qui est systématique, et ajouté un paramètre à la signature
qu'AC-3 verrouille.

**Le nom public ne dit pas « élargir ».** La liste noire d'AC-3 refuse `elargi` dans tout symbole
public de `recherche.py`, précisément pour interdire `elargir_le_niveau` : on ne l'affaiblit pas pour
se faire de la place. Le geste s'appelle `_elargir_sur_le_jour`, privé.

**Le drapeau qualifie des candidats, jamais un vide.** Vrai, il dit « ceux-ci ne sont pas disponibles
le jour demandé » — nécessairement vrai, sinon l'exact les aurait rendus. Sur un vivier vide ou un
sport inconnu il reste faux : le résultat ne prétend pas que le jour était en cause.

## Verification

**Commands :**
- `uv run pytest` — attendu : suite verte, aucune régression de 2.1.
- `uv run python -c "from exaequo.domaine import recherche; print(recherche.__all__)"` — attendu :
  `chercher_candidats` présent, aucun symbole public portant `elargi`.

## Suggested Review Order

**Le point d'entrée produit — l'exact d'abord, le jour relâché ensuite**

- Le seul endroit qui décide d'élargir : « si et seulement si » l'exact rend vide.
  [`recherche.py:132`](../../exaequo/domaine/recherche.py#L132)
- Le drapeau, avec défaut, pour ne casser aucune construction de 2.1.
  [`recherche.py:74`](../../exaequo/domaine/recherche.py#L74)

**Le partage plutôt que la copie — ce qui ne peut pas diverger entre les deux entrées**

- Les cinq gardes, la normalisation, et l'unique appel au port, matérialisé pour deux passes.
  [`recherche.py:201`](../../exaequo/domaine/recherche.py#L201)
- L'égalité de niveau vit ici, et nulle part ailleurs : le seul endroit à relire.
  [`recherche.py:373`](../../exaequo/domaine/recherche.py#L373)
- Le seul point où l'exact et l'élargissement diffèrent : appartenance contre non-vacuité.
  [`recherche.py:392`](../../exaequo/domaine/recherche.py#L392)
- Le geste privé : il ne reçoit même pas de quoi relâcher le sport ou le niveau.
  [`recherche.py:256`](../../exaequo/domaine/recherche.py#L256)

**Vérification — le repère, puis les gardes que la revue a durcies**

- « Tennis, mardi, intermédiaire » rend Anna, Iris et Tessa, dans l'ordre du vivier.
  [`test_recherche.py:655`](../../tests/test_recherche.py#L655)
- Le cas le plus tentant : un seul exact interdit un élargissement plus généreux.
  [`test_recherche.py:715`](../../tests/test_recherche.py#L715)
- Autre sport, autre niveau : le port n'est même pas interrogé ailleurs.
  [`test_recherche.py:734`](../../tests/test_recherche.py#L734)
- Tous ses jours immobilisés : aucun candidat sans jour n'est jamais proposé.
  [`test_recherche.py:868`](../../tests/test_recherche.py#L868)
- Le test négatif du niveau sur la grille — sans les chiffres de SM-3, qui sont à 2.4.
  [`test_recherche.py:1004`](../../tests/test_recherche.py#L1004)
- La signature du nouveau point d'entrée est celle de l'exact, à la lettre.
  [`test_recherche.py:1507`](../../tests/test_recherche.py#L1507)
- `__all__` fixé : un alias public ne traverse plus liste noire et liste blanche.
  [`test_recherche.py:1448`](../../tests/test_recherche.py#L1448)

