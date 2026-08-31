- source_spec: `documentation/implementation-artifacts/spec-e1-socle-du-vivier.md`
  summary: Le chemin du CSV d'amorçage (`Path(__file__).parents[2]`) ne résout que depuis une arborescence source ; le fichier n'est pas empaqueté par hatchling.
  evidence: `pyproject.toml` construit un wheel (`packages = ["exaequo"]`) sans inclure `documentation/`. Une installation non éditable échouerait au démarrage. Hors périmètre d'E1, dont l'enveloppe est une exécution locale depuis le dépôt.

- source_spec: `documentation/implementation-artifacts/spec-e1-socle-du-vivier.md`
  summary: Aucun index sur `profil.sport_id`, alors que « chercher les profils d'un sport » est l'usage central d'E2.
  evidence: SQLite n'indexe pas automatiquement les clés étrangères. `jour_disponible.profil_id` est couvert par le préfixe de `uq_jour_disponible_profil_jour`, `profil.sport_id` ne l'est pas. À trancher avec la recherche d'E2, qui connaîtra ses accès.

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
