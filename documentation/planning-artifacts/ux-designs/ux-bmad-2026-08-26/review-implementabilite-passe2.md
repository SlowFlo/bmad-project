# Implémentabilité aval — Ex Aequo

> Revue d'architecte. Question unique : **peut-on construire à partir de DESIGN.md et EXPERIENCE.md seuls ?**
> Sévérités : **blocage** (impossible d'avancer sans réponse) · **élevé** (on avance en devinant, risque de refonte) · **moyen** · **faible**.
> Les identifiants (T-, C-, M-, P-, D-, R-, X-) servent de références de suivi.

## Verdict d'ensemble

**Non en l'état — oui après réponse à 18 questions bloquantes.** Les deux spines sont d'une qualité rare sur l'identité visuelle, la posture de marque et le plancher d'accessibilité : un développeur peut en tirer une feuille de jetons et une page qui ressemble au produit dès le premier jour. Mais elles décrivent **un couloir heureux et sa mise en scène**, pas un système : trois exigences fonctionnelles entières du PRD (FR-13 à quatre statuts, FR-14 et sa page d'acceptation, FR-15 et l'établissement du niveau) n'ont **aucune** existence dans l'expérience, la machine à états du fil est incomplète sur tous ses cas concurrents, et le point de rupture est chiffré à trois valeurs différentes selon l'artefact qu'on lit.

Le défaut le plus grave n'est pas une omission mais une **contradiction interne à EXPERIENCE.md** sur le contrat de rendu d'un tour de parole (mutation unique *versus* étapes narrées en temps réel) : c'est la première décision d'architecture front à prendre, et les deux règles qui la gouvernent s'excluent.

---

## Questions bloquantes

*Ce que j'irais demander avant d'écrire la première ligne.*

1. **Le point de rupture vaut-il 720 px, 45 rem ou 48 rem, et la requête média est-elle en `px` ou en `em` ?** EXPERIENCE dit 720 px « la largeur de lecture définie par `{spacing.thread-max-width}` » ; le jeton vaut 45 rem, qui n'égale 720 px qu'à racine 16 px ; les trois maquettes utilisent `48rem` (768 px). Et que fait-on entre 720 px et 784 px, où la colonne de 720 px + deux gouttières de 32 px ne rentre plus ?
2. **Une rencontre a-t-elle deux statuts ou quatre ?** EXPERIENCE : « Deux valeurs seulement : *en attente*, *confirmée* ». PRD FR-13 : quatre statuts (*en attente*, *confirmée*, *déclinée*, *expirée*), avec l'interdiction explicite de présenter un refus comme une absence de réponse. Si quatre : quels jetons pour *déclinée* et *expirée*, sachant que `status-danger` est contractuellement réservé à la jouabilité et que l'ambre a « un seul métier » ?
3. **Qui spécifie la page d'acceptation du partenaire (FR-14) ?** C'est la seule surface du produit hors du fil (l'addendum le dit), elle porte au moins six états (accepter, refuser, lien déjà utilisé, expiré, profil désinscrit, chevauchement avec une rencontre confirmée), et elle n'existe ni dans l'IA d'EXPERIENCE, ni dans les composants de DESIGN, ni dans une maquette.
4. **Où vit FR-15 — l'établissement du niveau par au plus deux questions factuelles ?** Aucun état, aucun composant, aucun parcours. Pire : EXPERIENCE le contredit deux fois (« Demande incomplète | Sport **ou niveau** manquant » ; parcours 1 où Thomas déclare « je suis intermédiaire » et est cru sur parole), alors que FR-15 interdit de demander le niveau et impose de poser les questions même quand la personne s'attribue un libellé.
5. **La ville est-elle demandée ou non ?** PRD FR-11 : Lyon uniquement, « il n'y a pas de ville à demander ». EXPERIENCE : état « Ville inconnue », règle « la ville est demandée en prose … une seule fois par conversation », parcours 1 étape 6. Maquettes : Nantes et le Tennis Club de la Beaujoire. Trois réponses.
6. **Un tour de parole s'insère-t-il en une mutation ou se construit-il progressivement ?** *Accessibility Floor* : « Le message, ses lignes d'étape et ses cartes arrivent ensemble … en **une seule mutation**. Jamais trois insertions successives. » *Component Patterns* : les lignes d'étape « s'empilent **pendant** le travail multi-étapes ». L'addendum renforce le second : chaque appel externe « observable et diffusé au fil en temps réel ». Les deux ne peuvent pas être vrais.
7. **La « frappe au vol » est-elle retirée ou pas ?** *Interaction Primitives* la retire explicitement, avec sa justification WCAG 2.1.4. Le tableau *Responsive & Platform* la prescrit encore comme comportement nominal PC (« Frappe au vol et Échap arment le champ »). Un tableau normatif contredit une règle normative du même document.
8. **Que fait le produit quand deux demandes coexistent ?** Une rencontre en attente avec Anna, puis une recherche de badminton dans le même fil : deux récapitulatifs ? un niveau à réétablir ? quel « point de vérité » ? Aucune transition n'existe.
9. **Que se passe-t-il quand la personne envoie un message pendant que le bot travaille ?** La zone de saisie est « toujours active, même pendant que le bot travaille » — mais rien ne dit si l'envoi interrompt la recherche en cours, s'empile, ou est traité en parallèle, ni ce que deviennent les lignes d'étape déjà affichées.
10. **Comment revient-on sur une décision prise ?** « On ne revient jamais en arrière modifier un choix : on le redit au bot. » Dit au bot « en fait, Iris » après avoir retenu Anna : la carte d'Anna redevient-elle active ? un second récapitulatif apparaît-il ? le premier passe-t-il dans un statut qui n'existe pas ? l'événement d'agenda est-il supprimé ? Aucune réponse.
11. **Quel signal reçoit une personne qui a remonté le fil quand un partenaire confirme ?** La confirmation ne produit **aucun** nouveau message (règle explicite) ; la pastille « nouveau message » n'apparaît que « quand un message arrive ». Le seul événement que la personne attend est donc, visuellement, silencieux et hors écran.
12. **Quelle balise porte la zone de saisie ?** La spine impose Maj+Entrée et une croissance jusqu'à quatre lignes ; les trois maquettes utilisent `<input type="text">`, qui ne peut faire ni l'un ni l'autre.
13. **D'où vient l'attribut couvert / extérieur d'un lieu ?** FR-10 fait dépendre toute la jouabilité de cet attribut. Il n'apparaît dans aucune des deux spines, ni dans le récapitulatif, ni dans la proposition de lieu, ni dans une maquette. Sans lui, l'encadré de jouabilité n'est pas calculable — et le parcours 1 s'écroule à l'étape 8.
14. **Le récapitulatif d'alerte différée est-il le composant « récapitulatif de rencontre » ?** L'état « Alerte différée posée » exige « un récapitulatif dans le fil **avec un moyen d'annuler** », alors que le composant récapitulatif est spécifié « non interactif ». Quel composant, quel jeton, quel bouton, et que se passe-t-il après annulation ?
15. **Sarah sans compte entre-t-elle dans le vivier ?** Parcours 2, variante sans alerte : « il l'enregistre quand même dans le vivier en le lui disant ». FR-3 : « Un visiteur sans compte ne sort jamais comme candidat d'une recherche », l'entrée au vivier se fait « à la création de son compte, et pas avant ». Le bot énoncerait donc un mensonge — sur le produit dont la thèse entière est de ne pas mentir.
16. **Comment un utilisateur connu est-il reconnu, et comment se connecte-t-il s'il ne l'est pas ?** L'état « Fil à froid, connu » suppose une reconnaissance dont le mécanisme n'est pas dit (cookie ? session ? durée ?), et il n'existe **aucun point d'entrée de connexion** hors du « moment connexion » déclenché par la mise en relation. Un utilisateur inscrit sur une autre machine est indistinguable d'un inconnu et n'a aucun moyen de se retrouver.
17. **Quels sont les paramètres d'animation et de temporisation ?** Durée et courbe du fondu, amplitude de la « translation verticale de quelques pixels », forme et période de la pulsation, valeur de la borne « au-delà de quelques secondes », durée de la « pause de saisie » avant qu'une annonce soit émise, seuil au-delà duquel le bot est déclaré indisponible. Six valeurs, zéro chiffre.
18. **Y a-t-il un en-tête persistant ?** La maquette du fil à froid porte un bloc-marque « EX AEQUO » en capitales forcées, dans les deux cadres. Les deux spines n'en parlent jamais, interdisent toute navigation, et DESIGN interdit explicitement les capitales forcées.

---

## 1. Traduction des jetons en système

**Ce qui passe mécaniquement.** Les 22 couleurs, les 4 rayons et les 6 échelons d'espacement se traduisent en `custom properties` sans arbitrage. Les 6 rôles typographiques aussi, à la réserve de forme près (T-09). **Aucune couleur n'est du poids mort** : les 22 sont consommées par au moins un composant ou une règle. C'est bien tenu et il faut le dire.

**Ce qui ne passe pas.**

| ID | Constat | Sévérité |
|---|---|---|
| **T-01** | **`{spacing.thread-max-width}` = 45 rem est déclaré égal à 720 px par EXPERIENCE.** L'égalité n'est vraie qu'à racine 16 px. La spine choisit `rem` précisément pour que la colonne « suive le zoom texte » — donc à 200 % de zoom texte la colonne veut 1440 px pendant que le point de rupture reste à 720 px. Le jeton et la règle qui l'invoque se combattent. | **blocage** |
| **T-02** | **Unités mélangées sans règle.** `typography` est intégralement en `rem` avec une consigne explicite (« Toutes les tailles sont en `rem`, jamais en pixels ») ; `spacing`, `rounded`, `target-min` et `focus-ring-width` sont intégralement en `px`. Le tableau *Do's and Don'ts* condamne « des px figés qui résistent au zoom » — condamnant, littéralement, la moitié de son propre frontmatter. Aucune règle ne dit quelles familles restent en px et pourquoi. | **élevé** |
| **T-03** | **`{spacing.message-gap}` et `{spacing.turn-gap}` ne sont référencés par aucun composant.** Ils existent en prose (« sépare deux messages consécutifs », « sépare un tour du suivant ») sans dire *sur quel élément* ni *sous quelle propriété* : `margin-bottom` du tour ? `gap` du conteneur de fil ? Les maquettes, elles, emploient en plus `message-gap` (24 px) comme écart intra-tour entre le message et ses cartes, son encadré, son récapitulatif — un troisième usage que la spine ne prévoit pas. | **élevé** |
| **T-04** | **`{spacing.6}` (32 px) n'est consommé par aucun composant** et double `turn-gap` et `gutter-desktop`. `{spacing.5}` (24 px) double `message-gap`. Trois jetons pour deux valeurs, sans règle de préséance : un développeur ne sait pas lequel écrire. | **moyen** |
| **T-05** | **`{typography.display}` n'est référencé par aucun composant.** Le seul endroit où il vit est l'état « Fil à froid » d'EXPERIENCE. L'accroche n'a donc ni entrée dans `components`, ni jeton d'espacement, ni bornes de longueur. | **moyen** |
| **T-06** | **Valeurs composites non traduisibles telles quelles.** `message-user.align: right` n'est pas un couple propriété/valeur CSS. `partner-card.cursor: pointer` place du comportement dans un jeton. `border: '1px solid {colors.border-interactive}'` mêle raccourci CSS et référence : il faut un résolveur, et rien ne le décrit. Enfin `focus-ring-width` est logé sous `spacing` alors qu'il désigne une épaisseur de contour. | **moyen** |
| **T-07** | **Le point de la ligne d'étape mesure « 6 px » en prose et n'a pas de jeton** — valeur hors de l'échelle 4/8/12/16/24/32. L'écart entre le point et le texte n'a ni jeton ni prose (les maquettes inventent 10 px, également hors échelle). | **élevé** |
| **T-08** | **Aucun paramètre de mouvement n'est tokenisé.** « fondu bref », « translation verticale de quelques pixels », « pulsation », « au-delà de quelques secondes ». Zéro durée, zéro courbe, zéro amplitude. Deux développeurs produiront deux produits différents sur le seul mouvement admis par la spine. | **élevé** |
| **T-09** | **Typage incohérent dans le frontmatter.** `fontWeight: 600` est un nombre, `lineHeight: '1.2'` une chaîne, les clés de `spacing` sont des chaînes numériques (`'1'`…`'6'`). Un convertisseur YAML → jetons doit être écrit sur mesure ; les clés numériques quotées sont un piège classique de plusieurs outils de jetons. | **faible** |
| **T-10** | **`{components.unknown-value}` est référencé comme une valeur** dans EXPERIENCE (« Sans donnée, le lieu prend `{components.unknown-value}` ») alors que c'est un jeu de deux propriétés. La syntaxe `{chemin}` mélange donc référence de valeur et référence de jeu de styles, sans convention déclarée. | **moyen** |
| **T-11** | **`auth-block` et `agenda-choice` sont identiques à un jeton près** (`gap` 12 px contre 8 px), alors que la prose affirme « même anatomie ». Soit la différence est intentionnelle et non motivée, soit c'est une coquille — impossible de trancher. | **faible** |
| **T-12** | **`playability-callout` n'a pas de jeton typographique** ni de jeton pour sa contre-proposition (la ligne secondaire que les maquettes rendent en `meta`/`ink-secondary`), ni de jeton pour la rangée de boutons qui l'accompagne dans les maquettes et que `components` ignore. | **élevé** |
| **T-13** | **Le bouton d'envoi désactivé est invisible par construction.** `composer.background` = `surface-overlay` ; `button-primary.backgroundDisabled` = `surface-overlay`. Fond identique, aucun filet prévu : le bouton disparaît dans son conteneur au repos, c'est-à-dire dans son état le plus fréquent. Les maquettes s'en sont aperçues et ont ajouté un `border: 1px solid border-decorative` qui n'existe dans aucun jeton. | **élevé** |
| **T-14** | **Aucune échelle `z-index`** alors que trois choses se superposent : le fil qui défile, la zone de saisie « seule surface qui flotte au-dessus », et la pastille « nouveau message » ancrée au-dessus d'elle. | **moyen** |

### Le trou du tableau de contraste

Le tableau *Cibles de contraste* est présenté comme contractuel — « tout jeton ou toute composition qui les enfreint est un défaut ». Il **omet précisément les paires qui échouent** :

| ID | Paire absente du tableau | Ratio mesuré | Conséquence | Sévérité |
|---|---|---|---|---|
| **T-15** | `border-decorative` / `surface-raised` | **1,72:1** | C'est le **seul** porteur de la distinction carte active / carte inerte, que la spine exige « perceptible sans pointeur » et « visible sans pointeur ». Un filet à 1,7:1 porte donc à lui seul une information d'état — ce que la spine interdit dans la phrase même qui définit `border-decorative` (« il ne porte jamais à lui seul une information »). | **blocage** |
| **T-16** | `surface-raised` / `surface-base` | **1,09:1** | La première des « trois marches » de la hiérarchie est imperceptible. Le récapitulatif de rencontre — « le point de vérité du parcours » — n'est donc délimité que par un filet à 1,72:1 posé sur une marche à 1,09:1. Idem pour le bloc de connexion et le bloc d'agenda. | **élevé** |
| **T-17** | `surface-overlay` / `surface-base` | 1,24:1 | Sans conséquence : la zone de saisie porte `border-interactive` à 4,79:1. Mentionné pour montrer que le tableau ne certifie que les paires gagnantes. | **faible** |

---

## 2. Composants — ce qui manque pour construire

| Composant | Visuel suffisant ? | Comportement suffisant ? | Ce qui manque |
|---|---|---|---|
| **Message du bot** | Oui | Oui | Balise indéterminée (`<p>` par message ? `<div>` de tour ?). Rien sur la prose multi-paragraphes : « une idée par message » n'interdit pas deux phrases, et l'écart entre elles n'est pas tokenisé. Aucune borne de longueur. **(C-01, moyen)** |
| **Message de la personne** | Oui | Presque | `maxWidth: 80%` — de la colonne ou du conteneur ? Comportement d'un mot de 60 caractères sans espace (URL collée) : pas de règle de césure, `overflow-wrap` non spécifié, débordement horizontal probable alors que la spine interdit tout défilement horizontal. **(C-02, moyen)** |
| **Ligne d'étape** | Non | Non | Taille du point hors échelle et non tokenisée ; écart point/texte absent ; **la pulsation n'a ni forme, ni durée, ni période, ni borne chiffrée** ; le double rendu exigé par l'accessibilité (liste visible persistante dans le fil **et** région `role="status"` où seule la dernière remplace la précédente) n'est décrit nulle part comme mécanisme — les maquettes ne l'implémentent d'ailleurs pas. Nombre maximal d'étapes non borné : que fait-on à 12 étapes ? Aucune forme pour une **étape en échec**, que la grammaire de l'honnêteté exige pourtant. **(C-03, blocage)** |
| **Carte de partenaire** | Presque | Presque | Balise : `<button>` ✔ (dit deux fois). Mais : **contenu non borné** — un prénom de 40 caractères dans une carte d'environ 14 rem (aucune règle de coupure, et « aucun conteneur de texte n'a de hauteur fixe » interdit l'élision par hauteur) ; **sept jours disponibles** sans règle de repli ni de troncature ; **zéro jour disponible** — cas non traité alors que `unknown-value` existerait pour ça. **Une ou deux cartes** : « sur une ligne, trois au maximum » ne dit pas si une carte seule occupe toute la colonne. L'**écart de niveau « écrit en toutes lettres sur la carte »** n'a ni gabarit de phrase, ni emplacement, ni jeton, ni maquette. Ordre des cartes non spécifié. Et si le focus **est sur la carte** au moment où elle devient inerte, il se perd : cas non traité. **(C-04, blocage)** |
| **Pastille de statut** | Oui, pour 2 valeurs | Non | Deux valeurs spécifiées, **quatre exigées par FR-13**. Ni jeton ni libellé pour *déclinée* et *expirée*, et les deux couleurs de statut restantes sont contractuellement réservées ailleurs. Balise indéterminée. **(C-05, blocage)** |
| **Récapitulatif de rencontre** | Presque | Non | « Non interactif » mais doit porter un `aria-label` mis à jour — donc un `role` (`group`/`region`) que rien ne nomme ; sur un `<div>` nu comme dans les maquettes, l'`aria-label` est ignoré par plusieurs technologies. **Plusieurs récapitulatifs** : la spine reconnaît que « au-delà de deux ou trois rencontres, un récapitulatif en prose devient illisible » puis « accepte cette limite » sans dire ce qui est rendu. Le récapitulatif d'**alerte différée** exige un contrôle d'annulation dans un composant déclaré non interactif. Débordement à 320 px : la pastille « alignée à droite du titre » passe à la ligne, non spécifié. Le lieu et l'heure ont des états inconnus ✔, mais **le partenaire, le sport et le jour n'en ont pas** — alors que la règle dérivée exige que « toute donnée affichable ait un état inconnu rendu ». **(C-06, blocage)** |
| **Bloc de connexion** | Oui | Presque | Le lien « Pourquoi ? » : mécanisme de dépliement non spécifié (état ouvert/fermé, `aria-expanded`, marqueur, animation), et **contrainte difficilement tenable telle qu'écrite** — un lien en `meta` doit respecter `target-min` (48 px) tout en étant inline, sans que la mise en page qui le permet soit décrite. Contenu du dépliement (« la portée exacte de l'accès demandé ») non rédigé. Devenir du bloc après connexion réussie : non dit. **(C-07, élevé)** |
| **Bloc de choix d'agenda** | Oui | Presque | Le « second geste explicite » de consentement d'écriture n'a **aucun composant** : bouton ? case à cocher ? nouveau tour du bot ? Même question de devenir après résolution. **(C-08, élevé)** |
| **Encadré de jouabilité** | Non | Non | Pas de jeton typographique ; la contre-proposition (sous-ligne) n'a pas de jeton ; **la rangée d'actions n'existe pas comme composant** alors qu'elle est indispensable (« Retenir 19 h » / « Garder 17 h » / « Un autre jour » dans la maquette, en nombre variable d'un cadre à l'autre sans règle). Trois seuils possibles (chaleur, vent, air) et rien ne dit ce qui s'affiche quand **deux ou trois** sont dépassés : un encadré ou trois ? Devenir de l'encadré après décision : non dit. **(C-09, élevé)** |
| **Zone de saisie** | Presque | Presque | **Balise indéterminée et contredite** : quatre lignes de croissance + Maj+Entrée impliquent `<textarea>` ou `contenteditable`, les trois maquettes emploient `<input type="text">`. Mécanique de croissance non spécifiée. Le bouton d'envoi est déclaré `button-primary` (jeton avec `padding 12/24` et police `label`, donc **textuel**) mais rendu en icône carrée de 48 px dans les trois maquettes : lequel ? Invisibilité à l'état désactivé (T-13). « On ne perd pas le brouillon silencieusement » : quel message, quel composant ? **(C-10, blocage)** |
| **Pastille « nouveau message »** | Oui | Non | Emplacement précis non tokenisé (décalage au-dessus de la zone de saisie). **Ne se déclenche que sur un message**, donc jamais sur la confirmation d'un partenaire, qui par règle ne produit pas de message (voir M-08). Position dans l'ordre de tabulation non spécifiée. **(C-11, élevé)** |
| **Bouton primaire** | Oui | Non | « Un seul bouton primaire visible à la fois dans le fil » est **inapplicable tel quel** : le fil n'est jamais purgé, les tours passés gardent leurs boutons, et « le passé est inerte » n'est énoncé que pour les cartes. Un bouton primaire d'un tour résolu reste-t-il primaire, devient-il discret, disparaît-il ? La règle la plus citée de la spine n'a pas de mécanisme. **(C-12, blocage)** |
| **Bouton discret** | Oui | Presque | Même question de devenir. Pas d'état pressé (le primaire en a un, le discret non). Pas d'état désactivé. **(C-13, moyen)** |
| **Proposition de lieu** | Non | Presque | Pas d'entrée dans `components` — c'est de la prose dans un message, ce qui est cohérent, mais alors **l'attribut couvert / extérieur exigé par FR-11 n'a nulle part où se rendre**, et la jouabilité en dépend. Deux lieux au maximum ✔, format de présentation non spécifié (liste ? phrase ?), alors que les listes à puces dans la prose sont interdites par *Voice and Tone*. **(C-14, blocage)** |
| **Valeur inconnue** | Oui | Oui | Rien à signaler ; c'est le composant le mieux spécifié du lot. |
| **Indicateur de focus** | Oui | Oui | Complet et cohérent (`outline` opaque, 3 px, décalage 2 px, jamais supprimé). |
| **Accroche du fil à froid** | Non | Non | Aucune entrée `components`. Texte non rédigé, écart accroche/sous-titre non tokenisé, sous-titre sans rôle typographique attribué. **L'exemple de phrase est placé « sous le champ » par EXPERIENCE et au-dessus, dans la colonne, par la maquette.** Devenir de l'accroche au premier message (disparaît ? reste en tête de fil ?) non dit. **(C-15, élevé)** |
| **États de service (hors-ligne, échec d'envoi, bot indisponible, ligne d'attente de reprise)** | Non | Partiel | Quatre états comportementaux réels, **zéro composant, zéro jeton, zéro maquette**. « Une ligne d'état persistante, non modale » : quelle surface, quelle couleur ? La contrainte de palette rend la question non triviale — le rose-rouge est interdit pour les pannes, l'ambre pour tout sauf *en attente*, donc **il ne reste aucune couleur autorisée pour signaler un échec**, alors que la spine exige que les erreurs soient « identifiées en texte, à côté de l'élément concerné ». « Marqué non envoyé, avec une action de réémission » : quel marqueur, quel bouton, où ? **(C-16, blocage)** |
| **Bloc / récapitulatif d'alerte différée** | Non | Non | Composant implicite, jamais spécifié, avec un contrôle d'annulation contradictoire (C-06). **(C-17, blocage)** |
| **En-tête / bloc-marque** | Non | Non | Présent dans une maquette, absent des deux spines, en capitales que DESIGN interdit. Existe-t-il ? **(C-18, élevé)** |
| **Page d'acceptation du partenaire (FR-14)** | Non | Non | Surface entière manquante, six états au moins. **(C-19, blocage)** |

---

## 3. Machine à états du fil — transitions non spécifiées

### Ce que je peux reconstituer

Le fil est une machine à **un état de conversation** plus **quatre superpositions orthogonales** (réseau, service externe, bot, OAuth). L'état de conversation, tel qu'il est reconstructible :

```
      OUVERTURE
         │
    ┌────┴──────────────────┐
    ▼                       ▼
FROID_INCONNU          FROID_CONNU ──(récap pas prêt)──► REPRISE_EN_CHARGEMENT
    │                       │
    └──────────┬────────────┘
               ▼
        DEMANDE_ANALYSÉE
         ├─(sport ou jour manquant)─► DEMANDE_INCOMPLÈTE ──┐
         ├─(sport absent du vivier)─► SPORT_HORS_VIVIER    │ (retour)
         ├─(hors sujet)─────────────► HORS_PÉRIMÈTRE ──────┘
         └─(complète)───────────────► RECHERCHE_EN_COURS
                                          │
        ┌──────────────┬──────────────────┼─────────────────┐
        ▼              ▼                  ▼                 ▼
  CORRESPONDANCE  ÉLARGISSEMENT_JOUR  ÉLARGISSEMENT_NIVEAU  VIVIER_VIDE
        └──────────────┴──────────────────┘                 │
                       ▼                          ┌─────────┴─────────┐
              PARTENAIRE_RETENU                   ▼                   ▼
                       │                    ALERTE_PROPOSÉE     (refus) FIN
                       ▼                          │
               VILLE_?  ← contredit par FR-11     ▼
                       ▼                   CONNEXION_DEMANDÉE ─► ALERTE_POSÉE
              LIEU_PROPOSÉ | AUCUN_LIEU                            (annulation ?)
                       ▼
              JOUABILITÉ_ÉVALUÉE
                ├─(danger)───────► CONTRE_PROPOSITION ─┐
                ├─(hors portée)───────────────────────►│
                └─(rien à signaler)────────────────────▼
                                              HEURE_VALIDÉE
                                                     ▼
                                           CONNEXION_DEMANDÉE
                                        ┌────────┬───────────┐
                                        ▼        ▼           ▼
                                     réussi   annulé      refusé
                                        ▼        └─────┬─────┘
                                 CHOIX_AGENDA          ▼
                                        ▼        (reprise sur place)
                                 CONSENTEMENT_ÉCRITURE
                                  ┌─────┴─────┐
                                  ▼           ▼
                              accordé      refusé
                                  └─────┬─────┘
                                        ▼
                           RÉCAPITULATIF (en attente) ──► (confirmée)
                                                      ??? déclinée / expirée
```

### Les transitions qui n'existent pas

| ID | Transition non spécifiée | Sévérité |
|---|---|---|
| **M-01** | **Deux demandes en cours.** Rien n'interdit à Thomas de lancer une recherche de badminton alors que la rencontre avec Anna est en attente. Combien de récapitulatifs ? Lequel est « le point de vérité » ? Le niveau est-il réétabli (FR-15 dit oui, par sport) ? Le lieu et la ville retenus « une seule fois par conversation » valent-ils pour la seconde demande ? La *reprise* les récapitule-t-elle tous ? La spine reconnaît le problème (« au-delà de deux ou trois rencontres … illisible ») et **l'accepte au lieu de le résoudre**. | **blocage** |
| **M-02** | **Envoi pendant le travail du bot.** Le champ « reste actif » — décision explicite — mais l'effet d'un envoi pendant `RECHERCHE_EN_COURS` n'est nulle part. Interruption ? file d'attente ? traitement parallèle ? Les lignes d'étape en cours sont-elles abandonnées, et si oui restent-elles visibles (la spine dit qu'elles « constituent la trace de ce que le bot a réellement consulté » — une trace tronquée est-elle honnête) ? | **blocage** |
| **M-03** | **Retour sur une décision prise.** « On le redit au bot » est une politique, pas une transition. Redire « en fait Iris » après avoir retenu Anna : nouvelle carte ? nouveau récapitulatif ? le premier passe dans quel statut (aucun des deux, ni des quatre du PRD, ne couvre « abandonnée par le demandeur ») ? L'événement d'agenda déjà écrit est-il supprimé, mis à jour, laissé ? Le partenaire déjà prévenu est-il détrompé ? | **blocage** |
| **M-04** | **Changement de créneau après écriture agenda.** Même famille que M-03, avec en plus le contrat FR-12 (« tout changement de statut … met à jour l'événement d'agenda »). Aucune interface pour ça. | **blocage** |
| **M-05** | **Confirmation d'un partenaire pendant que la personne est ailleurs dans le fil.** Spécifié pour le cas nominal (mutation sur place + `role="status"`), non spécifié si : le récapitulatif est hors écran (M-08), la personne est en train de taper (« rien n'est annoncé pendant que la personne tape » — l'annonce est donc différée d'une durée non chiffrée), ou la personne est au milieu d'un `CONNEXION_DEMANDÉE` pour une seconde demande. | **élevé** |
| **M-06** | **Déclinée et expirée.** FR-13 les impose et exige qu'elles restent « consultables dans le fil avec leur statut ». Aucun état, aucun jeton, aucune phrase de bot, aucune annonce. La bascule *en attente* → *expirée* est de surcroît **déclenchée par le temps**, sans message ni action : le seul déclencheur non conversationnel du produit, et il n'existe pas dans la spine. | **blocage** |
| **M-07** | **Refus de la contre-proposition de jouabilité.** « La personne peut passer outre » ✔, mais l'encadré reste-t-il, devient-il inerte, garde-t-il ses boutons cliquables une fois le tour résolu ? La règle d'inertie ne couvre que les cartes. | **élevé** |
| **M-08** | **Aucun signal pour la confirmation hors écran.** La pastille « nouveau message » se déclenche sur l'arrivée d'un message ; la confirmation ne produit par règle **aucun** message. Une personne qui a remonté le fil ne voit donc rien, et n'a qu'une annonce éphémère qu'elle a peut-être manquée — alors que la spine affirme que « le seul événement que la personne attendait ne peut pas être inaudible ». La règle et le mécanisme divergent. | **blocage** |
| **M-09** | **Timeout du bot.** L'état « Bot indisponible » existe, son **déclencheur** (« panne du service de conversation ») n'est pas observable côté client sans seuil. Au bout de combien de temps sans réponse le fil bascule-t-il ? Que montre-t-il entretemps, une fois la pulsation « bornée » retombée en texte statique ? | **élevé** |
| **M-10** | **Fin de vie d'un fil.** « Le fil ne se réinitialise jamais tout seul », le PRD lui donne 30 jours sans compte. Que se passe-t-il au jour 31 ? Quel est le stockage (cookie, `localStorage`, session serveur), et donc que voit la même personne dans un second onglet, sur un second appareil, en navigation privée ? Aucune réponse, alors que « aucune expiration de session ne vide la conversation » est une promesse d'infrastructure. | **blocage** |
| **M-11** | **Connexion hors du moment de mise en relation.** Il n'existe aucun chemin vers `FROID_CONNU` autre que la reconnaissance implicite. Un inscrit sur un nouvel appareil est piégé dans `FROID_INCONNU` sans point d'entrée. | **blocage** |
| **M-12** | **Reprise sur un fil dont l'état a avancé côté serveur pendant l'OAuth.** Le retour « rouvre le fil au même endroit » — mais si la confirmation d'Anna est arrivée pendant la redirection, l'« endroit » a changé. Ordre de rejeu non spécifié. | **moyen** |
| **M-13** | **Refus de l'alerte différée puis changement d'avis.** « Le bot n'insiste pas, ne redemande pas de compte » : si la personne redemande l'alerte deux tours plus tard, on rentre dans `CONNEXION_DEMANDÉE` après avoir promis de ne pas redemander. | **faible** |
| **M-14** | **Annulation d'une alerte posée.** Le contrôle est exigé, l'état d'arrivée n'existe pas. | **élevé** |

