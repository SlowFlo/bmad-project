# Rapport de validation — Ex Aequo

- **DESIGN.md :** `documentation/planning-artifacts/ux-designs/ux-bmad-2026-08-26/DESIGN.md`
- **EXPERIENCE.md :** `documentation/planning-artifacts/ux-designs/ux-bmad-2026-08-26/EXPERIENCE.md`
- **Exécuté le :** 2026-08-26T19:05:20Z
- **Lentilles :** marcheur de rubrique · accessibilité (passe 2) · dérive amont · implémentabilité aval · voix & microcopie

---

## Verdict d'ensemble

Sur ses qualités propres, cette paire de spines est au-dessus de la moyenne, et il faut le dire d'emblée : la forme est irréprochable (ordre canonique tenu, huit sections obligatoires présentes, deux sections conditionnelles correctement déclenchées), **les 49 références de jetons se résolvent toutes**, aucun jeton couleur n'est sans hexadécimal, et **les treize ratios de contraste annoncés sont exacts au centième** — recalculés indépendamment par deux relecteurs. La palette n'a aucun poids mort. Le plancher d'accessibilité, `unknown-value` et la grammaire de l'honnêteté sont prêts à coder tels quels.

Le problème n'est pas la qualité de rédaction : **la paire décrit un produit qui n'est plus celui de ses sources.** Les deux spines sont figées à 16 h 46 ; `prd.md` a été réécrit à 20 h 33 le même jour et est passé en `final` sans journal de modifications, en gardant la même date `updated`. Cette réécriture a ajouté deux exigences neuves (FR-14, FR-15), verrouillé la géographie sur Lyon, porté FR-13 à quatre statuts, corrigé le chiffre de 55 % et **renversé le sens de deux entrées du glossaire**. Aucune de ces décisions n'est présente dans les spines ; quatre sont activement contredites. Les quatre divergences que les spines traçaient honnêtement — dont l'encadré « Divergence assumée » de *Foundation* — pointent toutes vers du texte de PRD déjà corrigé : ce ne sont plus des arbitrages, ce sont des accusations périmées qui discréditent la source.

Trois relecteurs indépendants convergent sur un second registre de défauts, celui-là interne : **trois des correctifs d'accessibilité les plus lourds de la passe 1 reposent sur des prémisses ARIA fausses et ne produisent aucun effet** (`role="log"` n'implique pas `aria-relevant="additions"` ; `aria-label` est prohibé sur un `<div>` sans rôle). Deux des trois mécanismes d'annonce du produit sont des non-opérations, et la table de contraste, présentée comme contractuelle, **ne liste que des paires conformes** — toutes celles que le système produit et qui échouent en sont absentes.

**Verdict global : la paire n'est pas « à refaire », elle est à resynchroniser puis à recâbler.** La structure d'accueil existe pour presque tout ce qui manque.

---

## Verdicts par catégorie

| Catégorie | Verdict |
|---|---|
| 1. Couverture des parcours | **mince** |
| 2. Complétude des jetons | adéquat |
| 3. Couverture des composants | **mince** |
| 4. Couverture des états | **mince** |
| 5. Couverture des références visuelles | adéquat |
| 6. Boursouflure et sur-spécification | adéquat |
| 7. Discipline d'héritage | **cassé** |
| 8. Conformité de forme | **solide** |

### Volumétrie par lentille

| Lentille | Total | Détail |
|---|---|---|
| Marcheur de rubrique | 41 | 7 critiques · 14 élevés · 14 moyens · 6 faibles |
| Accessibilité (passe 2) | 31 | 5 critiques · 8 élevés · 12 moyens · 6 faibles (+ 23 correctifs contre-vérifiés) |
| Dérive amont | 18 + 18 | 18 contradictions dont 14 silencieuses · 18 exigences orphelines · 11 items de dette amont |
| Implémentabilité aval | 95 | 28 blocages · 41 élevés · 20 moyens · 6 faibles · 18 questions bloquantes |
| Voix & microcopie | 28 | 8 élevés · 14 moyens · 6 faibles |

---

## Convergence des lentilles

Les cinq relecteurs ont travaillé en aveugle les uns des autres. Ne sont listés ici que les points sur lesquels **trois lentilles ou plus** ont buté indépendamment — c'est le meilleur indicateur de ce qu'il faut traiter en premier, et l'ordre ci-dessous est l'ordre de traitement recommandé.

| # | Point | Lentilles | Sévérité |
|---|---|---|---|
| 1 | **FR-13 — deux statuts au lieu de quatre.** *Déclinée* et *expirée* n'ont ni état, ni jeton, ni mot. Faute de statut *déclinée*, le produit présente un refus comme une absence de réponse — ce que le PRD interdit explicitement. | 4/5 | blocage |
| 2 | **FR-14 — la page d'acceptation du partenaire n'existe pas.** Surface entière du périmètre MVP, au moins six états, zéro ligne d'UX. Pire qu'un oubli : *Foundation* l'exclut par principe. | 4/5 | blocage |
| 3 | **FR-15 — l'établissement du niveau est absent et contredit.** La spine écrit « le niveau se déclare dans la phrase », rétablissant l'auto-déclaration que `research-niveau.md` §4.1 condamne : elle croit rejeter Playtomic et rejette la parade. | 4/5 | blocage |
| 4 | **La ville est demandée / il n'y a pas de ville à demander.** Le PRD verrouille sur Lyon et supprime la question ; les spines spécifient un état *Ville inconnue* bloquant ; les maquettes montrent Nantes. Trois réponses. | 4/5 | blocage |
| 5 | **La « frappe au vol » retirée survit dans *Responsive & Platform*.** `EXPERIENCE.md:240` la prescrit encore comme comportement nominal PC. Correctif WCAG 2.1.4 appliqué d'un côté du fichier, laissé ouvert de l'autre. | 4/5 | blocage |
| 6 | **Les profils d'amorçage : prémisse renversée en amont, conséquence fausse en aval.** Le PRD §4 dit qu'ils *peuvent* accepter via le lien SMS ; les spines les disent « incapables de répondre » et en tirent « la personne le sait » — alors qu'aucune phrase ne le lui dit. | 3/5 | critique |
| 7 | **Le point de rupture vaut 720 px, 45 rem ou 48 rem selon l'artefact.** Les deux premiers ne coïncident qu'à racine 16 px — le seul cas que le choix du `rem` visait à dépasser. Plus un trou non couvert entre 720 et 784 px. | 3/5 | blocage |
| 8 | **Les 55 % dimensionnent le mauvais parcours.** C'est le taux d'échec de la recherche *exacte* ; le refus total réel est de 5,2 %. Un découpage en stories priorisera le refus au-dessus de l'élargissement. | 3/5 | critique |
| 9 | **Aucune couleur autorisée pour signaler un échec.** Rose-rouge verrouillé sur la jouabilité, ambre sur *en attente*. Quatre états de panne exigent une identification en texte. Un développeur retombera sur du rouge — la violation explicite de la règle. | 3/5 | blocage |
| 10 | **`border-decorative` porte un état à 1,70:1.** Seul porteur de la distinction carte active/inerte, exigée « perceptible sans pointeur », alors que `DESIGN.md:309` promet 25 lignes plus haut qu'il « ne porte jamais à lui seul une information ». | 3/5 | blocage |
| 11 | **La maquette invente un seuil de 32 °C** quand FR-10 fixe 28 °C. Aucune spine n'énonce de seuil : la règle « la spine l'emporte » ne sauve pas ce cas. | 4/5 | élevé |
| 12 | **« Sarah » est le prénom d'un profil du vivier.** Le PRD avait renommé UJ-2 en « Nadia » précisément pour éviter cette collision. La spine fait de surcroît dire au bot une phrase fausse selon FR-8. | 3/5 | élevé |

