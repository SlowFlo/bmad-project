- source_spec: `documentation/implementation-artifacts/spec-e1-socle-du-vivier.md`
  summary: Le chemin du CSV d'amorçage (`Path(__file__).parents[2]`) ne résout que depuis une arborescence source ; le fichier n'est pas empaqueté par hatchling.
  evidence: `pyproject.toml` construit un wheel (`packages = ["exaequo"]`) sans inclure `documentation/`. Une installation non éditable échouerait au démarrage. Hors périmètre d'E1, dont l'enveloppe est une exécution locale depuis le dépôt.

- source_spec: `documentation/implementation-artifacts/spec-e1-socle-du-vivier.md`
  summary: Aucun index sur `profil.sport_id`, alors que « chercher les profils d'un sport » est l'usage central d'E2.
  evidence: SQLite n'indexe pas automatiquement les clés étrangères. `jour_disponible.profil_id` est couvert par le préfixe de `uq_jour_disponible_profil_jour`, `profil.sport_id` ne l'est pas. À trancher avec la recherche d'E2, qui connaîtra ses accès.
  resolution: Clos par `documentation/implementation-artifacts/spec-2-1-chercher-des-candidats-du-niveau-exact.md`. `DepotVivier.profils_du_sport` joint `profil` à `sport` sur la clé de sport et devient l'accès central du lot — 2.4 le parcourra 231 fois. L'index est posé : `Index("ix_profil_sport_id", "sport_id", "id")` dans les `__table_args__` de `ProfilORM` — **composite**, `sport_id` pour la jointure et `id` pour le `ORDER BY profil.id` qui la suit, faute de quoi SQLite retrie dans un `USE TEMP B-TREE`. Éprouvé dans `tests/test_recherche.py` par `PRAGMA index_list`, `PRAGMA index_info`, et surtout par un `EXPLAIN QUERY PLAN` sur la requête réellement émise : l'index doit y être nommé, sans `SCAN profil` ni `USE TEMP B-TREE`. Réserve : `creer_schema` est un `create_all` sans Alembic — un `exaequo.db` déjà créé n'obtient pas l'index et doit être supprimé pour le recevoir.

- source_spec: `documentation/implementation-artifacts/spec-e1-socle-du-vivier.md`
  summary: Rien n'interdit qu'un profil de population *inscrit* porte une `cle_amorcage`, ni ne relie *inscrit* à un `compte_id`.
  evidence: Le commentaire de la colonne affirme « elle ne contraint jamais un utilisateur inscrit » ; la contrainte symétrique n'existe pas. Aucun code n'écrit ce cas aujourd'hui — la première écriture d'un inscrit arrive avec E4/E5.

- source_spec: `documentation/implementation-artifacts/spec-e1-socle-du-vivier.md`
  summary: `.env.example` documente six clés mais aucun code ne lit de fichier `.env`.
  evidence: `python-dotenv` n'est pas dans la table *Stack* de la spine — l'ajouter relève du « Ask First ». Seules les variables d'environnement du shell ont un effet ; à trancher quand une clé sera réellement consommée (E3 pour Anthropic, E7 pour ATMO).

- source_spec: `documentation/implementation-artifacts/spec-e1-socle-du-vivier.md`
  summary: Une cellule « Sports pratiqués » multi-valuée fonderait un sport unique de clé jointe, sans erreur.
  evidence: `profil.sport_id` est scalaire et la cellule est prise telle quelle comme libellé, alors que « Jours disponibles » est découpée sur `;`. Les 86 lignes du CSV ne portent qu'un sport chacune, donc le cas est inatteignable en v1 ; il se pose si un profil inscrit déclare plusieurs sports.

- source_spec: `documentation/implementation-artifacts/spec-e1-socle-du-vivier.md`
  summary: `poser_synonyme` n'interdit ni une clé qui est déjà celle d'un sport, ni une chaîne de synonymes ; une fondation après redirection produirait un sport de clé cible et de libellé d'origine.
  evidence: Inatteignable en v1 — la table naît vide et `poser_synonyme` exige un `sport_id` existant. Le garde-fou devient nécessaire dès qu'une écriture peuplera la table de synonymes.

