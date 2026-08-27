---
name: Ex Aequo
description: Chatbot de mise en relation sportive à niveau égal. Web responsive conçu pour le PC, sombre par défaut, bleu-nuit et vert froid. Professionnel sans être froid ; il ne fait jamais semblant.
status: final
updated: 2026-08-27
version: 3
changelog:
  - "v3.5 (2026-08-27) — AUCUN CHANGEMENT DANS CE DOCUMENT. Le numero avance pour tenir le contrat jumeau : un document aval cite les spines par un seul numero, et les laisser diverger ferait designer deux etats differents par la meme reference. La correction de la v3.5 est une phrase de redaction dans EXPERIENCE.md, dont la glose du changement de creneau se lisait a l envers de son mecanisme. La pastille de statut, ses cinq valeurs et le partage de status-badge-neutral sont inchanges depuis la v3.4."
  - "v3.4 (2026-08-27) — Resynchronisation sur prd.md v3. La pastille de statut passe de QUATRE a CINQ valeurs : abandonnee rejoint declinee et expiree sur status-badge-neutral, sans teinte — l ambre et le rose-rouge ont chacun un seul metier, et la doctrine du produit veut que ce soit le mot qui porte. La ligne du jour bloque du recapitulatif de rencontre disparait aussi sur abandonnee, et le comptage de profile-recap suit. Vocabulaire : le glossaire du PRD ayant enfin defini le geste, la validation du creneau cesse d etre employee comme glose de button-primary. AUCUN jeton de couleur, de typographie, d espacement ni d arrondi n est ajoute : le cinquieme statut est assemble a partir de l existant, comme les trois composants de la v3."
  - "v3.3 (2026-08-27) — Contre-verification par la lentille d accessibilite sur la v3.2. Aucun defaut de contraste : les 32 ratios de la v3.2 sont recalcules exacts. Les corrections sont comportementales et vivent dans EXPERIENCE.md ; ce document est touche sur un seul point, le bouton primaire, dont le NOM ACCESSIBLE doit desormais nommer ce qu il retient et non le verbe seul. Le produit exigeait des cartes de partenaires que leur nom contienne le texte visible mot pour mot, et n exigeait rien de son unique controle engageant."
  - "v3.2 (2026-08-27) — Fermeture des questions bloquantes d implementabilite restees ouvertes apres la v3.1. Un composant nouveau : profile-recap, le recapitulatif DE PROFIL, meme coque que meeting-recap et aucun jeton de couleur, typo, espacement ni arrondi ajoute. button-primary recoit son unique instance dans le fil, Retenir ce creneau, et la collision avec le bouton d envoi — que ce document declarait seule instance permanente — est resolue : l envoi est un controle du composeur qui emprunte l accent, il n appartient a aucun tour. La contre-proposition de playability-callout devient un bouton reel au lieu d une ligne de prose, alors qu une regle d inertie la visait. agenda-choice gagne son second geste. candidate-group-label devient un gabarit et non une chaine. La pastille recoit un second libelle : un changement de statut ne produit aucun message et ne peut pas s annoncer comme tel."
  - "v3.1 (2026-08-27) — Passe de relecture et de polissage, ecartee en v1 et v2. Quatre lentilles techniques (rubrique, accessibilite, derive amont, implementabilite) puis deux editoriales (structure, prose). Corriges : le conflit de creneaux de FR-14 qui inversait la decision produit en silence, des jours de partenaires inventes dans le parcours de reference, les 3,1 points attribues au mauvais parcours, la regle d ordre de FR-6 glosee a l envers, le canal courriel du partenaire inscrit absent, une date au mauvais jour de semaine, et le plancher de largeur ecrit a quatre endroits avec deux valeurs. Completes : la definition de tour resolu dont neuf regles dependaient, le bloc de recapitulatif d alerte, l etape echouee, l etat resolu de level-choice, l apparence active du bouton d envoi. Typographie francaise appliquee : 1 339 apostrophes, 452 espaces insecables, 474 chevrons."
  - "v3 (2026-08-27) — Resynchronisation sur prd.md v2, qui renverse le modele du niveau. Trois composants nouveaux : level-choice (le bloc de declaration du niveau, trois choix empiles portant chacun un mot et une ligne de fait), sport-replace (le remplacement mono-sport de FR-3, precede du rappel de ce qui sera perdu) et candidate-group-label (le niveau porte une fois au-dessus des cartes). La carte de partenaire PERD le niveau et l'ecart de niveau — FR-7 retiree, l'appariement est a niveau strictement egal. Le recapitulatif gagne la ligne du jour bloque (FR-16). Aucun jeton de couleur, de typo, d'espacement ni d'arrondi n'est ajoute : les trois composants sont assembles a partir de l'existant."
  - "v2 (2026-08-26) — Resynchronisation sur prd.md reecrit apres la v1 : FR-14 (page d'acceptation du partenaire) ecrite, FR-13 porte a quatre statuts, FR-15 pose comme decision ouverte au lieu d'etre contredit, geographie lyonnaise appliquee, chiffre de 5,2 pct retabli. Microcopie : 21 formulations d'etat et 4 textes sortants rediges. Accessibilite : aria-relevant, roles reels sur les conteneurs nommes, regions live pre-existantes, double rendu des etapes, anneau de focus du champ, mot visible sur la jouabilite et sur les cartes inertes. Encadre de divergence perime supprime."
  - "v1 (2026-08-26) — Redaction initiale."
sources:
  - ../../prds/prd-bmad-2026-08-26/prd.md
  - ../../prds/prd-bmad-2026-08-26/addendum.md
  - ../../prds/prd-bmad-2026-08-26/research-paysage.md
  - ../../prds/prd-bmad-2026-08-26/research-niveau.md
colors:
  surface-base: '#0B1220'
  surface-raised: '#111C2E'
  surface-raised-hover: '#1E314E'
  surface-raised-pressed: '#24395C'
  surface-overlay: '#18263C'
  surface-user: '#1B2C46'
  ink-primary: '#E8EDF5'
  ink-primary-soft: '#D6DEE9'
  ink-secondary: '#94A3B8'
  ink-disabled: '#55677F'
  ink-on-accent: '#04241C'
  accent: '#2DD4A7'
  accent-hover: '#4EE0BA'
  accent-pressed: '#22B48D'
  accent-quiet: '#123A32'
  status-pending: '#E8A33D'
  status-pending-quiet: '#3A2C13'
  status-danger: '#F0637A'
  status-danger-quiet: '#3B1620'
  border-interactive: '#6B82A6'
  border-strong: '#8AA0C4'
  focus-ring: '#7DD3FC'
typography:
  display:
    fontFamily: "'Inter', system-ui, -apple-system, 'Segoe UI', sans-serif"
    fontSize: '1.75rem'
    fontWeight: 600
    lineHeight: '1.2'
    letterSpacing: '-0.02em'
  message:
    fontFamily: "'Inter', system-ui, -apple-system, 'Segoe UI', sans-serif"
    fontSize: '1.0625rem'
    fontWeight: 400
    lineHeight: '1.6'
    letterSpacing: '0'
  card-name:
    fontFamily: "'Inter', system-ui, -apple-system, 'Segoe UI', sans-serif"
    fontSize: '1.0625rem'
    fontWeight: 600
    lineHeight: '1.3'
  meta:
    fontFamily: "'Inter', system-ui, -apple-system, 'Segoe UI', sans-serif"
    fontSize: '0.875rem'
    fontWeight: 400
    lineHeight: '1.45'
  meta-unknown:
    fontFamily: "'Inter', system-ui, -apple-system, 'Segoe UI', sans-serif"
    fontSize: '0.875rem'
    fontWeight: 400
    lineHeight: '1.45'
    fontStyle: italic
  label:
    fontFamily: "'Inter', system-ui, -apple-system, 'Segoe UI', sans-serif"
    fontSize: '0.8125rem'
    fontWeight: 500
    lineHeight: '1.3'
    letterSpacing: '0.02em'
