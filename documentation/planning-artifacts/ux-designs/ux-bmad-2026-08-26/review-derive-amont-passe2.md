---
title: "Dérive amont — PRD ↔ spines UX"
date: 2026-08-26
scope: EXPERIENCE.md + DESIGN.md confrontés à prd.md, addendum.md, research-paysage.md, research-niveau.md
predecessor: ../../prds/prd-bmad-2026-08-26/review-drift-prd-ux.md
---

# Dérive amont — PRD ↔ spines UX

## Verdict d'ensemble

**Le sens de la dérive s'est inversé depuis la relecture précédente, et personne ne l'a dit aux spines.** `review-drift-prd-ux.md` concluait « le PRD rattrape l'UX » ; le PRD l'a fait — il est passé en `status: final` à 20:33, a adopté le nom *Ex Aequo*, le PC comme surface principale, les seuils de jouabilité, l'heure de la rencontre, l'ordre des candidats, le canal e-mail, et il a **ajouté deux exigences neuves (FR-14, FR-15) et changé le sens de deux entrées du glossaire**. Les deux spines, figées à 16:46, n'ont rien vu : elles citent encore un PRD qui n'existe plus, y compris dans l'encadré de divergence qui était leur meilleur réflexe.

Résultat pour un consommateur aval : **18 points d'incompatibilité, dont 14 silencieux**, et aucune règle de préséance lisible. Le PRD §0 dit que l'UX en dérive ; `EXPERIENCE.md` dit « cette spine fait foi sur la surface » et « l'emporte sur toute maquette ». Les deux documents portent `status: final` et se contredisent frontalement sur le nombre de statuts d'une rencontre, sur l'existence d'une surface hors conversation, et sur la manière dont le niveau est établi. Un développeur qui lit les deux ne peut pas savoir laquelle des deux versions construire ; les quatre divergences *tracées* pointent toutes vers du texte de PRD qui a été corrigé depuis, ce qui les rend pires qu'inutiles — elles accusent l'amont d'une faute qu'il a réparée.

---

## 1. Contradictions frontales