- source_spec: `documentation/implementation-artifacts/spec-e1-socle-du-vivier.md`
  summary: Aucune intégration continue : la suite ne s'exécute que si une personne tape `uv run pytest`.
  evidence: `.github/` ne contient que des définitions d'agents, aucun `workflows/`. Choix d'outillage à faire au niveau du dépôt, pas du lot.

- source_spec: `documentation/implementation-artifacts/spec-2-1-chercher-des-candidats-du-niveau-exact.md`
  summary: Aucun chemin de migration : une modification de schéma postérieure à E1 — l'index `ix_profil_sport_id` en est le premier cas réel — n'atteint jamais une base déjà créée, et rien ne le détecte.
  evidence: `creer_schema` est un `Base.metadata.create_all` sans Alembic. Reproduit : sur une base créée puis privée de l'index par `DROP INDEX`, rejouer `creer_schema` ne le repose pas et n'émet aucun message. Tous les tests restent verts, la fixture `moteur` fabriquant une base neuve dans `tmp_path` à chaque test. La seule protection est qu'une personne lise la réserve et supprime son `exaequo.db`.

- source_spec: `documentation/implementation-artifacts/spec-2-1-chercher-des-candidats-du-niveau-exact.md`
  summary: `_vers_profil` déclenche une requête `jour_disponible` par profil, et `profils_du_sport` en hérite : dix requêtes pour une seule recherche sur le tennis.
  evidence: Mesuré — une jointure plus neuf lectures. L'argument qui a justifié l'index vaut aussi ici : 2.4 parcourra 231 combinaisons, soit des milliers d'allers-retours là où l'index n'en économise que 231. Le code vient d'E1 ; la recherche ne fait que devenir son premier consommateur chaud. À trancher avec un `selectinload` ou une agrégation, quand une mesure dira que ça compte.

- source_spec: `documentation/implementation-artifacts/spec-2-1-chercher-des-candidats-du-niveau-exact.md`
  summary: Les entrées de ce fichier ne portent aucun identifiant, alors que `modeles.py` et `tests/test_recherche.py` citent « DW-1 » en dur.
  evidence: Seul le rang identifie une entrée. Insérer une entrée en tête renumérote silencieusement toutes les références écrites dans le code. Rien ne distingue non plus visuellement une entrée close d'une entrée ouverte. Correctif minimal : un champ `id:` par entrée, posé une fois pour toutes.

## Deferred from: code review of spec-2-1-chercher-des-candidats-du-niveau-exact (2026-08-31)

*Trois constats de cette revue — le N+1 de `_vers_profil`, l'absence d'`id:` sur les entrées de ce
fichier, et l'absence d'intégration continue — sont déjà enregistrés ci-dessus et ne sont pas
redoublés ici.*

- source_spec: `documentation/implementation-artifacts/spec-2-1-chercher-des-candidats-du-niveau-exact.md`
  summary: `assert isinstance(depot, PortVivier)` ne prouve que la présence des méthodes, jamais leur signature.
  evidence: Un `Protocol` `@runtime_checkable` ne vérifie ni le nom des paramètres, ni l'arité, ni le type de retour. Un `DepotVivier.profils_du_sport` qui se mettrait à filtrer, ou qui perdrait `cle_sport`, passerait encore. Le correctif — une affectation statique `_: PortVivier = DepotVivier(session)` — ne vaut que s'il existe un vérificateur de types, ce qui rattache cette entrée à celle de l'outillage.

