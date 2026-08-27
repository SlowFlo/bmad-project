# Revue d'accessibilité — Ex Aequo v3

**Référentiel** : WCAG 2.2 niveau AA (les critères AAA sont signalés comme tels et n'entrent pas dans le décompte d'échec).
**Périmètre** : `DESIGN.md` v3, `EXPERIENCE.md` v3, et les quatre maquettes `mockups/key-fil-a-froid.html`, `key-declaration-niveau.html`, `key-proposition-partenaires.html`, `key-recap-en-attente.html`.
**Date** : 2026-08-27.

**Méthode.** Tous les ratios de contraste ont été **recalculés** à partir des valeurs hexadécimales de la frontmatter de `DESIGN.md` (formule de luminance relative WCAG 2.x), sans reprendre aucun chiffre écrit. Les maquettes ont été chargées dans un navigateur réel et instrumentées : largeur de redistribution, débordement horizontal, espacement de texte forcé de 1.4.12, tailles de cible calculées, noms accessibles calculés, inventaire des repères et des rôles. Chaque constat cite le fichier et la ligne. Les encadrés d'explication des deux spines ont été lus avant conclusion : **une section entière ci-dessous liste ce qui a été vérifié et délibérément non signalé**, parce que le document l'a déjà identifié et traité.

> **Note de périmètre.** Trois maquettes supplémentaires (`key-page-acceptation.html`, `key-remplacement-sport.html`, `key-vivier-vide.html`) sont apparues dans `mockups/` pendant cette revue, après son cadrage. Elles ne sont **pas** auditées ici. L'inventaire automatique montre qu'elles portent les mêmes défauts systémiques que les quatre en périmètre (aucun `<article>`, aucun titre, aucun `aria-atomic`, `outline:none` sur le champ, `text-transform:uppercase` sur des composants produit, plusieurs `<main>` par document) : les constats A7, B1, B2 et B6 s'y appliquent sans modification.

---

## Synthèse

| Gravité | Nombre |
|---|---|
| **CRITIQUE** | **0** |
| **ÉLEVÉ** | **7** |
| **MOYEN** | **9** |
| **FAIBLE** | **10** |
| **Total** | **26** |

**Critères WCAG 2.2 AA en échec avéré :**

| Critère | Constats |
|---|---|
| **1.3.1** Information et relations (A) | A1, A7, B6, C-8 |
| **1.4.10** Redistribution (AA) | B9 |
| **2.4.1** Contourner des blocs (A) | A7, B6 |
| **2.4.6** En-têtes et étiquettes (AA) | A7 |
| **2.4.7** Visibilité du focus (AA) | A6, B2, C-7 |
| **3.3.2** Étiquettes ou instructions (A) | A4, B7, C-9 |
| **4.1.2** Nom, rôle et valeur (A) | A1, B8, C-4, C-5 |
| **4.1.3** Messages d'état (AA) | A2, A3, B3, B4 |

**Critères à risque, non prouvés en échec** : 1.4.3 et 1.4.11 (constat A5 — l'apparence de l'état actif du bouton d'envoi n'est spécifiée nulle part, donc ni conforme ni non conforme : elle est **indéterminable**).

**Aucun défaut de contraste n'a été trouvé.** C'est le résultat le plus net de cette revue et il mérite d'être dit avant les constats : **34 valeurs de ratio déclarées ont été recalculées, 34 sont exactes**, y compris les trois paires ajoutées en v3 pour `level-choice`. Le système de couleur n'est pas le problème de ce produit.

---

## Axe 1 — Contraste (1.4.3, 1.4.11)

### 1.1 Recalcul intégral des valeurs déclarées