---

## 4. Décisions non tranchées déguisées en prose

| ID | Formulation | Ce qu'un développeur doit inventer | Sévérité |
|---|---|---|---|
| **P-01** | « Le bot **récapitule** en tête de fil les demandes en cours et les rencontres, puis rend la parole » | La forme entière de la reprise : prose ou composants ? un récapitulatif par rencontre, ou un message qui les cite ? dans quel ordre ? avec quelle borne ? Le paragraphe suivant admet que la forme casse à trois rencontres, puis « accepte cette limite » — c'est-à-dire ne décide pas. | **blocage** |
| **P-02** | « Le retour rouvre le fil **au même endroit**, sans perte de contexte » | Quelle position de défilement, quel élément focalisé (l'A11y dit « le message qui reprend la conversation » — lequel exactement ?), quel état si un tour a été inséré entre-temps, quelle durée de survie du brouillon, quel stockage. « Sans perte de contexte » n'est pas un comportement. | **élevé** |
| **P-03** | « Colonne pleine largeur » sous le point de rupture | À quel point de rupture (Q1), et « pleine largeur » signifie-t-il `100 %` moins les gouttières, ou `100 %` tout court ? La plage 720–784 px n'est couverte par aucune des deux colonnes du tableau. | **blocage** |
| **P-04** | « Les annonces **attendent une pause de saisie** » | Une durée, un mécanisme (bascule `aria-live` off/on ? file interne ?), et le comportement si la personne tape sans discontinuer pendant deux minutes. C'est une machine à états supplémentaire présentée comme une phrase. | **élevé** |
| **P-05** | « La pulsation de l'étape courante est **bornée**. Au-delà de **quelques secondes**, elle cède la place à un texte statique » | La borne, la forme de la pulsation, et le texte statique de remplacement (le même « en cours » que sous `prefers-reduced-motion` ?). | **élevé** |
| **P-06** | « **Un seul bouton primaire visible à la fois** dans le fil » | Ce que devient un bouton primaire du passé dans un fil qui n'est jamais purgé (C-12). | **blocage** |
| **P-07** | « Elle **ne doit jamais recouvrir** un élément qui vient de recevoir le focus : le fil se réduit d'autant » | Le mécanisme : `scroll-margin-bottom` ? `scrollIntoView` sur `focusin` ? mise en page en colonne flex non chevauchante ? La phrase voisine d'*Elevation* décrit pourtant la zone de saisie comme « la seule surface qui **flotte au-dessus** du fil qui défile » — flotte ou ne chevauche pas, il faut choisir. | **élevé** |
| **P-08** | « Le bot **le glose la première fois** qu'il emploie *vivier* » | Où est stocké « la première fois » ? Par fil, par compte, par session ? Que se passe-t-il à la reprise trois jours plus tard ? | **moyen** |
| **P-09** | « Le brouillon **survit** à une redirection OAuth » puis « la spine ne promet pas qu'il survivra toujours, elle promet qu'on ne le perd pas silencieusement » | Le second énoncé annule le premier et le remplace par une exigence non spécifiée : quel message, quel composant, à quel moment quand le brouillon est perdu. | **élevé** |
| **P-10** | « Le produit **doit rester intact** sous les valeurs d'espacement forcées » / « rien n'est perdu ni chevauché » | Des critères mesurables. Utilisable comme test manuel, pas comme spécification. | **moyen** |
| **P-11** | « Les lieux proposés **correspondent au sport** de la demande » | La règle d'appariement sport → type d'équipement, et son repli pour les six sports du vivier qui n'ont pas d'équipement dédié (course à pied, yoga, pilates, danse, escalade en extérieur…). | **élevé** |
| **P-12** | « Le bot **nomme précisément** ce qu'il n'a pas pu faire » | Le vocabulaire par intégration, et surtout la frontière : jusqu'où « précisément » avant de tomber dans le jargon que la règle voisine interdit (« nomme l'échec sans jargon »). | **moyen** |
| **P-13** | « Le mot est **toujours écrit** » (pastille de statut) | Les quatre mots, dont deux n'existent pas (M-06). | **blocage** |
| **P-14** | « **Aucun composant ne rend un champ obligatoire à l'affichage** » | Règle excellente, mais non appliquée : le prénom, le sport, le jour et le niveau n'ont pas d'état inconnu rendu, ni sur la carte ni dans le récapitulatif. La règle se contredit elle-même par omission. | **élevé** |
| **P-15** | « La ville est demandée … **une seule fois par conversation, puis retenue** » | Retenue où — dans le fil, en session, au profil ? Que fait la reprise trois jours plus tard ? Et le PRD dit qu'il n'y a pas de ville à demander (Q5). | **élevé** |