rounded:
  sm: 8px
  md: 12px
  lg: 18px
  full: 9999px
spacing:
  '1': 4px
  '2': 8px
  '3': 12px
  '4': 16px
  '5': 24px
  '6': 32px
  thread-max-width: 45rem
  gutter-desktop: 32px
  breakpoint: 49rem
  gutter-mobile: 16px
  message-gap: 24px
  turn-gap: 32px
  target-min: 48px
  focus-ring-width: 3px
components:
  message-bot:
    background: transparent
    color: '{colors.ink-primary}'
    font: '{typography.message}'
    padding: '0'
  message-user:
    background: '{colors.surface-user}'
    color: '{colors.ink-primary}'
    font: '{typography.message}'
    radius: '{rounded.lg}'
    padding: '{spacing.3} {spacing.4}'
    maxWidth: '80%'
    align: right
  step-line:
    color: '{colors.ink-secondary}'
    font: '{typography.meta}'
    marker: '{colors.accent}'
    padding: '{spacing.1} 0'
  partner-card:
    background: '{colors.surface-raised}'
    backgroundHover: '{colors.surface-raised-hover}'
    backgroundPressed: '{colors.surface-raised-pressed}'
    color: '{colors.ink-primary}'
    font: '{typography.card-name}'
    fontMeta: '{typography.meta}'
    colorMeta: '{colors.ink-secondary}'
    border: '1px solid {colors.border-interactive}'
    borderHover: '1px solid {colors.border-strong}'
    borderSelected: '2px solid {colors.accent}'
    borderPressed: '1px solid {colors.border-strong}'
    borderInert: '1px solid {colors.border-interactive}'
    radius: '{rounded.md}'
    padding: '{spacing.4}'
    gap: '{spacing.2}'
    minHeight: '{spacing.target-min}'
    cursor: pointer
  status-badge-pending:
    background: '{colors.status-pending-quiet}'
    color: '{colors.status-pending}'
    font: '{typography.label}'
    radius: '{rounded.full}'
    padding: '{spacing.1} {spacing.3}'
  status-badge-confirmed:
    background: '{colors.accent-quiet}'
    color: '{colors.accent}'
    font: '{typography.label}'
    radius: '{rounded.full}'
    padding: '{spacing.1} {spacing.3}'
  meeting-recap:
    background: '{colors.surface-raised}'
    border: '1px solid {colors.border-interactive}'
    color: '{colors.ink-primary}'
    font: '{typography.card-name}'
    fontMeta: '{typography.meta}'
    colorMeta: '{colors.ink-secondary}'
    radius: '{rounded.md}'
    padding: '{spacing.4}'
    gap: '{spacing.2}'
  profile-recap:
    background: '{colors.surface-raised}'
    border: '1px solid {colors.border-interactive}'
    color: '{colors.ink-primary}'
    font: '{typography.card-name}'
    fontMeta: '{typography.meta}'
    colorMeta: '{colors.ink-secondary}'
    radius: '{rounded.md}'
    padding: '{spacing.4}'
    gap: '{spacing.2}'
  auth-block:
    background: '{colors.surface-raised}'
    border: '1px solid {colors.border-interactive}'
    radius: '{rounded.md}'
    padding: '{spacing.4}'
    gap: '{spacing.3}'
  agenda-choice:
    background: '{colors.surface-raised}'
    border: '1px solid {colors.border-interactive}'
    radius: '{rounded.md}'
    padding: '{spacing.4}'
    gap: '{spacing.2}'
  new-message-pill:
    background: '{colors.surface-overlay}'
    border: '1px solid {colors.border-interactive}'
    color: '{colors.ink-primary}'
    font: '{typography.label}'
    radius: '{rounded.full}'
    padding: '{spacing.2} {spacing.4}'
    minHeight: '{spacing.target-min}'
  playability-callout:
    background: '{colors.status-danger-quiet}'
    fontLabel: '{typography.label}'
    fontMeta: '{typography.meta}'
    colorMeta: '{colors.ink-secondary}'
    borderLeft: '3px solid {colors.status-danger}'
    color: '{colors.ink-primary}'
    radius: '{rounded.sm}'
    padding: '{spacing.4}'
  composer:
    background: '{colors.surface-overlay}'
    border: '1px solid {colors.border-interactive}'
    borderFocus: '1px solid {colors.border-strong}'
    color: '{colors.ink-primary}'
    colorPlaceholder: '{colors.ink-secondary}'
    font: '{typography.message}'
    radius: '{rounded.lg}'
    padding: '{spacing.3} {spacing.4}'
    minHeight: '{spacing.target-min}'
  button-primary:
    background: '{colors.accent}'
    backgroundHover: '{colors.accent-hover}'
    backgroundPressed: '{colors.accent-pressed}'
    backgroundDisabled: '{colors.surface-overlay}'
    border: '1px solid transparent'
    borderHover: '1px solid {colors.ink-on-accent}'
    borderPressed: '1px solid {colors.ink-on-accent}'
    borderDisabled: '1px solid {colors.border-interactive}'
    color: '{colors.ink-on-accent}'
    colorDisabled: '{colors.ink-disabled}'
    font: '{typography.label}'
    radius: '{rounded.sm}'
    padding: '{spacing.3} {spacing.5}'
    minHeight: '{spacing.target-min}'
  button-quiet:
    background: transparent
    backgroundHover: '{colors.surface-raised-hover}'
    color: '{colors.ink-primary}'
    border: '1px solid {colors.border-interactive}'
    borderHover: '1px solid {colors.border-strong}'
    font: '{typography.label}'
    radius: '{rounded.sm}'
    padding: '{spacing.3} {spacing.5}'
    minHeight: '{spacing.target-min}'
  status-badge-neutral:
    background: '{colors.surface-overlay}'
    color: '{colors.ink-primary}'
    font: '{typography.label}'
    radius: '{rounded.full}'
    padding: '{spacing.1} {spacing.3}'
  service-notice:
    background: '{colors.surface-raised}'
    border: '1px solid {colors.border-interactive}'
    color: '{colors.ink-primary}'
    font: '{typography.meta}'
    radius: '{rounded.sm}'
    padding: '{spacing.3} {spacing.4}'
  acceptance-page:
    background: '{colors.surface-base}'
    color: '{colors.ink-primary}'
    maxWidth: '{spacing.thread-max-width}'
    padding: '{spacing.6} {spacing.4}'
    gap: '{spacing.5}'
  level-choice:
    background: '{colors.surface-raised}'
    border: '1px solid {colors.border-interactive}'
    radius: '{rounded.md}'
    padding: '{spacing.4}'
    gap: '{spacing.3}'
    direction: column
    optionBackground: transparent
    optionBackgroundHover: '{colors.surface-raised-hover}'
    optionBorder: '1px solid {colors.border-interactive}'
    optionBorderHover: '1px solid {colors.border-strong}'
    optionRadius: '{rounded.sm}'
    optionPadding: '{spacing.3} {spacing.5}'
    optionMinHeight: '{spacing.target-min}'
    optionAlign: left
    wordFont: '{typography.card-name}'
    wordColor: '{colors.ink-primary}'
    factFont: '{typography.meta}'
    factColor: '{colors.ink-secondary}'
    factGap: '{spacing.1}'
  sport-replace:
    background: '{colors.surface-raised}'
    border: '1px solid {colors.border-interactive}'
    radius: '{rounded.md}'
    padding: '{spacing.4}'
    gap: '{spacing.4}'
    lossFont: '{typography.meta}'
    lossColor: '{colors.ink-primary}'
    lossBorderTop: '1px solid {colors.border-interactive}'
  candidate-group-label:
    color: '{colors.ink-secondary}'
    font: '{typography.meta}'
    padding: '0 0 {spacing.2} 0'
  unknown-value:
    color: '{colors.ink-secondary}'
    font: '{typography.meta-unknown}'
  focus-indicator:
    outline: '{spacing.focus-ring-width} solid {colors.focus-ring}'
    outlineOffset: '2px'