- source_spec: `documentation/implementation-artifacts/spec-2-1-chercher-des-candidats-du-niveau-exact.md`
  summary: Aucun vérificateur de types ni linter, alors que le dépôt porte des `# type: ignore` qui ne sont vérifiés par rien.
  evidence: `pyproject.toml` ne déclare que `pytest==8.4.2` en dépendance de développement et n'a que `[tool.pytest.ini_options]`. Le défaut que la spec consigne elle-même — `niveau="debutant"` rendant un vide muet — est précisément la classe de bug qu'un vérificateur de types attrape ; la garde `_exiger_membre` le compense à l'exécution pour ce cas seul. Distinct de l'entrée « aucune intégration continue » : celle-ci porte sur l'outil, celle-là sur son déclenchement.
  resolution: Clos par `documentation/implementation-artifacts/spec-outillage-verification-statique.md`. `ruff==0.14.5` (lint seul, pas de formatage) et `mypy==1.18.2` sont épinglés au groupe `dev` de `pyproject.toml`, qui reçoit `[tool.ruff]` — `line-length = 88`, sélection `E,W,F,I,N,UP,B,C4,SIM,RUF,ARG,RET,TID`, chaque règle écartée portant sa raison en clair — et `[tool.mypy]` — `strict = true` sur `files = ["exaequo", "tests"]`, plus `enable_error_code = ["ignore-without-code"]`, sans quoi un `# type: ignore` nu échapperait à `warn_unused_ignores`. Le dépôt est à zéro erreur des deux côtés : 41 constats ruff et 67 constats mypy levés sans changer un seul comportement, et les 180 tests passent au même décompte. Les tests sont vérifiés au même titre que le code, puisque c'est là que vivent les huit `# type: ignore` : la mesure d'avant le lot en signalait un inutile — l'appel de `tests/test_recherche.py` volontairement privé de `niveau` — mais il ne l'était que faute de typage sur les deux points d'entrée ; un `Protocol` portant leur vraie signature a rétabli la vérification statique, et l'ignore est redevenu vivant. Les huit sont désormais prouvés utiles à chaque exécution. Le framework installé n'est jamais analysé : `extend-exclude` couvre `_bmad/` ainsi que `.claude/skills/` et `.agents/skills/`, ses deux copies conformes — et eux seuls, ce que le projet écrirait lui-même sous `.claude/` restant analysé. Réserve, en clair : **rien ne déclenche** `uv run ruff check .` ni `uv run mypy` — aucun hook, aucun job, aucun test ne les appelle. Le dépôt est propre à cet instant et ne le reste que si quelqu'un tape les deux commandes avant de livrer ; leur déclenchement est l'objet de l'entrée « aucune intégration continue », qui reste ouverte.

- source_spec: `documentation/implementation-artifacts/spec-2-1-chercher-des-candidats-du-niveau-exact.md`
  summary: `profils_du_sport` accepte un libellé d'affichage non normalisé et rend une liste vide indiscernable d'un sport absent.
  evidence: Le contrat de `PortVivier` exige la clé normalisée, et `chercher_candidats_exacts` la produit toujours par `cle_sport`. Mais rien dans le dépôt ne refuse `profils_du_sport("Tennis")`, qui rend simplement vide. Aucun appelant fautif n'existe aujourd'hui — la recherche est le seul consommateur. Une garde `replier_texte(cle) == cle` fermerait la porte avant qu'un adaptateur primaire d'E3 ne l'ouvre.

- source_spec: `documentation/implementation-artifacts/spec-2-1-chercher-des-candidats-du-niveau-exact.md`
  summary: Trois exclusions de CAP-5 ne sont éprouvées que contre le faux port, jamais contre le vivier réel.
  evidence: `test_le_port_rend_un_niveau_inconnu_que_le_domaine_ecarte` existe précisément parce que prouver une exclusion contre le seul faux port la prouve « là où c'est le plus facile ». Les lignes « Soi-même », « Jour indisponible » et « Sans jour déclaré » de la matrice n'ont pas reçu le même traitement.