---

## 5. Contrats de données implicites

Les deux spines n'énoncent **aucun** contrat de données. Voici ce qu'elles supposent, ce qui manque, et ce que l'interface doit faire quand la donnée manque, arrive tard ou est incohérente.

| ID | Donnée supposée | Forme non dite | Manque / tard / incohérent | Sévérité |
|---|---|---|---|---|
| **D-01** | **Niveau** | Énumération de trois valeurs jamais énumérée. Elle n'est déductible que de la phrase « Débutant et Avancé ne se croisent jamais », qui suppose aussi un **ordre**. Casse et accord (« Intermédiaire ») non spécifiés — la carte l'écrit capitalisé, la prose du bot en minuscule. Qui formate, le backend ou l'interface ? | Niveau absent d'un profil : pas d'état rendu (P-14). | **élevé** |
| **D-02** | **Écart de niveau** | Champ calculé, ni nommé ni typé : chaîne prête à afficher, ou entier signé que l'interface met en mots ? La spine exige qu'il soit « écrit en toutes lettres sur la carte » sans donner le gabarit ni l'emplacement. | Non couvert. | **blocage** |
| **D-03** | **Jours disponibles** | Liste de jours de semaine (le CSV le confirme), sans dates ni heures. Non bornée : 1 à 7. Ordre (chronologique depuis lundi ? depuis aujourd'hui ?), casse (minuscule sur la carte, capitale dans le récapitulatif), séparateur (« , » sur la carte, « · » entre méta), règle de repli à 7 jours. | Zéro jour : non couvert. | **élevé** |
| **D-04** | **Lieu** | `{nom, ville, couvert\|extérieur}`. **L'attribut couvert/extérieur, dont dépend toute la jouabilité (FR-10), n'apparaît nulle part** — ni composant, ni prose, ni maquette. Longueur du nom non bornée. | Absent ✔ (`unknown-value`, bien traité). En retard : non couvert — le lieu peut-il arriver après le récapitulatif, qui se mettrait à jour sur place ? | **blocage** |
| **D-05** | **Météo** | Trois mesures (ressenti, rafales, ATMO) **à granularité horaire** — sans quoi le pivot du parcours 1 (« mercredi 34 °C **à 17 h**, je vous propose 19 h ») est impossible. La granularité n'est jamais dite. Horizon de prévision non chiffré, alors que l'état « Prévision hors portée » en dépend. Unités et arrondis non spécifiés. | Absente ✔. En panne ✔. **Partielle** (température oui, qualité de l'air non) : non couvert, et c'est le cas le plus probable en production. | **blocage** |
| **D-06** | **Statut de rencontre** | 2 valeurs contre 4. Pas de champ « date de bascule », alors que *expirée* est déclenchée par le temps. | *Déclinée*/*expirée* : rien. | **blocage** |
| **D-07** | **Partenaire** | `{prénom}` — et **jamais** de nom ni de téléphone ✔ (règle nette et bien tenue). Longueur du prénom non bornée ; **homonymes** non traités : deux « Anna » dans une même proposition rendent ambiguë la commande vocale « cliquer Anna », sur laquelle la spine s'appuie explicitement. La nature du profil (amorçage / inscrit) est délibérément non exposée ✔, mais elle conditionne le statut atteignable — l'interface doit-elle la connaître ? | — | **élevé** |
| **D-08** | **Date et heure** | Format « Mercredi 3 septembre, 19 h » observé une fois dans une maquette. Aucun contrat : minutes (19 h 30 ?), année, fuseau, locale, durée par défaut de la rencontre (que FR-12 doit pourtant écrire dans l'agenda). Le bot énonce des heures que l'agenda écrit : c'est un contrat, pas une présentation. | — | **élevé** |
| **D-09** | **Étapes narrées** | Contrat de flux : identifiant, libellé, état (en cours / franchie / **échouée**). L'état échoué est exigé par la grammaire de l'honnêteté (« quand la météo tombe, la ligne d'étape le montre ») et n'a **ni jeton, ni couleur autorisée, ni forme** — la palette n'offre rien pour ça. | Étape qui n'arrive jamais : non couvert. | **blocage** |
| **D-10** | **Identité et session** | Rien. Ni mécanisme de reconnaissance, ni durée, ni portée (appareil / onglet). | Voir M-10, M-11. | **blocage** |
| **D-11** | **Événement d'agenda** | FR-12 exige que l'événement porte le statut et soit mis à jour à chaque bascule. Aucun retour d'interface n'est prévu pour la mise à jour : le récapitulatif dit-il « agenda à jour » ? Que se passe-t-il si la mise à jour échoue après coup, alors que la personne n'est plus dans le fil ? | Échec différé : non couvert. | **élevé** |
| **D-12** | **Cohérence croisée** | Aucune règle : un partenaire dont les jours ne contiennent pas le jour retenu, un lieu hors de la ville, une rencontre confirmée dans le passé, un créneau météo antérieur à maintenant. Pour un produit dont la thèse est « le bot n'invente rien », l'absence de règle d'incohérence est un manque de principe autant que de spécification. | **Aucun** cas traité. | **élevé** |
| **D-13** | **Canal d'alerte différée** | Assumé comme e-mail par une hypothèse déclarée ✔ (l'honnêteté est exemplaire ici), mais l'interface qui en découle n'existe pas : la personne voit-elle son adresse ? peut-elle la changer ? que dit le fil si l'envoi échoue ? | Non couvert. | **élevé** |

---

## 6. Responsive et points de rupture

**Le point de rupture est chiffré — trois fois, à trois valeurs.**

| ID | Constat | Sévérité |
|---|---|---|
| **R-01** | **720 px (EXPERIENCE) ≠ 45 rem (jeton, sous zoom texte) ≠ 48 rem / 768 px (les trois maquettes).** EXPERIENCE présente les deux premières comme identiques (« 720 px, la largeur de lecture définie par `{spacing.thread-max-width}` ») ; elles ne le sont qu'à racine 16 px, c'est-à-dire dans le seul cas que le choix du `rem` visait à dépasser. | **blocage** |
| **R-02** | **Trou entre 720 et 784 px.** Colonne 720 px + `gutter-desktop` × 2 = 784 px. Entre les deux, la disposition « nominale » comprime la colonne sous sa largeur de lecture alors que la disposition « adaptation », avec ses gouttières de 16 px, lui donnerait plus de place. Le point de rupture est posé au mauvais endroit ; et rien ne dit si `thread-max-width` inclut ou exclut les gouttières. | **élevé** |
| **R-03** | **Incohérence DESIGN / EXPERIENCE sur le déclencheur.** DESIGN : « `gutter-mobile` est l'adaptation **sous la largeur de colonne** ». EXPERIENCE : « **sous 720 px** ». Même intention, deux définitions dont une est relative et l'autre absolue. | **moyen** |
| **R-04** | **Le tableau Responsive prescrit une primitive que la spine a retirée.** Dernière ligne : « Frappe au vol et Échap arment le champ ». *Interaction Primitives* : « Elle est **retirée** … contraire à WCAG 2.1.4 ». Un développeur qui implémente le tableau introduit une violation d'accessibilité que le même document documente comme telle. | **blocage** |
| **R-05** | **Les maquettes contredisent la disposition des cartes au-dessus du point de rupture.** DESIGN : « sur une ligne, trois au maximum ». Maquette : `flex-wrap: wrap` avec `flex: 1 1 12rem` — donc renvoi à la ligne autorisé, et deux cartes s'étalent à 50 % chacune. Comportement à une et à deux cartes non spécifié. | **moyen** |
| **R-06** | **Zone sûre du bas d'écran** : exigée, mais `viewport-fit=cover` n'est déclaré dans aucune maquette et aucun jeton ne porte l'inset. Le mécanisme (`env(safe-area-inset-bottom)`) et son interaction avec le clavier virtuel ne sont pas décrits. | **moyen** |
| **R-07** | **Redistribution à 400 %.** « La mise en page bascule sur la disposition sous-720 px » : vrai avec une requête en `px`, faux avec une requête en `em` face à un zoom **texte seul**. La réponse dépend de R-01, et la spine affirme le résultat sans avoir tranché le moyen. | **élevé** |
| **R-08** | **Plages non spécifiées** : tablette 768–1024 px (nominal par défaut, mais la colonne y touche presque les bords), et paysage téléphone à moins de 400 px de haut, où colonne + zone de saisie + clavier virtuel ne tiennent plus. | **moyen** |
| **R-09** | **Hauteur du fil non décidée** : le fil défile-t-il dans un conteneur à hauteur bornée, ou est-ce le document qui défile avec une zone de saisie `sticky` ? Cette question commande la solution de P-07 (non-recouvrement du focus), l'implémentation du défilement conditionnel, et la position de la pastille « nouveau message ». | **élevé** |
| **R-10** | **Ordre de tabulation non borné.** Le fil n'est jamais purgé et tous les boutons des tours passés (hors cartes inertes) restent focalisables. « Elle atteint les cartes par Maj+Tab depuis le champ » suppose que le dernier tour est adjacent au champ ; après vingt tours, Maj+Tab remonte tout l'historique. Non traité. | **élevé** |

---

## 7. Contradictions entre spines et maquettes

**Rappel de la règle affichée : la spine l'emporte.** Elle ne protège pas des maquettes fausses, qui restent la première chose qu'un développeur ouvre.

### 7.1 Contradictions internes aux spines (les plus graves)

| ID | Contradiction | Sévérité |
|---|---|---|
| **X-01** | **Mutation unique contre étapes progressives.** *Accessibility Floor* : « Le message, ses lignes d'étape et ses cartes arrivent ensemble … en une seule mutation. Jamais trois insertions successives. » *Component Patterns* : les étapes « s'empilent **pendant** le travail ». *State Patterns* : « Lignes d'étape **narrées** ». L'addendum tranche dans le sens du flux (« diffusé au fil en temps réel » ; « une orchestration qui prépare une réponse complète avant de la rendre ne peut pas satisfaire cette contrainte »). La règle d'accessibilité entre donc en collision frontale avec la garantie produit la plus structurante. | **blocage** |
| **X-02** | **Frappe au vol : retirée et prescrite** (R-04). | **blocage** |
| **X-03** | **Deux statuts contre quatre**, entre EXPERIENCE et le PRD qu'elle déclare pour source. | **blocage** |
| **X-04** | **La ville est demandée / il n'y a pas de ville à demander** (Q5). | **blocage** |
| **X-05** | **Sarah entre dans le vivier sans compte** (parcours 2, variante) contre FR-3. Le bot y énonce une phrase fausse — dans le produit qui fait de la non-invention sa contrainte n° 1. | **blocage** |
| **X-06** | **« Rien ne sort du fil » et la fenêtre modale bannie**, mais FR-14 impose une page web autonome et OAuth impose de quitter le produit. La seconde figure dans l'IA, la première en est absente : le principe est donc partiel sans le dire. | **élevé** |
| **X-07** | **« Un seul mouvement est admis : l'apparition d'un nouveau message … Rien d'autre n'anime »** (DESIGN, *Elevation & Depth*) contre **la pulsation de l'étape en cours** (DESIGN, *Components*, deux paragraphes plus haut ; EXPERIENCE la confirme et la borne). Deux mouvements. | **élevé** |
| **X-08** | **« `border-decorative` ne porte jamais à lui seul une information »** contre **« La distinction actif / inerte passe par le filet, perceptible sans pointeur »** — qui est exactement `border-decorative`, à 1,72:1 (T-15). | **blocage** |
| **X-09** | **« Aucun composant ne rend un champ obligatoire à l'affichage »** contre l'absence d'état inconnu pour le prénom, le sport, le jour et le niveau (P-14). | **élevé** |
| **X-10** | **« Les étapes ne s'accumulent pas dans le flux d'annonce » contre « les étapes franchies restent visibles ».** Les deux sont tenables, mais seulement par un double rendu (liste visible dans le `log` + région à remplacement) que rien ne décrit et qu'aucune maquette n'implémente. | **élevé** |
| **X-11** | **DESIGN exige un filet réel sur « chaque surface qui compte » sous `forced-colors`**, en citant nommément l'encadré de jouabilité — qui ne porte qu'un filet **gauche**. Défendable, non tranché. | **moyen** |

### 7.2 Maquettes contre spines

| ID | Maquette | Contredit | Sévérité |
|---|---|---|---|
| **X-12** | `<input type="text">` dans les trois maquettes | Zone de saisie « grandit jusqu'à quatre lignes », « Maj+Entrée passe à la ligne » — impossibles sur un `input`. | **élevé** |
| **X-13** | Bouton d'envoi en icône carrée 48×48 | `button-primary` tokenisé en `padding 12/24` + police `label` (donc textuel). Les jetons et les maquettes décrivent deux boutons différents. | **élevé** |
| **X-14** | `border: 1px solid border-decorative` sur le bouton d'envoi désactivé | Aucun jeton ne le prévoit ; la maquette a silencieusement corrigé un défaut du système (T-13). | **moyen** |
| **X-15** | Nantes, « Tennis Club de la Beaujoire », « complexe du Petit-Port » | FR-11 : Lyon et son agglomération exclusivement. | **élevé** |
| **X-16** | « Au-dessus de **32 °C**, l'effort soutenu devient risqué » | FR-10 : ressenti **> 28 °C**. La maquette invente un seuil et le met dans la bouche du bot. | **élevé** |
| **X-17** | Bloc-marque « EX AEQUO » en capitales, présent dans une maquette sur trois | DESIGN : « Pas de capitales forcées ». EXPERIENCE : aucune navigation, aucun en-tête, « le fil est l'application entière ». | **élevé** |
| **X-18** | Phrase d'exemple placée dans la colonne, au-dessus de la zone de saisie | EXPERIENCE : « Un exemple de phrase … **sous le champ** ». | **moyen** |
| **X-19** | Cartes inertes rendues en `<div>` avec `<span class="sr-only">Retenue</span>` **après** le contenu | Spine : le nom accessible est « **préfixé** de son sort ». Et un `<div>` n'a pas de nom accessible du tout : le contrat de relecture au lecteur d'écran n'est pas tenu. | **élevé** |
| **X-20** | Nom accessible réel des cartes actives : « Anna Intermédiaire · mercredi, samedi » | Spine : « Anna, niveau intermédiaire, disponible mercredi et samedi ». Le « · » est annoncé de façon imprévisible et les mots de liaison manquent. | **élevé** |
| **X-21** | `role="status"` sur la liste d'étapes, **imbriqué** dans `role="log"`, avec deux `<li>` accumulés | Régions live imbriquées (double annonce probable) + accumulation explicitement interdite par la spine. | **élevé** |
| **X-22** | `aria-label` posé sur un `<div>` sans rôle (récapitulatif) | La spine exige que cet `aria-label` soit lu et mis à jour à la confirmation ; sans rôle, plusieurs technologies l'ignorent. | **élevé** |
| **X-23** | Récapitulatif portant une troisième ligne « Intermédiaire, à votre niveau » | DESIGN : le récapitulatif porte « le partenaire et le sport en `card-name`, la date, l'heure et le lieu en `meta` ». Le niveau n'y est pas prévu. | **moyen** |
| **X-24** | Encadré de jouabilité à 3 boutons dans un cadre, 2 dans l'autre | Aucune règle sur le nombre ni sur la présence de « Un autre jour ». | **moyen** |
| **X-25** | « C'est dans votre agenda Google. » sans qu'aucun bloc de choix d'agenda ni consentement n'ait été montré | Le parcours impose deux gestes explicites avant l'écriture. La maquette du climax saute les deux moments les plus sensibles du produit en matière de consentement. | **moyen** |
| **X-26** | Textes indicatifs du champ : absent / « Écrivez-moi » / « …ou dites-moi simplement un prénom » | Aucune règle. Trois valeurs pour un même champ, sur trois maquettes. | **faible** |
| **X-27** | Couleurs `#060A12` et `#080E1A` hors palette, dont `#060A12` derrière une étiquette **à l'intérieur** de la zone produit | Palette « délibérément pauvre » ; `surface-base` « le seul fond de la page ». Décor de présentation pour l'essentiel, mais la frontière décor / produit n'est pas marquée. | **faible** |
| **X-28** | **Huit composants n'ont aucune référence visuelle** : bloc de connexion, bloc de choix d'agenda, pastille « nouveau message », carte portant l'écart de niveau, récapitulatif d'alerte différée, ligne d'état hors-ligne, message non envoyé, ligne d'attente de reprise. Les composants les plus risqués du produit sont les non maquettés. | **élevé** |

---

## Récapitulatif des sévérités

| Sévérité | Nombre |
|---|---|
| **Blocage** | 28 |
| **Élevé** | 41 |
| **Moyen** | 20 |
| **Faible** | 6 |
| **Total** | **95 constats** · **18 questions bloquantes** |

Répartition par section : jetons 17 · composants 19 · machine à états 14 · prose 15 · données 13 · responsive 10 · contradictions 28 (dont 11 internes aux spines).

---

## Ce qui, à l'inverse, est prêt à construire

Pour être juste, et parce qu'un architecte doit savoir ce qu'il peut prendre tel quel :

- **La palette est complète, cohérente et sans poids mort.** 22 couleurs, toutes consommées, avec une doctrine d'emploi (une teinte, un métier) qui se transforme directement en règles de revue.
- **Le plancher d'accessibilité est le meilleur artefact du lot.** Le choix `role="log"` contre `aria-live="polite"` est argumenté au bon niveau, le doublage non visuel du geste signature est identifié, et la rétractation motivée de la « frappe au vol » est exemplaire — il est rare qu'un document UX explique *pourquoi* une règle a été retirée.
- **`unknown-value` et la grammaire de l'honnêteté** sont spécifiés de bout en bout : jeton, prose, justification chiffrée du rejet de la variante grise, emploi dans une maquette. Aucune question à poser.
- **Les interdits sont opérationnels.** La liste des composants bannis, les interdits de vocabulaire et le tableau *Do's and Don'ts* se convertissent en règles de revue de code et en tests de non-régression de microcopie.
- **La divergence assumée avec le PRD sur la surface principale** est datée, motivée, signée, et son périmètre de validité est délimité. C'est exactement ainsi qu'un conflit de source doit être traité — et c'est précisément ce traitement qui manque à FR-11, FR-13, FR-14 et FR-15.
