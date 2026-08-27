---
title: Relecture par rubrique — DESIGN.md / EXPERIENCE.md v3
date: 2026-08-27
cible: DESIGN.md v3 (479 l.) · EXPERIENCE.md v3 (503 l.)
sources vérifiées: ../../prds/prd-bmad-2026-08-26/{prd.md, addendum.md, research-niveau.md, research-paysage.md}
méthode: lecture intégrale des deux spines, puis vérification ligne à ligne contre les sources
---

# Relecture par rubrique — la passe du marcheur

Passe de couverture systématique sur les deux spines jumelles en version 3, après la
resynchronisation sur le PRD v2 qui renverse le modèle du niveau (FR-15 retirée, FR-7
retirée, FR-16 nouvelle, FR-3 mono-sport, FR-2 liste ouverte).

## Tableau des verdicts

| # | Axe | Verdict | En une phrase |
|---|---|---|---|
| 1 | **Forme** | **SOLIDE** | Ordre canonique respecté des deux côtés, frontmatter YAML valide et complète, les huit sections d'EXPERIENCE sont là. |
| 2 | **Héritage** | **ADÉQUAT** | Tous les chiffres résistent à la vérification ; deux attributions glissent (les 3,1 points collés au mauvais parcours, « les onze sports » sous une liste ouverte) et une décision fermée en amont reste ouverte ici. |
| 3 | **Jetons** | **ADÉQUAT** | Les 18 références `{}` résolvent toutes, aucun jeton défini n'est orphelin ; mais `level-choice` redéclare `button-quiet` et `surface-overlay` fait trois métiers. |
| 4 | **Parcours** | **ADÉQUAT** | Quatre protagonistes nommés, numérotation continue, un climax chacun, fermeture de l'IA vérifiée — une rupture de chronologie au parcours 1. |
| 5 | **Composants** | **MINCE** | Un composant déclaré « distinct » n'est spécifié nulle part, un autre n'existe que d'un côté, et l'exemple de nom accessible décrit une carte que la v3 a supprimée. |
| 6 | **États** | **ADÉQUAT** | Chargement, vide, erreur, panne, refus et cas limites sont couverts ; deux états promis ailleurs dans le document manquent de la table. |
| 7 | **Boursouflure** | **MINCE** | Un encadré de six lignes recopié **cinq fois** — et devenu faux — plus une vingtaine de rappels de ce que faisaient la v1 et la v2. |
| 8 | **Résidus du renversement** | **MINCE** | Un seul survivant, mais il est normatif et il tombe exactement sur le point que le renversement a supprimé : un niveau affiché sur une carte de partenaire. |

---

## Constats classés par gravité

### CRITIQUE

#### C1 — Un niveau sur une carte de partenaire, dans une règle normative

**Emplacement :** `EXPERIENCE.md:354` (Accessibility Floor › Structure et attribution)

**Le problème.** La règle du nom accessible s'illustre ainsi :