---

## Constats par sévérité

### Blocages et critiques (22)

**[Implémentabilité] Le contrat de rendu d'un tour de parole est auto-contradictoire** (EXPERIENCE.md · Accessibility Floor vs Component Patterns)
*Accessibility Floor* : « le message, ses lignes d'étape et ses cartes arrivent ensemble… en une seule mutation. Jamais trois insertions successives. » *Component Patterns* : les étapes « s'empilent pendant le travail ». L'addendum tranche dans le sens du flux : « une orchestration qui prépare une réponse complète avant de la rendre ne peut pas satisfaire cette contrainte ». C'est la première décision d'architecture front à prendre, et les deux règles qui la gouvernent s'excluent.
*Correctif :* trancher pour le flux, et résoudre l'accessibilité par le double rendu que deux relecteurs recommandent — liste visible persistante dans le `log` + nœud satellite `role="status" aria-atomic="true"` à remplacement.

**[Rubric · Dérive · Implémentabilité · Voix] FR-13 est verrouillé sur deux statuts quand le PRD en définit quatre** (EXPERIENCE.md · Component Patterns, State Patterns ; DESIGN.md · Components)
FR-13 fait des quatre statuts une machine à états dont dépend ce que le bot a le droit de dire : « un refus produit le statut *déclinée* et jamais *en attente* : le bot ne présente jamais un refus comme une absence de réponse ». Faute de statut *déclinée*, la spine n'a pas d'autre choix que de le faire — la grammaire de l'honnêteté est cassée là où elle coûte le plus. Ni jeton, ni couleur disponible, ni mot. La bascule vers *expirée* est déclenchée par le temps : le seul déclencheur non conversationnel du produit, et il n'existe pas.
*Correctif :* quatre valeurs de pastille, deux états, deux jetons dans une teinte neutre, et les deux phrases — « Anna a décliné. Mercredi 19 h est libre : je peux chercher quelqu'un d'autre. » / « Mercredi est passé et Anna n'a pas répondu. Je laisse la rencontre dans le fil, pour mémoire. »

**[Rubric · Dérive · Implémentabilité · Voix] FR-14 : la page d'acceptation du partenaire n'existe nulle part** (EXPERIENCE.md · Foundation, Information Architecture)
Le PRD §9 et FR-14 posent une page hors conversation à jeton unique, avec quatre états terminaux et une règle de conflit de chevauchement ; l'addendum la nomme « seule surface du produit qui vit en dehors du fil ». *Foundation* pose au contraire « un composant qui ne peut pas vivre dans le fil ne fait pas partie du produit ». C'est un conflit d'architecture, pas un trou à combler. Le texte de sollicitation — seul contact qu'un profil d'amorçage aura jamais avec le produit — n'est pas écrit non plus.
*Correctif :* un quatrième parcours côté partenaire, une ligne de surface dans l'IA, et reformuler *Foundation* en « le fil est l'application entière **du côté demandeur** ».

**[Rubric · Dérive · Implémentabilité] FR-15 est absent, et la spine rejette la parade en croyant rejeter le repoussoir** (EXPERIENCE.md · Inspiration & Anti-patterns, State Patterns, parcours 1 étape 2)
FR-15 pose que « le bot ne demande jamais *quel est votre niveau* » et qu'un libellé auto-attribué « n'est ni contredit ni retenu tel quel ». Trois passages prescrivent l'inverse. Le plus grave : « ici le niveau **se déclare dans la phrase** » rejette explicitement le mécanisme que `research-niveau.md` §4.1 prescrit — « amorcer par un questionnaire comportemental, pas une auto-étiquette ; ne jamais proposer débutant/intermédiaire/avancé comme saisie ». **La spine croit rejeter Playtomic et rejette la parade.** Seule infidélité à la recherche qui change ce que le produit *fait*, et elle touche la promesse centrale.
*Correctif :* réécrire *Demande incomplète* (sport et jours seulement), ajouter un état **Établissement du niveau** (au plus deux questions factuelles, jamais de verdict récité), corriger la puce d'*Inspiration*, insérer le beat manquant au parcours 1.

**[Rubric · Dérive · Implémentabilité] L'état « Ville inconnue » est interdit, et l'état que FR-2 exige est absent** (EXPERIENCE.md · State Patterns, Component Patterns, parcours 1 étape 6)
Le PRD §5.4 : « Le produit ne desservant qu'une agglomération, il n'y a pas de ville à demander », question fermée. Symétriquement, FR-2 exige qu'« une demande visant explicitement une autre ville que Lyon reçoive une réponse explicite » : cet état n'existe pas. La paire spécifie un tour à supprimer et omet celui à construire. « Lyon », « secteur » et « arrondissement » : zéro occurrence dans les deux spines.
*Correctif :* supprimer *Ville inconnue*, ajouter un état **Hors zone** sur le modèle de *Sport hors vivier*, et substituer le secteur/arrondissement facultatif de FR-11.

**[Rubric · Dérive] Une section entière est bâtie sur une prémisse que la source a renversée** (EXPERIENCE.md · Les deux populations du vivier, State Patterns)
La spine : « 86 profils d'amorçage — un téléphone et rien d'autre, **incapables de répondre** ». Le PRD §4 désormais : « Ce qui sépare les deux populations **n'est pas la capacité de répondre** — c'est le canal et l'initiative… il peut accepter en suivant le lien (FR-14). » Le memlog du PRD journalise le renversement. La conséquence est portée jusque dans *State Patterns* : un consommateur écrirait une interface qui ment dans le sens inverse de celui qu'elle prétend éviter.
*Correctif :* réécrire la section sur l'axe canal/initiative et corriger la ligne *Rencontre en attente*.

