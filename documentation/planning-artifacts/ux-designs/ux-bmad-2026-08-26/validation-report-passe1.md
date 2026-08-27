# Rapport de validation — Ex Aequo

- **DESIGN.md :** `documentation/planning-artifacts/ux-designs/ux-bmad-2026-08-26/DESIGN.md`
- **EXPERIENCE.md :** `documentation/planning-artifacts/ux-designs/ux-bmad-2026-08-26/EXPERIENCE.md`
- **Exécuté le :** 2026-08-26
- **Lentilles :** parcours du rubric · accessibilité (WCAG 2.2 AA)

## Verdict global

Le couple de spines était **exploitable en aval mais pas extractible sans arbitrage**. La mécanique de base était saine — quatre sources résolvent, dix références `{jeton}` résolvent, aucune couleur sans hex, glossaire du PRD §3 tenu littéralement sans un seul synonyme, et l'état dominant « aucun candidat » réellement traité en chemin nominal. Les manques étaient concentrés en trois foyers : des composants du chemin critique n'existant que d'un côté du couple, trois familles d'états d'échec absentes, et le jeton phare du pivot desktop inopérant à la mesure.

La lentille accessibilité a été plus sévère, et son constat central est le plus utile de toute la session : **la spine se contredisait sur son propre jeton moral**. `ink-muted` — la couleur qui portait « ce que le produit ne sait pas », donc la garantie d'honnêteté — plafonnait à 3,14:1 là où la maquette rendait « Lieu non déterminé ». Le texte qui dit *je ne sais pas* était le moins lisible de l'interface. Deux règles comportementales étaient par ailleurs non conformes, dont une littéralement non implémentable telle qu'écrite.

**Aucun correctif n'a exigé d'abandonner un parti de conception.** Tous ont exigé qu'un parti visuel reçoive un doublon non visuel — ce qui est exactement ce qu'une spine doit produire.

## Verdicts par catégorie

| Catégorie | Verdict initial | Après correctifs |
|---|---|---|
| Couverture des parcours | adéquat | traité |
| Complétude des jetons | adéquat | traité |
| Couverture des composants | **mince** | traité |
| Couverture des états | **mince** | traité |
| Couverture des références visuelles | adéquat | traité |
| Ballonnement et surspécification | adéquat | partiellement traité |
| Discipline d'héritage | adéquat | traité |
| Conformité de forme | solide | inchangé |
| Accessibilité | **auto-contredit** | traité |

## Constats par sévérité

### Critiques (6) — tous corrigés

**`ink-muted` échoue AA partout où il sert** — `DESIGN.md.Colors`
3,44:1 sur le fond, 3,14:1 sur les cartes, 2,79:1 dans la zone de saisie, en 14 px italique. La garantie « le produit n'invente rien » reposait sur le seul jeton illisible de la palette.
*Correctif appliqué :* le jeton est **supprimé**. Corrigé à un niveau lisible il ne se distinguait plus de `ink-secondary` (écart de 1,24) — deux gris identiques ne sont pas un système. L'inconnu s'écrit désormais en `ink-secondary` à pleine lisibilité, et c'est **l'italique et les mots** qui le désignent.

**`aria-live="polite"` sur le fil rendait inaudible le seul événement attendu** — `Accessibility Floor` × `State Patterns`
Une région polie annonce toute mutation de son sous-arbre : la pastille passant au vert « sur place » produisait soit un « Confirmée » nu sans sujet, soit rien du tout.
*Correctif appliqué :* `role="log"` sur le fil, plus une région `role="status"` dédiée aux changements de statut portant une phrase complète — « Anna a confirmé. Mercredi 3 septembre, 19 h. » La règle « pas de nouveau message triomphal » reste tenue : le silence est un choix *visuel*, jamais un choix d'annonce.

**La frappe au vol : échec de WCAG 2.1.4, avec un garde-fou inversé** — `Interaction Primitives`
Raccourci à caractère unique actif hors focus. Son garde-fou testait `activeElement === body` — précisément l'état du mode lecture NVDA/JAWS qu'il prétendait exclure, et dont la détection est impossible depuis JavaScript.
*Correctif appliqué :* la règle est **retirée**, sa justification conservée dans la spine. Le champ se focalise seul au chargement et après chaque envoi ; c'est suffisant.

**Double et triple annonce à l'arrivée d'un tour**
*Correctif appliqué :* message, étapes et cartes sont insérés en une seule mutation, le tour portant un `aria-label` qui résume sa composition.

**Le bouton d'envoi n'existait pas pour les technologies d'assistance**
`<div class="send" aria-hidden="true">` dans les trois maquettes.
*Correctif appliqué :* `<button>` réel, nom accessible « Envoyer », `disabled` natif, 48 px.

**Aucune attribution de locuteur programmatique**
Le geste signature — le bot n'a ni bulle, ni avatar, ni horodatage — n'avait aucun équivalent non visuel : au lecteur d'écran, la conversation était un mur de texte sans interlocuteur.
*Correctif appliqué :* étiquette de locuteur visuellement masquée sur chaque tour, et la règle est inscrite dans `DESIGN.md.Shapes` à côté du geste qu'elle double.