> « si la carte affiche « Anna » et « **Intermédiaire** · mercredi, samedi », le nom
> accessible commence par ces mots-là […] (« Anna, **intermédiaire**, disponible mercredi
> et samedi » n'est acceptable que si les mots visibles s'y retrouvent dans l'ordre) »

C'est exactement l'anatomie que la v3 a démontée. `EXPERIENCE.md:200` écrit **« Elle ne
porte plus le niveau »**, `EXPERIENCE.md:206` fait monter le niveau dans l'intitulé de
groupe, `DESIGN.md:433` écrit **« Le niveau n'y figure plus »**, et le changelog des deux
documents annonce que la carte **perd** le niveau. L'exemple de la ligne 354 n'est ni un
encadré historique ni une mention datée : c'est la seule description concrète du contenu
d'une carte dans toute la section d'accessibilité, celle qu'un développeur recopiera pour
composer son `aria-label`. Il produira une carte à trois valeurs dont une est interdite,
et il aura suivi la spine.

Aggravant : le rappel `EXPERIENCE.md:372` prend soin de dire que « la v2 listait ici
l'*écart de niveau* ; il ne peut plus exister » — la section a donc été relue et corrigée
**dix-huit lignes plus bas** que l'endroit où le résidu survit.

**Correction proposée.** Réécrire l'exemple sur l'anatomie v3 :

> si la carte affiche « Anna » et « mercredi, samedi · 3 jours d'attente », le nom
> accessible commence par ces mots-là (« Anna, disponible mercredi et samedi, 3 jours
> d'attente »). Le niveau n'entre pas dans le nom de la carte : il est porté une fois par
> le nom du `role="group"` qui les contient.

Et ajouter la phrase manquante : ce que contient le nom accessible du **groupe**, puisque
`candidate-group-label` est désormais le seul porteur du niveau.

---

### ÉLEVÉ

#### E1 — Le bloc de récapitulatif d'alerte est déclaré distinct, puis jamais spécifié

**Emplacement :** `EXPERIENCE.md:246` (déclaration), `EXPERIENCE.md:230` et `247`
(usages) — absent de `EXPERIENCE.md:195-217` (Component Patterns) et de
`DESIGN.md:94-274` / `DESIGN.md:430-450`.

**Le problème.** La ligne 246 écrit : « Un bloc dans le fil récapitule l'alerte **avec un
bouton d'annulation** — c'est donc un composant distinct du récapitulatif de rencontre,
qui est non interactif. » Le document désigne donc explicitement un composant, justifie
son existence séparée, et lui donne un contrôle. Puis :

- aucune ligne dans la table **Component Patterns** ;
- aucun jeton dans la frontmatter de DESIGN, aucune puce dans **Components** ;
- `EXPERIENCE.md:247` lui donne « son statut » et `EXPERIENCE.md:230` lui donne une
  **pastille**, alors que la pastille de statut est définie (`EXPERIENCE.md:212`,
  `DESIGN.md:434`) comme portant les **quatre valeurs de FR-13**, qui décrivent une
  *rencontre* et non une alerte. Quel mot porte la pastille d'une alerte active ? d'une
  alerte expirée ? Le produit ne le dit pas ;
- il porte le seul bouton d'annulation du produit, dans un fil où `EXPERIENCE.md:298`
  déclare que **tout contrôle d'un tour résolu devient inerte**. Une alerte vit 60 jours
  et son annulation doit rester cliquable : c'est la seule exception connue à la règle
  d'inertie, et elle n'est écrite nulle part.

**Correction proposée.** Ajouter une ligne `alert-recap` dans Component Patterns et un
jeton dans DESIGN (même coque que `meeting-recap`, plus un `button-quiet`), nommer les
deux valeurs de sa pastille (*active* / *expirée*, `status-badge-neutral` pour la seconde)
et écrire l'exception à l'inertie : un bloc d'alerte reste interactif tant que l'alerte
court, parce qu'il n'appartient à aucun tour.

#### E2 — L'état « étape échouée » est déclaré neuf et requis, puis laissé sans mots

**Emplacement :** `EXPERIENCE.md:199` (Component Patterns › Ligne d'étape)

**Le problème.** Le texte écrit que les lignes d'étape ont « **trois états** : en cours,
franchie, **échouée** — ce dernier est requis par la grammaire de l'honnêteté et
n'existait pas ». Il est bien fondé en amont : `addendum.md:56` exige qu'« une source en
échec remonte comme telle jusqu'à la conversation, sans repli silencieux ». Mais :

- il n'y a **aucune ligne « Étape échouée »** dans la table des State Patterns
  (`EXPERIENCE.md:227-269`) ;
- il n'y a **aucune formulation arrêtée** dans les *Formulations arrêtées*
  (`EXPERIENCE.md:112-142`), qui en comptent pourtant une trentaine, dont *Service externe
  indisponible* — la cause, sans son effet dans la trace narrée ;
- `DESIGN.md:432` décrit la ligne d'étape avec **deux** états seulement (franchie à point
  plein, en cours à pulsation) et ne dit pas à quoi ressemble une étape échouée. La
  palette n'a aucune teinte libre pour elle (`DESIGN.md:307`), ce qui rend la question
  moins évidente qu'elle n'en a l'air.

C'est précisément le cas que `EXPERIENCE.md:110` interdit : « Un état décrit sans être
rédigé est un endroit où le modèle comblera. »

**Correction proposée.** Ajouter une ligne d'état, une formulation (« Je n'ai pas pu
consulter la météo. ») et deux lignes dans `DESIGN.md.Components` : le point de l'étape
échouée n'est ni `accent` ni `status-danger` — l'échec se rend sans couleur
(`DESIGN.md:307`), donc point creux et mot écrit.

#### E3 — Les 3,1 points sont attribués au parcours qui ne les contient pas

**Emplacement :** `EXPERIENCE.md:463` (encadré du parcours 2) ; secondairement
`EXPERIENCE.md:245`

**Le problème.** L'encadré écrit : « En v2, Nadia arrivait ici après *deux*
élargissements, dont un sur le niveau. FR-7 étant retirée […] **ce parcours décrit deux
fois plus de cas qu'avant**. Le PRD assume ces 3,1 points — ils correspondent au droit de
proposer Sarah, débutante, à quelqu'un qui ne l'est pas. C'est le prix de la promesse, et
il se paie **exactement ici**. »

Or `prd.md:383-386` est précis : les 3,1 points « correspondent **tous** à *Pilates
Intermédiaire* ». Et `EXPERIENCE.md:461` fait de Nadia une **avancée**. Sarah étant
débutante, un élargissement au niveau *voisin* ne l'aurait jamais rendue proposable à une
avancée — deux crans les séparent. Le cas de Nadia figurait déjà **en entier** dans les
3,0 % de la v2 : ce parcours ne décrit pas deux fois plus de cas qu'avant, il décrit
exactement les mêmes. Les sept combinaisons nouvellement refusées sont *Pilates
Intermédiaire*, un parcours que la spine n'écrit pas.

« il se paie exactement ici » est donc la seule phrase de l'encadré qui soit fausse au sens
strict — et c'est la chute. Dans un document dont le parcours 2 a pour thèse entière que le
bot ne dit rien de faux, l'endroit est coûteux.

**Correction proposée.** Réécrire l'encadré :

> Le résidu de refus complet est passé de 3,0 % à 6,1 % : **le produit refuse désormais
> deux fois plus de combinaisons**. Les sept nouvelles sont *Pilates Intermédiaire* — le
> droit qu'aurait donné FR-7 de proposer Sarah, débutante, à quelqu'un qui ne l'est pas.
> Le cas de Nadia, lui, était déjà sans issue en v2 : avancée, elle n'aurait pas non plus
> rencontré une débutante par élargissement d'un cran. Ce parcours n'a pas changé ; c'est
> le nombre de personnes qui y arrivent qui a doublé.

#### E4 — Un encadré recopié cinq fois, et devenu faux

**Emplacement :** `DESIGN.md:397`, `DESIGN.md:454`, `EXPERIENCE.md:68`,
`EXPERIENCE.md:223`, `EXPERIENCE.md:288` — cinq occurrences **mot pour mot** du même
paragraphe de six lignes.

**Le problème.** Double.

*Il est faux.* Il annonce « **Les quatre maquettes** sont à jour de la v3 ». Le dossier
`mockups/` en contient **sept** : `key-page-acceptation.html`,
`key-remplacement-sport.html` et `key-vivier-vide.html` s'ajoutent aux quatre citées, et
leurs horodatages (11:06–11:09) sont **postérieurs** aux spines elles-mêmes (09:02). Trois
maquettes existent, dont deux couvrent l'un des composants **nouveaux de la v3**
(`sport-replace`) et la surface hors du fil la moins illustrée (`acceptance-page`), et
aucune n'est référencée nulle part. Le lecteur qui cherche à quoi ressemble le bloc de
remplacement de sport ne trouve aucun lien, alors que le fichier est là.

*Il est cinq fois trop long.* Le paragraphe est un journal de correction de la génération
précédente de maquettes — `border-decorative`, `outline: none`, `<input>` vs `<textarea>`,
`aria-label` sur `<div>`, le lieu nantais. Chacun de ces défauts est **déjà** traité comme
une règle à son endroit propre (`DESIGN.md:409`, `DESIGN.md:442`, `EXPERIENCE.md:197`,
`EXPERIENCE.md:340`). Recopié cinq fois, il occupe plus de place que la section *Shapes*
entière et ne décide rien.

**Correction proposée.** Une seule occurrence, dans DESIGN, réécrite en trois lignes :
l'inventaire à jour des **sept** maquettes, la règle de primauté de la spine, et la règle
« aucun chiffre de seuil météo d'une maquette ne fait autorité ». Aux quatre autres
emplacements, ne garder que le lien vers la maquette. Référencer les trois maquettes
orphelines depuis les sections qu'elles illustrent (`DESIGN.md:439` pour `sport-replace`,
`DESIGN.md:449` et `EXPERIENCE.md:271` pour la page d'acceptation, `EXPERIENCE.md:245`
pour le vivier vide).