**[Rubric · Dérive] L'encadré « Divergence assumée » est devenu un faux avertissement qui discrédite la source** (EXPERIENCE.md · Foundation)
Il affirme que « le PRD §6 énonce l'inverse » ; le PRD §6 dit maintenant exactement ce que la spine dit. L'encadré est dans la section que tout consommateur lit en premier : un lecteur prudent conclura que le PRD n'est pas fiable et cessera d'y retourner. Même sort pour les deux `[ASSUMPTION]` — canal d'alerte (tranché : e-mail) et SMS aux 86 profils (fermé par « oui ») — dont l'une renvoie à une « question 6 » qui n'existe pas.
*Correctif :* supprimer l'encadré et les deux hypothèses ; poser l'e-mail comme acquis et faire aller le parcours 2 jusqu'à la réception.

**[Rubric] Le parcours 2 est dimensionné à dix fois sa taille réelle** (EXPERIENCE.md · Key Flows, parcours 2)
« Ce parcours couvre 55 % des recherches : c'est un chemin nominal, pas un traitement d'erreur. » Le PRD dit l'inverse : les 55 % sont le taux d'échec de la recherche *exacte*, donc le domaine de UJ-1 et de son élargissement ; le vrai « personne, point » est de 12 combinaisons sur 231, soit 5,2 %. Un découpage en stories priorisera le refus au-dessus de l'élargissement.
*Correctif :* remplacer par « 5,2 % des combinaisons, toutes du Pilates », et déplacer « chemin nominal » vers l'état *Élargissement sur le jour*.

**[Accessibilité] `role="log"` sans `aria-relevant` : le correctif n°1 de la passe 1 est sans effet** (EXPERIENCE.md:189-190 ; maquettes 2 et 3) — [WCAG 4.1.3, AA]
La spine énonce comme un fait que « `role="log"` n'annonce que les ajouts ». C'est faux : en ARIA 1.2, ce rôle porte pour seule valeur implicite `aria-live="polite"` ; `aria-relevant` conserve son défaut `additions text`. La pastille passant de « En attente » à « Confirmée » est donc toujours annoncée nue, **et** la région `role="status"` annonce en parallèle la phrase complète : le produit obtient la double annonce au lieu de l'annonce unique. Zéro occurrence d'`aria-relevant` dans les cinq fichiers.
*Correctif :* poser explicitement `role="log" aria-relevant="additions" aria-atomic="false"`, et documenter que le comportement dépend de cet attribut et non du rôle.

**[Accessibilité · Implémentabilité] Deux des trois mécanismes d'annonce reposent sur un `aria-label` inopérant** (EXPERIENCE.md:190-191 ; maquettes 2:132, 3:149) — [WCAG 4.1.2, A]
`aria-label` est prohibé par ARIA 1.2 sur `role=generic`, c'est-à-dire sur tout `<div>` sans rôle explicite. Le récapitulatif est le « point de vérité du parcours » et son étiquette était le seul canal par lequel la mutation de statut devait rester lisible après coup : ce canal n'existe pas. Le résumé du tour, sur lequel repose le dénombrement des propositions, n'existe pas non plus.
*Correctif :* donner un rôle réel aux conteneurs (`<section aria-label>` ou `role="group"`, `<article>` pour le tour) et préférer `aria-labelledby`.

**[Accessibilité] L'encadré de jouabilité porte une information de santé sans équivalent non visuel** (DESIGN.md:339 ; maquette 3:135) — [WCAG 1.3.1, A ; 1.4.1, A]
DESIGN.md décrit le composant uniquement par ses couleurs et son filet latéral, et conclut : « sa singularité est le signal » — l'aveu que le signal est purement graphique. La maquette le rend en `<div>` sans rôle ni nom accessible. Cela contredit la règle interne « statut, écart de niveau et **jouabilité** portent tous leur mot » : la jouabilité ne porte de mot nulle part. Seul composant dont le PRD dit qu'il traite « une question de santé et non de confort ».
*Correctif :* un mot en tête (« Conditions de jeu — chaleur »), `role="group"` + `aria-labelledby`. Pas `role="alert"` : l'encadré arrive avec le tour.

**[Accessibilité] La zone de saisie n'a aucun indicateur de focus dans les trois maquettes** (mockups 1:71, 2:94, 3:95) — [WCAG 2.4.7, AA]
`form.composer input:focus{outline:none}` a une spécificité de (0,2,2) et l'emporte sur `:focus-visible` en (0,1,0). Le contrôle le plus utilisé du produit — focalisé au chargement, refocalisé après chaque envoi, présenté comme « *le* mécanisme d'accès » — n'a aucun anneau. Le seul remplacement offert est un changement de filet séparé par 1,47:1 : imperceptible.
*Correctif :* supprimer `outline:none`, ou porter l'anneau sur le `<form>` via `:focus-within` avec le même `outline` opaque de 3 px.

**[Accessibilité] Aucune région live à l'état à froid : la première phrase du produit est inaudible** (mockups/key-fil-a-froid.html) — [WCAG 4.1.3, AA]
Une région live doit préexister à la mutation qu'elle annonce. L'écran « fil à froid » est précisément l'état où le premier message va arriver, et il ne contient ni `role="log"` ni `role="status"`. Le premier tour — la première chose que le produit dise jamais — n'est annoncé par rien, et le défaut se reproduit à chaque nouvel onglet.
*Correctif :* inscrire dans *Accessibility Floor* que le fil, la région d'étapes et la région de statut sont présents et **vides** dès le premier octet de HTML.

**[Accessibilité · Implémentabilité] `border-decorative` porte un état à 1,70:1, en violation de sa propre définition** (DESIGN.md:309 vs 334) — [WCAG 1.4.11, AA]
La scission des filets a laissé `border-decorative` à l'ancienne valeur sous seuil (1,87 / 1,70 / 1,52) puis lui a confié un **état** : « Inerte (tour résolu) : filet `border-decorative` […] différence perceptible sans pointeur », alors que la spine promet 25 lignes plus haut qu'il « ne porte jamais à lui seul une information ». Sous `forced-colors`, les deux natures de filet deviennent identiques et le contrat s'effondre exactement là où on l'a chargé.
*Correctif :* soit remonter `border-decorative` au-dessus de 3:1, soit porter l'état inerte par un mot visible.

**[Implémentabilité] Quatre transitions concurrentes n'existent pas** (EXPERIENCE.md · State Patterns, Interaction Primitives)
Deux demandes en cours (la spine reconnaît le problème et *l'accepte au lieu de le résoudre*) ; envoi pendant le travail du bot (interruption, file d'attente ou parallèle ? et la trace des étapes, tronquée, reste-t-elle honnête ?) ; retour sur une décision (« on le redit au bot » est une politique, pas une transition — aucun statut ne couvre « abandonnée par le demandeur ») ; changement de créneau après écriture agenda, alors que FR-12 l'exige.
*Correctif :* une section *Concurrence*, ou une règle explicite d'exclusion (« une seule demande active à la fois ») qui serait au moins une décision.