---

# Ex Aequo — Design Spine

> Identité visuelle. Le comportement, les états et les parcours vivent dans [EXPERIENCE.md](EXPERIENCE.md).
> Cette spine l’emporte sur toute maquette, tout wireframe et tout import en cas de conflit.
> **Entre les deux spines, la règle est différente et symétrique** : chacune fait autorité sur son domaine — ce document sur *à quoi ça ressemble*, `EXPERIENCE.md` sur *comment ça marche*. Un conflit entre elles n’est jamais arbitré par préséance : c’est un **défaut à corriger des deux côtés**, et le signaler vaut mieux que de deviner laquelle avait raison.

## Brand & Style

**Ex Aequo** est un terme de classement sportif : deux concurrents exactement au même niveau. C’est la promesse du produit dite dans la langue du sport, et c’est aussi son unique vantardise — le produit ne prétend pas remplir les terrains, ni animer une communauté, ni vous faire progresser. Il trouve quelqu’un à votre niveau, ou il vous dit franchement qu’il n’y a personne.

Le produit se construit contre deux repoussoirs identifiés par la recherche amont ([research-paysage.md](../../prds/prd-bmad-2026-08-26/research-paysage.md)). Le premier est **la place de marché de réservation** — Playtomic, Anybuddy — qui s’utilise avec des listes, des cartes et des filtres, et dont l’esthétique est celle du catalogue. Le second, plus dangereux, est **le chatbot de support**, que les utilisateurs détestent explicitement (« aucun moyen de parler à un vrai humain, toujours renvoyé vers un chatbot »). Ex Aequo est une conversation, mais il ne doit pas *ressembler* à un widget d’assistance : pas de bulle flottante en bas à droite, pas d’avatar souriant, pas de badge de notification, pas de « Bonjour 👋 comment puis-je vous aider ? ».

La posture visuelle qui en découle : **la nuit calme d’un agenda ouvert tard**. Le PRD situe précisément le moment d’usage — mardi soir, on regarde son agenda, on voit un trou la semaine prochaine. Fond bleu-nuit profond, texte reposant, beaucoup d’air vertical, un seul vert froid qui ne sert qu’à ce qui est acquis. Rien ne clignote, rien ne réclame l’attention, rien ne célèbre.

Sobre sans être austère. Le vouvoiement est tenu partout, y compris dans les libellés d’interface — on parle à quelqu’un qu’on respecte, pas à un utilisateur qu’on anime.

## Colors

La palette est délibérément pauvre. Une seule teinte porte l’interface, une seule porte l’action, deux portent les statuts. Tout le reste est du texte sur du fond.

- **Bleu-nuit (`#0B1220`)** — le canevas. Un bleu suffisamment désaturé pour ne pas fatiguer sur une longue conversation, suffisamment bleu pour ne pas se lire comme du gris. C’est le fond par défaut et le seul fond de la page.
- **Bleu ardoise (`#111C2E`, `#18263C`, `#1B2C46`)** — la profondeur se fait par **tons empilés**, jamais par ombre. `surface-raised` porte les cartes, `surface-overlay` la zone de saisie, `surface-user` les messages de la personne. Trois marches, pas quatre. `surface-raised-hover` et `surface-raised-pressed` sont les deux réponses d’une carte au pointeur et au doigt ; elles ne créent pas de marche supplémentaire dans la hiérarchie.
- **Vert froid (`#2DD4A7`)** — l’unique couleur d’action. Elle signifie **acquis** : le bouton qui engage, la rencontre confirmée, l’étape franchie. Elle ne décore rien, ne souligne rien, ne colore aucun titre. C’est la seule teinte saturée d’une interface par ailleurs monochrome : sur un grand écran où le regard balaie une longue colonne, elle est le seul point d’accroche, et elle ne doit donc jamais désigner autre chose qu’une chose acquise.
- **Ambre (`#E8A33D`)** — **en attente**, et rien d’autre. C’est la couleur du statut le plus important du produit : la rencontre posée dans l’agenda avec un partenaire qui n’a pas répondu, et qui, s’il s’agit d’un profil d’amorçage, ne répondra jamais. L’ambre n’est jamais détourné vers un avertissement générique, ni vers **la ligne du jour bloqué**, ni vers quoi que ce soit d’autre — il a un seul métier. Le jour bloqué est la tentation la plus forte depuis la v3 : il ressemble à un avertissement, il n’en est pas un, et il s’écrit en `meta` / `ink-secondary` comme tout ce qui informe sans alerter.
- **Rose-rouge (`#F0637A`)** — la **jouabilité dangereuse** : chaleur excessive, vent dangereux, alerte de qualité de l’air. Le PRD est explicite, c’est une question de santé et non de confort. Cette couleur ne sert jamais à signaler une erreur de saisie ou une panne réseau.
- **Bleu clair (`#7DD3FC`)** — l’anneau de focus clavier, et uniquement lui. Volontairement pris hors de la famille verte pour qu’un élément focalisé ne se lise jamais comme un élément confirmé. Rendu en `outline` opaque, jamais en ombre translucide.

