---
title: '2.1 — Chercher des candidats du niveau exact'
type: 'feature'
created: '2026-08-31'
status: 'done'
baseline_commit: '0802668b2e6c3a1650b7c037da0378befca837b1'
review_loop_iteration: 0
context:
  - '{project-root}/documentation/implementation-artifacts/epic-2-context.md'
  - '{project-root}/documentation/specs/spec-ex-aequo/criteres-acceptation.md'
  - '{project-root}/documentation/specs/spec-ex-aequo/glossaire.md'
---

<frozen-after-approval reason="human-owned intent — do not modify unless human renegotiates">

## Intent

**Problème :** Le socle du vivier est livré, mais rien ne sait l'interroger : aucun code ne rend les
profils d'un sport, d'un jour et d'un niveau. Tant que la recherche exacte n'existe pas, la promesse
qui fonde le produit — l'égalité stricte de niveau — reste une intention, et SM-3 n'est pas mesurable.

**Approche :** Poser le premier morceau de `domaine/recherche` : un point d'entrée unique qui, à
partir d'un libellé de sport, d'un jour et d'un niveau, rend les candidats **exactement** de ce
niveau. La règle vit dans le domaine, pur et sans SQL ; la persistance ne fait que rétrécir par la
clé de sport, derrière un protocole déclaré dans `domaine/ports.py` comme la spine le prescrit.

## Boundaries & Constraints

**Always :**
- L'égalité de niveau est **structurelle** : `niveau: Niveau` est obligatoire, jamais `None`, et
  aucune signature n'expose de paramètre de tolérance, d'adjacence ou de repli.
- La comparaison porte sur la **clé de sport normalisée** (`cle_sport`), jamais sur le libellé.
- Toutes les exclusions sont appliquées **dans le domaine**, donc éprouvables sans base : niveau
  inconnu (`niveau is None`), profil sorti du vivier (`sortie_vivier_le is not None`), le demandeur
  lui-même, et un profil dont le jour considéré est déclaré indisponible.
- La recherche accepte dès maintenant un **ensemble de jours indisponibles** en paramètre, pour
  qu'E5 y branche la dérivation du jour bloqué sans réécrire cette signature (AD-6).
- Ordre déterministe : celui du vivier (`ORDER BY profil.id`), préservé de bout en bout.
- Vocabulaire du glossaire jusque dans les symboles : `candidat`, `vivier`, `niveau`,
  `jour_disponible`. Jamais `match`, `slot`, `booking`.

**Ask First :**
- Toute dépendance nouvelle dans `pyproject.toml`.
- Toute modification du schéma autre que l'ajout de l'index sur `profil.sport_id`.
- Tout changement des types ou des dépôts livrés par E1 au-delà d'un ajout de méthode.

**Never :**
- Consulter la table de synonymes à la lecture (`synonymes()`, `resoudre_libelle`,
  `resoudre_a_l_ecriture` sont interdits ici — AD-5), ni fonder un sport pendant une recherche.
- Importer `sqlalchemy` ou quoi que ce soit de `exaequo.adaptateurs` depuis `exaequo/domaine/`.
- Implémenter l'élargissement sur le jour (2.2), le délai d'attente, le tri par délai ou le plafond
  de trois candidats (2.3), le parcours des 231 combinaisons (2.4).
- Lever une exception sur un sport inconnu : le résultat est vide.

## I/O & Edge-Case Matrix

| Scénario | Entrée / État | Sortie / Comportement attendu | Traitement d'erreur |
|----------|---------------|-------------------------------|---------------------|
| Chemin nominal | Vivier d'amorçage ; « Tennis », mardi, débutant | Un seul candidat : Emma Leroy | N/A |
| Vide en exact | Même demande en intermédiaire | Aucun candidat ; aucun élargissement tenté | N/A |
| Niveau inconnu | Profil du bon sport et du bon jour, `niveau is None` | Jamais rendu | N/A |
| Sorti du vivier | Profil correspondant, `sortie_vivier_le` valué | Jamais rendu | N/A |
| Soi-même | Demandeur au vivier, même sport et même niveau | Jamais rendu comme son propre partenaire | N/A |
| Casse et accents | « tennis », « Tennis », «  TENNIS  » | Les trois rendent le même ensemble | N/A |
| Jour indisponible | `(profil.id, mardi)` dans `jours_indisponibles` | Écarté ce jour-là, rendu sur ses autres jours | N/A |
| Sans jour déclaré | Profil sans aucune ligne `jour_disponible` | Jamais rendu | N/A |
| Sport inconnu | « squash », absent du vivier | Résultat vide, aucune écriture | Aucune exception |