| Point | Ce que dit la source | Ce que disent les spines | Tracée ? | Sévérité |
|---|---|---|---|---|
| **Un profil d'amorçage peut-il confirmer ?** | prd.md §3 et §4 : « Ne parle jamais au bot — **mais peut accepter une rencontre en suivant le lien de son SMS** (FR-14) ». FR-13 : « Une rencontre passe à *confirmée* ou *déclinée* quand le partenaire suit le lien de son message » | EXPERIENCE *Les deux populations* : « 86 profils d'amorçage — un téléphone et rien d'autre, **incapables de répondre** » ; *State Patterns* : « Un partenaire issu d'un profil d'amorçage reste **en attente indéfiniment** » ; « Rencontre confirmée \| **Un utilisateur inscrit** accepte » | **Non** | **Critique** |
| **Combien de statuts a une rencontre ?** | prd.md §3 et FR-13 : « Elle porte un statut et un seul : **en attente, confirmée, déclinée ou expirée** ». Quatre lignes de tableau, avec la microcopie de chacune | EXPERIENCE *Component Patterns*, pastille de statut : « **Deux valeurs seulement** : *en attente*, *confirmée* ». DESIGN ne définit que `status-badge-pending` et `status-badge-confirmed`, et réserve `status-danger` à la seule jouabilité | **Non** | **Critique** |
| **Existe-t-il une surface hors du fil ?** | prd.md §9, *dans le périmètre* : « **Notification du partenaire et lien d'acceptation à usage unique** (FR-14) : **une page hors conversation**, qui accepte ou refuse ». addendum.md : « Seule surface du produit qui vit en dehors du fil » | EXPERIENCE *Foundation* : « **Un composant qui ne peut pas vivre dans le fil ne fait pas partie du produit** » ; la table d'IA ne liste aucune page d'acceptation ; la fenêtre modale est bannie | **Non** | **Critique** |
| **Comment le niveau est-il obtenu ?** | prd.md §3 : « **Ce sont les valeurs internes du produit, jamais une question posée à la personne** » ; FR-15 : « Le bot ne demande jamais “quel est votre niveau”… il pose des questions factuelles… Un libellé que la personne s'attribue spontanément n'est **ni contredit ni retenu tel quel** » | EXPERIENCE *Inspiration & Anti-patterns* : « **Ici le niveau se déclare dans la phrase**, au fil de la conversation, ce qui ne le rend pas plus exact mais évite d'installer un rituel d'évaluation ». Parcours 1 : Thomas écrit « je suis intermédiaire » et le bot enchaîne directement sur la recherche — aucun *beat* de FR-15 | **Non** | **Critique** |
| **Le bot ment sur le vivier (Pilates)** | FR-8, conséquence testable : « le vivier ne compte **qu'une pratiquante de Pilates, de niveau Débutant**, et Débutant n'est pas adjacent d'Avancé ». §7 : « Aucun nom de partenaire qui ne vienne du vivier… en cas de doute, le bot dit qu'il ne sait pas » | EXPERIENCE *Key Flows*, parcours 2, étape 3 : « **personne ne pratique le Pilates dans le vivier** ». C'est faux, et c'est la réplique du moment que le PRD désigne comme « le moment où le bot est le plus tenté de broder » | **Non** | **Critique** |
| **Ville / périmètre géographique** | prd.md §5.4 : « Le produit ne desservant qu'une agglomération (§1), **il n'y a pas de ville à demander** ». FR-11 : « Le bot peut demander **un secteur ou un arrondissement** pour affiner, mais ne l'exige jamais » | EXPERIENCE, composant *Proposition de lieu* : « **La ville est demandée en prose** avec son motif » ; état *Ville inconnue* : « Tant qu'elle manque, aucun lieu n'est proposé » ; parcours 1, étape 6 : « Le bot demande la ville ». **« Lyon » n'apparaît pas une seule fois dans les deux spines**, ni « secteur », ni « arrondissement » | **Non** | **Élevée** |
| **Qu'est-ce qui manque dans une demande incomplète ?** | FR-2 : le bot extrait « **le sport et les jours**, et réclame ce qui manque un élément à la fois. **Le niveau n'est jamais demandé directement** : il est établi par FR-15 » | EXPERIENCE *State Patterns* : « Demande incomplète \| **Sport ou niveau manquant** ». Le jour — la dimension sur laquelle porte tout l'élargissement — est absent du déclencheur, et le niveau, qui ne doit jamais être demandé, y figure | **Non** | **Élevée** |
| **Le protagoniste du parcours 2** | prd.md §2.3 UJ-2 : « **Nadia** cherche un partenaire là où il n'y a personne », **niveau avancé** ; §11.1 : les prénoms « ont été choisis **absents des données d'amorçage** pour éviter toute confusion avec un profil du vivier » | EXPERIENCE parcours 2 : « **Sarah** cherche un partenaire là où il n'y a personne ». `SportsProfiles.csv` l. 13 : `Sarah,Andre,+33639980012,Pilates,Mardi;Jeudi,Débutant`. La demandeuse porte le prénom du seul profil d'amorçage de Pilates — celui qui « ne parle jamais au bot ». Le niveau avancé, qui est *la raison* pour laquelle le refus est correct, a disparu | **Non** | **Élevée** |
| **Fréquence du refus total** | prd.md §2.3 : « 55 % ne renvoient aucun candidat *exact* — **mais l'élargissement en rattrape la quasi-totalité**, et il ne reste que 12 combinaisons, soit **5,2 %**… **le comportement principal n'est pas le refus** ». Plus un `[NOTE FOR PM]` en §5.2 : 55 % est « un fait sur la grille, **pas une prévision du taux d'échec** » | EXPERIENCE parcours 2 : « **Ce parcours couvre 55 % des recherches** : c'est un chemin nominal » ; *Voice and Tone* : « Le produit délivre une mauvaise nouvelle dans **55 % des recherches** ». Le parcours du vide est dimensionné à dix fois sa taille réelle, et le chiffre est requalifié en taux vécu | **Non** | **Élevée** |
| **Surface principale** | prd.md §6, *Surface* : « **Le navigateur d'un ordinateur est le cas d'usage principal** ; le mobile est servi à parité fonctionnelle complète, à partir de 360 px ». §9 : « pensé pour l'ordinateur d'abord » | EXPERIENCE *Foundation*, encadré : « **Le PRD §6 énonce l'inverse** : “Le site s'utilise au téléphone via le navigateur ; c'est le cas d'usage principal.” Cette phrase est **caduque**… la correction du PRD est à porter en amont » | **Oui — mais la trace est devenue fausse** | **Élevée** |
| **Persistance du fil anonyme** | prd.md §6, *Reprise de conversation* : « Un visiteur **sans compte** retrouve son fil pendant **30 jours** sur le même navigateur, **après quoi il est effacé** » | EXPERIENCE *Interaction Primitives* : « Le fil **ne se réinitialise jamais** tout seul » ; *Charge cognitive* : « il n'est donc **jamais purgé, jamais réinitialisé** ». Aucune mention de 30 jours ni d'effacement | **Non** | **Moyenne** |
| **Repli quand les terrains tombent** | prd.md §6, *Robustesse* : « **sans données de terrains l'utilisateur indique le lieu lui-même** » | EXPERIENCE, état *Aucun lieu disponible* : « Le créneau reste retenable **sans lieu** » ; parcours 1, *Défaillance* : « Le lieu apparaît en `{components.unknown-value}` ». Le repli prescrit — la saisie manuelle — n'existe nulle part | **Non** | **Moyenne** |
| **Réaction à une demande de liste / carte / filtre** | prd.md §7, *L'enfermement dans la conversation* : « le bot **ne répond pas qu'il ne sait pas faire** — il donne ce qu'il peut sous une forme plus dense, et **note la demande**. SM-5 surveille ce symptôme » | EXPERIENCE, état *Hors périmètre* : « Le bot dit ce qu'il fait et ce qu'il ne fait pas, en une phrase, **sans tenter de répondre** » ; *Voice and Tone*, à faire : « Je ne sais faire que ça » — exactement la réponse que le PRD interdit. Aucun état ne traite la demande de liste/carte/filtre | **Non** | **Moyenne** |
| **SMS réellement envoyé aux 86 profils** | prd.md §11, *Questions fermées* : « *Les 86 personnes sont-elles contactées pour de bon ?* — **oui**, par un SMS auto-explicatif portant un lien d'acceptation et un moyen de sortir du vivier (FR-14) » | EXPERIENCE : « `[ASSUMPTION: le PRD laisse ouvert (**question 6**) si un SMS part réellement vers les 86 personnes. L'expérience est rédigée pour être vraie dans les deux cas]` ». La question est fermée, et le §11 ne compte que **cinq** questions — il n'y a pas de question 6 | **Oui — mais périmée et mal numérotée** | **Moyenne** |
| **Canal de l'alerte différée** | FR-9 : « La notification part **par e-mail à l'adresse du compte, dans l'heure** qui suit… Une alerte vaut **60 jours**, puis expire ; le bot prévient par e-mail lors de l'expiration » | EXPERIENCE *IA* : « le **canal d'alerte différée** est la seule surface qu'aucun parcours ne traverse, parce qu'elle est hors du produit et que **sa forme n'est pas tranchée** » + `[ASSUMPTION: … le PRD a identifié le trou … sans le combler]`. Le trou est comblé depuis | **Oui — mais périmée** | **Moyenne** |
| **Température de la scène pivot** | prd.md §2.3 UJ-1 : « mercredi s'annonce à **31 °C** ressentis… au-dessus du seuil de **28 °C** » ; FR-10 fixe 28 °C / 40 km/h / ATMO ≥ 4 | EXPERIENCE *Voice and Tone* et parcours 1, étape 8 et 11 : « **34 °C** » (trois occurrences). Les maquettes portent encore « **32 °C** ». Aucun des trois seuils du PRD n'apparaît dans les spines | **Non** | **Faible** |
| **Question ouverte adressée par *Voice and Tone*** | prd.md §11.3 est désormais « **Le niveau reste une inférence sans vérification** » ; le ton figure dans les *questions fermées* et renvoie à `EXPERIENCE.md` | EXPERIENCE *Voice and Tone* : « Cette section répond à la **question ouverte n° 3** du PRD (“le ton du bot n'a pas été discuté”) ». La citation n'existe plus et le numéro pointe ailleurs | **Oui — mais périmée** | **Faible** |
| **(interne au couple)** Frappe au vol | — | EXPERIENCE *Interaction Primitives* : la frappe au vol est « **retirée** » (WCAG 2.1.4). EXPERIENCE *Responsive & Platform*, dernière ligne du tableau : « **Frappe au vol et Échap arment le champ** ». Déjà signalé par `review-drift-prd-ux.md`, **non corrigé** | **Non** | **Moyenne** |

**Bilan : 18 points, dont 14 silencieux.** Les 4 tracés le sont contre un texte de PRD qui n'existe plus : ce ne sont plus des arbitrages, ce sont des accusations périmées. Un lecteur aval qui suit l'encadré de *Foundation* ira corriger dans le PRD une phrase qui a déjà été corrigée, et conclura que le corpus est instable.

---

## 2. Fidélité de nommage

**La traçabilité par identifiant est quasi inexistante, et c'est la cause mécanique de tout le reste.**

- `EXPERIENCE.md` ne cite nommément que **FR-4, FR-9 et FR-13** — 3 exigences sur 15. `DESIGN.md` n'en cite **aucune**. Il n'existe aucune matrice de couverture, donc aucun moyen de constater qu'une exigence neuve (FR-14, FR-15) est arrivée en amont.
- **`UJ-1` est cité une fois**, dans une balise `[ASSUMPTION]`. **`UJ-2` n'est jamais nommé**, alors que le parcours 2 prétend le réaliser — et le renomme (« Sarah » pour « Nadia »), ce qui rend le lien indétectable par recherche textuelle.
- **Aucune FR inexistante n'est référencée** — FR-4, FR-9 et FR-13 existent et sont correctement désignées. Le défaut n'est pas la fausse citation, c'est le silence.

**Citations approximatives et numéros décalés :**

| Citation dans la spine | Texte réel de la source | Nature |
|---|---|---|
| « Le PRD §6 énonce l'inverse : *Le site s'utilise au téléphone via le navigateur ; c'est le cas d'usage principal.* » | §6 dit aujourd'hui : « **Le navigateur d'un ordinateur est le cas d'usage principal** » | Citation d'une version disparue, présentée comme actuelle |
| « la question ouverte n° 3 du PRD (*le ton du bot n'a pas été discuté*) » | §11.3 = « Le niveau reste une inférence sans vérification » ; le ton est fermé | Numéro décalé + citation disparue |
| « le PRD laisse ouvert (**question 6**) si un SMS part réellement » | §11 ne compte que 5 questions ; celle-ci est fermée par « oui » | Renvoi à une question inexistante |
| « le PRD a arbitré pour “partenaire” » (interdit de vocabulaire) | Exact — §3, entrée *Partenaire* | ✅ conforme |
| « une contre-métrique explicite contre le bot qui *paraît attentif et devient pénible* (SM-C2) » | Verbatim exact de SM-C2 — mais SM-C2 mesure **le nombre de tours avant la première proposition**, pas l'auto-félicitation que la règle de ton en tire | Citation exacte, usage détourné |
| « 55 % des recherches » | §2.3 et §5.2 : 55 % des **combinaisons de la grille**, sans résultat **exact** | Requalification silencieuse d'une statistique |
| « Anna, Iris et Tessa » (parcours 1) | FR-6 : verbatim identique | ✅ conforme — mais les **jours** de Iris et Tessa sont faux dans les maquettes (déjà signalé, non corrigé) |

Les questions ouvertes du PRD étant numérotées par une liste ordonnée sans identifiant stable, **toute renumérotation en amont casse silencieusement toutes les citations aval**. C'est arrivé deux fois en une journée.

---

## 3. Exigences orphelines

Une exigence est *orpheline* quand aucune surface, aucun composant, aucun état et aucun parcours des deux spines ne lui donne de foyer. **18 orphelines, dont 4 NFR.**

### Exigences fonctionnelles

| # | Exigence orpheline | Localisation source | Sévérité |
|---|---|---|---|
| O1 | **FR-15 en entier** — établir le niveau par des faits vérifiables, au plus deux questions, niveau propre au sport, ne jamais réciter le verdict | prd.md l. 276–307 | **Critique** — c'est la promesse centrale du produit, et c'est une exigence **neuve** que les spines n'ont jamais vue |
| O2 | **FR-14 en entier** — page d'acceptation hors conversation, lien à usage unique, message auto-explicatif, sortie définitive du vivier, conflit de créneaux, lien déjà utilisé / expiré / désinscrit | prd.md l. 567–597 ; §9 périmètre ; addendum *Intégrations* | **Critique** — une surface entière du MVP sans une ligne d'UX |
| O3 | **FR-13, statuts *déclinée* et *expirée*** — état, jeton de couleur, microcopie (« il / elle a décliné », « personne n'a répondu à temps »), et « reste consultable dans le fil » | prd.md l. 542–566 | **Critique** — DESIGN n'a pas de jeton disponible : `status-danger` est verrouillé sur la jouabilité |
| O4 | **FR-13** — « tout changement de statut … **met à jour l'événement d'agenda** » | prd.md, FR-13 | Élevée |
| O5 | **FR-12** — contenu de l'événement d'agenda (sport, prénom du partenaire, lieu, jour, heure, statut ; aucun numéro) | prd.md l. 528–541 | Élevée — **déjà signalé par `review-drift-prd-ux.md`, non traité** |
| O6 | **FR-11** — « chaque lieu proposé indique s'il est **couvert ou en extérieur** » | prd.md l. 506 | Élevée — c'est l'attribut dont dépend FR-10 |
| O7 | **FR-11** — secteur / arrondissement facultatif, enregistré au profil et réutilisé | prd.md l. 508–511 | Moyenne |
| O8 | **FR-10** — « pour un lieu couvert, le bot **ne mentionne aucune condition extérieure** » | prd.md l. 481 | Élevée — aucun état ne distingue couvert / extérieur |
| O9 | **FR-10** — les trois seuils (28 °C ressentis, 40 km/h, ATMO ≥ 4) | prd.md, tableau §5.3 | Moyenne — le memlog UX les déclarait « non fixés » ; ils le sont depuis |
| O10 | **FR-9** — validité 60 jours, notification d'expiration, alertes multiples simultanées | prd.md l. 432–450 | Moyenne — la spine écrit « aucune promesse de délai », ce qui n'est pas un foyer |
| O11 | **FR-6** — ordre des candidats par **délai d'attente croissant**, ordre du vivier à égalité, et « au-delà de trois, le bot dit combien il y en a d'autres et propose de les montrer » | prd.md l. 388–395 | Élevée — la spine plafonne à trois et bannit le carrousel, sans dire lesquels ni comment montrer les autres |
| O12 | **FR-3** — seconde demande d'un profil connu : un sport nouveau **s'ajoute**, un sport connu **se met à jour** | prd.md l. 316–325 | Moyenne — **déjà signalé, non traité** ; le parcours 3 est bâti sur une personne qui ne demande rien |
| O13 | **FR-2** — « une demande qui vise explicitement **une autre ville que Lyon** reçoit une réponse explicite » | prd.md l. 269–270 | Moyenne — la spine a l'état *Sport hors vivier*, pas son jumeau géographique |
| O14 | **§7** — face à une demande de liste / carte / filtre, « donner ce qu'il peut sous une **forme plus dense**, et **noter la demande** » | prd.md l. 666–669 | Moyenne — garde-fou mesuré par SM-5, sans foyer, et contredit par l'état *Hors périmètre* |

### Exigences non fonctionnelles — les plus oubliées, comme prévu

| # | NFR orpheline | Localisation source | Sévérité |
|---|---|---|---|
| O15 | **Latence conversationnelle** — signe de vie **< 2 s**, réponse complète **< 20 s**, et au-delà « le bot dit ce qu'il est en train de faire **et pourquoi c'est long** » | prd.md l. 603–607 | Élevée — les lignes d'étape couvrent le *signe de vie*, mais **aucun chiffre, aucun seuil, aucun état de dépassement** n'existe dans les spines |
| O16 | **Plancher de 360 px** de large | prd.md l. 619–620 | Moyenne — la spine n'a qu'un point de rupture (720 px) et ne nomme aucune largeur minimale ; « 360 » n'apparaît nulle part |
| O17 | **Rétention de 30 jours** du fil d'un visiteur sans compte, puis effacement | prd.md l. 613–616 | Moyenne — non seulement orpheline, mais **contredite** (cf. §1) |
| O18 | **Robustesse** — « sans agenda la rencontre existe et **le bot propose de réessayer l'écriture plus tard** » est couvert ; « sans météo la rencontre se prend **sans contrôle de jouabilité et le bot le dit** » n'a pas d'état propre (l'état *Service externe indisponible* est générique) | prd.md l. 608–612 | Faible |

**Rien de l'addendum n'est orphelin en tant que tel** — il est presque entièrement architectural. Sa seule conséquence d'interface, « le lien d'acceptation : page web hors conversation, seule surface du produit qui vit en dehors du fil », est l'orpheline O2.

---

## 4. Dérive inverse (élargissement de périmètre)

Il faut distinguer ce qui est la conséquence légitime d'une décision d'interface de ce qui est une décision de **produit** prise en UX.

### Ajouts de produit — non autorisés par le PRD

| Ajout | Où | Pourquoi c'est un ajout de produit |
|---|---|---|
| **Demander la ville à l'utilisateur** | EXPERIENCE : composant *Proposition de lieu*, état *Ville inconnue*, parcours 1 étape 6, règle de ton n° 3 (« Ville, niveau, compte, accès agenda ») | Le PRD a **supprimé** cette question (§5.4 : « il n'y a pas de ville à demander ») au profit d'un *secteur* facultatif. La spine crée un champ de profil, un état bloquant (« tant qu'elle manque, aucun lieu n'est proposé ») et un tour de conversation qui n'existent pas — et qui coûtent directement sur SM-C2 |
| **Persistance illimitée du fil anonyme** | EXPERIENCE *Interaction Primitives*, *Charge cognitive* | Promesse de rétention indéfinie d'une conversation non authentifiée : c'est une décision de conservation de données personnelles, pas d'interface. Le PRD la borne à 30 jours ; §7 *Vie privée* ne traite toujours pas le fil anonyme |
| **Réduction du modèle de statut à deux valeurs** | EXPERIENCE *Component Patterns* ; DESIGN *Colors*, *Components* | Un **rétrécissement** de périmètre décidé en UX : deux statuts du PRD deviennent inexprimables. C'est de la dérive inverse par soustraction, plus dangereuse que l'ajout, parce qu'elle ne se voit pas |
| **« Un composant qui ne peut pas vivre dans le fil ne fait pas partie du produit »** | EXPERIENCE *Foundation* | Formulée comme un principe d'interface, elle **exclut du produit** une exigence explicitement dans le périmètre MVP (FR-14, page d'acceptation) |
| **« Le niveau se déclare dans la phrase »** | EXPERIENCE *Inspiration & Anti-patterns* | Réintroduit l'auto-déclaration que FR-15 et le glossaire interdisent. Ce n'est pas un choix d'interface : c'est le mécanisme central du produit, remplacé |
| **Deux lieux au maximum** | EXPERIENCE *Proposition de lieu* | Plafond d'affichage non arbitré ; UJ-1 en montre deux, mais le PRD ne fixe rien. Comme le plafond de trois candidats (que le PRD a fini par adopter), un plafond crée une troncature, et une troncature sans règle d'ordre est une décision produit laissée à l'implémentation |

### Conséquences légitimes d'une décision UX — à conserver

- **Le fil comme application entière, sans navigation ni tableau de bord** — élaboration directe du §1 (« une conversation ») et des non-objectifs §8. Le point de rupture est même énoncé honnêtement (« au-delà de deux ou trois rencontres, un récapitulatif en prose devient illisible »).
- **Cartes cliquables + équivalent dicible** — l'exigence de plafond à trois a depuis été adoptée par le PRD (FR-6) : la boucle s'est refermée correctement.
- **Thème sombre exclusif, sans bascule** — parti esthétique, sans conséquence produit ; assumé explicitement.
- **Section *La grammaire de l'honnêteté*** — traduction d'interface du §7 ; c'est le meilleur travail du couple et il n'ajoute rien au périmètre.
- **Section *Les deux populations du vivier*** — traduction du §4… mais **fondée sur la version périmée du glossaire** (cf. §1). L'intention est légitime, le contenu est faux.
- **Plancher d'accessibilité (`role="log"`, région `role="status"`, cibles 48 px, retrait du raccourci à touche unique)** — conformité, jamais du périmètre produit.
- **Parcours 3 (Thomas revient et ne demande rien)** — **correctement tracé** comme `[ASSUMPTION]` dérivé de la NFR *Reprise de conversation*. C'est le modèle de ce qu'aurait dû être chaque divergence.
- **Les étapes narrées comme trace vérifiable** — le PRD les a depuis adoptées en §7 et en addendum. Boucle refermée.

---

## 5. Glissements de glossaire

Le §3 du PRD se déclare **contraignant** (« les exigences fonctionnelles l'emploient littéralement, sans synonyme »). Sept glissements :

| Terme | Sens au PRD | Sens dans les spines | Effet |
|---|---|---|---|
| **Profil d'amorçage** | « Ne parle jamais au bot — **mais peut accepter** une rencontre en suivant le lien de son SMS » | « **incapables de répondre** », « reste en attente **indéfiniment** » | Le terme a changé de sens **en amont** ; la spine conserve l'ancien et en tire une règle de produit fausse. **Le plus grave** |
| **Niveau** | « les valeurs internes du produit, **jamais une question posée** », déduites de faits (FR-15) | « le niveau **se déclare dans la phrase** » ; état *Demande incomplète* déclenché par « niveau manquant » | Le niveau redevient une saisie utilisateur — l'exact contraire |
| **Candidat / Partenaire** | « Un **candidat** est un profil que la recherche a retenu et que le bot présente, **avant** que l'utilisateur en retienne un. Un candidat retenu devient un *partenaire* » | « **Carte de partenaire** », dès l'affichage des trois propositions ; « candidat » n'apparaît qu'**une fois** dans EXPERIENCE | Le composant central du produit porte le mauvais mot du glossaire, à l'étape où la distinction existe précisément |
| **Rencontre** | Quatre statuts nommés, « c'est le seul mot du glossaire pour cet objet » | Deux statuts ; *déclinée* et *expirée* n'existent ni en mot, ni en jeton, ni en état | Deux tiers du vocabulaire de statut est perdu |
| **Ville / secteur** | Aucune entrée « ville » ; FR-11 parle de **secteur** ou **arrondissement**, dans une agglomération unique (Lyon) | « ville » employé six fois comme donnée de profil ; « Lyon », « secteur » et « arrondissement » : **zéro occurrence** | Un terme absent du glossaire est promu en concept structurant ; le terme réel est perdu |
| **Utilisateur / la personne** | « **Utilisateur inscrit** », « l'utilisateur », « un visiteur » | « la personne », systématiquement | Choix défendable (un visiteur n'est pas un inscrit) mais **absent du glossaire** ; déjà signalé par la relecture précédente, jamais porté en amont |
| **Demande** | « ce que l'utilisateur exprime : un sport, un ou plusieurs jours, un niveau » ; §6 : « retrouve **ses demandes**, ses alertes et ses rencontres » | Reprise = « les **rencontres et alertes** en cours » | Une demande sans rencontre ni alerte n'est pas reprise : écart de couverture qui se lit comme un synonyme |

Le PRD est lui-même en faute sur deux d'entre eux : **« secteur » et « arrondissement » ne sont pas au glossaire** alors que FR-11 les emploie, et le glossaire dit du vivier « **il grossit ; il ne diminue pas** » quand FR-14 permet d'en sortir définitivement. Voir §7.

---

## 6. Fidélité à la recherche

**Globalement bonne, avec une infidélité grave et deux amplifications.**

### Fidèle

- « **Aucun produit grand public de mise en relation entre joueurs n'utilise le chat comme interface principale** » (EXPERIENCE *Inspiration*, DESIGN *Brand & Style*) — reprend `research-paysage.md` §3 sans le durcir, et en tire la bonne conséquence : « il n'existe pas de modèle à imiter, ce qui rend les anti-patterns d'autant plus importants ».
- Le verbatim Trustpilot « aucun moyen de parler à un vrai humain, toujours renvoyé vers un chatbot » est cité **exactement**, attribué à la bonne source, et transformé en anti-pattern précis (pas de bulle flottante, pas d'avatar, pas de badge).
- « **niveaux gonflés de 0,5 à 1,0 point qui mettent très longtemps à se corriger** » — conforme à `research-niveau.md` §1 (Playskan + ProperPadel).
- « **la cause de mort n° 1 de cette catégorie** » (densité, parcours 2) — conforme à `research-paysage.md` §2 et §4, premier régime d'échec.
- « **En réserve — l'incertitude affichée** (UTR *Projected*, astérisque DUPR) » — conforme à §2(d) et §3, et honnêtement rangé en réserve.
- Le rejet du classement public s'appuie sur §4.7 de `research-niveau.md` : conforme, et c'est aussi un non-objectif du PRD.

### Infidèle

- **`research-niveau.md` §4.1 dit exactement l'inverse de ce que la spine en tire.** La recherche écrit : « **Amorcer par un questionnaire comportemental, pas une auto-étiquette.** Demander des faits vérifiables… **Ne jamais proposer “débutant/intermédiaire/avancé” comme saisie.** » Le PRD en a fait FR-15. La spine, elle, rejette le questionnaire Playtomic puis conclut : « **Ici le niveau se déclare dans la phrase**, au fil de la conversation, ce qui **ne le rend pas plus exact** mais évite d'installer un rituel d'évaluation ». Elle transforme la parade sourcée en simple économie de rituel, et **rétablit l'auto-déclaration que la source condamne**. C'est la seule infidélité qui change ce que le produit fait.

### Amplifications

- « **la plainte n° 1 des plateformes à l'échelle porte justement sur l'intégrité de la note** » — `research-paysage.md` §4 dit que c'est la principale cause de churn **pour les apps de réservation à l'échelle**, et cite la friction financière et les no-shows au second ordre. « Plainte n° 1 » durcit légèrement ; sans conséquence pratique.
- « **Le produit délivre une mauvaise nouvelle dans 55 % des recherches** » — ce chiffre n'est pas de la recherche mais du PRD, et le PRD interdit explicitement de le lire comme un taux vécu (`[NOTE FOR PM]`, §5.2). L'amplification est réelle et elle **dimensionne un parcours entier** (cf. §1).

---

## 7. Dette amont — à corriger dans le PRD

Ordonnée par impact sur un consommateur aval. Ces items sont à corriger **dans `prd.md`**, pas dans les spines.

1. **Donner un identifiant stable aux questions ouvertes du §11** (l. 805–837). Elles sont aujourd'hui une liste ordonnée : la fermeture de la question du ton et l'ajout de FR-15 ont décalé toute la numérotation en une journée, et les deux spines pointent désormais vers « la question n° 3 » et « la question 6 » — l'une désigne autre chose, l'autre n'existe pas. Numéroter `QO-1`…`QO-n` et **conserver les entrées fermées à leur numéro** au lieu de les déplacer dans une seconde liste.

2. **Résoudre la contradiction interne du glossaire sur le vivier** — §3, l. 169 : « Il grossit ; **il ne diminue pas** » contre FR-14 (l. 583) : « un moyen de **ne plus jamais être contacté** ; l'exercer **retire le profil du vivier définitivement** ». Deux exigences du même document se contredisent sur la propriété la plus structurante de l'objet central. C'est la seule contradiction *interne* au PRD qu'aucun aval ne peut arbitrer.

3. **Ajouter *secteur* et *arrondissement* au glossaire §3** (l. 164–204), employés par FR-11 (l. 508–511) alors que le §0 déclare le vocabulaire du §3 contraignant et sans synonyme. En l'état, le seul terme géographique disponible pour l'aval est « ville », qui est précisément celui que le §5.4 interdit — ce qui explique mécaniquement le glissement des spines.

4. **Ajouter un journal des modifications, ou au minimum une ligne de version dans le frontmatter.** Le PRD a changé de statut (`draft` → `final`), gagné deux exigences (FR-14, FR-15), fixé trois seuils, changé de surface principale et **modifié le sens de deux entrées du glossaire**, tout en gardant `updated: 2026-08-26` — la même date que les spines qu'il invalide. Aucun aval ne peut détecter qu'il a bougé. C'est la cause racine des 18 points du §1.

5. **Signaler dans le §0 quels documents aval sont invalidés.** Le §0 (l. 20–23) pointe vers `EXPERIENCE.md` et `DESIGN.md` comme documents dérivés, sans dire que leur encadré de divergence sur la surface, leurs deux `[ASSUMPTION]` et leur modèle de statut sont périmés. Le PRD est le seul document en position de le dire.

6. **Spécifier le comportement de FR-10 quand l'attribut couvert / extérieur est inconnu** — §5.3, l. 481. Trois cas existent (extérieur, couvert, attribut absent) et deux sont spécifiés. Or le §11.4 reconnaît que la source des terrains n'est pas identifiée : le troisième cas est aujourd'hui **le plus probable**, et c'est celui que ni le PRD ni les spines ne décrivent.

7. **Donner une exigence testable au garde-fou §7 *L'enfermement dans la conversation*** (l. 660–669). Il prescrit un comportement précis — « donner ce qu'il peut sous une forme plus dense, et **noter la demande** » — et SM-5 le mesure, mais aucune FR ne le porte. Un garde-fou mesuré sans exigence n'est construit par personne : les spines ont d'ailleurs écrit le comportement inverse.

8. **Traiter le fil du visiteur anonyme au §7 *Vie privée*** (l. 671–698). La NFR §6 crée une rétention de 30 jours d'une conversation non authentifiée — une donnée personnelle conservée sans compte — et §7 n'en dit rien, alors qu'il traite en détail les numéros de téléphone et l'asymétrie de consentement. La relecture précédente l'avait demandé ; seule la durée a été ajoutée, pas le traitement.

9. **Rendre contraignante la règle de nommage des protagonistes** — §11.1 (l. 806–809) la formule comme un constat (« les prénoms ont été choisis absents des données d'amorçage ») et non comme une contrainte pour l'aval. Résultat : le parcours 2 des spines a été rebaptisé « Sarah », prénom du seul profil d'amorçage de Pilates. Une phrase impérative dans §2.3 suffit.

10. **Marquer les chiffres narratifs de UJ-1 comme illustratifs ou les aligner sur FR-10** — §2.3 raconte 31 °C ressentis et 19 h à 24 °C, FR-10 fixe le seuil à 28 °C, les spines racontent 34 °C et les maquettes 32 °C. Quatre nombres pour une seule scène, dont trois sans source. Soit UJ-1 devient l'exemple canonique et l'aval le recopie, soit il porte une mention explicite d'illustration.

11. **Reformuler l'`[ASSUMPTION]` du §6** (l. 601) pour distinguer ce qui est encore une hypothèse. Les bornes 2 s / 20 s / 30 jours / 360 px y sont regroupées comme « posées par défaut », ce qui les fait lire comme négociables — et les spines les ont toutes ignorées (§3, O15–O17). Une NFR que l'aval croit provisoire n'est pas une NFR.

---

*Aucun fichier existant n'a été modifié par cette relecture.*