---

### MOYEN

#### M1 — Une phrase promise au bot, jamais rédigée : le brouillon perdu

**Emplacement :** `EXPERIENCE.md:197` et `EXPERIENCE.md:365`

Les deux passages promettent la même chose : « ce qui est promis n'est pas qu'il survive
toujours, c'est qu'il ne disparaisse jamais en silence — **s'il est perdu, le bot le
dit** ». Aucune ligne des *Formulations arrêtées* ne dit ce qu'il écrit alors, et il
n'existe aucun état correspondant. C'est un message d'échec, donc soumis aux règles 4 et 5
du ton (`EXPERIENCE.md:100-101`) : il doit dire ce qui n'est pas perdu et ne pas s'ouvrir
sur une excuse. Un modèle laissé seul écrira « Désolé, votre message a été perdu ».

**Correction.** Ajouter à la table : **Brouillon perdu** — « Je n'ai pas retrouvé ce que
vous étiez en train d'écrire. Le reste de la conversation est intact. »

#### M2 — « Les onze sports », sous une liste de sports ouverte

**Emplacement :** `DESIGN.md:357`

« toute teinte supplémentaire introduite pour "distinguer les sports" — **les onze
sports** partagent la même interface. » Or `prd.md:284` : « **La liste des sports est
ouverte.** Les 11 sports des données d'amorçage sont un jeu d'amorçage, pas un catalogue. »
Le nombre onze n'est plus une propriété du produit, seulement de son fichier d'amorçage.
La contradiction est visible à l'intérieur du couple : `EXPERIENCE.md:204` et
`EXPERIENCE.md:233` insistent deux fois sur des libellés génériques « pour un sport fondé
demain », et `DESIGN.md:438` reprend l'argument — pendant que DESIGN continue de les
compter.