</frozen-after-approval>

## Code Map

- `exaequo/domaine/vivier.py:48` `Niveau` (trois membres) · `:60` `JourSemaine` (sept membres,
  **sans ordre de semaine**) · `:127` `Profil` — champs utiles ici : `id`, `sport_id`,
  `jours_disponibles: frozenset[JourSemaine]`, `niveau: Niveau | None`, `:152` `sortie_vivier_le`.
  Le **niveau inconnu est une absence**, jamais une quatrième valeur.
- `exaequo/domaine/sports.py:33` `cle_sport(libelle) -> str` — la seule normalisation à appeler.
  `:55` `resoudre_libelle` — **interdit en lecture**.
- `exaequo/domaine/ports.py` — **n'existe pas encore**, prescrit par la spine ; à créer ici.
- `exaequo/adaptateurs/secondaires/persistance/depots.py:117` `DepotVivier(session)` · `:156`
  `profils_ordonnes()` (motif `ORDER BY profil.id` à reprendre) · `:224` `_vers_profil` — **le seul
  mapper ORM→domaine, à réutiliser** (une requête `jour_disponible` par profil ; indolore sur 86).
  `:49` `DepotSports.par_cle` — lecture par clé, ne consulte jamais les synonymes.
- `exaequo/adaptateurs/secondaires/persistance/modeles.py:110` `ProfilORM` (`:129` FK `sport_id`,
  `:133` `niveau` nullable) · `:98` `SynonymeORM`. **Aucun `Index` dans tout le paquet** — c'est DW-1.
- `exaequo/adaptateurs/secondaires/persistance/base.py:50` `creer_schema` = `create_all`, **sans
  Alembic** : un index ajouté n'atteint pas un `exaequo.db` déjà créé.
- `tests/test_domaine_sans_dependance.py:18` — l'AST refuse tout import de `sqlalchemy` ou de
  `exaequo.adaptateurs` sous `exaequo/domaine/`. Le nouveau module y est soumis automatiquement.
- `tests/conftest.py:26` `moteur` (base fichier dans `tmp_path`) · `:43` dépôts. **Aucune fixture de
  vivier peuplé** ; motif de chargement dans `tests/test_chargement_amorcage.py:23`.
- `documentation/implementation-artifacts/deferred-work.md` — entrée DW-1 (index `profil.sport_id`).

## Tasks & Acceptance

**Execution :**
- [x] `exaequo/domaine/ports.py` — créer. `PortVivier(Protocol)` avec la seule méthode
  `profils_du_sport(cle_sport: str) -> Sequence[Profil]`, contrat documenté : rend **tous** les
  profils de cette clé, dans l'ordre du vivier, sans filtrer ni le niveau ni la sortie du vivier —
  les exclusions appartiennent au domaine. `typing` seul, aucune autre dépendance.
- [x] `exaequo/domaine/recherche.py` — créer. `ResultatRecherche` (`frozen=True, slots=True`) portant
  `cle_sport`, `jour`, `niveau`, `candidats: tuple[Profil, ...]`, et
  `chercher_candidats_exacts(vivier, *, libelle_sport, jour, niveau, demandeur_id=None,
  jours_indisponibles=frozenset())`. Normalise le libellé, appelle le port, applique les exclusions,
  préserve l'ordre reçu. Pur.
- [x] `exaequo/adaptateurs/secondaires/persistance/modeles.py` — poser
  `Index("ix_profil_sport_id", "sport_id", "id")` dans les `__table_args__` de `ProfilORM` : la
  jointure par clé de sport est l'accès central du lot (DW-1). **Composite** : la seule colonne
  `sport_id` sert la jointure mais laisse le `ORDER BY profil.id` se payer un `USE TEMP B-TREE`.