- source_spec: `documentation/implementation-artifacts/spec-2-1-chercher-des-candidats-du-niveau-exact.md`
  summary: `sprint-status.yaml` : clés d'histoires tronquées et diversement accentuées, `action_items` documenté mais absent, dates en MM-DD-YYYY non étiquetées.
  evidence: `2-1-chercher-…` est en ASCII quand `2-2-élargir-…` garde ses accents ; `6-4-…-explique-d-où-il-s`, `7-2-…-jouabilité-applicabl` et `9-2-…-d-un-profi` sont coupées vers 60 caractères. Aucune clé ne se relie mécaniquement à un nom de fichier de spec. L'en-tête définit des statuts d'`action_items` et une clé `action_items:` qui n'existe pas dans le fichier. Fichier produit par `sprint-planning`, pas par ce lot : à traiter chez son générateur.

- source_spec: `documentation/implementation-artifacts/spec-2-1-chercher-des-candidats-du-niveau-exact.md`
  summary: `epic-2-context.md` se dit compilé depuis les artefacts de planification sans citer un seul chemin source, et ses nombres contractuels n'ont aucune provenance.
  evidence: L'en-tête dit « Régénérez avec compile-epic-context si les documents de planification changent » sans nommer ni `epics.md`, ni le PRD, ni la SPEC : rien ne permet de savoir si le fichier est périmé. « 127 combinaisons sans candidat exact », « au moins 85 % sans dépasser 89 % », « de 6,1 % à 3,0 % » sont affirmés à plat, alors que 2.4 est précisément l'histoire qui les mesurera — sans dire contre quelle révision du jeu de données ni ce qu'il advient d'un désaccord.

- source_spec: `documentation/implementation-artifacts/spec-2-1-chercher-des-candidats-du-niveau-exact.md`
  summary: `test_recherche.py` (967 lignes) mêle quatre préoccupations sans rapport.
  evidence: Règles du domaine contre faux port, repères sur les données d'amorçage, assertions SQLite (`PRAGMA index_list`, `PRAGMA index_info`, `EXPLAIN QUERY PLAN`) et gardes par AST/introspection. Les tests d'index et de plan sont des tests de persistance, pas de recherche ; le dépôt montre déjà la séparation avec `tests/test_domaine_sans_dependance.py`.

## Deferred from: spec-2-2-elargir-sur-le-jour-et-sur-lui-seul (2026-08-31)

- source_spec: `documentation/implementation-artifacts/spec-2-2-elargir-sur-le-jour-et-sur-lui-seul.md`
  summary: Les candidats sont rendus avec leurs jours **déclarés**, non avec leurs jours effectivement disponibles : un jour immobilisé par `jours_indisponibles` resterait affiché par E3.
  evidence: `_jours_effectivement_disponibles` retranche bien les jours immobilisés pour *décider* — l'exact exige que le jour demandé y soit, l'élargissement que l'ensemble soit non vide — mais le `Profil` rendu porte toujours son `jours_disponibles` d'origine, et rien ne projette la différence dans le résultat. Inatteignable aujourd'hui : `jours_indisponibles` est vide par défaut et E5 n'existe pas encore, donc aucun appelant réel ne passe de blocage. La projection appartient à 2.3, qui en a besoin de toute façon pour compter le délai d'attente vers l'avant depuis le jour demandé : compter sur un jour immobilisé donnerait un délai faux, pas seulement un affichage faux.

- source_spec: `documentation/implementation-artifacts/spec-2-2-elargir-sur-le-jour-et-sur-lui-seul.md`
  summary: Un résultat vide ne porte rien qui dise que l'élargissement a été tenté puis épuisé, alors que CAP-7 exige de le dire.
  evidence: CAP-7 veut que la réponse « nomme le sport et le jour tentés, et dise ce qui a été élargi — tous les autres jours — avant de conclure qu'il n'y a personne à ce niveau ». Or `jour_demande_indisponible` qualifie des candidats et reste faux sur un vide, par conception assumée (voir les notes de conception de 2.2) : « Pilates, avancé » élargi puis épuisé, « squash » inconnu du vivier, et un exact vide sont trois résultats indiscernables. E3 devra soit recevoir cette information du domaine, soit la reconstruire — et la reconstruire, c'est inventer. À trancher au moment d'écrire CAP-7, pas ici : 2.2 n'a pas d'exigence qui la porte.