**Correction.** « — **tous les sports** partagent la même interface, y compris ceux que le
vivier ne connaît pas encore. » La règle en sort renforcée : c'est précisément parce que la
liste est ouverte qu'aucune teinte ne peut être allouée par sport.

#### M3 — `level-choice` redéclare `button-quiet` au lieu de le référencer

**Emplacement :** `DESIGN.md:243-251` (frontmatter), contre `DESIGN.md:207-215`

Les sept jetons `option*` de `level-choice` reproduisent **valeur pour valeur** le contrat
de `button-quiet` : fond transparent, filet `border-interactive`, survol
`surface-raised-hover` + `border-strong`, rayon `rounded.sm`, `padding {spacing.3}
{spacing.5}`, `minHeight {spacing.target-min}`. Or `DESIGN.md:438` écrit en prose « Trois
`button-quiet` empilés en colonne » — la prose référence, la frontmatter recopie. Un
changement de `button-quiet` laissera silencieusement `level-choice` en arrière, et le seul
composant dont les **libellés** sont contractuels sera le premier à dériver sur ses jetons.

Le traitement est de surcroît **incohérent avec ses jumeaux** : `sport-replace`
(`DESIGN.md:256-264`), `auth-block` et `agenda-choice` composent tous leurs boutons par
référence, sans les redéclarer.

**Correction.** Remplacer les sept jetons `option*` par
`option: '{components.button-quiet}'` et ne garder en propre que ce qui est réellement
spécifique : `optionAlign: left`, `wordFont`, `wordColor`, `factFont`, `factColor`,
`factGap`.

#### M4 — `surface-overlay` fait plusieurs métiers pour une doctrine qui en annonce un

**Emplacement :** `DESIGN.md:403` (doctrine), contre `DESIGN.md:184` (`composer`),
`DESIGN.md:196` (`button-primary.backgroundDisabled`), `DESIGN.md:217-219`
(`status-badge-neutral`), `DESIGN.md:166` (`new-message-pill`)

*Elevation & Depth* définit `surface-overlay` comme une **marche d'élévation** : « la zone
de saisie, **seule surface qui flotte au-dessus du fil qui défile** ». Le jeton sert en
réalité quatre choses : cette marche, le fond de la pastille « nouveau message » (qui
flotte aussi — cohérent), le fond des pastilles de statut *déclinée* / *expirée* (qui ne
flottent pas du tout, elles sont **dans** le récapitulatif), et le fond désactivé du bouton
primaire (qui ne flotte pas davantage). Le troisième usage est le plus gênant : une
pastille neutre posée sur `meeting-recap` porte le fond réservé à la couche du dessus, sur
une surface qui appartient à la couche du dessous.

Le document le sait à moitié — `DESIGN.md:442` note que le fond désactivé du bouton d'envoi
« est identique à celui du conteneur » et compense par un filet — mais ne referme jamais la
doctrine.