- [x] `exaequo/adaptateurs/secondaires/persistance/depots.py` — ajouter
  `DepotVivier.profils_du_sport(cle_sport)` : jointure `profil → sport` sur `sport.cle`,
  `ORDER BY profil.id`, mappée par `_vers_profil`. `DepotVivier` satisfait dès lors `PortVivier`.
- [x] `tests/conftest.py` — ajouter une fixture `vivier_amorce` qui charge les 86 profils et commite.
- [x] `tests/test_recherche.py` — créer. Couvrir chaque ligne de la matrice d'E/S : les cas de règle
  avec un faux port en mémoire, les repères Tennis et la non-consultation des synonymes sur le vivier
  amorcé. Vérifier que `DepotVivier` satisfait `PortVivier`.
- [x] `documentation/implementation-artifacts/deferred-work.md` — clore l'entrée DW-1 en lui ajoutant
  une ligne `resolution:` nommant cette spec et l'index posé. Ne toucher à aucune autre entrée.

**Acceptance Criteria :**
- Étant donné une base créée par `creer_schema`, quand on inspecte les index de `profil`, alors
  `ix_profil_sport_id` existe.
- Étant donné le chemin de recherche, quand on y cherche un appel à `synonymes`, `resoudre_libelle`
  ou `resoudre_a_l_ecriture`, alors il n'y en a aucun.
- Étant donné n'importe quelle signature publique de `recherche.py`, quand on l'inspecte, alors aucun
  paramètre ne permet d'obtenir un candidat d'un niveau autre que celui demandé.

## Spec Change Log

- **2026-08-31 — index composite plutôt que sur la seule clé de sport.** La revue adversariale a lu
  le plan de la requête réelle : `SEARCH profil USING INDEX ix_profil_sport_id (sport_id=?)` était
  bien suivi de `USE TEMP B-TREE FOR ORDER BY`. L'index porte désormais `("sport_id", "id")` et sert
  aussi l'ordre du vivier. Le **nom est inchangé** — le critère d'acceptation, le test et la ligne
  `resolution:` de `deferred-work.md` le citent.
- **2026-08-31 — `niveau` et `jour` refusent une chaîne.** `Niveau` et `JourSemaine` étant des
  `StrEnum` et le dépôt n'ayant pas de vérificateur de types, `niveau="debutant"` rendait **zéro
  candidat sans la moindre erreur** — un vide indiscernable d'un vivier vide, sur la promesse qui
  fonde le produit — et `jour="mardi"` comparait juste par accident. `chercher_candidats_exacts`
  lève maintenant `TypeError` sur l'un comme sur l'autre. On refuse, on ne convertit pas :
  rattraper une chaîne rouvrirait une seconde façon de nommer un niveau.

## Design Notes

**Pourquoi un port plutôt qu'une fonction sur une liste déjà chargée.** La spine veut le domaine sans
dépendance sortante, ses protocoles dans `ports.py`. Le port donne au fil (E3) un point d'entrée
unique, au lieu de laisser « normaliser → charger → filtrer » se réinventer dans chaque appelant.

**Le port ne filtre pas, il rétrécit.** Il ne connaît que la clé de sport. Le niveau, la sortie du
vivier, le demandeur et les jours indisponibles sont écartés par le domaine — c'est ce qui rend les
règles éprouvables avec un faux port, sans base.

**La forme des jours indisponibles.** Un ensemble de couples `(UUID, JourSemaine)`, pas un ensemble
de jours : le blocage d'E5 est propre à un profil et à un jour, et un profil bloqué mardi reste rendu
le jeudi. La valeur par défaut vide rend le paramètre inerte tant qu'E5 n'existe pas.

**L'index n'est pas cosmétique.** `profils_du_sport` joint `profil` à `sport` : sans index sur
`profil.sport_id`, SQLite balaie la table à chaque recherche — et 2.4 en fera 231. À signaler à
l'humain : `create_all` ne pose l'index que sur une base neuve ; un `exaequo.db` local existant doit
être supprimé pour l'obtenir.

