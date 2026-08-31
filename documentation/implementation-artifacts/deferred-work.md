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