**Correction.** Deux voies, l'une suffit. Soit reformuler `DESIGN.md:403` :
« `surface-overlay` est la marche du dessus **et le fond neutre du système** — ce qui
flotte, et ce qui n'a droit à aucune teinte » ; soit introduire un alias `surface-neutral`
de même valeur pour les deux usages non flottants, ce qui coûte un jeton et rend le système
relisible.

#### M5 — Thomas ferme l'onglet, puis le bot lui parle deux fois

**Emplacement :** `EXPERIENCE.md:451-453` (parcours 1, étapes 11 à 13)

L'étape 11, marquée **Climax**, se termine par : « **Thomas ferme l'onglet** avec un
créneau bloqué, un lieu, une heure choisie pour une raison ». L'étape 12 fait pourtant dire
au bot deux phrases nouvelles — le jour gagné et le jour bloqué — et l'étape 13 une
troisième, sur l'entrée au vivier. Or le contenu de l'étape 12 est daté par son propre
titre : « **dit au moment où ça change** », et l'état correspondant (`EXPERIENCE.md:236`)
précise « Écrit **au moment où ça arrive** ». Ces phrases doivent donc précéder la
fermeture de l'onglet, pas la suivre.

Le défaut n'est pas seulement narratif : il déplace le climax. Tel qu'écrit, le beat sommet
du parcours principal est suivi de deux beats de conséquence, ce qui l'affaisse.

**Correction.** Déplacer les phrases des étapes 12 et 13 **avant** la fermeture de l'onglet
— c'est-à-dire faire des étapes 12 et 13 les étapes 11 et 12, et refermer le parcours sur
le climax. La règle « au moment où ça arrive » redevient vraie dans le parcours qui
l'illustre.

#### M6 — Une décision laissée ouverte dont l'amont a déjà fermé une branche

**Emplacement :** `EXPERIENCE.md:72` et `EXPERIENCE.md:342`, contre `addendum.md:57`

La spine pose : « Un tour arrive-t-il en **une mutation unique**, ou se construit-il en flux
pendant que le bot travaille ? L'addendum impose la diffusion temps réel ; le plancher
d'accessibilité impose une annonce unique. » Elle présente les deux voies comme également
disponibles (`EXPERIENCE.md:342` : « Les deux voies satisfont cette règle »).

Mais `addendum.md:57` tranche déjà : « **Une orchestration qui prépare une réponse complète
avant de la rendre ne peut pas satisfaire cette contrainte.** » La branche « mutation
unique » est morte en amont. Ce qui reste ouvert n'est pas *si* le tour se construit en
flux, mais *comment* l'`<article>` reste silencieux pendant qu'il se construit — et la
spine en donne déjà la réponse (`aria-busy="true"`).

Aggravant léger : `EXPERIENCE.md:198` écrit que le message du bot « **arrive en un bloc, pas
en flux** », ce qui se lit comme un arbitrage rendu — même s'il ne porte, à la lettre, que
sur le flux caractère par caractère.

**Correction.** Refermer la décision : la construction en flux est imposée par l'addendum,
l'`<article>` est inséré vide et porte `aria-busy="true"` jusqu'à complétion. Ne laisser
ouvert que le transport (SSE, WebSocket), qui est réellement une question d'architecture.
Et préciser `EXPERIENCE.md:198` : ce qui est interdit est le rendu **caractère par
caractère** du texte, pas la construction progressive du tour.

#### M7 — « Proposition de lieu » n'existe que d'un côté

**Emplacement :** `EXPERIENCE.md:210` (Component Patterns), sans contrepartie dans
`DESIGN.md.Components` ni dans la frontmatter

C'est le seul des vingt et un composants de la table d'EXPERIENCE sans jumeau visuel. Il
porte pourtant une exigence de rendu non triviale : « **Chaque lieu indique s'il est couvert
ou en extérieur** : c'est cet attribut, et lui seul, qui détermine si la jouabilité
s'applique (FR-10). » Cet attribut est la condition d'apparition de l'encadré de jouabilité,
seul composant de santé du produit — et rien ne dit comment il se rend : un mot dans la
phrase ? une ligne `meta` ? une étiquette ?

**Correction.** Soit ajouter la puce à `DESIGN.md.Components` (« Proposition de lieu — deux
lieux au maximum, en prose de `message` ; la nature du lieu, *couvert* ou *en extérieur*,
est un **mot de la phrase**, jamais une étiquette ni une icône »), soit écrire dans
EXPERIENCE que ce composant n'a aucune forme propre parce qu'il est du texte de message —
ce qui est probablement le cas, et mérite d'être dit plutôt que déduit.