## Verification

**Commands :**
- `uv run pytest` — attendu : les 94 tests existants passent toujours, plus ceux de
  `tests/test_recherche.py`.
- `uv run python -m exaequo --amorcer-seulement` sur une base neuve, puis `PRAGMA index_list(profil)`
  — attendu : `ix_profil_sport_id` présent.

## Suggested Review Order

**Le protocole — ce que le domaine attend, et ce qu'il ne délègue pas**

- Le port du vivier : une seule méthode, et un contrat qui dit explicitement qu'elle **ne filtre rien**.
  [`ports.py:27`](../../exaequo/domaine/ports.py#L27)

**Le domaine — l'égalité de niveau rendue structurelle**

- Le résultat : la clé interrogée, le jour, le niveau commun du groupe, et les candidats gelés.
  [`recherche.py:37`](../../exaequo/domaine/recherche.py#L37)
- Le point d'entrée : `niveau: Niveau` obligatoire, aucun paramètre de tolérance, d'adjacence ni de repli.
  [`recherche.py:51`](../../exaequo/domaine/recherche.py#L51)
- La garde qui refuse un libellé à la place d'un membre d'énumération — sans quoi `"debutant"` rendrait un vide muet.
  [`recherche.py:102`](../../exaequo/domaine/recherche.py#L102)
- Les cinq exclusions de CAP-5, toutes ici et donc éprouvables sans base.
  [`recherche.py:124`](../../exaequo/domaine/recherche.py#L124)

**La persistance — rétrécir par la clé, sans jamais décider**

- La jointure `profil → sport` sur `sport.cle`, `ORDER BY profil.id`, sans consulter les synonymes (AD-5).
  [`depots.py:161`](../../exaequo/adaptateurs/secondaires/persistance/depots.py#L161)
- L'index composite qui clôt DW-1 : `sport_id` pour la jointure, `id` pour l'ordre du vivier.
  [`modeles.py:131`](../../exaequo/adaptateurs/secondaires/persistance/modeles.py#L131)

**Vérification — la matrice d'E/S, ligne par ligne**

- Le faux port en mémoire : il porte sa propre correspondance clé → profils, et laisse aux profils leur libellé d'affichage.
  [`test_recherche.py:49`](../../tests/test_recherche.py#L49)
- Le refus bruyant d'une chaîne à la place d'un `Niveau` ou d'un `JourSemaine`.
  [`test_recherche.py:446`](../../tests/test_recherche.py#L446)
- Le repère de CAP-5 sur les données réelles : « Tennis, mardi, débutant » rend Emma Leroy.
  [`test_recherche.py:505`](../../tests/test_recherche.py#L505)
- `DepotVivier` satisfait `PortVivier`.
  [`test_recherche.py:626`](../../tests/test_recherche.py#L626)
- La frontière du contrat contre la base : le port rend un niveau inconnu, le domaine l'écarte.
  [`test_recherche.py:701`](../../tests/test_recherche.py#L701)
- L'ordre du vivier quand il diverge de l'ordre d'insertion, et la clause `ORDER BY` qui le porte.
  [`test_recherche.py:747`](../../tests/test_recherche.py#L747)
- L'index constaté par `PRAGMA index_list`, puis ses colonnes par `PRAGMA index_info`.
  [`test_recherche.py:804`](../../tests/test_recherche.py#L804)
- Le plan de la requête réellement émise : l'index est emprunté, `profil` n'est pas balayé, l'ordre ne coûte pas un tri.
  [`test_recherche.py:827`](../../tests/test_recherche.py#L827)
- Aucune consultation de la table de synonymes sur le chemin de lecture, lue par l'AST.
  [`test_recherche.py:861`](../../tests/test_recherche.py#L861)
- Le test négatif de l'égalité stricte : aucune surface publique — fonction, classe ou méthode — n'ouvre sur un autre niveau.
  [`test_recherche.py:920`](../../tests/test_recherche.py#L920)
- La fixture du vivier amorcé, chargé par le chemin réel du produit.
  [`conftest.py:55`](../../tests/conftest.py#L55)