Les 34 valeurs chiffrées présentes dans `DESIGN.md` (16 lignes de la table *Cibles de contraste*, 10 lignes de la table *Compositions à surveiller*, 5 valeurs en prose, 3 valeurs de l'énumération de la ligne 407) ont été recalculées. **Résultat : 34 exactes, 0 écart.**

| Paire | Déclaré | Recalculé | Seuil | Verdict |
|---|---|---|---|---|
| `ink-primary` / `surface-base` | 15,93 | **15,927** | 4,5 | ✅ |
| `ink-primary` / `surface-raised` | 14,53 | **14,530** | 4,5 | ✅ |
| `ink-primary` / `surface-raised-hover` | 11,13 | **11,133** | 4,5 | ✅ |
| `ink-secondary` / `surface-base` | 7,30 | **7,302** | 4,5 | ✅ |
| `ink-secondary` / `surface-raised` | 6,66 | **6,662** | 4,5 | ✅ |
| `ink-secondary` / `surface-raised-hover` | 5,10 | **5,104** | 4,5 | ✅ |
| `ink-secondary` / `surface-overlay` | 5,93 | **5,929** | 4,5 | ✅ |
| `accent` / `surface-base` | 9,88 | **9,885** | 4,5 | ✅ |
| `ink-on-accent` / `accent` | 8,70 | **8,701** | 4,5 | ✅ |
| `status-pending` / `status-pending-quiet` | 6,28 | **6,284** | 4,5 | ✅ |
| `status-danger` / `status-danger-quiet` | 5,12 | **5,123** | 4,5 | ✅ |
| `accent` / `accent-quiet` | 6,61 | **6,611** | 4,5 | ✅ |
| `border-interactive` / `surface-base` | 4,79 | **4,787** | 3 | ✅ |
| `border-interactive` / `surface-raised` | 4,37 | **4,367** | 3 | ✅ |
| `border-strong` / `surface-raised-hover` | 4,93 | **4,927** | 3 | ✅ |
| `focus-ring` / `surface-base` | 11,23 | **11,230** | 3 | ✅ |
| `surface-raised` / `surface-base` | 1,10 | **1,096** | — | conforme au constat |
| `surface-overlay` / `surface-base` | 1,23 | **1,232** | — | idem |
| `surface-user` / `surface-base` | 1,33 | **1,333** | — | idem |
| `surface-raised-hover` / `surface-raised` | 1,31 | **1,305** | — | idem |
| `surface-raised-pressed` / `surface-raised` | 1,48 | **1,476** | — | idem |
| `accent-hover` / `accent` | 1,15 | **1,145** | — | idem |
| `accent-pressed` / `accent` | 1,39 | **1,389** | — | idem |
| `accent-quiet` / `surface-base` | 1,50 | **1,495** | — | idem |
| `status-pending-quiet` / `surface-base` | 1,38 | **1,382** | — | idem |
| `status-danger-quiet` / `surface-base` | 1,18 | **1,178** | — | idem |
| `ink-primary-soft` / `surface-base` (l. 309) | 13,81 | **13,806** | 4,5 | ✅ |
| `ink-secondary` / `surface-raised-pressed` (l. 351) | 4,513 | **4,513** | 4,5 | ✅ (marge 0,013) |
| `focus-ring` / `accent` (l. 353) | 1,14 | **1,136** | 3 | ❗ voir 1.2 |
| filet gauche de l'encadré (l. 349) | 6,04 | **6,037** | 3 | ✅ |
| `border-interactive` → `border-strong` (l. 442) | 1,47 | **1,473** | — | conforme au constat |
| `border-interactive` / `surface-overlay` (l. 407) | 3,89 | **3,887** | 3 | ✅ |
| `border-interactive` / `surface-user` (l. 407) | 3,59 | **3,590** | 3 | ✅ |
| `border-interactive` / `surface-raised-hover` (l. 407) | 3,35 | **3,346** | 3 | ✅ |

Le « 6,04:1 » de la ligne 349 méritait une vérification particulière : la table le présente comme le filet gauche de l'encadré de jouabilité, dont le fond intérieur est `status-danger-quiet`. Le calcul montre que **6,037 est le ratio contre `surface-base`**, pas contre le fond de l'encadré (qui vaut 5,123). Les deux dépassent 3:1, donc le constat tient dans les deux sens ; le chiffre est exact, seule son attribution est ambiguë. Ce n'est pas un défaut.

### 1.2 `focus-ring` sur `accent` — la dépendance contractuelle est réelle

`focus-ring` / `accent` = **1,136:1**. Le document le déclare (l. 353) et fonde sa conformité sur `outlineOffset: 2px`, qui interpose du fond parent. **Vérification :** cette conformité tient si et seulement si le fond parent atteint 3:1 contre `focus-ring`. Recalculé sur tous les fonds où un `button-primary` peut se trouver :

- `focus-ring` / `surface-base` = 11,23 ✅
- `focus-ring` / `surface-raised` = 10,25 ✅ (bouton dans un bloc)
- `focus-ring` / `surface-overlay` = 9,12 ✅
- `focus-ring` / `surface-raised-hover` = 7,85 ✅
- `focus-ring` / `surface-user` = 8,42 ✅

Le mécanisme tient partout. **Rien à signaler** — le document a identifié le risque et son garde-fou est effectivement suffisant.

### 1.3 Les trois paires ajoutées en v3 sont les bonnes, et elles suffisent

`level-choice` produit trois compositions nouvelles : le mot (`ink-primary`) et la ligne de fait (`ink-secondary`) sur `surface-raised` au repos, et les deux sur `surface-raised-hover` au survol. Les trois paires ajoutées (l. 320, 321, 324) couvrent exactement ce périmètre. La ligne de fait au survol tombe à **5,104:1** — au-dessus du seuil, et c'était bien le point à vérifier, puisque c'est le premier texte secondaire porteur de sens dans une cible qui se survole.

### 1.4 Le piège de contraste que crée le constat B5

Recalculé : **`border-interactive` / `surface-raised-pressed` = 2,958:1**, sous le seuil de 3:1. Cette composition **n'est produite par rien aujourd'hui**, parce que la carte de partenaire échange son filet contre `border-strong` (4,356) à l'appui. Elle deviendrait réelle à l'instant où quelqu'un ajouterait un état pressé à `button-quiet` — ce que recommande le constat B5 — en reprenant seulement le fond. La table *Compositions à surveiller* ne la liste pas, alors que c'est précisément une régression qu'une table de risque devrait pouvoir signaler.

> **C-1 · FAIBLE · hygiène de contrat.** Ajouter `border-interactive` / `surface-raised-pressed` (**2,96:1**) à la table *Compositions à surveiller*, avec la mention que la composition est aujourd'hui inatteignable et pourquoi. C'est la seule composition du système qui échoue son seuil, et elle n'est nulle part.

### 1.5 Trois compositions réelles absentes d'une table qui se déclare contractuelle

Toutes conformes, mais produites par le système et non listées :

- `focus-ring` / `surface-raised` = **10,25** — l'anneau de toute option de `level-choice`, de `sport-replace`, du bloc de connexion et du bloc d'agenda. C'est le décalage de 2 px qui expose ce fond, pas `surface-base`.
- `focus-ring` / `surface-raised-hover` = **7,85** — la même option survolée et focalisée.
- `border-strong` / `surface-raised` = **6,43** — le filet extérieur d'une option ou d'une carte au survol, du côté du bloc parent.

> **C-2 · FAIBLE · hygiène de contrat.** La v3 a amendé la table pour `level-choice` en y ajoutant trois paires de texte ; les trois paires de **contour et d'anneau** que le même composant produit sont restées dehors.

### 1.6 Une énumération qui ne correspond pas à l'usage réel

`DESIGN.md` l. 407 : « Il franchit 3:1 sur les cinq fonds où il est réellement posé : 4,79 / 4,37 / 3,89 / 3,59 / 3,35. » Les cinq valeurs sont exactes. Mais deux des cinq fonds ne portent jamais ce filet : `surface-user` (3,59) est la bulle de la personne, qui n'a aucun contour dans toute la spine ; `surface-raised-hover` (3,35) est l'état de survol, où le filet devient `border-strong` par règle explicite (l. 411, l. 433).

> **C-3 · FAIBLE · exactitude.** L'énumération est arithmétiquement juste et descriptivement fausse. Sans conséquence pour l'utilisateur, mais la phrase « où il est réellement posé » est le genre d'affirmation qu'un implémenteur lit comme une autorisation.

---

## Axe 2 — Nom, rôle, valeur (4.1.2)

**Inventaire complet des contrôles des quatre maquettes, avec les noms accessibles calculés par le navigateur.**

| Contrôle | Fichier · ligne | Élément | Rôle | Nom accessible calculé | Verdict |
|---|---|---|---|---|---|
| Champ de saisie | fil-a-froid 109-110, decl. 141-142/171-172/204-205, prop. 172-173/244-245, recap 160-161/197-198/231-232 | `<textarea>` + `<label class="sr-only">` | textbox | « Votre message » | ✅ |
| Bouton d'envoi | idem, +1 ligne | `<button disabled aria-label>` | button | « Envoyer » | ✅ |
| Option de niveau ×3 | decl. 123-134 | `<button type="button">` | button | « Débutant Je débute, ou je reprends après une longue coupure. » (etc.) | ✅ |
| Bloc de niveau | decl. 122 | `<div role="group" aria-label>` | group | « Votre niveau » | ✅ |
| Fiche au niveau inconnu | decl. 194 | `<div role="group" aria-label>` | group | « Votre fiche » | ✅ |
| Groupe de candidats | prop. 150, 193, 231 | `<div role="group" aria-label>` | group | « Trois intermédiaires, comme vous » | ✅ (voir C-4, C-5) |
| Carte de partenaire ×3 | prop. 153-164, 234-236 | `<button type="button">` | button | « Anna Mercredi, vendredi · dans 1 jour » | ⚠️ voir B8 |
| Carte inerte ×3 | prop. 196-210 | `<div>` sans rôle, sans `aria-label` | — (texte) | — | ✅ |
| Encadré de jouabilité | recap 129 | `<div role="group" aria-label>` | group | « Conditions de jeu — chaleur » | ✅ (voir C-4) |
| Récapitulatif ×3 | recap 139, 181, 217 | `<div role="group" aria-label>` | group | « Rencontre avec Anna » | ✅ |
| Région de statut | recap 191 | `<p role="status">` | status | (sans nom, correct) | ⚠️ voir A3 |

**Conclusion de l'axe : la règle « pas d'`aria-label` sur un `div` nu » est tenue partout.** C'était le défaut nommé comme corrigé en v3 par les trois encadrés identiques (`DESIGN.md` l. 397 et 454, `EXPERIENCE.md` l. 68 et 223) ; la correction est réelle et vérifiée. **Aucun `aria-label` orphelin n'a été trouvé dans les quatre fichiers.** La carte inerte est un `<div>` sans rôle **et sans `aria-label`** — c'est la bonne façon de la rendre inerte, et le verdict (« Retenue » / « Non retenue ») est du texte visible, pas un attribut.

**Le choix `<button>` plutôt que `radiogroup` pour `level-choice` est correct, et il a été vérifié.** Trois options mutuellement exclusives suggèrent un `role="radiogroup"` avec `aria-checked`. Ce serait ici une **erreur** : les boutons radio promettent une sélection réversible que l'on confirme ensuite, alors que l'activation d'une option envoie immédiatement le tour et n'a pas d'étape de confirmation. Un `radiogroup` annoncerait « non coché, 1 sur 3 » pour une décision qui, une fois prise, ne se reprend qu'en la redisant au bot (`EXPERIENCE.md` l. 298). Le `<button>` dit la vérité sur ce qui va se passer. **Rien à signaler, et c'était le point le plus susceptible d'être mal jugé sur ce composant.**

> **B8 · MOYEN · 4.1.2.** `EXPERIENCE.md` l. 354 : « Le séparateur `·` n'est jamais prononcé : il est remplacé par une virgule dans le nom. » Les maquettes posent le point médian **dans le contenu du bouton** (`key-proposition-partenaires.html` l. 155, 159, 163, 234-236) sans nom accessible de substitution. Le nom calculé est donc « Anna Mercredi, vendredi · dans 1 jour », point médian inclus, dont la restitution dépend du niveau de verbosité du lecteur d'écran. La règle est bonne ; la maquette ne l'implémente pas. *Correction : `aria-label="Anna, mercredi, vendredi, dans 1 jour"` — la containment de 2.5.3 reste satisfaite, tous les mots visibles y sont dans l'ordre.*

> **C-4 · FAIBLE · 4.1.2.** Trois groupes portent un `aria-label` qui **duplique mot pour mot un libellé visible situé à l'intérieur du groupe** : `candidate-group-label` (`key-proposition-partenaires.html` l. 150 vs 151), et l'en-tête de l'encadré de jouabilité (`key-recap-en-attente.html` l. 129 vs 130). Le lecteur d'écran annonce donc la phrase deux fois — une fois comme nom de groupe à l'entrée, une fois comme contenu. `aria-labelledby` pointant sur le `<p>` visible supprime le doublon et lie le nom au texte plutôt que d'en tenir une copie qui peut diverger (elle diverge déjà : le libellé visible porte un point final, l'attribut non).

> **C-5 · FAIBLE · 4.1.2.** Le nom du groupe reste « Trois intermédiaires, comme vous » après résolution du tour (`key-proposition-partenaires.html` l. 193), alors que les trois cartes ne sont plus des propositions mais un historique. Le nom devrait suivre le sort du groupe, comme les cartes suivent le leur.

---

## Axe 3 — Régions live (4.1.3)

C'est l'axe qui porte les constats les plus lourds de cette revue. Le raisonnement de la spine est **plus juste que ce qu'on lit habituellement** — l'encadré de la ligne 338 corrige explicitement une erreur antérieure sur `role="log"` et a raison de le faire — mais il s'arrête une étape trop tôt, et les maquettes n'en implémentent presque rien.

### 3.1 Ce que la spine dit, et qui est exact

`EXPERIENCE.md` l. 338 affirme : en ARIA 1.2, `role="log"` ne porte comme valeur implicite que `aria-live="polite"` ; `aria-relevant` garde son défaut global `additions text`. **C'est exact**, et c'est précisément le piège que l'énoncé du cadrage de cette revue signalait. La spine ne tombe pas dedans : elle écrit `aria-relevant="additions"` explicitement, et elle explique pourquoi. Ce point est **vérifié et non signalé**.

### 3.2 Mais le mécanisme échoue sur le cas exact pour lequel il a été inventé

> **A2 · ÉLEVÉ · 4.1.3.** `aria-relevant="additions"` supprime l'annonce des **mutations de texte**. Il ne supprime pas l'annonce des **ajouts de nœuds** — c'est littéralement ce que le mot signifie. Or `EXPERIENCE.md` l. 201 et `DESIGN.md` l. 435 imposent qu'au moment de la confirmation, le récapitulatif **gagne une ligne** : la date du changement de statut (« Confirmée le 28 août », visible en `key-recap-en-attente.html` l. 188). Cette ligne est un **nœud ajouté à l'intérieur de la région `role="log"`**, puisque le récapitulatif « persiste dans le fil ». Elle sera donc annoncée. Et comme la région `role="status"` annonce au même instant la phrase complète (l. 339), le produit obtient exactement le résultat que l'attribut existait pour empêcher : **une annonce nue et sans sujet — « Confirmée le 28 août » — en plus de la phrase complète.**
>
> Le raisonnement de la ligne 338 est bon, mais il n'a examiné qu'une des deux mutations que la confirmation produit. La pastille change de texte ; la date, elle, **apparaît**. On ne peut pas neutraliser la seconde avec `aria-relevant`.
>
> *Correction :* poser `aria-live="off"` sur le récapitulatif lui-même, ou le sortir du sous-arbre `role="log"`. Le récapitulatif est le seul élément du fil qui **mute** ; tout le reste ne fait que s'ajouter. Le traiter comme un contenu statique dont la région de statut est le porte-parole résout les deux mutations d'un coup, et rend `aria-relevant="additions"` inutile plutôt que subtilement insuffisant.

### 3.3 La région de statut est posée exactement comme la spine l'interdit

> **A3 · ÉLEVÉ · 4.1.3.** `key-recap-en-attente.html` l. 191 :
> ```html
> <p class="sr-only" role="status">Anna a confirmé la rencontre de mercredi 3 septembre à 19 h.</p>
> ```
> Cette région viole **deux** règles écrites de la spine qu'elle est censée illustrer :
> 1. `EXPERIENCE.md` l. 339 : la région de statut est « **distincte du fil** ». Ici elle est à l'intérieur du `.turn`, donc à l'intérieur de `.column` — c'est-à-dire à l'intérieur de ce qui doit porter `role="log"`. Une région live imbriquée dans une autre région live produit une double annonce ; c'est le même défaut que A2, par un autre chemin.
> 2. `EXPERIENCE.md` l. 341 : « Les régions live existent avant d'avoir quoi que ce soit à annoncer […] présentes et **vides dès le premier octet de HTML** ». La maquette insère la région **avec son contenu déjà dedans**. Une région live insérée avec son contenu n'est, dans la plupart des couples navigateur/lecteur d'écran, **pas annoncée du tout**.
>
> La maquette est statique, donc le second point est en partie un artefact de sa nature. Le premier ne l'est pas : c'est un choix de **placement dans l'arbre**, et il est faux. C'est aussi la seule région de statut posée dans les quatre maquettes — l'unique démonstration du mécanisme le montre à l'envers.

### 3.4 Une contrainte d'implémentation non écrite

> **B3 · MOYEN · 4.1.3.** Même en écartant la ligne de date (A2), la neutralisation de la pastille par `aria-relevant="additions"` ne tient que si la pastille est mutée **en place** (le nœud de texte est remplacé, l'élément survit). Si l'implémentation re-rend le bloc — ce que fait n'importe quel moteur de rendu qui remplace un sous-arbre, et ce que suggère le changement de classe `badge pending` → `badge confirmed` — le nouvel élément est une **addition**, et il est annoncé nu. La spine présente son mécanisme comme certain (« Les trois attributs sont **requis** ») alors qu'il repose sur une contrainte d'implémentation qu'elle n'énonce pas. *Correction : écrire la contrainte, ou appliquer la correction de A2 qui la rend sans objet.*

### 3.5 Ce que les maquettes ne font pas

> **B4 · MOYEN · 4.1.3.** La spine déclare trois attributs requis sur le fil : `role="log" aria-relevant="additions" aria-atomic="false"`. La seule maquette en périmètre qui porte le fil (`key-proposition-partenaires.html` l. 138) en pose **deux** : `aria-atomic` est absent. La valeur par défaut d'`aria-atomic` étant `false`, l'effet est nul — mais un attribut déclaré contractuel et omis dans l'unique référence visuelle est une invitation à l'omettre partout ailleurs.

**Trois fils sur quatre n'ont aucune région live du tout.** `key-fil-a-froid.html`, `key-declaration-niveau.html` et `key-recap-en-attente.html` ne portent aucun `role="log"` sur leur `.column`. Ce point est intégré au constat A7 ci-dessous, avec le reste de l'ossature manquante.

**La règle de la ligne 343 est la meilleure de la section, et aucune maquette ne l'implémente.** « Poser `role="status"` sur la liste elle-même est une faute double : le rôle écrase le rôle `list` et prive les `<li>` de leur dénombrement, et la pile entière est ré-annoncée à chaque ajout. » C'est rigoureusement exact et rarement écrit. Le nœud satellite qu'elle prescrit est absent de `key-proposition-partenaires.html` — voir A1, qui traite la conséquence la plus grave de cette absence.

---

## Axe 4 — Focus (2.4.7, 2.4.11)

> **Note normative.** Le cadrage citait 2.4.13 *Apparence du focus*. Ce critère est **AAA** en WCAG 2.2 ; 2.4.12 *Focus non masqué (amélioré)* l'est aussi. Le seul critère de focus de niveau AA ajouté par WCAG 2.2 est **2.4.11 *Focus non masqué (minimum)***. Les constats ci-dessous s'y tiennent, avec une note sur 2.4.13 là où c'est instructif.

### 4.1 L'anneau est bon partout où il est défini

`focus-indicator` : `outline` opaque de 3 px en `focus-ring`, décalage 2 px, identique sur tous les composants. Vérifié dans les maquettes : `.opt:focus-visible` (decl. l. 67), `.card:focus-visible` (prop. l. 92), `form:focus-within` (fil l. 77, decl. l. 89, prop. l. 111, recap l. 98). Contrastes recalculés : entre 6,94 et 11,23 selon le fond exposé par le décalage — **tous très au-dessus de 3:1** (voir 1.2). Les écarts de grille (`gap:12px` sur `.cards` et `.level-choice`) dépassent les 5 px que l'anneau et son décalage occupent : aucun chevauchement d'anneau entre deux cibles voisines. **Le refus de l'ombre portée comme indicateur de focus (`DESIGN.md` l. 401) est correct** : une ombre à opacité partielle ne peut pas garantir 3:1 contre un fond variable.

À titre indicatif sur **2.4.13 (AAA, non requis)** : un anneau de 3 px non contigu satisfait la surface minimale du critère, et le contraste de 11,23:1 dépasse largement les 3:1 requis contre les états adjacents. Le produit passerait ce critère AAA.

### 4.2 L'anneau du conteneur n'identifie pas quel contrôle a le focus

> **A6 · ÉLEVÉ · 2.4.7.** Les quatre maquettes portent l'anneau du champ sur le **conteneur** : `form:focus-within{outline:3px solid var(--focus-ring)}`. `EXPERIENCE.md` l. 361 autorise explicitement ce montage. Le problème est ailleurs : **le `<form>` contient deux contrôles**, le champ et le bouton d'envoi. `:focus-within` s'applique aux deux, à l'identique. Dès que le bouton d'envoi devient focusable — c'est-à-dire dès que le champ n'est plus vide, l'état normal au moment où l'on veut envoyer — **Tab déplace le focus du champ vers le bouton sans que l'anneau bouge d'un pixel**.
>
> Aucune des quatre maquettes ne définit `.send:focus-visible`. Aucune ne montre le bouton d'envoi actif : il est `disabled` dans les huit instances, donc hors ordre de tabulation, donc le défaut n'est jamais rendu visible par la maquette elle-même.
>
> 2.4.7 exige que l'interface utilisateur soit dotée d'un **mode de fonctionnement où l'indicateur de focus est visible**. Un indicateur qui ne se déplace pas entre deux contrôles adjacents n'indique pas où est le focus ; il indique seulement qu'il est quelque part dans le formulaire. *Correction : conserver `:focus-within` pour le champ (le montage est légitime), et donner au bouton d'envoi son propre `:focus-visible` — l'anneau se pose alors sur le bouton, à l'intérieur du conteneur, et les deux positions sont distinguables.*

### 4.3 L'état actif du bouton d'envoi n'est spécifié nulle part

> **A5 · ÉLEVÉ · 1.4.3 / 1.4.11 / 2.4.7 (indéterminable).** Le bouton d'envoi est le second contrôle le plus utilisé du produit. Recherche exhaustive dans les deux spines : **son état actif n'existe pas.**
> - `DESIGN.md` n'a **aucun composant** `send-button`. La seule mention (l. 442) décrit exclusivement l'état désactivé : « porte l'attribut `disabled` natif tant que le champ est vide, avec un filet `border-interactive` ».
> - `DESIGN.md` l. 305 spécifie `ink-disabled` — pour l'état désactivé.
> - `EXPERIENCE.md` l. 355 spécifie le nom accessible et l'usage de `disabled` — pour l'état désactivé.
> - Les quatre maquettes ne rendent que l'état désactivé (`.send{color:var(--ink-disabled);cursor:not-allowed}`), huit fois.
>
> Résultat : **ni la couleur du glyphe actif, ni son fond, ni son filet, ni son survol, ni son anneau de focus ne sont contractés.** Le contraste de l'icône `↑` à l'état actif n'est ni conforme ni non conforme : il est indéterminable. Un implémenteur qui lit ces documents littéralement produira un bouton actif visuellement identique au bouton désactivé, puisque c'est la seule apparence décrite.
>
> Le paradoxe est que `DESIGN.md` l. 442 argumente longuement sur la visibilité du bouton **désactivé** (« son fond désactivé est identique à celui du conteneur, il disparaîtrait sinon dans son état le plus fréquent ») sans jamais dire à quoi il ressemble quand il fonctionne. *Correction : ajouter une entrée `send-button` avec ses états actif, survolé, pressé et focalisé, et sa paire de contraste dans la table.*

### 4.4 `outline: none` est toujours là, et il est annoncé comme corrigé

> **B2 · MOYEN · 2.4.7.** `EXPERIENCE.md` l. 361 : « **Aucune règle `outline: none` n'existe dans ce produit, sur aucun élément, sous aucun prétexte de style.** » `DESIGN.md` l. 476 en fait un *Don't* explicite. Les trois encadrés identiques de correction v3 (`DESIGN.md` l. 397 et 454, `EXPERIENCE.md` l. 68 et 223) listent « `outline: none` sur la zone de saisie » parmi les défauts **corrigés**.
>
> La règle est présente **sept fois** dans les maquettes : `key-fil-a-froid.html` l. 78, `key-declaration-niveau.html` l. 90, `key-proposition-partenaires.html` l. 112, `key-recap-en-attente.html` l. 99 (et trois fois dans les maquettes hors périmètre).
>
> **L'effet net pour l'utilisateur est neutre** — l'anneau du conteneur est bien là, et la maquette le commente honnêtement (« l'anneau est sur le conteneur, pas retiré du système »). Ce n'est donc pas un échec de 2.4.7 sur le champ. C'est un défaut de **véracité du document** : trois encadrés affirment une correction qui n'a pas eu lieu au sens littéral de la règle, et la règle est formulée en absolu (« sur aucun élément ») alors que l'intention est relative (« aucun contrôle sans indicateur visible »). Un absolu que le produit enfreint lui-même n'est pas un garde-fou, c'est du bruit. *Correction : reformuler la règle en « aucun contrôle ne perd son indicateur visible ; `outline: none` n'est admis que lorsqu'un anneau conforme est porté par le conteneur, jamais autrement », et retirer cette ligne de la liste des corrections v3.*

### 4.5 Focus non masqué et focus qui devient inerte

`EXPERIENCE.md` l. 362 traite 2.4.11 correctement, y compris le détail que la pastille « nouveau message » entre dans le calcul de la zone exclue — précision rarement pensée. `EXPERIENCE.md` l. 364 et `DESIGN.md` l. 433 traitent le déplacement du focus quand une carte devient inerte, vers le message du tour porteur de `tabindex="-1"`. **Les deux règles sont bonnes et ne sont pas signalées.**

> **C-6 · FAIBLE.** Ni l'une ni l'autre n'est démontrée. Dans les quatre maquettes, la zone de saisie est un **frère statique** (`.composer-wrap{flex:none}`), jamais ancrée ni collante : le cas de recouvrement que 2.4.11 vise n'est jamais rendu. Et le `tabindex="-1"` annoncé par la note de `key-proposition-partenaires.html` l. 220 **n'existe dans le balisage d'aucun fichier** — l'inventaire n'en trouve zéro occurrence. Les deux mécanismes les plus délicats du produit sont décrits en prose et jamais montrés.

> **C-7 · FAIBLE.** `.opt` et `.card` ne définissent que `:focus-visible`, sans repli `:focus`. Sans conséquence sur les navigateurs cibles, mais l'anneau disparaît entièrement là où `:focus-visible` n'est pas supporté — c'est-à-dire précisément là où l'on ne peut plus le vérifier.

---

## Axe 5 — Cibles (2.5.8)

**Mesures réelles au navigateur, viewport 1265 px et 320 px :**

| Cible | Taille rendue | Plancher AA (24 px) | Objectif produit (48 px) |
|---|---|---|---|
| Option de niveau | 687 × 72 px (desktop), plus haute à 320 px | ✅ | ✅ |
| Carte de partenaire | pleine largeur × ≥ 48 px | ✅ | ✅ |
| Bouton d'envoi | 48 × 48 px | ✅ | ✅ |

**Aucun défaut de cible.** Les écarts inter-cibles (12 px de `gap`) excluent tout chevauchement au sens de l'exception d'espacement de 2.5.8.

**Le traitement de « Pourquoi ? » est correct, et il est correct pour la bonne raison.** `EXPERIENCE.md` l. 366 et `DESIGN.md` l. 436 posent : 24 × 24 px est le plancher normatif de 2.5.8, 48 px est un choix produit, et les cibles en ligne dans du texte en sont exemptées. C'est **exactement** la lecture juste du critère, y compris la correction explicite d'une version antérieure qui « inventait » une distinction par type de pointeur que la norme ne fait pas. À noter, sans que ce soit un défaut : si « Pourquoi ? » se rend en pratique comme un troisième bouton posé **sous** les deux boutons de fournisseur plutôt que dans une phrase, l'exception *inline* ne s'applique plus et le plancher de 24 px redevient obligatoire — ce que le composant respecte de toute façon. La conclusion tient dans les deux lectures.

---

## Axe 6 — Structure (1.3.1, 2.4.1, 2.4.6)

### 6.1 L'attribution de locuteur est bonne

Le geste signature (le bot n'a ni bulle, ni avatar, ni horodatage) est doublé partout d'une étiquette masquée : `<span class="sr-only">Ex Aequo : </span>` / `<span class="sr-only">Vous : </span>`. Vérifié sur les 14 messages des quatre maquettes, sans exception. `.sr-only` utilise le motif de masquage correct (`clip`, 1 px, `white-space:nowrap`), qui ne retire pas le nœud de l'arbre d'accessibilité. **Rien à signaler** — et c'est la règle sur laquelle repose la lisibilité de tout le produit au lecteur d'écran.

### 6.2 L'ossature promise n'existe dans aucune maquette

> **A7 · ÉLEVÉ · 1.3.1 / 2.4.1 / 2.4.6.** Inventaire automatique des quatre fichiers en périmètre :
>
> | Élément prescrit | Où c'est écrit | fil-a-froid | decl.-niveau | prop.-partenaires | recap-attente |
> |---|---|---|---|---|---|
> | `<article>` par tour de parole | EXP. l. 340, 342 | **0** | **0** | **0** | **0** |
> | `<h1>` masqué permanent | EXP. l. 352 | 2 visibles¹ | **0** | **0** | **0** |
> | `<h2>` masqué par tour | EXP. l. 352 | **0** | **0** | **0** | **0** |
> | `role="log"` sur le fil | EXP. l. 338, 351 | **0** | **0** | 1 | **0** |
> | Nœud satellite `role="status"` des étapes | EXP. l. 343 | s.o. | s.o. | **0** | s.o. |
>
> ¹ *les deux `<h1>` de `key-fil-a-froid.html` sont l'accroche `display`, que la spine dit disparaître au premier message — ce n'est pas le titre permanent qu'elle prescrit, et ils sont deux dans un même document.*
>
> Le raisonnement de la spine (l. 352) est excellent : « sans autre titre, la navigation par titres — le premier réflexe en mode lecture — ne renvoie rien sur une conversation de trente tours ». Le produit est un fil unique et infini ; **la navigation par titres et par régions y est le seul moyen de se déplacer autrement qu'en lisant tout**. Zéro titre sur trois des quatre maquettes, et un seul `role="log"` sur quatre, signifie que la référence visuelle que l'implémenteur copiera ne contient aucun des mécanismes qui rendent ce produit navigable.
>
> *Ce constat est une divergence maquette / spine, pas un défaut de conception : la spine a raison sur tous les points. Il est classé ÉLEVÉ parce que les maquettes sont ce qu'on copie.*

> **B6 · MOYEN · 1.3.1 / 2.4.1.** `EXPERIENCE.md` l. 351 : « **un seul `main` par page** ». `key-declaration-niveau.html`, `key-proposition-partenaires.html` et `key-recap-en-attente.html` en portent **trois chacun** (l. 115/159/187, l. 137/190/227, l. 124/178/213). HTML n'autorise qu'un seul `main` non masqué par document, et les lecteurs d'écran exposent tous les repères trouvés : la navigation par régions devient ambiguë. C'est un artefact du format « plusieurs cadres de démonstration dans un fichier », mais il est réparable (`<div>` pour les cadres secondaires, ou `aria-hidden` sur les répétitions).

> **C-8 · FAIBLE · 1.3.1.** Les intitulés de section des maquettes (`<p class="tag">`) sont visuellement des titres — capitales, interlettrage, position — et sémantiquement des paragraphes. Sur des documents de spécification qui seront lus, la structure du document lui-même mérite les mêmes égards que celle du produit qu'il décrit.

> **C-9 · FAIBLE · 3.3.2.** Le texte d'exemple sous le champ (`key-fil-a-froid.html` l. 113 et 135, `<p class="hint">`) n'est associé au `<textarea>` ni par `aria-describedby` ni autrement. Il porte pourtant la seule instruction du produit sur la manière de lui parler.

---

## Axe 7 — Mouvement (2.2.2, 2.3.1) et `prefers-reduced-motion`

### 7.1 Le décompte de la pulsation est juste

`key-proposition-partenaires.html` l. 77 : `animation:pulse 1.4s ease-in-out 3` — **4,2 secondes au total**, sous le seuil de 5 secondes de 2.2.2. `EXPERIENCE.md` l. 375 chiffre la règle et explique pourquoi (« "quelques secondes" pouvait vouloir dire dix, et échouer le critère dans l'intervalle »). Vérifié : **conforme**, et le raisonnement est exact.

**2.3.1** : la période est de 1,4 s, soit 0,71 Hz, très loin du seuil de trois flashs par seconde. La transformation est un changement d'échelle sur un disque de 6 px, pas un flash de luminance. **Conforme.**

`@media (prefers-reduced-motion:reduce){.steps li.now::before{animation:none}}` est présent (l. 79). Le fondu d'arrivée des messages n'est pas rendu par les maquettes, donc ni conforme ni non conforme.

### 7.2 Mais l'information portée par l'animation n'a aucun équivalent

> **A1 · ÉLEVÉ · 1.3.1 / 4.1.2.** `EXPERIENCE.md` l. 373 pose une règle remarquable : « L'état courant d'une étape est exposé programmatiquement, pas seulement animé. Le marqueur textuel "en cours" n'est pas un repli réservé à `prefers-reduced-motion` : il existe **toujours**, masqué visuellement quand la pulsation joue. Sinon l'utilisateur de lecteur d'écran perd l'information sauf s'il a activé la préférence — un repli d'accessibilité plus riche que le chemin nominal est un défaut, pas une faveur. »
>
> `key-proposition-partenaires.html` l. 147 :
> ```html
> <li class="now">Je classe par délai d'attente.</li>
> ```
> **Il n'y a aucun marqueur textuel.** La chaîne « en cours » n'apparaît dans le fichier que dans un commentaire CSS (l. 76) et dans l'en-tête de documentation. La seule différence entre l'étape en cours et les étapes franchies est la classe `.now`, dont le seul effet est l'animation.
>
> Conséquences en cascade :
> 1. **Au lecteur d'écran**, les trois lignes sont identiques : aucune n'est signalée comme en cours. L'état n'est pas déterminable par programme (4.1.2), et la relation « celle-ci est en cours, celles-là sont franchies » n'est pas exposée (1.3.1).
> 2. **Sous `prefers-reduced-motion`**, la règle de la ligne 79 met `animation:none` — et comme il n'y a rien d'autre, **l'étape en cours n'est plus distinguable pour personne**, y compris à l'œil. La préférence de réduction de mouvement supprime purement et simplement une information, ce qui est le défaut exact que la ligne 373 nomme et interdit.
> 3. Le nœud satellite `role="status" aria-atomic="true"` prescrit par la ligne 343 est également absent, donc rien n'annonce la progression non plus.
>
> La spine a écrit la bonne règle, avec le bon argument, et la maquette de référence la contredit sur les trois plans à la fois. *Correction : `<li class="now"><span class="sr-only">En cours — </span>Je classe par délai d'attente.</li>`, et rendre ce `sr-only` visible sous `prefers-reduced-motion`.*

### 7.3 Capitales forcées sur un composant produit

> **B1 · MOYEN · cohérence de spine (1.4.12 marginal).** `DESIGN.md` l. 373 : « **Pas de capitales forcées**, pas de police d'affichage, pas de taille au-dessus de `display`. » Le jeton `label` (frontmatter) ne porte aucun `textTransform`.
>
> `key-recap-en-attente.html` l. 71 :
> ```css
> .playability .head{font-size:.8125rem;font-weight:500;letter-spacing:.02em;text-transform:uppercase;margin-bottom:8px}
> ```
> Le mot en tête de l'encadré de jouabilité — « CONDITIONS DE JEU — CHALEUR » — est en capitales forcées. C'est un **composant produit**, pas du décor de maquette (les `.tag` des maquettes, eux, sont explicitement hors produit).
>
> C'est le composant qui porte la seule information de **santé** du produit. Les capitales dégradent la reconnaissance de la forme des mots, ce qui pénalise la lecture en basse vision et en dyslexie, et certaines restitutions braille et vocales les traitent comme des sigles. Ce n'est pas un échec AA en soi — 1.4.8 est AAA — mais c'est une violation directe d'une règle que le document pose lui-même, sur le composant où elle compte le plus.

---

## Axe 8 — Zoom et redistribution (1.4.10, 1.4.12)

### 8.1 Vérification instrumentée — les maquettes tiennent mieux que ce qu'elles promettent

`key-recap-en-attente.html` chargé à **320 × 800 px** :
- `document.documentElement.clientWidth` = 320, `scrollWidth` = **320** — aucun débordement horizontal.
- Balayage des 300+ éléments du document : **aucun** élément dont le bord droit dépasse la fenêtre.

Puis, feuille de style de **1.4.12** appliquée par-dessus (`line-height:1.5`, `letter-spacing:0.12em`, `word-spacing:0.16em`, `margin-bottom:2em` sur les blocs de texte) :
- `scrollWidth` = `clientWidth` = 305 — **toujours aucun débordement**.
- Aucun conteneur ne tronque son contenu, hormis les `.sr-only` (masquage voulu) et le `<textarea>`, qui défile — comportement natif attendu, sans perte de contenu.

**Conclusion : 1.4.12 est satisfait, et 1.4.10 l'est en pratique à 320 px.** La règle « aucun conteneur de texte n'a de hauteur fixe » (`DESIGN.md` l. 375) est tenue dans le balisage : les seules contraintes sont des `min-height`, jamais des `height`.

### 8.2 Le plancher déclaré contredit le critère

> **B9 · MOYEN · 1.4.10.** `EXPERIENCE.md` l. 393 : « **Plancher : 360 px de large. En deçà, le produit n'est pas garanti.** » Repris par `DESIGN.md` l. 389.
>
> 1.4.10 exige l'absence de défilement bidirectionnel à une largeur équivalente à **320 pixels CSS** — c'est la définition même du critère, et c'est ce que produit un zoom à 400 % sur une fenêtre de 1280 px, précisément le cas que `EXPERIENCE.md` l. 409 promet de tenir. **Les deux affirmations sont incompatibles :** on ne peut pas garantir 400 % de zoom sur un écran de PC et refuser de garantir 320 px.
>
> L'ironie est que **les maquettes tiennent 320 px sans le moindre débordement** (mesuré ci-dessus). Le plancher de 360 px n'est pas une limite technique constatée, c'est une phrase héritée du plancher de largeur d'appareil du PRD, appliquée par erreur à la conformité de redistribution. *Correction : « Plancher de conformité : 320 px CSS, conformément à 1.4.10. Plancher d'appareil visé : 360 px. » Les deux chiffres ont chacun leur objet, et ils ne parlent pas de la même chose.*

### 8.3 Le raisonnement sur le point de rupture en `em` est juste

`EXPERIENCE.md` l. 391 explique pourquoi 720 px était faux et pourquoi la requête média s'écrit en `em`. C'est exact : une requête média en `em` se résout contre la taille de police **par défaut du navigateur**, donc elle suit le réglage de taille de texte de l'utilisateur, ce qu'une valeur en pixels ne fait pas. Le point de rupture inclut les gouttières, ce qui ferme effectivement la plage de compression. **Vérifié, rien à signaler.**

> **C-10 · FAIBLE.** `max-height:8.5rem` et `field-sizing:content` — les deux propriétés qui produisent le comportement « grandit jusqu'à quatre lignes puis défile » de `DESIGN.md` l. 442 — n'existent que dans `key-fil-a-froid.html` (l. 74). Les trois autres maquettes posent un `<textarea>` sans plafond de croissance.

---

## Axe 9 — Le refus du niveau : barrière d'accessibilité ou non ?

C'est la question la plus intéressante du dossier, et elle mérite d'être instruite dans les deux sens avant de conclure.

### 9.1 Le dispositif, exactement

`level-choice` propose trois issues sous forme de boutons : *Débutant*, *Intermédiaire*, *Avancé*. Une quatrième issue existe — refuser de déclarer son niveau, autorisée par FR-2 — et elle n'est atteignable qu'**en l'écrivant dans le champ**. `DESIGN.md` l. 438 : « **Aucun `button-primary`, aucun préréglé, aucun quatrième bouton** — le refus autorisé par FR-2 s'écrit et ne se clique pas. » `EXPERIENCE.md` l. 234 : « **Aucun bouton ne mène ici** : le refus s'écrit, il ne se clique pas. »

### 9.2 Ce qui plaide pour la barrière

1. **L'asymétrie de coût est réelle et elle est maximale pour les utilisateurs les plus contraints.** Activer un bouton coûte deux frappes (Tab, Entrée) ou un clic. Composer « je préfère ne pas le dire » coûte vingt-six caractères. Pour un utilisateur de contacteur unique en balayage, ou de commande oculaire, l'écart n'est pas de deux à vingt-six : il est d'environ trois secondes contre une à deux minutes. Pour un utilisateur dysgraphique, aphasique, ou en fatigue cognitive, le coût n'est pas en temps mais en effort de formulation — et c'est exactement la population que la formulation libre pénalise.
2. **La découvrabilité est nulle, et c'est le point qui mord.** Rien dans l'interface ne dit que refuser est possible. La prose au-dessus du bloc (`EXPERIENCE.md` l. 114-115) énonce le motif de la demande, jamais la possibilité de la décliner. Le bloc porte `aria-label="Votre niveau"` et trois boutons. Un utilisateur qui ne sait pas qu'une porte existe ne peut pas la franchir, quel que soit son coût.
3. **La spine s'interdit ce motif ailleurs, explicitement.** `EXPERIENCE.md` l. 302 bannit « le raccourci clavier sans équivalent visible ». La ligne 363 va plus loin : le chemin `Maj+Tab` vers les cartes doit être « **énoncé par le produit** […] un chemin clavier sans équivalent visible est interdit ailleurs dans cette spine, il ne peut pas s'en exempter ici ». Le refus du niveau est le cas symétrique : une action disponible, sans affordance visible et sans énoncé. La règle existe, elle est bien formulée, et elle n'a pas été appliquée à ce cas.
4. **Le succès dépend d'une classification par modèle.** « je préfère ne pas le dire » fonctionne (`key-declaration-niveau.html` l. 190). « bof », « passe », « je sais pas », « laisse tomber » tomberont probablement dans l'état *Niveau non interprétable* (`EXPERIENCE.md` l. 232), qui **réaffiche le bloc**. Un chemin dont le succès dépend d'une classification non spécifiée n'est pas un chemin fiable.

### 9.3 Ce qui plaide contre

1. **Aucun critère WCAG 2.2 n'exige la parité d'affordance.** Il n'existe pas de critère « toute issue possible doit être exposée comme un contrôle ». 2.1.1 *Clavier* est satisfait : le champ est focalisé au chargement et à chaque envoi, et il est opérable au clavier. Le refus est **atteignable**, ce que le critère demande.
2. **La réciproque est, elle, garantie — et c'est une décision de conception forte.** `EXPERIENCE.md` l. 292 : « Toute carte cliquable a un équivalent en langage naturel. […] **Aucun choix n'existe uniquement en bouton.** » Le produit garantit bouton → frappe. Il ne garantit pas frappe → bouton, et il n'a pas à le faire pour toute phrase concevable : c'est un agent conversationnel, l'espace des énoncés y est ouvert par construction.
3. **Le refus mène à un cul-de-sac, et le produit a raison de ne pas le mettre au même rang.** Un profil de niveau inconnu est « inerte des deux côtés — ni trouvable, ni capable de chercher » (`EXPERIENCE.md` l. 154, l. 315). Un quatrième bouton de même poids visuel que les trois autres présenterait comme équivalentes trois issues qui marchent et une qui ne mène nulle part. L'argument est écrit et il est bon.
4. **Aucune conséquence n'est irréversible.** 3.3.4 et 3.3.6 (*Prévention des erreurs*) ne sont pas engagés : rien n'est juridique, financier ni destructeur. Le bot dit « Vous pourrez me le dire plus tard, à tout moment » (l. 118), et il ne redemande pas. La porte reste ouverte indéfiniment.
5. **Le refus n'est pas une tâche que l'utilisateur cherche à accomplir.** Personne n'ouvre Ex Aequo pour refuser de déclarer son niveau. C'est une échappatoire, pas un but. Le rendre coûteux et le rendre inaccessible ne sont pas la même chose.

### 9.4 Conclusion

**Le refus par saisie libre n'est pas, en soi, un échec de WCAG 2.2 AA.** L'action est opérable au clavier, elle n'est pas requise pour accomplir la tâche du produit, elle est réversible, et aucun critère n'impose qu'une issue soit exposée comme un contrôle. **L'absence de quatrième bouton est défendable et je la maintiens** : l'argument de la ligne 438 est juste, et un quatrième bouton dégraderait la décision pour tout le monde.

**Mais le dispositif échoue sur un point précis, et il y échoue en tant que critère.** Ce n'est pas *comment* on refuse, c'est que **personne n'est jamais informé qu'on peut refuser**. FR-2 accorde un droit ; l'interface ne le mentionne nulle part. Il n'y a ni étiquette, ni instruction, ni énoncé du bot qui le rende connaissable.

> **A4 · ÉLEVÉ · 3.3.2 (Étiquettes ou instructions, A).** Le bloc `level-choice` sollicite une saisie de l'utilisateur et n'énonce pas l'une de ses issues autorisées. Aucune des formulations contractuelles de `EXPERIENCE.md` l. 114-116 ne mentionne la possibilité de décliner ; la seule phrase qui en parle (l. 118) n'apparaît qu'**après** que la personne a deviné toute seule qu'elle pouvait le faire. Le produit s'impose ailleurs (l. 363) d'énoncer ses chemins non visibles ; il ne l'a pas fait pour celui-ci.
>
> *Correction, à coût nul pour la conception et qui n'ajoute aucun bouton :* une clause dans la prose au-dessus du bloc, dans la voix du produit et sans la mettre au même rang que les trois issues —
>
> > « Tennis, le mardi. Il me manque votre niveau — c'est ce qui permettra de vous trouver quelqu'un d'équivalent. **Si vous préférez ne pas le dire, dites-le-moi.** »
>
> Cette phrase fait trois choses d'un coup : elle rend le droit connaissable, elle donne la formulation exacte que le classifieur reconnaîtra (fermant le point 9.2.4), et elle réduit le coût de frappe à quelques mots dictables ou copiables. Elle laisse intacte la décision de n'avoir aucun quatrième bouton, et elle applique au refus la règle que la spine applique déjà à `Maj+Tab`.

---

## Ce qui a été vérifié et délibérément non signalé

Cette section existe parce qu'une revue qui ne dit pas ce qu'elle a écarté ne se laisse pas vérifier.

- **`role="log"` et `aria-relevant`.** L'affirmation de `EXPERIENCE.md` l. 338 — le rôle n'implique que `aria-live="polite"`, `aria-relevant` conserve son défaut `additions text` — est **exacte**. La spine corrige elle-même une erreur antérieure sur ce point. Le constat A2 porte sur une conséquence non examinée, pas sur cette affirmation.
- **`aria-label` sur `role=generic`.** La règle (l. 340) est juste, et elle est **appliquée sans exception** dans les quatre maquettes. Le défaut nommé comme corrigé en v3 l'est réellement.
- **Le gris « sourd » supprimé** (`DESIGN.md` l. 303). Le raisonnement — un jeton qui ne peut être ni lisible ni distinct doit être supprimé, et le porteur du sens changé — est correct, et il est appliqué deux fois (`ink-muted`, puis `border-decorative`). Le doublon lexical (« je ne sais pas encore » plutôt que « Lieu non déterminé ») est la bonne réponse.
- **`ink-disabled` à 2,63:1 sur `surface-overlay`.** Exempté par 1.4.3 (composant inactif), et le document le nomme comme tel (l. 305). L'usage d'un `disabled` natif plutôt que d'`aria-disabled` (l. 355) est le bon choix pour se qualifier à l'exemption.
- **L'échec rendu sans couleur** (`DESIGN.md` l. 307). Encre primaire, filet réel, mot écrit : conforme à 1.4.1 et supérieur à ce qu'exige le critère.
- **Le mot visible sur les cartes inertes.** Signal qui survit au contraste forcé, à la basse vision et à l'absence de pointeur — le raisonnement est exact et l'implémentation est correcte (`key-proposition-partenaires.html` l. 199-209).
- **La pastille de statut sans teinte pour *déclinée* et *expirée*.** Cohérent avec 1.4.1 : le mot porte, la couleur accompagne.
- **`prefers-contrast: less`** avec `ink-primary-soft` à **13,806:1** — recalculé, très au-delà d'AA, et l'argument (un thème sombre à contraste maximal produit un halo en astigmatie) est réel.
- **Le décompte de 4,2 secondes de la pulsation**, sous les 5 secondes de 2.2.2. Chiffré parce que « quelques secondes » ne l'était pas : bonne décision.
- **Le choix `<button>` plutôt que `radiogroup`** pour `level-choice` — analysé en détail à l'axe 2, et **correct**.
- **Le traitement de 2.5.8**, y compris la correction explicite d'une lecture antérieure fausse du critère.
- **L'absence de raccourci à touche unique** (`EXPERIENCE.md` l. 295), avec l'analyse du garde-fou inversé (`activeElement === body` est l'état du mode lecture) — c'est un raisonnement d'expert, rarement vu écrit, et il est juste.
- **WCAG 3.3.7 (*Saisie redondante*)** est traité correctement à la ligne 384 : la relisibilité du fil ne satisfait pas le critère, l'information déjà donnée doit être **proposée**. Exact.

---

## Constats consolidés

| # | Gravité | Critère | Constat | Localisation |
|---|---|---|---|---|
| **A1** | ÉLEVÉ | 1.3.1, 4.1.2 | L'étape en cours n'a aucun marqueur textuel : distinguée par la seule animation, et par rien du tout sous `prefers-reduced-motion` | prop.-partenaires l. 77-79, 147 ; contre EXP. l. 343, 373 |
| **A2** | ÉLEVÉ | 4.1.3 | `aria-relevant="additions"` ne neutralise pas la ligne datée **ajoutée** au récapitulatif : la double annonce qu'il devait supprimer se produit quand même | EXP. l. 201, 338 ; DESIGN l. 435 ; recap-attente l. 188 |
| **A3** | ÉLEVÉ | 4.1.3 | La région `role="status"` est posée **dans** le fil et **avec** son contenu, contre les deux règles qui la gouvernent | recap-attente l. 191 ; contre EXP. l. 339, 341 |
| **A4** | ÉLEVÉ | 3.3.2 | Le refus du niveau n'est énoncé nulle part : droit accordé par FR-2, jamais rendu connaissable | EXP. l. 114-118, 234 ; DESIGN l. 438 |
| **A5** | ÉLEVÉ | 1.4.3, 1.4.11, 2.4.7 (indéterminable) | L'apparence du bouton d'envoi **actif** n'existe dans aucun jeton, aucun composant, aucune maquette | DESIGN l. 305, 442 ; EXP. l. 355 ; 8 instances `disabled` |
| **A6** | ÉLEVÉ | 2.4.7 | `form:focus-within` ne distingue pas le champ du bouton d'envoi ; aucun `.send:focus-visible` nulle part | fil l. 77, decl. l. 89, prop. l. 111, recap l. 98 |
| **A7** | ÉLEVÉ | 1.3.1, 2.4.1, 2.4.6 | Aucun `<article>`, aucun titre masqué, `role="log"` sur 1 fil sur 4 : l'ossature de navigation promise n'existe dans aucune maquette | les 4 fichiers ; contre EXP. l. 340, 342, 351, 352 |
| **B1** | MOYEN | cohérence (1.4.12 marg.) | `text-transform:uppercase` sur l'en-tête de l'encadré de jouabilité, contre « pas de capitales forcées » | recap-attente l. 71 ; contre DESIGN l. 373 |
| **B2** | MOYEN | 2.4.7 | `outline:none` présent 7× alors que la règle est absolue et que 3 encadrés l'annoncent corrigé en v3 | fil l. 78, decl. l. 90, prop. l. 112, recap l. 99 |
| **B3** | MOYEN | 4.1.3 | La neutralisation de la pastille repose sur une contrainte d'implémentation non écrite (muter le texte, jamais l'élément) | EXP. l. 338 |
| **B4** | MOYEN | 4.1.3 | `aria-atomic="false"`, déclaré requis, absent de la seule maquette portant `role="log"` | prop.-partenaires l. 138 ; contre EXP. l. 338 |
| **B5** | MOYEN | parité mobile (hors critère) | `button-quiet` n'a **aucun état pressé** : niveau, remplacement de sport, connexion, agenda et page d'acceptation n'ont aucun retour tactile, alors que DESIGN l. 433 en fait un impératif pour la carte | DESIGN frontmatter `button-quiet`, `level-choice` |
| **B6** | MOYEN | 1.3.1, 2.4.1 | Trois `<main>` par document dans 3 maquettes sur 4, contre « un seul `main` par page » | decl., prop., recap ; contre EXP. l. 351 |
| **B7** | MOYEN | 3.3.2 | Le chemin `Maj+Tab`, que la spine impose d'énoncer « une fois à froid », n'apparaît nulle part dans la maquette du fil à froid | fil-a-froid l. 113, 135 ; contre EXP. l. 363 |
| **B8** | MOYEN | 4.1.2 | Le séparateur `·` n'est pas remplacé par une virgule dans les noms accessibles des cartes | prop.-partenaires l. 155, 159, 163, 234-236 ; contre EXP. l. 354 |
| **B9** | MOYEN | 1.4.10 | Plancher de conformité déclaré à 360 px contre les 320 px du critère, alors que les maquettes tiennent 320 px (mesuré) | EXP. l. 393, 409 ; DESIGN l. 389 |
| **C-1** | FAIBLE | hygiène 1.4.11 | `border-interactive` / `surface-raised-pressed` = **2,96:1**, seule composition du système sous son seuil, absente de la table de risque | DESIGN l. 338-349 |
| **C-2** | FAIBLE | hygiène 1.4.11 | Trois compositions d'anneau et de contour produites par `level-choice` absentes de la table amendée pour lui | DESIGN l. 317-334 |
| **C-3** | FAIBLE | exactitude | « les cinq fonds où il est réellement posé » en énumère deux où le filet n'est jamais posé | DESIGN l. 407 |
| **C-4** | FAIBLE | 4.1.2 | `aria-label` dupliquant un libellé visible interne, au lieu d'`aria-labelledby` (et déjà divergent d'un point final) | prop. l. 150/151 ; recap l. 129/130 |
| **C-5** | FAIBLE | 4.1.2 | Le nom du groupe de candidats reste au présent après résolution du tour | prop.-partenaires l. 193 |
| **C-6** | FAIBLE | 2.4.11 | Ni le recouvrement par la saisie ancrée, ni le `tabindex="-1"` de repli du focus ne sont démontrés — zéro occurrence de `tabindex` dans les 4 fichiers | les 4 fichiers ; prop. l. 220 (prose seule) |
| **C-7** | FAIBLE | 2.4.7 | `:focus-visible` sans repli `:focus` sur `.opt` et `.card` | decl. l. 67 ; prop. l. 92 |
| **C-8** | FAIBLE | 1.3.1 | Les intitulés de section des maquettes sont des `<p>` stylés en titres | les 4 fichiers |
| **C-9** | FAIBLE | 3.3.2 | Le texte d'exemple sous le champ n'est pas associé au `<textarea>` | fil-a-froid l. 113, 135 |
| **C-10** | FAIBLE | — | `max-height` / `field-sizing` du champ (« quatre lignes puis défile ») présents dans une seule maquette sur quatre | fil-a-froid l. 74 |

*Note : `sport-replace`, composant nouveau en v3 portant l'unique zone en lecture seule du système, n'a aucune référence visuelle parmi les quatre maquettes en périmètre. Une maquette dédiée est apparue hors cadrage pendant cette revue et n'a pas été auditée.*

---

## Recommandation d'ordre de traitement

1. **A2 et A3** — les deux défauts de région live, à traiter ensemble : sortir le récapitulatif du sous-arbre live (ou lui poser `aria-live="off"`) et poser la région de statut vide, à la racine, hors du fil. Cela résout aussi **B3** et rend `aria-relevant` accessoire plutôt que critique.
2. **A1** — deux mots dans un `sr-only`, et la règle la mieux écrite de la section *Perception et préférences* cesse d'être contredite par sa propre référence visuelle.
3. **A4** — une clause dans la prose contractuelle au-dessus du bloc de niveau. Aucun bouton ajouté, la décision de conception est préservée.
4. **A5** — écrire l'état actif du bouton d'envoi, avec sa paire de contraste. **A6** en découle directement.
5. **A7, B6** — l'ossature structurelle dans les maquettes : `<article>`, titres masqués, `role="log"` sur les quatre fils, un seul `main`.
6. Le reste par gravité décroissante. **B9** et **B2** sont des corrections de texte dans les spines, pas de code.