#### M8 — « Niveau non interprétable » a ses mots mais pas son état

**Emplacement :** `EXPERIENCE.md:115` (Formulations arrêtées), absent de la table des State
Patterns

La microcopie existe, précise, et porte une règle forte : « Le bot **nomme le mot qu'il n'a
pas su lire** plutôt que de faire comme s'il n'avait rien vu. » Aucune ligne de la table des
états ne la déclenche. Le plus proche, *Niveau pris dans la phrase* (`EXPERIENCE.md:232`),
traite le cas inverse et n'en dit qu'une clause finale (« toute autre formulation ouvre le
bloc ») — sans jamais dire que le mot non lu doit être **cité**.

L'écart compte : c'est la différence entre un bloc qui s'ouvre sèchement et un bloc précédé
d'un accusé de réception. C'est aussi le seul endroit où le produit admet une incompétence
de lecture, ce qui relève de la grammaire de l'honnêteté.

**Correction.** Ajouter une ligne d'état **Niveau non interprétable** entre
`EXPERIENCE.md:232` et `233`, renvoyant à la formulation et portant la règle de citation du
mot.

#### M9 — `border-interactive` sert aussi de séparateur interne, hors doctrine

**Emplacement :** `DESIGN.md:264` (`sport-replace.lossBorderTop`), contre `DESIGN.md:407`

*Elevation & Depth* est catégorique : « `border-interactive` est le **contour de toute
surface qui compte** — carte active, carte inerte, zone de saisie, bouton discret,
récapitulatif, bloc de connexion, bloc de choix d'agenda. » L'énumération est fermée et ne
mentionne aucun filet **intérieur**. `sport-replace` l'emploie pourtant comme trait de
séparation horizontal entre le rappel de perte et les deux boutons — un rôle de division,
pas de délimitation.

Ce n'est pas un défaut de contraste (le jeton tient 4,37:1 sur `surface-raised`,
`DESIGN.md:332`) mais un défaut de doctrine : un jeton dont la définition énumère ses
porteurs acquiert un usage hors liste, et la prochaine relecture ne saura pas s'il est
voulu.

**Correction.** Étendre `DESIGN.md:407` d'une phrase : « Il sert aussi, et c'est son seul
autre emploi, de **filet de séparation à l'intérieur d'un bloc** quand celui-ci contient
deux zones de nature différente — le seul cas est le rappel de perte de `sport-replace`. »

---

### FAIBLE