**Il n’y a pas de gris « sourd » dans ce système, et c’est une décision.** Une première version réservait une encre plus éteinte à ce que le produit ne sait pas — « Lieu non déterminé », « Prévisions indisponibles ». Mesurée, elle plafonnait à 3,1:1 : le produit rendait *illisible* le texte qui porte sa garantie d’honnêteté. Ramenée à un niveau lisible, elle devenait indistinguable de `ink-secondary`. La conclusion est que **l’inconnu ne doit pas être plus discret, il doit être différent** : il s’écrit en `ink-secondary`, à la même lisibilité que tout le reste, et c’est **l’italique et les mots** qui le désignent. Voir `{components.unknown-value}` et [La grammaire de l’honnêteté](EXPERIENCE.md#la-grammaire-de-lhonnêteté). **Les deux formulations citées ci-dessus sont aujourd’hui bannies pour une seconde raison** : « Lieu non déterminé » et « Prévisions indisponibles » sont des participes passés passifs, la langue d’un champ vide dans une base de données et non celle d’un interlocuteur qui admet une ignorance. Le style typographique de l’inconnu ne suffit pas sans son lexique — le produit écrit « je ne sais pas encore ». Ce jumeau lexical vit dans le [Lexique de l’inconnu](EXPERIENCE.md#lexique-de-linconnu).

`ink-disabled` (`#55677F`) subsiste pour un seul usage : le bouton d’envoi lorsqu’il porte l’attribut `disabled` natif — le seul cas exempté des seuils de contraste, parce que le contrôle est réellement inopérant.

**L’échec se rend sans couleur, et c’est une règle.** Le produit a quatre états de panne — envoi, réseau, OAuth, agenda — et **aucune teinte disponible** : le rose-rouge appartient à la seule jouabilité, l’ambre au seul statut *en attente*. Plutôt qu’introduire une cinquième teinte dans une palette délibérément pauvre, l’échec se rend comme l’inconnu : **en encre primaire, avec un filet réel et le mot écrit**, via `{components.service-notice}`. La règle est écrite ici parce que son absence conduisait mécaniquement au rouge — c’est-à-dire à la violation de l’interdit énoncé deux paragraphes plus haut.

**Un palier de contraste réduit existe, et lui seul.** `ink-primary-soft` (`#D6DEE9`, **13,81:1** sur le fond) remplace `ink-primary` pour la prose longue sous `prefers-contrast: less`. Le thème sombre unique à contraste maximal est la configuration qui produit le halo pour les lecteurs astigmates ; aucun critère AA n’est enfreint — un contraste trop élevé n’est jamais une non-conformité — mais **refuser un thème clair est une décision produit défendable, refuser tout recours ne l’est pas**. C’est le seul assouplissement du système, et il reste très au-delà d’AA.

### Cibles de contraste

Ces valeurs sont contractuelles. Tout jeton ou toute composition qui les enfreint est un défaut, pas un arbitrage esthétique.

*Trois paires ont été ajoutées en v3. Elles étaient produites par le système depuis la v1 sans figurer ici : l’encre primaire sur une surface surélevée, et les deux encres sur cette même surface au survol. `level-choice` les rend décisives : c’est le premier composant dont le texte **secondaire** porte du sens (la ligne de fait sous chaque mot) à l’intérieur d’une cible qui se survole. Une ligne de fait illisible au survol viderait l’anatomie de son intérêt.*

| Paire | Ratio | Seuil | Conforme |
|---|---|---|---|
| `ink-primary` / `surface-base` | 15,93:1 | 4,5 | ✅ |
| `ink-primary` / `surface-raised` | 14,53:1 | 4,5 | ✅ |
| `ink-primary` / `surface-raised-hover` | 11,13:1 | 4,5 | ✅ |
| `ink-secondary` / `surface-base` | 7,30:1 | 4,5 | ✅ |
| `ink-secondary` / `surface-raised` | 6,66:1 | 4,5 | ✅ |
| `ink-secondary` / `surface-raised-hover` | 5,10:1 | 4,5 | ✅ |
| `ink-secondary` / `surface-overlay` | 5,93:1 | 4,5 | ✅ |
| `accent` / `surface-base` | 9,88:1 | 4,5 | ✅ |
| `ink-on-accent` / `accent` | 8,70:1 | 4,5 | ✅ |
| `status-pending` / `status-pending-quiet` | 6,28:1 | 4,5 | ✅ |
| `status-danger` / `status-danger-quiet` | 5,12:1 | 4,5 | ✅ |
| `accent` / `accent-quiet` | 6,61:1 | 4,5 | ✅ |
| `border-interactive` / `surface-base` | 4,79:1 | 3 | ✅ |
| `border-interactive` / `surface-raised` | 4,37:1 | 3 | ✅ |
| `border-strong` / `surface-raised-hover` | 4,93:1 | 3 | ✅ |
| `focus-ring` / `surface-base` | 11,23:1 | 3 | ✅ |
| `ink-primary` / `status-danger-quiet` | 13,52:1 | 4,5 | ✅ |
| `border-interactive` / `status-danger-quiet` | 4,06:1 | 3 | ✅ |
| `border-strong` / `status-danger-quiet` | 5,98:1 | 3 | ✅ |
| `focus-ring` / `status-danger-quiet` | 9,53:1 | 3 | ✅ |

**Compositions à surveiller.** Une table qui ne contient que ses succès n’est pas un contrat, c’est un certificat : elle ne peut signaler aucune régression parce qu’elle n’énumère aucun risque. Les compositions ci-dessous sont réellement produites par le système et **n’atteignent pas 3:1** ; chacune est acceptable **uniquement** parce qu’un autre signal porte l’information.

| Composition | Ratio | Pourquoi c’est admis |
|---|---|---|
| `surface-raised` / `surface-base` | 1,10:1 | La carte est identifiée par son filet `border-interactive` (4,37:1), jamais par sa marche tonale |
| `surface-overlay` / `surface-base` | 1,23:1 | Idem, filet `border-interactive` |
| `surface-user` / `surface-base` | 1,33:1 | La bulle de la personne est identifiée par son alignement **et** par l’étiquette de locuteur non visuelle |
| `surface-raised-hover` / `surface-raised` | 1,31:1 | Le survol est porté par `border-strong` (4,93:1) ; le fond ne fait que confirmer |
| `surface-raised-pressed` / `surface-raised` | 1,48:1 | L’appui gagne le même filet `border-strong` que le survol — **sans ce filet, ce serait un défaut**, et c’en était un |
| `accent-hover` / `accent` | 1,15:1 | Le survol du bouton primaire gagne un filet `ink-on-accent` (8,70:1) — **sans lui, la règle *Do’s and Don’ts* du produit était enfreinte par le produit lui-même** |
| `accent-pressed` / `accent` | 1,39:1 | Idem, filet `ink-on-accent` |
| `border-interactive` / `surface-raised-pressed` | 2,96:1 | **Composition aujourd’hui inatteignable** — aucun composant ne pose ce filet sur ce fond : `surface-raised-pressed` n’existe que sur `partner-card`, qui passe simultanément à `border-strong`. Elle est listée ici comme **garde-fou** : ajouter un état pressé à `button-quiet` la rendrait réelle et ferait tomber le filet sous 3:1. Si cet état est ajouté un jour, il prend `border-strong`, comme la carte |
| `accent-quiet` / `surface-base` | 1,50:1 | La pastille porte son mot |
| `status-pending-quiet` / `surface-base` | 1,38:1 | Idem |
| `status-danger-quiet` / `surface-base` | 1,18:1 | L’encadré est identifié par son filet gauche (6,04:1) **et par le mot qu’il porte en tête** |
| `surface-raised-hover` / `status-danger-quiet` | 1,21:1 | Le survol du bouton de contre-proposition, **à l’intérieur** de l’encadré de jouabilité. Le survol y est porté par `border-strong` (5,98:1) comme partout ailleurs ; le fond ne fait que confirmer. **Composition nouvelle en v3.2**, créée le jour où la contre-proposition est devenue un bouton |

*Les quatre dernières lignes de la table sont **nouvelles en v3.2** : elles n’étaient produites par aucun composant tant que la contre-proposition de l’encadré de jouabilité se rendait en prose. En devenant un `button-quiet`, elle a posé pour la première fois du texte, un filet interactif et un anneau de focus sur `status-danger-quiet` — trois compositions qu’aucune ligne ne couvrait.*

**La marge la plus fine du système** est `ink-secondary` sur `surface-raised-pressed` : **4,513:1**, soit 0,013 au-dessus du seuil. C’est la méta d’une carte pendant l’appui tactile. Tout ajustement de l’un des deux jetons la fait basculer sous le seuil sans qu’aucun autre garde-fou ne le signale : les deux valeurs sont gelées.

**Dépendance contractuelle du décalage de focus.** `focus-ring` sur `accent` ne fait que **1,14:1**. L’anneau du bouton primaire n’est conforme que grâce à `outlineOffset: 2px`, qui interpose deux pixels du fond parent entre l’anneau et le vert. Ce décalage n’est pas un détail de rendu : le supprimer ou le mettre à zéro rend l’indicateur de focus invisible sur le seul bouton qui engage.

Aucun texte du produit n’atteint le seuil « grand texte » : `message` est à 17 px régulier, `meta` à 14 px. **Le seuil applicable est 4,5:1 partout**, et 3:1 pour tout contour porteur d’information.

À éviter : les dégradés, le rouge sur autre chose que la jouabilité, les fonds pleins colorés derrière du texte long, et toute teinte supplémentaire introduite pour « distinguer les sports » — les onze sports partagent la même interface.

## Typography

Une seule famille sur toute l’interface. `Inter` est choisie pour sa neutralité et son excellent rendu en petites tailles sur écran, avec repli sur la pile système.
`[ASSUMPTION: aucune police n'a été imposée ; Inter est un choix par défaut sobre et gratuit, à remplacer si une préférence apparaît. Le reste de la spine ne dépend pas de ce choix.]`

Le rôle central est `message` — 1,0625 rem (17 px au défaut navigateur), interligne 1,6. C’est délibérément plus grand que la valeur habituelle d’une interface web : le contenu du produit *est* de la prose, souvent lue tard, à distance de bureau. Un écran de PC est plus éloigné de l’œil qu’un téléphone, ce qui interdit de descendre vers les 15 px usuels des applications de gestion — et le produit n’a de toute façon aucune densité d’information à gagner.

- `display` — l’accroche de la page vide, avant le premier message. Apparaît une seule fois dans la vie du produit.
- `message` — la conversation, dans les deux sens. Le bot et la personne se lisent à la même taille : ni l’un ni l’autre n’est un accessoire.
- `card-name` — le prénom d’un partenaire proposé. Même corps que `message`, en demi-gras.
- `meta` — les jours disponibles, le délai d’attente, les étapes narrées, l’intitulé de groupe des candidats, la ligne de fait sous chaque mot du bloc de niveau, la ligne du jour bloqué. *La v2 listait ici l’écart de niveau ; il n’existe plus, l’appariement étant à niveau strictement égal.*
- `meta-unknown` — `meta` en italique. Le seul marqueur typographique du système, et il ne sert qu’à une chose : signaler une valeur que le produit ne connaît pas.
- `label` — les libellés de boutons et de pastilles de statut.

**Toutes les tailles sont en `rem`**, jamais en pixels : le zoom texte du navigateur et le réglage de taille système doivent tous deux s’appliquer. Pas de capitales forcées, pas de police d’affichage, pas de taille au-dessus de `display`.

Le produit doit rester intact sous les valeurs d’espacement forcées de WCAG 1.4.12 — interligne 1,5×, espacement de lettres 0,12 em, de mots 0,16 em, de paragraphes 2 em. Aucun conteneur de texte n’a de hauteur fixe.

## Layout & Spacing

Échelle : 4 / 8 / 12 / 16 / 24 / 32 px. Trois tokens nommés portent la sensation d’aération, et ce sont eux qui font le produit :

- `message-gap` (24 px) sépare deux messages consécutifs du même interlocuteur.
- `turn-gap` (32 px) sépare un tour de parole du suivant. L’écart est franc et volontairement plus grand que dans une messagerie : il fait respirer, et il marque que chaque tour est une décision, pas une réplique.
- `thread-max-width` (45 rem) borne la largeur de lecture. C’est le token le plus contesté de la spine, et il est tenu : au-delà d’environ 75 caractères par ligne, la prose cesse d’être confortable, et le contenu de ce produit *est* de la prose. Exprimé en `rem`, il suit le zoom texte au lieu de le combattre.

**Une seule colonne, centrée, avec du vide autour — et le vide est le produit.** L’usage principal est le navigateur d’un PC, donc un écran large. La colonne y occupe 45 rem et laisse plusieurs centaines de pixels de bleu-nuit de chaque côté. Ce n’est pas de la place perdue faute de contenu : c’est le choix qui rend la lecture calme, et c’est ce qui distingue visuellement Ex Aequo d’un catalogue de réservation. Il n’y a ni barre latérale, ni panneau de filtres, ni disposition à deux colonnes, à aucune taille d’écran.

Gouttières : `gutter-desktop` (32 px) est le cas nominal ; `gutter-mobile` (16 px) est l’adaptation, où la colonne prend toute la place disponible.

**Le point de rupture est un jeton, et il vit ici.** `breakpoint` (**49 rem**) = `thread-max-width` + deux fois `gutter-desktop`. Il est exprimé en `rem` et la requête média s’écrit en `em`, pour la même raison que la colonne : il doit suivre le zoom texte au lieu de le combattre. Une valeur en pixels aurait figé le basculement à la taille de police par défaut — précisément le cas que le choix du `rem` visait à dépasser. Inclure les gouttières ferme aussi la plage où la colonne se comprimait sous sa largeur de lecture faute de place pour elles. **La largeur minimale supportée n’est pas chiffrée ici** : elle appartient à [EXPERIENCE.md § Responsive & Platform](EXPERIENCE.md#responsive--platform), seul propriétaire de cette valeur. Ce document la chiffrait lui aussi jusqu’à la v3, et les deux valeurs avaient divergé.

Les cartes de partenaires se rangent sur une ligne, **trois au maximum**, dans la colonne — disposition canonique. Sous le point de rupture elles s’empilent verticalement. Jamais de carrousel horizontal, à aucune taille.

La zone de saisie est ancrée au bas de la colonne. Elle **ne doit jamais recouvrir un élément qui vient de recevoir le focus** : le fil se réduit d’autant, et l’élément focalisé reste entièrement visible au-dessus d’elle. Sous le point de rupture, elle respecte en plus la zone sûre du bas d’écran et n’est jamais recouverte par le clavier virtuel.

→ Référence visuelle : [`mockups/key-fil-a-froid.html`](mockups/key-fil-a-froid.html) — la colonne, le vide latéral assumé, la zone de saisie ancrée.

> **Les sept maquettes sont à jour de la v3.2** (2026-08-27), rendues dans le cadre canonique du PC avec l’adaptation téléphone, et **mesurées au navigateur à 320 px sans débordement horizontal**, y compris sous la feuille d’espacement forcé de WCAG 1.4.12. La v3 en a ajouté trois — la déclaration du niveau, la page d’acceptation (seule surface hors du fil, jamais maquettée auparavant) et le remplacement de sport — puis une septième, le vivier vide, après relecture. **La spine l’emporte malgré tout sur la maquette en cas de conflit**, et aucun chiffre de seuil météo d’une maquette ne fait autorité : seul FR-10 le fait.

## Elevation & Depth

**Aucune ombre portée.** Sur un fond bleu-nuit, une ombre ne produit pas de la profondeur mais de la salissure. La hiérarchie se fait entièrement par **tons empilés** et par filets. L’anneau de focus lui-même est un `outline` opaque, pas une ombre translucide — une ombre à 28 % d’opacité ne serait pas un indicateur de focus conforme.

Trois marches et pas davantage : `surface-base` (la page) → `surface-raised` (les cartes, le récapitulatif, les blocs) → `surface-overlay` (la zone de saisie, seule surface qui flotte au-dessus du fil qui défile). Les messages de la personne utilisent `surface-user`, qui n’est pas une quatrième marche mais une teinte de même niveau que `surface-overlay`, légèrement plus chaude, pour se lire comme « vous » plutôt que comme « au-dessus ».

**Un seul filet porteur, et il atteint toujours 3:1.**

`border-interactive` (`#6B82A6`) est le contour de **toute surface qui compte** — carte active, carte inerte, zone de saisie, bouton discret, récapitulatif, bloc de connexion, bloc de choix d’agenda. Il franchit 3:1 sur les cinq fonds où il est réellement posé : 4,79 / 4,37 / 3,89 / 3,59 / 3,35. `border-strong` (`#8AA0C4`) prend le relais au survol, à l’appui et au focus de ce qui est interactif.

> **Un jeton supprimé, et pourquoi.** Le système comptait un second filet, `border-decorative` (`#2C4364`), présenté comme « ne portant jamais à lui seul une information » — puis chargé, vingt-cinq lignes plus loin, de porter l’état *inerte* d’une carte, à **1,70:1**. Il délimitait aussi le récapitulatif, « point de vérité du parcours », à un contraste où il ne se lit pas comme un filet discret mais comme une absence de filet. Le remonter au-dessus de 3:1 l’aurait rendu indistinguable de `border-interactive`, supprimant la distinction qu’il existait pour porter. Le jeton est donc **supprimé**, comme `ink-muted` l’a été avant lui et pour la même raison : quand un jeton ne peut être ni lisible ni distinct, ce n’est pas sa valeur qu’il faut corriger, c’est **le porteur du sens qu’il faut changer**. La distinction actif / inerte est désormais portée par **un mot visible sur la carte**, par la perte du curseur main et par la perte du rôle de bouton — trois signaux qui survivent au contraste forcé, à la basse vision et à l’absence de pointeur, ce qu’aucun filet ne faisait.

La marche tonale d’une carte survolée (1,31:1) est **délibérément insuffisante à elle seule** : le survol est porté par le changement de filet, qui lui atteint 4,93:1. La couleur de fond ne fait que confirmer.

Un seul mouvement est admis : l’apparition d’un nouveau message, en fondu bref accompagné d’une translation verticale de quelques pixels. Rien d’autre n’anime. Pas de rebond, pas de célébration à la confirmation, pas d’animation d’entrée sur les cartes.

**Mode contraste forcé.** Toute la hiérarchie reposant sur des fonds, elle disparaît sous `forced-colors: active`, qui remplace chaque fond par la couleur système. Les composants doivent donc rester lisibles par leurs **contours** seuls : chaque surface qui compte — carte, récapitulatif, bloc de connexion, encadré de jouabilité, zone de saisie — porte un filet réel, jamais un simple changement de fond, et les pastilles de statut portent leur mot.

## Shapes

- `rounded/sm` (8 px) — boutons, encadré de jouabilité.
- `rounded/md` (12 px) — cartes, récapitulatif, blocs. Rayon par défaut.
- `rounded/lg` (18 px) — bulles de message de la personne et zone de saisie. Plus rond que le reste, parce que ce sont les deux seuls endroits où *vous* parlez.
- `rounded/full` — uniquement les pastilles de statut et la pastille « nouveau message ». Aucune surface pleine n’est en pilule.

Les messages du bot **n’ont pas de forme** : pas de bulle, pas de fond, pas de contour. C’est le geste visuel le plus important du produit. Une bulle grise à gauche est la signature exacte du widget de support que la recherche identifie comme détesté ; du texte nu sur le fond de la page se lit comme une lettre, pas comme un ticket.

Ce geste étant purement visuel, il **doit** être doublé d’une attribution de locuteur non visuelle — voir [Accessibility Floor](EXPERIENCE.md#accessibility-floor). Sans elle, la conversation est un mur de texte sans interlocuteur pour un lecteur d’écran.

## Components

- **Message du bot** (`message-bot`) — texte nu sur `surface-base`, aligné à gauche, sans bulle ni avatar ni horodatage. Pleine largeur de la colonne.
- **Message de la personne** (`message-user`) — bulle `surface-user` alignée à droite, `rounded/lg`, largeur maximale 80 % de la colonne.
- **Ligne d’étape** (`step-line`) — une ligne en `meta`, `ink-secondary`, précédée d’un point `accent` de 6 px. Les étapes s’empilent pendant le travail du bot et restent visibles ensuite. Une étape franchie garde son point à pleine opacité — jamais un `accent` délavé, qui tomberait sous le seuil de contraste. **Trois états, et aucun ne repose sur une couleur nouvelle** :
  - *franchie* — encre `ink-secondary`, phrase à l’accompli, point plein ;
  - *en cours* — mêmes valeurs, plus une **pulsation bornée à 5 secondes** et, surtout, **une suspension typographique en fin de phrase** : la pulsation seule ne dit rien à un lecteur d’écran et n’existe pas sous `prefers-reduced-motion`, c’est donc le **texte** qui porte l’état et l’animation qui l’accompagne ;
  - *échouée* — **encre `ink-primary`**, seule ligne d’étape à quitter `ink-secondary`, et une phrase qui dit ce qui n’a pas pu être fait. Pas de teinte : la palette n’en a aucune de libre, le rose-rouge appartient à la seule jouabilité, et la doctrine du produit veut que **l’échec s’écrive en encre primaire, avec un mot**.
- **Carte de partenaire** (`partner-card`) — `surface-raised`, filet `border-interactive`, `rounded/md`. Le prénom en `card-name`, **les jours et le délai d’attente** en `meta`. **Le niveau n’y figure plus** : sous l’égalité stricte il est identique sur les trois cartes, donc il monte dans `candidate-group-label` et la ligne `meta` revient à ce qui les différencie. Toute la carte est la cible, hauteur minimale `target-min`. **Survol** (pointeur) : fond `surface-raised-hover`, filet `border-strong`, curseur main ; rien ne se déplace ni ne se redimensionne. **Pressée** (tactile) : fond `surface-raised-pressed` **et filet `border-strong`** — la marche de fond seule ne fait que 1,48:1, le doigt aurait reçu dix fois moins de signal que le pointeur. **Sélectionnée** : filet `accent` de 2 px. **Inerte** (tour résolu) : garde son filet, perd le curseur main et le rôle de bouton, et **porte son sort écrit en toutes lettres** — *retenue* / *non retenue* — en `meta`. Le mot est le signal ; il survit au contraste forcé et à l’absence de pointeur, ce qu’un changement de filet ne fait pas.
- **Pastille de statut** — `rounded/full`, fond sourd et texte de la même famille. **Cinq valeurs** : *en attente* (`status-badge-pending`, ambre), *confirmée* (`status-badge-confirmed`, vert), *déclinée*, *expirée* et *abandonnée* (`status-badge-neutral`, **sans teinte**). Les trois dernières n’ont pas de couleur parce qu’il n’en reste aucune de disponible — l’ambre et le rose-rouge ont chacun un seul métier — et c’est cohérent avec la doctrine du produit : **c’est le mot qui porte, la couleur ne fait qu’accompagner**. Le mot est toujours écrit : jamais une pastille de couleur seule, jamais une icône seule.
- **Récapitulatif de rencontre** (`meeting-recap`) — `surface-raised`, filet `border-interactive`, `rounded/md`. Non interactif, mais **porte un rôle réel et un nom accessible** : c’est le point de vérité du parcours, il persiste dans le fil et se met à jour sur place. Le partenaire et le sport en `card-name`, la date, l’heure et le lieu en `meta`, la pastille alignée à droite du titre — et **la date du dernier changement de statut**, en `meta`, pour qu’une mutation silencieuse laisse une trace visible. **Depuis la v3, il porte aussi la ligne du jour bloqué** (FR-16), en `meta` / `ink-secondary` : le jour de la rencontre n’est plus proposé aux autres tant qu’elle tient. Cette ligne n’est **pas** un avertissement et ne prend aucune teinte de statut — voir la règle de l’ambre en [Colors](#colors) ; elle disparaît quand le statut passe à *déclinée*, *expirée* ou *abandonnée*. Sous la largeur de colonne, la pastille passe à la ligne sous le titre plutôt que de le comprimer.
- **Récapitulatif de profil** (`profile-recap`) — **jeton pour jeton identique à `meeting-recap`**, et c’est délibéré : les deux blocs disent « voici ce qui est acquis », et rien ne justifierait qu’ils se ressemblent à peu près. Le sport en `card-name`, les jours et le niveau en `meta`, la valeur manquante en `unknown-value`, et **la phrase de coût en `meta` / `ink-secondary`** sous elle. **Aucune pastille de statut** : un profil n’a pas de statut, et emprunter l’une des cinq valeurs de FR-13 ferait mentir le vocabulaire — même raison que pour le bloc de récapitulatif d’alerte. Il naît au refus du niveau et à ce seul moment, persiste, et mute sur place quand le niveau est finalement donné. *Aucun jeton de couleur, de typographie, d’espacement ni d’arrondi n’est ajouté pour lui.*
- **Bloc de connexion** (`auth-block`) — `surface-raised`, filet `border-interactive`, `rounded/md`. Le motif de la demande est écrit **au-dessus du bloc, en prose de message**, jamais à l’intérieur. Deux `button-quiet` côte à côte, Google et Microsoft, puis **« Pourquoi ? », qui est un bouton de divulgation et non un lien** : il déplie sur place la portée exacte de l’accès demandé. Cible en ligne dans du texte, donc tenue à 24 × 24 px sans chevauchement — `target-min` ne s’y applique pas, et prétendre le contraire était une contrainte impraticable autant qu’inutile.
- **Bloc de choix d’agenda** (`agenda-choice`) — même anatomie que le bloc de connexion, filet `border-interactive`. Deux options, Google et Outlook, présentées au même rang : aucune n’est mise en avant. **Le consentement d’écriture est un troisième `button-quiet`, séparé**, qui n’apparaît qu’une fois le fournisseur choisi : deux gestes distincts pour deux décisions distinctes, et rien dans le style ne suggère que le second découle du premier. **Aucun `button-primary`** — écrire dans son propre agenda n’engage que soi.
- **Bloc de déclaration du niveau** (`level-choice`) — même coque que les deux blocs ci-dessus : `surface-raised`, filet `border-interactive`, `rounded/md`, motif en prose **au-dessus et hors du bloc**. Trois `button-quiet` **empilés en colonne**, texte aligné à gauche, chacun portant **le mot en `card-name` puis une ligne de fait en `meta` / `ink-secondary`**. L’empilement est une décision, pas une contrainte de place : trois options alignées se lisent comme une échelle horizontale dont le centre est le défaut, et le centre est exactement là où tombe la sur-évaluation que la recherche mesure à 0,5–1,0 point. **Aucun `button-primary`, aucun préréglé, aucun quatrième bouton** — le refus autorisé par FR-2 s’écrit et ne se clique pas. C’est le seul composant du produit dont les **libellés** sont contractuels au même titre que ses jetons ; ils sont arrêtés en [Voice and Tone](EXPERIENCE.md#voice-and-tone).
- **Bloc de remplacement de sport** (`sport-replace`) — même coque, et **le seul bloc qui contient une zone de lecture seule** : le rappel de ce qui sera perdu — sport, niveau, jours — rendu en `meta` / `ink-primary`, séparé des deux boutons par un filet `border-interactive` horizontal. L’encre est **primaire et non secondaire** sur ce rappel : c’est ce qu’on s’apprête à détruire, il n’a pas à être plus discret que le reste. Deux `button-quiet` de rang strictement égal en dessous. **Aucun `button-primary`** : le produit ne pousse ni vers le remplacement ni vers son refus.
- **Intitulé de groupe des candidats** (`candidate-group-label`) — une ligne en `meta` / `ink-secondary` au-dessus des cartes, portant le niveau **une seule fois** : « Trois intermédiaires, comme vous ». Ce n’est pas un titre décoratif — il nomme le `role="group"` qui contient les cartes, et c’est par lui que la promesse du produit reste énoncée après que la carte a cessé de la répéter. **C’est un gabarit, pas une chaîne**, et **chaque salve porte le sien** : le nombre s’écrit en toutes lettres, le mot du niveau s’accorde au masculin générique, et la ligne ne se répète jamais à l’identique d’un groupe au suivant. Le gabarit est arrêté en [Voice and Tone](EXPERIENCE.md#voice-and-tone) — c’est le second composant de ce document dont les mots sont contractuels au même titre que ses jetons.
- **Encadré de jouabilité** (`playability-callout`) — fond `status-danger-quiet`, filet gauche de 3 px en `status-danger`, texte en encre primaire. Seul composant à filet latéral de toute l’interface. **Sa singularité graphique n’est pas son signal** : elle ne dit rien à un lecteur d’écran et disparaît en contraste forcé. L’encadré porte donc **un mot en tête**, en `label` — « Conditions de jeu — chaleur », « — vent », « — qualité de l’air » — qui nomme aussi le groupe pour les technologies d’assistance. **La contre-proposition est un `button-quiet` réel** sous le constat, et non une ligne de prose : une règle d’inertie du produit la visait nommément alors qu’aucun bouton n’existait pour la porter, et une contre-proposition qu’on ne peut pas prendre d’un geste n’en est pas une. Discret et jamais primaire — l’encadré informe, il n’interdit pas, et il ne pousse pas vers son propre conseil ; le seul `button-primary` du fil arrive après lui, pour la validation. C’est le seul composant qui porte une information de **santé** ; il n’a pas le droit d’être seulement joli.
- **Zone de saisie** (`composer`) — `surface-overlay`, filet `border-interactive`, `rounded/lg`, ancrée en bas, hauteur minimale `target-min`, grandit jusqu’à quatre lignes puis défile. Texte indicatif en `ink-secondary`. **Son anneau de focus est celui de tout le monde** : `outline` opaque de 3 px en `focus-ring`, jamais supprimé, jamais remplacé par un changement de filet — `border-interactive` vers `border-strong` ne fait que 1,47:1, et ce serait le seul contrôle du produit sans indicateur visible alors qu’il est le plus utilisé. **Le bouton d’envoi a deux apparences, et les deux sont contractuelles.** *Désactivé* — tant que le champ est vide : `disabled` natif, encre `ink-disabled`, fond identique au conteneur, **avec un filet `border-interactive`** sans lequel il disparaîtrait dans son état le plus fréquent. *Actif* — dès qu’un caractère est saisi : fond `accent`, glyphe `ink-on-accent` (8,70:1), et l’anneau de focus commun. **Ce n’est pas pour autant une instance de `button-primary`, et la distinction est contractuelle** : le bouton d’envoi appartient au **composeur**, pas à un tour de parole. Il en emprunte le remplissage `accent` parce que l’envoi est l’action attendue du champ, mais il n’a ni le cycle de vie ni le rang d’un bouton primaire — il ne devient jamais inerte, aucun tour ne le résout, et il est actif en permanence. La règle « un seul bouton primaire actif à la fois » porte sur ce qui vit **dans le fil**, où la seule instance du produit est *« Retenir ce créneau »*. *Ce document écrivait que l’envoi était « la seule instance de `button-primary` » : c’était vrai tant qu’aucune autre n’était placée, mais cela rendait la règle d’unicité invérifiable — permanente d’un côté, exclusive de l’autre.* *L’apparence active manquait à ce document : le second contrôle le plus utilisé du produit n’avait ni contraste ni anneau contractuels.*
- **Pastille « nouveau message »** (`new-message-pill`) — `rounded/full`, `surface-overlay`, filet `border-interactive`, ancrée au-dessus de la zone de saisie. Apparaît quand **le fil change** alors que la personne a remonté : un message qui arrive, **et aussi une rencontre qui change de statut**, laquelle ne produit par règle aucun message et serait donc autrement le seul événement attendu et invisible. Elle **ne disparaît jamais d’elle-même** : elle s’efface uniquement quand le fil revient en bas. **Elle a deux libellés, un par nature d’événement** — le compteur ne compte que des messages, et un changement de statut s’annonce par son nom ; ils sont arrêtés en [Voice and Tone](EXPERIENCE.md#voice-and-tone). *Ce document écrivait « quand un message arrive », ce qui contredisait [Component Patterns](EXPERIENCE.md#component-patterns) et perdait le cas qui justifie la pastille. Le déclencheur a été corrigé en v3.1 ; le libellé, resté au singulier « 1 nouveau message », mentait encore sur une confirmation — corrigé en v3.2.*
- **Bouton primaire** (`button-primary`) — fond `accent`, texte `ink-on-accent`. Réservé aux actions qui engagent, et **le produit n’en place qu’une seule dans tout le fil** : *« Retenir ce créneau »*, seul geste qui engage **quelqu’un d’autre**. Tous les autres blocs le refusent — `level-choice`, `sport-replace` et `acceptance-page` posent des choix de rang égal, `auth-block` et `agenda-choice` des gestes qui n’engagent que la personne elle-même. **Survol et appui gagnent un filet `ink-on-accent`** : leurs fonds respectifs ne se distinguent du repos que de 1,15:1 et 1,39:1, ce qui enfreignait la règle que ce même document impose aux cartes. Désactivé : `surface-overlay` + `ink-disabled` + filet. Un seul bouton primaire **actif** à la fois dans le fil ; ceux des tours résolus deviennent inertes avec leur tour. **Le bouton d’envoi du composeur n’entre pas dans ce compte** — voir la règle juste au-dessus, à `composer`. *Jusqu’à la v3.1, ce composant était le plus finement spécifié du document et n’était placé nulle part : une règle globale portait sur un composant sans emploi.*
- **Bouton discret** — filet `border-interactive`, fond transparent, survol `surface-raised-hover` + `border-strong`. Tout le reste.
- **Valeur inconnue** — `ink-secondary` en `meta-unknown` (italique). Employé partout où le produit ne sait pas : une ville, un lieu, une prévision hors portée. Ce n’est pas un état d’erreur, c’est une valeur légitime, à la même lisibilité que toute autre.
- **Ligne d’état de service** (`service-notice`) — `surface-raised`, filet `border-interactive`, `rounded/sm`, ancrée sous le fil. **Sans couleur de statut** : encre primaire et mot écrit. Porte le hors-ligne et l’indisponibilité du bot. Voir la règle sur l’échec en [Colors](#colors).
- **Message non envoyé** — le message garde sa bulle `surface-user` et sa pleine lisibilité, précédé du mot « Non envoyé » en `label`, suivi d’un `button-quiet` « Renvoyer ». Jamais grisé au point de devenir illisible, jamais signalé par la seule couleur.
- **Page d’acceptation du partenaire** (`acceptance-page`) — la seule surface hors du fil. Même fond, mêmes jetons, même sobriété : une colonne bornée à `thread-max-width`, centrée, sans en-tête, sans navigation, sans pied de page. La demande en `message`, les deux réponses en `button-quiet` **de rang strictement égal** — ni couleur, ni taille, ni ordre qui privilégie l’acceptation — et la sortie du vivier en `button-quiet` plus bas, parfaitement lisible. Aucun `button-primary` sur cette page : rien n’y est poussé.
- **Indicateur de focus** (`focus-indicator`) — `outline` opaque de 3 px en `focus-ring`, décalé de 2 px. Jamais supprimé, jamais rendu en ombre translucide, identique sur tous les composants. **Le décalage de 2 px est contractuel** : sur le bouton primaire, il est la seule raison pour laquelle l’anneau reste conforme.

→ **Références visuelles**

- [`key-declaration-niveau.html`](mockups/key-declaration-niveau.html) — `level-choice` dans ses trois états, et `profile-recap` portant le niveau inconnu
- [`key-proposition-partenaires.html`](mockups/key-proposition-partenaires.html) — `partner-card` dans ses états, `candidate-group-label`, message sans bulle, lignes d’étape
- [`key-recap-en-attente.html`](mockups/key-recap-en-attente.html) — `playability-callout`, `meeting-recap` avec la ligne du jour bloqué, pastilles de statut, `unknown-value`
- [`key-remplacement-sport.html`](mockups/key-remplacement-sport.html) — `sport-replace` et sa zone de lecture seule
- [`key-page-acceptation.html`](mockups/key-page-acceptation.html) — `acceptance-page`, six états, deux `button-quiet` de rang égal, aucun `button-primary`
- [`key-vivier-vide.html`](mockups/key-vivier-vide.html) — le bloc de récapitulatif d’alerte
- [`key-fil-a-froid.html`](mockups/key-fil-a-froid.html) — `composer`, la colonne, le vide latéral

> **Statut des maquettes** — voir [Layout & Spacing](#layout--spacing), où il est posé une seule fois.

## Do’s and Don’ts

| À faire | À éviter |
|---|---|
| Texte nu pour le bot, bulle uniquement pour la personne — **doublé** d’une attribution de locuteur non visuelle | Bulle grise à gauche + avatar : la signature du widget de support |
| Le vert froid uniquement sur ce qui est acquis | Le vert comme couleur de marque répandue sur les titres et les icônes |
| L’ambre réservé à *en attente* | L’ambre recyclé en avertissement générique ou sur la ligne du jour bloqué |
| Trois choix de niveau **empilés**, chacun ancré dans un fait | Trois choix alignés : l’œil y lit une échelle dont le centre est le défaut |
| Écrire le mot du statut à côté de la couleur | Une pastille colorée seule, une icône seule |
| Profondeur par tons empilés et filets réels | Ombres portées, y compris pour l’anneau de focus |
| Un contour à 3:1 sur tout ce qui se clique | Un filet « au contraste le plus faible perceptible » sur un contrôle |
| Le survol porté par le filet | Le survol porté par un fond à 1,3:1 |
| Une colonne de 45 rem centrée, le vide autour assumé | Remplir la largeur du PC avec un panneau, une grille ou une carte |
| L’italique et les mots pour dire l’inconnu | Un gris plus sombre pour dire l’inconnu |
| Des tailles en `rem` et aucune hauteur fixe | Des px figés qui résistent au zoom et à l’espacement forcé |
| Un seul fondu bref à l’arrivée d’un message | Animation de célébration à la confirmation |
| Vouvoiement jusque dans les libellés de boutons | Emoji d’accueil, ton animateur, point d’exclamation |
| Le mot écrit sur une carte résolue | Un filet plus discret pour dire qu’une carte est close |
| Un filet d’état sur le bouton primaire au survol et à l’appui | Un survol de bouton porté par un fond à 1,15:1 — la règle vaut aussi pour les boutons |
| Un mot en tête de l’encadré de jouabilité | Une singularité graphique tenue pour un signal |
| L’anneau de focus sur la zone de saisie comme partout ailleurs | `outline: none` sur le contrôle le plus utilisé du produit |
| L’échec en encre primaire, filet réel et mot écrit | Une cinquième teinte introduite pour dire la panne |
| Une table de contraste qui liste ce qui échoue | Une table qui ne certifie que ses succès |
| Un point de rupture en `rem`, nommé une seule fois | Trois valeurs de point de rupture selon l’artefact qu’on ouvre |