**[Implémentabilité] Le seul événement que la personne attend est silencieux** (EXPERIENCE.md · new-message-pill, State Patterns)
La confirmation ne produit aucun nouveau message (règle explicite, et c'est un bon choix) ; la pastille « nouveau message » ne se déclenche que « quand un message arrive ». Une personne qui a remonté le fil ne voit donc rien — alors que la spine affirme que « le seul événement que la personne attendait ne peut pas être inaudible ». La règle et le mécanisme divergent.
*Correctif :* étendre le déclencheur de la pastille aux mutations de statut, avec son propre libellé.

**[Implémentabilité] Aucun point d'entrée de connexion, et aucune règle de stockage** (EXPERIENCE.md · IA, Interaction Primitives)
« Fil à froid, connu » suppose une reconnaissance dont le mécanisme n'est pas dit, et il n'existe aucun point d'entrée de connexion hors du moment déclenché par la mise en relation. Un inscrit sur une autre machine est indistinguable d'un inconnu et n'a aucun moyen de se retrouver. Corollaire : second onglet, second appareil, navigation privée, jour 31 — aucune réponse.
*Correctif :* une surface de connexion dans l'IA, et une règle de portée du fil.

**[Implémentabilité] Le bot énonce un mensonge dans le parcours conçu pour prouver son honnêteté** (EXPERIENCE.md · parcours 2, variante sans alerte)
« Il l'enregistre quand même dans le vivier en le lui disant. » FR-3 : « un visiteur sans compte ne sort jamais comme candidat d'une recherche », l'entrée au vivier se fait « à la création de son compte, et pas avant ».
*Correctif :* corriger la variante, ou obtenir du PRD que l'entrée sans compte soit autorisée et écrite.

**[Implémentabilité] Les spines n'énoncent aucun contrat de données** (les deux spines)
Treize données supposées sans être décrites. Les plus coûteuses : **l'écart de niveau**, exigé « écrit en toutes lettres sur la carte », sans gabarit ni type ; **la météo**, dont le pivot du parcours 1 exige une granularité horaire jamais dite, et dont le cas *partiel* — le plus probable en production — n'est pas couvert ; **les étapes narrées**, dont l'état *échouée* est exigé par la grammaire de l'honnêteté et n'a ni jeton, ni couleur autorisée, ni forme ; **la cohérence croisée**, sur laquelle il n'existe aucune règle. Pour un produit dont la thèse est « le bot n'invente rien », l'absence de règle d'incohérence est un manque de principe autant que de spécification.
*Correctif :* une section de contrats de données, ou leur renvoi explicite à l'architecture — mais alors le dire.

**[Implémentabilité] Le contenu variable n'est borné nulle part** (partner-card, meeting-recap)
Prénom de 40 caractères sans règle de coupure (et « aucun conteneur de texte n'a de hauteur fixe » interdit l'élision par hauteur) ; sept jours sans repli ; **zéro jour disponible : cas non traité**, alors que `unknown-value` existerait pour ça ; une ou deux cartes non spécifiées ; l'écart de niveau sans gabarit ni emplacement.
*Correctif :* borner chaque champ affichable et lui donner son état inconnu, comme la règle dérivée de *La grammaire de l'honnêteté* l'exige déjà — elle se contredit aujourd'hui par omission.

**[Dérive] Cause racine n°1 : le PRD n'a aucun journal de modifications** (prd.md · frontmatter)
Le PRD a changé de statut, gagné deux exigences, fixé trois seuils, changé de surface principale et modifié le sens de deux entrées du glossaire — tout en gardant `updated: 2026-08-26`, la même date que les spines qu'il invalide. Aucun consommateur aval ne peut détecter qu'il a bougé. C'est la cause mécanique des 18 points d'incompatibilité.
*Correctif (dans le PRD) :* un journal des modifications, ou au minimum une ligne de version.

**[Dérive] Cause racine n°2 : les questions ouvertes n'ont pas d'identifiant stable** (prd.md §11)
Liste ordonnée renumérotée deux fois en une journée. Les spines pointent vers « la question n°3 » (qui désigne autre chose) et « la question 6 » (qui n'existe pas).
*Correctif (dans le PRD) :* numéroter `QO-1…QO-n` et conserver les entrées fermées à leur numéro.

---

### Élevés (sélection — 25 des 71)

**[Rubric · Implémentabilité] Aucun jeton ne porte l'échec, et la palette en interdit tous les candidats** (DESIGN.md · Colors)
Quatre états de panne sont spécifiés et *Accessibility Floor* exige que les erreurs soient identifiées en texte. Or `status-danger` est explicitement interdit pour cet usage, l'ambre a « un seul métier », et rien ne les remplace. Un développeur retombera sur du rouge — la violation explicite de la règle.
*Correctif :* un couple `status-fault` / `status-fault-quiet` mesuré et inscrit à la table, ou une règle disant que l'échec se rend sans couleur, en `ink-secondary` + mot.

**[Accessibilité · Implémentabilité] La table de contraste ne liste que des paires conformes** (DESIGN.md · Cibles de contraste)
Son en-tête se dit contractuel. Toutes les compositions que le système produit et qui échouent en sont absentes : `border-decorative` contre ses trois fonds (1,87 / 1,70 / 1,52), `accent-hover`/`accent` à **1,15:1**, `accent-pressed`/`accent` à **1,39:1**, `surface-raised-pressed`/`surface-raised` à **1,48:1**. Une table qui ne contient que ses succès n'est pas un contrat, c'est un certificat : elle ne peut détecter aucune régression.
*Correctif :* inscrire les paires en échec, et la marge la plus fine du système — `ink-secondary`/`surface-raised-pressed` à **4,513:1**, soit 0,013 au-dessus du seuil.

**[Accessibilité] Le survol et l'appui du bouton primaire violent la propre règle de la spine** (DESIGN.md:184-186, 359) — [WCAG 1.4.11, AA]
`accent-hover`/`accent` = 1,15:1 ; `accent-pressed`/`accent` = 1,39:1, sans filet. Le tableau *Do's and Don'ts* condamne pourtant « le survol porté par un fond à 1,3:1 ». Même défaut sur l'état pressé de la carte : 1,48:1 — le pointeur reçoit 4,93:1 et le doigt 1,48:1, dans le produit qui promet la « parité fonctionnelle stricte ».
*Correctif :* un filet d'état au bouton primaire et à l'état pressé de la carte.

**[Accessibilité] La phrase de confirmation n'existe que pour les lecteurs d'écran** (EXPERIENCE.md:190,194 ; maquette 3:236)
La spine pose : « aucune information n'existe uniquement sous forme d'annonce ». La maquette rend pourtant « Anna a confirmé. Mercredi 3 septembre, 19 h. » en `sr-only`. Le correctif a *inversé* l'asymétrie de la passe 1 au lieu de la supprimer : l'utilisateur voyant qui a détourné le regard trouve une pastille verte sans savoir quand ni pourquoi elle a changé.
*Correctif :* rendre la phrase visible comme ligne de statut discrète — la règle de ton porte sur le registre, pas sur l'existence d'une trace.

**[Accessibilité] Le lien « Pourquoi ? » revendique une conformité impossible et manque la vraie** (DESIGN.md:337) — [WCAG 2.5.8, AA ; 4.1.2, A]
« Le lien respecte `target-min` comme tout le reste », soit 48 px pour un texte de 14 px : impraticable — et 2.5.8 exempte explicitement les cibles en ligne. La spine s'impose une contrainte fausse au lieu de la contrainte réelle. Second défaut, plus grave : c'est le seul endroit où la portée d'un consentement de données est révélée, et il n'a ni `aria-expanded`, ni rôle de bouton, ni contenu rédigé.
*Correctif :* `<button aria-expanded="false">`, et une zone d'atteinte de 24×24 px sans chevauchement.

**[Rubric · Dérive · Accessibilité · Implémentabilité] La frappe au vol retirée survit dans le tableau responsive** (EXPERIENCE.md:240)
Prescrite comme comportement nominal PC, alors qu'*Interaction Primitives* consacre un paragraphe à expliquer qu'elle est retirée pour violation de WCAG 2.1.4. « Échap » n'est défini nulle part ailleurs. Un développeur qui commence par le tableau réintroduit l'échec en toute bonne foi.
*Correctif :* remplacer par « Focus automatique du champ au chargement et après chaque envoi ».

**[Rubric · Implémentabilité] Les deux spines ne s'accordent pas sur la borne de largeur** (DESIGN.md · Layout & Spacing vs EXPERIENCE.md · Responsive & Platform)
DESIGN.md définit `thread-max-width: 45rem` et pose « toutes les tailles sont en rem » ; EXPERIENCE.md écrit trois fois 720 px et en fait le point de rupture ; les maquettes coupent à 48 rem. Les deux premiers divergent dès que la racine change — *le scénario même que DESIGN.md invoque pour justifier le rem*. Et DESIGN.md ne nomme jamais le point de rupture : la seule valeur écrite est celle qui contredit sa règle. Plus un trou non couvert entre 720 et 784 px.
*Correctif :* trancher `45rem` des deux côtés, requête média comprise, nommer la valeur une seule fois dans DESIGN.md.

**[Rubric] La spine garantit une persistance que le produit ne tient pas** (EXPERIENCE.md · Interaction Primitives)
« Aucune expiration de session ne vide la conversation. » Le PRD §6 pose 30 jours puis effacement pour les visiteurs sans compte, et *Accessibility Floor* s'appuie sur la garantie fausse. C'est aussi une décision de conservation de données personnelles prise en UX.
*Correctif :* qualifier la règle et ajouter l'état de bord — ce que voit un visiteur au 31ᵉ jour.

**[Rubric] La spine construit le comportement que le PRD désigne comme le symptôme à surveiller** (EXPERIENCE.md · Hors périmètre, Voice and Tone)
Le PRD §7 : « quand quelqu'un demande une liste, une carte ou un filtre, le bot ne répond pas qu'il ne sait pas faire — il donne ce qu'il peut sous une forme plus dense, et note la demande. SM-5 surveille ce symptôme. » La spine prescrit « sans tenter de répondre ». C'est exactement le grief du seul verbatim hostile du corpus de recherche.
*Correctif :* scinder l'état en deux — *hors sujet* et *demande de liste/carte/filtre*.

**[Rubric] La distinction couvert / extérieur est absente des deux spines** (EXPERIENCE.md · Component Patterns, State Patterns)
FR-10 fait dépendre toute la jouabilité de cet attribut. Un consommateur construira un contrôle météo sur un court couvert — et le parcours 1 s'écroule à l'étape 8. Le PRD lui-même ne spécifie pas le troisième cas (attribut inconnu), aujourd'hui le plus probable.
*Correctif :* ajouter l'attribut à *Proposition de lieu*, une condition d'entrée à *Jouabilité dangereuse*, et l'état **Lieu couvert**.

**[Rubric] Le débordement au-delà de trois candidats n'a pas d'état** (EXPERIENCE.md · State Patterns)
Le plafond est répété deux fois, mais la seconde moitié de FR-6 — « au-delà de trois candidats, le bot dit combien il y en a d'autres et propose de les montrer » — n'est traitée nulle part, pas plus que l'ordre (délai d'attente croissant, puis ordre du vivier).
*Correctif :* un état **Plus de trois candidats** et la règle d'ordre reprise verbatim.

**[Rubric] Dix-huit exigences n'ont aucun foyer, dont quatre NFR** (prd.md)
Outre les trois critiques : mise à jour de l'événement d'agenda, contenu de l'événement (FR-12), attribut couvert/extérieur, secteur facultatif, seuils de jouabilité, validité 60 jours et alertes multiples, ordre des candidats, seconde demande d'un profil connu, réponse hors-Lyon, garde-fou §7. NFR : latence 2 s / 20 s, plancher 360 px, rétention 30 jours, repli météo. **La traçabilité par identifiant est la cause mécanique :** EXPERIENCE.md ne cite que 3 exigences sur 15, DESIGN.md aucune, UJ-2 n'est jamais nommé.
*Correctif :* une matrice de couverture FR → surface / composant / état / parcours.

**[Rubric] Quatre affordances existent dans les états sans exister comme composants** (EXPERIENCE.md · State Patterns)
Ligne d'état persistante du hors-ligne, marqueur « non envoyé » et son action de réémission, ligne d'attente de la reprise, exemple de phrase sous le champ. Quatre éléments dont personne ne connaît la forme, l'ancrage ni le comportement de disparition — et pour lesquels aucune couleur n'est autorisée.
*Correctif :* les promouvoir en lignes de composant des deux côtés.

**[Rubric] « Proposition de lieu » n'existe que d'un côté** (EXPERIENCE.md · Component Patterns)
Ligne comportementale complète, aucune contrepartie visuelle. C'est le seul foyer de FR-11 dans toute la paire, et par conséquent **l'attribut couvert/extérieur n'a nulle part où se rendre**.
*Correctif :* une puce disant explicitement que le lieu est rendu en prose de message, avec son attribut et le repli `unknown-value`.

**[Rubric] Le seul élément textuel cliquable du produit n'a pas de style** (DESIGN.md · Components)
Le lien « Pourquoi ? » n'a ni couleur, ni soulignement, ni état visité, ni état focalisé propre. Le système ne définit aucun style de lien.
*Correctif :* une ligne dans *Components*, ou une règle disant que tout lien prend la forme de `button-quiet`.

**[Rubric · Implémentabilité] Le bouton d'envoi désactivé est invisible par construction** (DESIGN.md · composer / button-primary)
`composer.background` et `button-primary.backgroundDisabled` valent tous deux `surface-overlay`. Le bouton disparaît dans son conteneur au repos, c'est-à-dire dans son état le plus fréquent. Les maquettes ont ajouté un filet qui n'existe dans aucun jeton.
*Correctif :* promouvoir le filet en jeton, ou changer le fond désactivé.

**[Implémentabilité] La zone de saisie est spécifiée en contradiction avec sa propre balise** (DESIGN.md · composer ; mockups)
Quatre lignes de croissance + Maj+Entrée impliquent un `<textarea>` ; les trois maquettes emploient `<input type="text">`. Le bouton d'envoi est tokenisé comme textuel et rendu en icône carrée : les jetons et les maquettes décrivent deux boutons différents.
*Correctif :* trancher la balise, et donner au bouton d'envoi son propre jeton.

**[Implémentabilité] « Un seul bouton primaire visible à la fois » est inapplicable tel quel** (DESIGN.md · Components)
Le fil n'est jamais purgé, les tours passés gardent leurs boutons, et « le passé est inerte » n'est énoncé que pour les cartes. La règle la plus citée de la spine n'a pas de mécanisme.
*Correctif :* étendre la règle d'inertie du passé à tous les contrôles du fil.

**[Implémentabilité] Quinze formulations décident en apparence sans décider** (les deux spines)
« Le bot récapitule en tête de fil » ; « le retour rouvre le fil au même endroit, sans perte de contexte » ; « les annonces attendent une pause de saisie » (une machine à états présentée comme une phrase) ; « elle ne doit jamais recouvrir un élément focalisé » face à « la seule surface qui flotte au-dessus » — *flotte ou ne chevauche pas, il faut choisir*.
*Correctif :* chacune est une décision à prendre, pas une phrase à réécrire. Liste complète en §4 de `review-implementabilite.md`.

**[Implémentabilité] L'ordre de tabulation n'est borné par rien** (EXPERIENCE.md · Accessibility Floor)
Tous les boutons des tours passés restent focalisables. Après vingt tours, Maj+Tab remonte tout l'historique — et le chemin n'apparaît nulle part dans le produit, alors que la spine interdit « le raccourci clavier sans équivalent visible ».
*Correctif :* la règle d'inertie du passé règle les deux ; faire porter le chemin par la prose du bot une fois, à froid.

**[Implémentabilité] Aucun paramètre de mouvement n'est tokenisé** (DESIGN.md · Elevation & Depth)
« Fondu bref », « translation de quelques pixels », « pulsation », « au-delà de quelques secondes ». Six valeurs, zéro chiffre. Deux développeurs produiront deux produits différents sur le seul mouvement admis par la spine. La borne non chiffrée est aussi un risque WCAG 2.2.2, qui s'applique au-delà de 5 secondes.
*Correctif :* fixer les six valeurs, et écrire « 5 secondes ».

**[Voix] « Et la personne le sait » : elle ne le sait pas, personne ne le lui a dit** (EXPERIENCE.md:130,177)
Carte, statut et phrase sont identiques pour Anna-qui-ne-répondra-jamais et Anna-qui-répondra-demain. La spine décrit un état de connaissance qu'elle n'a produit par aucun moyen. C'est la définition exacte du mensonge par omission, et il porte sur la contrainte que le PRD qualifie de « la plus structurante ».
*Correctif :* ne pas badger les profils d'amorçage, mais énoncer la propriété générale du vivier **une seule fois**, à la pose du récapitulatif : « Une partie des personnes que je propose ne sont pas encore inscrites ici : elles peuvent ne jamais répondre. Votre créneau tient quand même, et le lieu aussi. »

**[Voix] Un adverbe qui promet une réponse que 86 profils sur 86 ne donneront jamais** (EXPERIENCE.md:71 ; maquette)
« Elle n'a pas **encore** confirmé » est un présupposé d'aspect. La spine se contredit elle-même — `EXPERIENCE.md:178` prescrit déjà la bonne forme, sans « encore ». Trois documents, trois formulations, et c'est la moins honnête qui est passée dans les maquettes.
*Correctif :* « Anna est prévenue. Elle n'a pas confirmé. » Et inscrire l'interdit : *ne jamais qualifier une absence de réponse d'un adverbe qui en promet une*.

**[Voix] L'inconnu est écrit en langue administrative, dans le document qui interdit cela** (DESIGN.md:237 ; maquette)
« Lieu non déterminé », « Prévisions indisponibles » : participes passés passifs, aucun locuteur, aucun aveu. **La spine a résolu le problème typographique de l'inconnu et laissé le problème lexical entier** — alors que *Voice and Tone*, vingt pages plus loin, écrit correctement le même état.
*Correctif — règle : l'inconnu se conjugue.* « Lieu : je ne sais pas encore », « Vous ne m'avez pas dit où », « L'heure reste à choisir ». Corollaire : l'`aria-label` porte la même formulation.

**[Voix] Le vivier vide n'a pas une phrase, et neuf états d'échec sur onze non plus** (EXPERIENCE.md · State Patterns)
Trois formulations écrites sur quinze états d'échec ou d'absence ; les trois sont bonnes. Pour les douze autres, un LLM « dont la pente naturelle est de faire plaisir » comblera — et il comblera avec la voix du chatbot de support. **L'interdiction sans la formulation de remplacement ne protège rien.**
*Correctif :* le jeu complet est rédigé en É4 de `review-voix.md`, plus deux règles transversales : tout message d'échec dit ce qui n'est pas perdu ; aucun ne s'ouvre sur une excuse.

**[Voix] Quatre textes sortants, dont le seul texte lu hors du produit, ne sont écrits nulle part** (EXPERIENCE.md:48 ; FR-9, FR-13, FR-14)
Si l'alerte différée est l'unique valeur produite par le parcours d'échec, ce courriel *est* la livraison. C'est aussi le seul texte affranchi du contexte du fil, donc celui où la pente vers « Bonne nouvelle ! 🎾 » est la plus raide. Trois autres sont dans le même cas et ne sont même pas *nommés*, dont **le message de sollicitation du partenaire — le seul contact qu'un profil d'amorçage aura jamais avec le produit**.
*Correctif :* les quatre textes sont rédigés en É5, avec des règles à graver : pas de salutation, pas d'emoji, pas de prénom du partenaire, une seule action, un moyen d'arrêter.

**[Voix] « Vouvoiement jusque dans les libellés de boutons » : énoncé deux fois, réalisé zéro fois** (DESIGN.md:224,364)
Neuf libellés, neuf infinitifs ou groupes nominaux. La règle a pourtant un modèle disponible à trois centimètres : les cartes portent déjà la voix de la personne, et la spine exige que tout cliquable soit *dicible*. Personne ne dit « Retenir 19 h » à voix haute.
*Correctif :* séparer deux familles. Les boutons qui sont une réplique de la personne portent sa voix (« Va pour 19 h ») avec pour test *puis-je le dire au bot à la place de cliquer ?* ; les commandes de l'appareil restent à l'infinitif.

**[Rubric] La maquette invente un seuil de santé et le met dans la bouche du bot** (mockups/key-recap-en-attente.html:137,188)
« Au-dessus de 32 °C » quand FR-10 fixe 28 °C ressentis — et le memlog du PRD journalise que cette maquette « doit être corrigée », correction jamais faite. **La règle « la spine l'emporte » ne sauve pas ce cas :** aucune spine n'énonce de seuil, donc la maquette est la seule source de chiffre.
*Correctif :* corriger à 28 °C, et faire dire aux spines où vivent les seuils.

**[Rubric] Huit composants n'ont aucune référence visuelle, et ce sont les plus risqués** (mockups/)
Bloc de connexion, choix d'agenda, pastille « nouveau message », carte portant l'écart de niveau, récapitulatif d'alerte, ligne hors-ligne, message non envoyé, ligne d'attente de reprise. L'état pressé n'apparaît nulle part non plus, alors que c'est le seul retour tactile du produit.
*Correctif :* si une quatrième maquette est produite, que ce soit celle des états de panne.

**[Rubric] Les maquettes contredisent les spines sur seize points** (mockups/)
Les plus lourds : Nantes contre le verrouillage lyonnais ; un bloc-marque en capitales dans un produit qui les interdit et bannit toute navigation ; `<input type="text">` contre une zone de saisie sur quatre lignes ; le sort de la carte inerte suffixé au lieu d'être préfixé ; le climax qui écrit « C'est dans votre agenda Google » sans avoir montré aucun des deux gestes de consentement.
*Correctif :* reprendre les maquettes après la resynchronisation, pas avant.

**[Rubric] Le protagoniste du parcours 2 porte le prénom d'un profil du vivier, et le bot ment** (EXPERIENCE.md · parcours 2)
« Sarah » est la seule pratiquante de Pilates des données d'amorçage. Et la spine fait dire « personne ne pratique le Pilates dans le vivier », faux selon FR-8 : il y a une pratiquante, débutante, et le refus vient de la non-adjacence Débutant/Avancé. Le niveau avancé de la protagoniste — *la raison* pour laquelle le refus est correct — a disparu.
*Correctif :* renommer en Nadia verbatim, rétablir le niveau avancé, faire narrer les deux élargissements.

**[Dérive] Le PRD se contredit lui-même sur la propriété centrale du vivier** (prd.md §3 l.169 vs FR-14 l.583)
« Il grossit ; il ne diminue pas » contre « l'exercer retire le profil du vivier définitivement ». **Seule contradiction interne au PRD qu'aucun aval ne peut arbitrer.**
*Correctif (dans le PRD) :* trancher, et propager au glossaire.

**[Dérive] Le glissement de vocabulaire des spines a une cause en amont** (prd.md §3 vs FR-11)
« Secteur » et « arrondissement » sont employés par FR-11 mais absents du glossaire, alors que le §0 déclare ce vocabulaire contraignant. Le seul terme géographique disponible pour l'aval est donc « ville » — précisément celui que le §5.4 interdit. Les spines ont employé le seul mot qu'on leur avait donné.
*Correctif (dans le PRD) :* ajouter les deux termes au glossaire.

**[Dérive] Un garde-fou mesuré sans exigence n'est construit par personne** (prd.md §7 ; SM-5)
Le §7 prescrit un comportement précis et SM-5 le mesure, mais aucune FR ne le porte. Les spines ont écrit le comportement inverse : c'est la démonstration empirique du problème.
*Correctif (dans le PRD) :* une exigence testable.

---

### Moyens (sélection — 10 des 60)

- **[Accessibilité] Thème sombre unique, sans aucune échappatoire.** `ink-primary` à 15,93:1 en 17 px sur une colonne de 45 rem de prose lue tard : la configuration qui produit le halo pour la population astigmate. Aucun critère AA n'est échoué, mais ni bascule, ni `prefers-color-scheme: light`, ni `prefers-contrast: less`. *Refuser un thème clair est une décision produit défendable ; refuser tout recours ne l'est pas.* → honorer `prefers-contrast: less` (`ink-primary` vers ~`#D6DEE9`, ≈13:1).
- **[Accessibilité] Le décompte de la passe 1 était faux, et il a rétréci le périmètre des correctifs.** Annoncé « 6 critiques, 9 élevés » ; le décompte des balises donne **8 / 15**. Plusieurs des « non résolus » de cette passe 2 sont dans les six élevés escamotés — ils n'ont jamais été corrigés parce qu'ils n'ont jamais été remontés. → décompte mécanique, jamais déclaratif.
- **[Accessibilité] Le document n'a aucun titre après le premier message.** L'accroche `display` est le seul `<h1>` et « apparaît une seule fois dans la vie du produit » ; la navigation par titres ne renvoie rien sur une conversation de trente tours. → `<h1 class="sr-only">` permanent et un `<h2 class="sr-only">` par tour, coût visuel nul.
- **[Accessibilité] La spine invente une distinction de modalité que WCAG 2.2 ne fait pas.** « ≥48 px au tactile et ≥24 px au pointeur » : 2.5.8 impose 24 px *sans distinction de type de pointeur*, 2.5.5 impose 44 px (AAA), pas 48. → « 24 px est le plancher normatif (2.5.8, AA) ; le produit s'impose 48 px partout, au-delà de 2.5.5 ».
- **[Rubric] Deux systèmes de nommage jamais reliés.** Kebab au frontmatter, français en prose, aucune table de correspondance. Sur 16 composants, EXPERIENCE.md n'en appelle que **deux** par jeton : un résolveur automatique ne verra que 2 liens sur 16. → faire porter à chaque puce son identifiant de jeton en tête. Coût : une ligne.
- **[Rubric] Les sources se contredisent entre elles et aucune règle de préséance n'existe.** L'addendum dit « le niveau est déclaratif » ; le PRD FR-15 dit l'inverse. La spine a suivi l'addendum, en retard sur le PRD. → une ligne de préséance au frontmatter.
- **[Rubric] Les deux sections inventées ne se valent pas.** *La grammaire de l'honnêteté* mérite sa place (elle porte une contrainte transversale qu'aucune autre section ne peut porter) ; *Les deux populations du vivier* non — ses quatre puces sont soit déjà écrites ailleurs, soit devenues fausses. → réduire la première à son préambule et à sa règle dérivée, dissoudre la seconde.
- **[Rubric] Les trois climax portent une queue éditoriale qui dilue le beat.** C'est de la voix éditoriale, qui appartient à DESIGN.md. Déjà journalisé comme non traité. → couper les queues.
- **[Voix] « Exactement à votre niveau » surpromet sur une donnée déclarative.** Le seul adverbe du produit qui affirme une précision que la donnée n'a pas — *dans un produit dont le nom même est une promesse d'égalité*. (Constat à réviser si FR-15 est appliqué : le niveau cesse alors d'être déclaratif.) → « se déclarent au même niveau que vous ».
- **[Voix] L'interdit d'emoji est écrit trop étroitement pour tenir.** « Tout emoji **d'accueil** » laisse passer météo, statut, sport — et surtout les messages sortants, où la pente est la plus forte. Idem pour le point d'exclamation, dont l'interdit ne couvre que « une phrase du bot » et laisse passer un objet de courriel. → « Aucun emoji, nulle part ».

---

### Faibles (sélection — 5 des 30)

- **[Rubric] Quatre nombres pour une seule scène** : la spine dit 34 °C, la maquette 34 au-dessus d'un seuil de 32, le PRD 31 au-dessus de 28. Aucun n'est contractuel, mais ils seront recopiés tels quels.
- **[Rubric] Un répertoire de travail est resté dans le livrable** : `.working/` contient trois copies des maquettes, rien n'indique laquelle fait foi.
- **[Rubric] La liaison entre les deux spines n'est pas symétrique** : DESIGN.md ne porte pas de clé `experience:` vers son jumeau.
- **[Accessibilité] `<span class="unknown">` sans `<em>`** : l'italique est « le seul marqueur typographique du système » et n'a, en CSS pur, aucune exposition sémantique. Le sens est heureusement porté par les mots.
- **[Voix] Les points de suspension des lignes d'étape** empruntent l'indicateur de frappe des widgets de discussion, dans un produit qui interdit par ailleurs l'arrivée caractère par caractère. → forme accomplie une fois l'étape franchie, suspension réservée à l'étape en cours.

---

## Notes mécaniques

- **Frontmatter** — complet et symétrique des deux côtés ; les cinq chemins relatifs se résolvent. Manque : `experience: ./EXPERIENCE.md` côté DESIGN.md.
- **Références de jetons** — 49 occurrences extraites, **49 résolvent**. Aucune orpheline, aucun jeton couleur sans hexadécimal.
- **Contrastes** — **13/13 exacts** après recalcul WCAG indépendant par deux relecteurs. Le défaut est l'omission des paires en échec, pas l'inexactitude des paires listées.
- **Renvois** — ancres internes bien formées, liens croisés et liens vers `mockups/` et les sources résolvent tous. **Un seul renvoi cassé : « question 6 » du PRD**, qui n'en compte que cinq.
- **Contradictions internes** (entre sections d'un même fichier) — **onze**, dont trois relevées par trois lentilles : frappe au vol prescrite après retrait ; brouillon OAuth « survit » / « s'il a survécu » ; purge à 30 jours niée. Plus « un seul mouvement est admis » contre la pulsation de l'étape (deux mouvements), et `border-decorative` qui « ne porte jamais à lui seul une information » tout en portant l'état inerte 25 lignes plus loin.
- **Incohérences de nommage** — deux systèmes de composants jamais reliés ; « Sarah » pour « Nadia » ; « niveau adjacent » jamais employé alors que le PRD impose son vocabulaire littéralement ; « 720 px » contre « 45 rem » ; « candidat » employé une seule fois là où le glossaire distingue candidat et partenaire.
- **Mermaid** — aucun diagramme. Rien à valider.
- **Fraîcheur des artefacts** — spines : 16 h 46. `addendum.md` : 20 h 25. `prd.md` et son memlog : 20 h 33. **La majorité des constats critiques est un effet de cette dérive, pas un défaut de conception.**

---

## Ce qui tient — et qu'il ne faut pas défaire

- **Les treize ratios annoncés sont exacts.** Aucun chiffre faux, aucun seuil manqué. C'est le socle sur lequel le reste peut être réparé.
- **`border-interactive` est un vrai correctif** : 4,79 / 4,37 / 3,89 / 3,59 / 3,35 sur les cinq fonds où il est réellement posé. Porter le survol sur le filet plutôt que sur le fond est la bonne décision, et le raisonnement documenté est exactement la manière dont ce genre d'arbitrage doit être écrit.
- **La suppression de `ink-muted` est le meilleur correctif des deux passes.** Le problème n'a pas été déplacé, il a été dissous en changeant le porteur du sens — de la luminosité vers l'italique et les mots.
- **La frappe au vol a été retirée avec sa justification conservée**, précisément pour empêcher la réintroduction. Il reste seulement à finir le nettoyage.
- **La palette n'a aucun poids mort** : 22 couleurs, toutes consommées, avec une doctrine d'emploi qui se convertit directement en règles de revue de code.
- **`unknown-value` et la grammaire de l'honnêteté** sont spécifiés de bout en bout. Aucune question à poser.
- **Les interdits sont opérationnels** : composants bannis, interdits de vocabulaire et *Do's and Don'ts* se convertissent en tests de non-régression de microcopie.
- **« Cliquer ou écrire, toujours les deux »** est une garantie de parité d'entrée qu'aucun critère WCAG n'exige et qui sert directement la commande vocale, les contacteurs et la commande oculaire.
- **Le parcours 3 est le modèle de ce qu'aurait dû être chaque divergence** : tracé comme `[ASSUMPTION]`, daté, motivé, périmètre de validité délimité. C'est précisément ce traitement qui manque à FR-11, FR-13, FR-14 et FR-15.

---

## Fichiers de relecture

| Fichier | Lentille |
|---|---|
| `review-rubric.md` | Marcheur de rubrique — 8 catégories, couverture + jugement |
| `review-accessibilite.md` | Accessibilité passe 2 — contre-vérification + audit à neuf, WCAG 2.2 AA |
| `review-derive-amont.md` | Dérive PRD ↔ spines — contradictions, orphelines, glossaire, dette amont |
| `review-implementabilite.md` | Implémentabilité aval — « peut-on construire à partir de ces deux fichiers seuls ? » |
| `review-voix.md` | Voix et microcopie FR — vouvoiement, repoussoir, honnêteté, textes sortants |

**Passe 1 archivée :** `review-rubric-passe1.md` · `review-accessibilite-passe1.md` · `validation-report-passe1.md`