| # | Emplacement | Problème | Correction |
|---|---|---|---|
| **F1** | `DESIGN.md:419` | *Shapes* attribue `rounded/sm` aux « boutons, encadré de jouabilité » et omet `service-notice`, qui l'emploie pourtant (`DESIGN.md:222`, `DESIGN.md:447`). | Ajouter « ligne d'état de service » à l'énumération. |
| **F2** | `DESIGN.md:90-91` | `message-gap` et `turn-gap` sont définis, décrits en prose (`DESIGN.md:381-382`) comme « ce qui fait le produit », et **câblés dans aucun composant**. Ce sont les deux seuls jetons d'espacement dans ce cas. | Les poser explicitement : une entrée `thread: { messageGap, turnGap }` dans la frontmatter, sans quoi l'aération du produit ne repose que sur de la prose. |
| **F3** | `DESIGN.md:448`, `EXPERIENCE.md:215` | **Message non envoyé** est nommé composant des deux côtés et n'a pas de jeton : il est composé (`message-user` + `label` + `button-quiet`). Légitime, mais indistinguable d'un oubli. | Une incise dans la puce : « composé, sans jeton propre ». |
| **F4** | `EXPERIENCE.md:213`, `271`, `284` | « **Six états terminaux** » (l. 213) : *Invitation ouverte* n'est pas terminal, c'est l'état d'entrée. Et le **conflit de créneaux** (l. 284) est traité en prose sous la table alors qu'il modifie cet état. | Écrire « six états » sans « terminaux », et rattacher le conflit de créneaux comme variante de la première ligne plutôt qu'en note. |
| **F5** | `EXPERIENCE.md:142` | **Entrée au vivier** a trois phrases arrêtées et aucune ligne d'état ; elle n'est déclenchée qu'à l'intérieur de *Vivier vide* (l. 245) alors qu'elle se produit aussi au parcours 1 (l. 453), après une rencontre. | Ajouter une ligne d'état déclenchée par la création de compte (FR-3), qui est le vrai déclencheur. |
| **F6** | `EXPERIENCE.md:260` | **Focus clavier** figure dans la table des *State Patterns* alors que c'est une primitive d'interaction, déjà traitée en `EXPERIENCE.md:361` et `EXPERIENCE.md:260`. La ligne n'ajoute rien et dilue la table. | Supprimer la ligne ; la règle vit déjà deux fois ailleurs. |
| **F7** | `DESIGN.md:438` | « la sur-évaluation que la recherche mesure à **0,5–1,0 point** ». `research-niveau.md:34` dit « 0,5 à 1,0 **au-dessus de leur niveau réel** » sur une échelle Playtomic que la spine ne nomme pas ; l'unité « point » est une inférence. Sur une échelle à **trois** valeurs, « 0,5 à 1,0 point » se lirait comme « un tiers de l'échelle ». | Écrire « 0,5 à 1,0 sur l'échelle Playtomic (0–7) », ou « d'un demi-cran à un cran ». |
| **F8** | `EXPERIENCE.md:200`, `244` vs `242` | Le plafond de trois candidats et l'ordre par délai d'attente sont attribués à FR-6, ce qui est exact (`prd.md:431-439`) — mais FR-6 est *Élargir sur le jour*, et la spine applique la règle aussi à la **correspondance exacte** (l. 242, FR-5), où le PRD ne la pose pas. Extension probablement voulue, jamais dite. | Une clause en l. 242 : « le plafond de trois et l'ordre de FR-6 s'appliquent aussi à la correspondance exacte ». |
| **F9** | plusieurs sections | Argumentaires dupliqués entre les deux spines : l'empilement du bloc de niveau est plaidé **quatre fois** (`DESIGN.md:438`, `DESIGN.md:463`, `EXPERIENCE.md:204`, `EXPERIENCE.md:233`) ; `prefers-contrast: less` est justifié deux fois dans les mêmes termes (`DESIGN.md:309`, `EXPERIENCE.md:376`) ; la promesse sur le brouillon deux fois (`EXPERIENCE.md:197`, `365`). | Dans chaque paire, garder l'argument dans le document propriétaire (DESIGN pour le visuel, EXPERIENCE pour le comportement) et réduire l'autre à un renvoi. |

---

## Notes de couverture — ce qui a été vérifié et tient

Ces points ont été contrôlés et ne produisent **aucun** constat. Ils sont notés pour que la
prochaine passe n'ait pas à les refaire.

- **Ordre canonique de DESIGN** — Brand & Style (282), Colors (292), Typography (359),
  Layout & Spacing (377), Elevation & Depth (399), Shapes (417), Components (428), Do's and
  Don'ts (456). Aucune section manquante, aucune interversion.
- **Frontmatter YAML** — les deux fichiers passent `yaml.safe_load`. DESIGN porte les cinq
  clés exigées (`colors`, `typography`, `rounded`, `spacing`, `components`) et 22
  composants.
- **Les huit sections d'EXPERIENCE** sont présentes : Foundation (24), Information
  Architecture (44), Voice and Tone (76), Component Patterns (191), State Patterns (225),
  Interaction Primitives (290), Accessibility Floor (332), Key Flows (433).
- **Résolution des jetons** — les 16 références `{chemin.du.jeton}` d'EXPERIENCE et les 2
  de DESIGN résolvent toutes dans la frontmatter. Aucune référence morte.
- **Jetons orphelins** — aucun. Les 22 couleurs, 6 rôles typographiques et 4 rayons sont
  tous employés au moins une fois (voir F2 pour le seul cas limite, `message-gap` /
  `turn-gap`, employés en prose et non dans un composant).
- **Ancres internes** — les liens `](#…)` d'EXPERIENCE pointent tous vers un titre
  existant. Aucune ancre cassée.
- **Chiffres du PRD** — vérifiés un par un : 55 % (`prd.md:160`), 127/231 (`prd.md:377`),
  113 et 89 % (`prd.md:377`), 6,1 % et 14/231 (`prd.md:162`), 3,0 % (`prd.md:383`),
  3,1 points (`prd.md:383`), 86 profils (`prd.md:172`), 60 jours, quatre statuts de FR-13,
  SM-C2 abaissée de 5 à 4 tours (`prd.md:893`), SM-C1 retirée avec FR-7 (`prd.md:994`).
  **Tous exacts.** Le 5,2 % périmé est absent des deux corps de texte — il ne survit que
  dans les changelogs de la v2, où il est à sa place.