### Élevés (22) — traités

- **`surface-raised-hover` à 1,10:1** — le survol ajouté par le pivot desktop était invisible. → Fond porté à `#1E314E`, et le survol est désormais porté par le **filet** (`border-strong`, 4,93:1), le fond ne faisant que confirmer.
- **Aucun contour de composant n'atteignait 1.4.11** — `Elevation & Depth` revendiquait « le contraste le plus faible qui reste perceptible » pour tous les filets. → Deux natures de filets désormais contractuelles : `border-decorative` pour le non-interactif, `border-interactive` (≥ 3:1) pour tout ce qui se clique ou se saisit.
- **Bloc de connexion et Récapitulatif de rencontre absents de DESIGN.md** alors qu'ils sont sur le chemin critique du parcours 1. → Ajoutés en jetons et en prose, avec le bloc de choix d'agenda et la pastille « nouveau message ».
- **Aucun état hors-ligne, échec d'envoi, OAuth annulé ou refusé, permission d'agenda refusée.** → Neuf lignes d'état ajoutées, dont le chargement à froid et la reprise en chargement.
- **FR-11 (proposition de lieu) sans foyer comportemental.** → Composant et deux états ajoutés.
- **Aucun beat ne posait l'heure du créneau** alors que le parcours 1 sautait de « deux lieux » à « 19 h ». → Étape 8 réécrite : l'heure se décide par la jouabilité, parce que le vivier ne connaît que des jours.
- **Contradiction inter-spines sur l'ambre** — EXPERIENCE faisait porter l'écart de niveau par `status-pending` que DESIGN interdit de détourner. → L'écart s'écrit en toutes lettres, sans couleur.
- **Anneau de focus rendu à 28 % d'opacité** (1,95:1 au lieu de 11,23:1) et par `box-shadow`, malgré l'interdit absolu des ombres. → `outline` opaque partout.
- **Cartes en `<div>`**, carte inerte indistinguable sans pointeur, nom accessible ne commençant pas par le texte visible (2.5.3). → `<button>` réels, filet décoratif à l'état inerte, nom accessible corrigé et suffixé du sort de la carte.
- **Maquettes sans requête média, colonne rognée par `overflow:hidden`** (1.4.10). → Requêtes média réelles, `min-height` au lieu de `height`.
- **Repli `prefers-reduced-motion` qui n'en était pas un** — retirer la pulsation laissait l'étape courante indistinguable. → Remplacée par un marqueur textuel « en cours ».
- **Mode contraste forcé** — toute la hiérarchie reposant sur des fonds. → Règle ajoutée : chaque surface qui compte porte un filet réel.
- **Divergence PRD §6 non tracée dans les spines**, seulement dans `.memlog.md` que les consommateurs aval ne lisent pas. → Encadré explicite en tête de `Foundation`.
- **Défaillance manquante au parcours 2** (Sarah abandonne la connexion). → Ajoutée.

### Moyens (25) — traités en partie

Traités : renommage `unknown-slot` → `unknown-value` (le composant sert à toute valeur inconnue, pas seulement un créneau), titre du parcours 1 remis verbatim sur le PRD, coquille « disable » → « dicible » sur une règle porteuse, tailles passées en `rem`, jeton `ink-disabled` ajouté, `spacing.target-min` et `focus-ring-width` promus en jetons, `rounded.DEFAULT` et `spacing.7` supprimés, focus non recouvert par la zone de saisie ancrée (2.4.11), erreurs identifiées en texte (3.3.1), `lang` et `<title>` inscrits au contrat, repères ARIA, espacement de texte forcé (1.4.12), charge mémorielle de « on le redit au bot » compensée par la persistance du fil, glose du mot « vivier ».

Journalisés sans correctif : halation du thème sombre unique sans échappatoire (le thème clair reste hors périmètre v1), redondance partielle de la section « Les deux populations du vivier », conflit potentiel des outils de traduction avec la région live.

### Faibles (18) — journalisés

Queues éditoriales des climax des parcours 2 et 3, valeurs en pixels subsistant dans la prose là où le jeton existe, position des liens de maquettes, « Choix par carte OU par frappe » déplacé de la table des composants vers Interaction Primitives.

## Ce qui tenait sans correction

- Les huit sections canoniques de DESIGN.md dans l'ordre verrouillé, les huit sections par défaut d'EXPERIENCE.md, les deux sections déclenchées à bon droit.
- Le glossaire du PRD §3 tenu littéralement sur les dix termes, sans un seul synonyme.
- L'état dominant « aucun candidat » traité en chemin nominal, confirmé par quatre marqueurs concordants.
- Les deux sections inventées gagnent leur place — « La grammaire de l'honnêteté » produit une règle de conception qu'aucune section par défaut ne pouvait porter.
- Aucune référence `{jeton}` cassée, aucune source introuvable, aucun conflit de nommage entre les deux fichiers.

## Fichiers de relecture

- `review-rubric.md` — 0 critique · 13 élevés · 14 moyens · 13 faibles · 10 résidus du pivot desktop
- `review-accessibilite.md` — 6 critiques · 9 élevés · 11 moyens · 5 faibles · tableau de 45 paires de contraste