- **Noms propres** — Playtomic, Anybuddy, MATCHi, Sportpartner (2,7 ★), Ten'Up, UTR, DUPR,
  Elo : tous conformes à `research-paysage.md`. Le verbatim « aucun moyen de parler à un
  vrai humain, toujours renvoyé vers un chatbot » est cité exactement
  (`research-paysage.md:63`). La citation de `research-niveau` §4 item 1
  (`research-niveau.md:65`) est fidèle, y compris « ne jamais proposer débutant /
  intermédiaire / avancé comme saisie ».
- **Nadia / Sarah** — la collision de prénoms est traitée et l'encadré `EXPERIENCE.md:465`
  est juste : le PRD emploie bien Nadia (`prd.md:144`) et Sarah désigne la pratiquante de
  Pilates des données d'amorçage.
- **Numérotation des parcours** — 1, 2, 3, 4, sans trou. Étapes : 1-13, 1-7, 1-4, 1-6, sans
  trou. Un beat **Climax** explicite dans chacun (l. 451, 472, 486, 497).
- **Fermeture de l'IA** — les onze surfaces de la table (l. 48-60) sont toutes traversées :
  fil à froid (P1.1), fil en conversation (P1), fil en reprise (P3.1), moment niveau
  (P2.2), moment remplacement de sport (P3 variante), moment connexion (P1.9), redirection
  OAuth (P1.9), moment agenda (P1.10), récapitulatif (P1.11), courriels sortants (P2.5,
  P4.6), page d'acceptation (P4). L'affirmation de `EXPERIENCE.md:62` est vérifiée.
- **Couverture des états** — chargement (*Chargement à froid*, *Reprise en chargement*,
  *Recherche en cours*, *Attente longue*), vide (*Vivier vide*, *Sport hors vivier*),
  erreur (*Échec d'envoi*), panne (*Service externe indisponible*, *Bot indisponible*,
  *Hors-ligne*), refus (*OAuth annulé*, *OAuth refusé*, *Permission d'agenda refusée*,
  *Refus du niveau*), cas limites (*Plus de trois candidats*, *Hors zone*, *Hors
  périmètre*, *Prévision hors portée*, *Aucun lieu disponible*, *Fil d'un visiteur au
  terme*). **Les six familles sont couvertes.**
- **Résidus du renversement** — recherche active de « niveau adjacent », « écart de
  niveau », « élargissement sur le niveau », « établissement du niveau », « 5,2 »,
  « FR-15 », « FR-7 », « SM-C1 ». **Toutes les occurrences trouvées sauf une sont
  légitimes** : datées et encadrées (`DESIGN.md:369`, `EXPERIENCE.md:74`, `99`, `200`,
  `231`, `233`, `245`, `372`, `427`, `429`, `443`, `463`, plus les changelogs). Aucune
  n'est trompeuse : chacune dit ce qui a changé et pourquoi. Le seul survivant **non daté
  et normatif** est C1.

---

## Ce que cette passe conclut

Les deux spines ont absorbé le renversement avec une rigueur inhabituelle : les chiffres
sont exacts jusqu'à la décimale, les mentions historiques sont datées au lieu d'être
effacées, et la carte de partenaire a été vidée du niveau partout où elle est décrite comme
composant.

Le renversement a été fait **section par section**, et c'est là que se trouvent les vrais
défauts. Le résidu de C1 survit dans la section d'accessibilité — la seule qui décrive le
contenu d'une carte sans être la section des cartes. L'attribution fautive de E3 survit dans
un encadré de parcours — le seul endroit où un chiffre du PRD est **interprété** au lieu
d'être cité. Et E1 et E2 sont deux composants que la v3 a nommés en passant, dans une phrase
de justification, sans redescendre les spécifier.

La boursouflure (E4, F9) est d'une autre nature : elle ne trompe personne sur le produit,
mais elle a déjà commencé à mentir sur les maquettes, ce qui est le mode d'échec habituel du
texte recopié.

**Ordre de traitement recommandé :** C1 d'abord (une ligne, et c'est un défaut
d'implémentation garanti), puis E3 (une ligne, et c'est une phrase fausse dans le parcours
de l'honnêteté), puis E1 et E2 (un composant et un état à écrire), puis E4 (une
déduplication qui rend au dossier ses trois maquettes perdues).
