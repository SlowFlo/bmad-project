# Relecture de dérive — PRD ↔ UX

- **PRD relu :** `documentation/planning-artifacts/prds/prd-bmad-2026-08-26/` (prd.md `status: draft`, addendum.md, .memlog.md, research-niveau.md, research-paysage.md, SportsProfiles.csv)
- **Travail UX relu :** `documentation/planning-artifacts/ux-designs/ux-bmad-2026-08-26/` (EXPERIENCE.md et DESIGN.md `status: final`, .memlog.md, 3 maquettes, validation-report.md, review-rubric.md, review-accessibilite.md)
- **Date :** 2026-08-26

## Verdict global

Le travail UX est **substantiellement fidèle** : le glossaire du §3 est tenu à la lettre, la règle « le jour se négocie, le niveau se défend » est reproduite sans glissement, et l'état dominant du produit — 55 % de recherches sans candidat — est réellement traité en chemin nominal. La dérive dominante n'est pas un dépassement de mandat : c'est une **avance**. L'UX a tranché, presque toujours bien, ce que le PRD avait laissé ouvert (le nom du produit, le ton, la surface principale, le canal de notification, l'heure du rendez-vous), et le PRD, resté en `draft`, n'a rien rattrapé — il porte aujourd'hui au moins trois affirmations devenues fausses pendant que les deux spines qui en dérivent sont en `final`. Le sens de la correction est donc massivement **PRD rattrape UX**. Les deux seuls vrais dépassements sont dans les maquettes, et tous deux touchent la contrainte que le PRD qualifie lui-même de la plus structurante : un seuil de température chiffré là où le PRD dit explicitement ne pas l'avoir fixé, et un profil d'amorçage montré en train de confirmer alors que le glossaire dit qu'il « ne répond jamais ».

## Ce qui tient

Court, mais réel — à ne pas rouvrir :

- **Le glossaire §3.** Les dix termes (*vivier*, *profil d'amorçage*, *utilisateur inscrit*, *partenaire*, *niveau*, *jour disponible*, *demande*, *élargissement*, *rencontre*, *jouabilité*) sont employés au sens du PRD, sans synonyme. L'UX va jusqu'à en faire des interdits de microcopie : « adversaire » quand il ne s'agit pas d'un sport de duel, « réservé », « confirmé » sur une rencontre qui ne l'est pas.
- **La règle de matching.** FR-5 → FR-8 sont reproduits état par état, y compris « Débutant et Avancé ne se croisent jamais » et « le niveau n'est pas commenté : il est tenu » sur l'élargissement jour.
- **Le vivier vide comme état principal.** `State Patterns` l'écrit littéralement : « État **principal**, pas une erreur ». C'est le constat le plus coûteux du PRD et il a survécu intact.
- **Les deux populations.** La carte identique pour un profil d'amorçage et un utilisateur inscrit, la différence reportée au seul statut de la rencontre, aucun numéro de téléphone nulle part : c'est le §4 du PRD rendu en interface, sans le travestir.
- **Les questions ouvertes 1, 5 et 6 sont laissées ouvertes honnêtement.** Le prénom substitut est reconduit avec son `[ASSUMPTION]`, le niveau reste déclaratif, et l'UX écrit que l'expérience « est rédigée pour être vraie dans les deux cas » sur la question du SMS aux 86 personnes.
- **Les non-objectifs.** Pas de catalogue, pas de note visible, pas de réservation, pas de profils à parcourir : la section `Inspiration & Anti-patterns` les rejette nommément.

## Constats

### critique — La maquette fixe un seuil de jouabilité que le PRD déclare non fixé

- **Côté PRD :** FR-10, §5.3, *Notes* : « `[NOTE FOR PM]` les seuils — à partir de quelle température, de quelle vitesse de vent, de quel indice de qualité d'air — **ne sont pas fixés**. Ils appartiennent au produit, pas à l'architecture. **À trancher avant l'implémentation.** » Repris en question ouverte §11.2.
- **Côté UX :** `mockups/key-recap-en-attente.html`, l. 137 et 188, deux fois : « **Au-dessus de 32 °C**, l'effort soutenu devient risqué. Je vous propose plutôt 19 h : 26 °C, vent faible, qualité de l'air correcte. » Le memlog UX affirme pourtant le contraire : « *(event) Hors perimetre UX, renvoye au PRD : les seuils de jouabilite […] restent non fixes […] L'UX specifie le COMPORTEMENT […] sans fixer les valeurs.* »
- **Nature :** question ouverte tranchée en douce — doublée d'une contradiction interne au dossier UX (le memlog dit ne pas trancher, la maquette tranche).
- **Sens de la correction :** le PRD rattrape. La valeur écrite dans une maquette est celle qu'un développeur recopiera, et elle n'a été arbitrée par personne. 32 °C n'est pas absurde, mais il n'a pas de source : ni le PRD, ni l'addendum, ni les deux recherches ne contiennent le moindre seuil.
- **Correction proposée :** trancher les trois seuils (chaleur, vent, indice de qualité d'air) dans FR-10 et fermer la question §11.2 ; puis, dans la maquette, remplacer le chiffre en dur par la valeur ainsi arbitrée. Si l'arbitrage ne peut pas se faire maintenant, neutraliser la phrase de la maquette (« Il fait trop chaud pour un effort soutenu ») pour qu'aucun nombre non décidé ne circule en aval.

### critique — La maquette montre Anna, profil d'amorçage, en train de confirmer

- **Côté PRD :** §3, glossaire : « **Profil d'amorçage** — […] N'a ni compte, ni e-mail, ni ville. **Ne répond jamais.** » Et §4 : « Un partenaire issu d'un profil d'amorçage donne une rencontre *en attente* **qui ne sera jamais confirmée**, et l'utilisateur le sait. » FR-13 réserve le passage à *confirmée* au seul utilisateur inscrit.
- **Côté UX :** la maquette se contredit dans le même fichier. `mockups/key-recap-en-attente.html` l. 118 : « **Anna est un profil d'amorçage : elle ne répondra jamais.** » Puis l. 222, titre du troisième cadre : « **Anna confirme** — la pastille change sur place, l'annonce ne se tait pas », avec la pastille *Confirmée* et la région de statut « Anna a confirmé. Mercredi 3 septembre, 19 h. » EXPERIENCE.md, *Les deux populations du vivier*, dit pourtant : « Un profil d'amorçage produit une rencontre *en attente* que le bot n'annonce jamais comme prête à basculer. »
- **Nature :** contradiction.
- **Sens de la correction :** l'UX recule. Le besoin de montrer l'état *confirmée* est légitime — FR-13 l'exige — mais il ne peut pas être illustré par Anna.
- **Correction proposée :** dans le troisième cadre, remplacer Anna par une partenaire explicitement présentée comme utilisatrice inscrite, et ajouter une ligne au commentaire de la maquette (« ce cadre n'est atteignable qu'avec un utilisateur inscrit »). Ajouter symétriquement à `State Patterns`, ligne *Rencontre confirmée*, la mention « jamais atteignable depuis un profil d'amorçage ».

### élevé — Les cartes de la maquette affichent des disponibilités qui contredisent les données d'amorçage

- **Côté PRD :** §7, *Le bot n'invente rien* : « Aucun nom de partenaire qui ne vienne du vivier. Aucune donnée météo, aucun terrain, **aucune disponibilité inventés**. » `SportsProfiles.csv` : `Iris,Payet,…,Tennis,Lundi;Mercredi,Intermédiaire` et `Tessa,Armand,…,Tennis,Lundi;Samedi,Intermédiaire`.
- **Côté UX :** `mockups/key-proposition-partenaires.html` : « Iris — Intermédiaire · **samedi, dimanche** » et « Tessa — Intermédiaire · **lundi, jeudi** ». Seule Anna (« mercredi, samedi ») est conforme. La maquette se présente pourtant comme la preuve du garde-fou : « Ce que la maquette prouve ».
- **Nature :** contradiction (avec la donnée d'amorçage, et avec le garde-fou que la maquette illustre).
- **Sens de la correction :** l'UX recule.
- **Correction proposée :** recopier les jours du CSV dans les trois cartes. Le coût est nul et l'exemplaire redevient citable par l'aval.

### élevé — Le PRD affirme toujours que le téléphone est l'usage principal

- **Côté PRD :** §6, exigences non fonctionnelles : « **Responsive.** Le site s'utilise au téléphone via le navigateur ; **c'est le cas d'usage principal.** »
- **Côté UX :** EXPERIENCE.md, *Foundation* : « **Surface unique : le web responsive, conçu pour le PC d'abord.** […] Le PRD §6 énonce l'inverse […] Cette phrase est **caduque** — l'utilisateur a corrigé la surface principale en cours de conception UX. […] **la correction du PRD est à porter en amont.** » Le memlog UX est plus net encore : « *(override) REVIREMENT DE SURFACE […] le PRD porte desormais une affirmation fausse a corriger en amont.* »
- **Nature :** contradiction franche, correctement tracée côté UX, jamais portée côté PRD.
- **Sens de la correction :** le PRD rattrape. L'arbitrage est légitime (signal vivant de l'utilisateur) et il est déjà rendu lisible en aval ; ce qui manque est l'amont. Un architecte qui lit le PRD d'abord dimensionnera pour le mobile.
- **Correction proposée :** réécrire la NFR *Responsive* du §6 (« Le navigateur d'un PC est le cas d'usage principal ; le mobile est servi à parité fonctionnelle complète »), et laisser l'encadré de divergence d'EXPERIENCE.md en place jusqu'à ce que le PRD soit corrigé.

### élevé — Le produit a un nom, décidé en UX, absent du PRD

- **Côté PRD :** frontmatter `title: "Trouve-moi un partenaire — chatbot de mise en relation sportive"` et, sous le titre : « *Titre de travail, à confirmer.* »
- **Côté UX :** memlog : « *(decision) NOM DU PRODUIT retenu : 'Ex Aequo'. Terme du classement sportif […] Remplace le titre de travail 'Trouve-moi un partenaire' du PRD.* » Le nom est devenu structurel : `name: Ex Aequo` dans les deux frontmatters, une section entière de `DESIGN.md.Brand & Style` le justifie, et il est dans la microcopie du produit (« Ex Aequo : », « Écrivez à Ex Aequo »).
- **Nature :** décision produit prise en UX, absente du PRD. Le PRD l'avait explicitement laissée ouverte, donc l'UX n'a pas dépassé son mandat — mais le nommage est une décision de produit, pas de design, et elle n'existe que dans un memlog que l'aval ne lit pas.
- **Sens de la correction :** le PRD rattrape.
- **Correction proposée :** porter « Ex Aequo » dans le `title` du PRD et retirer la mention « titre de travail ». Sans cela, toute recherche aval sur le nom du produit échoue d'un côté ou de l'autre de la chaîne.

### élevé — L'heure du rendez-vous : le PRD l'exclut, l'UX la collecte

- **Côté PRD :** FR-2, *Hors périmètre* : « l'heure de la journée. Les données d'amorçage ne descendent pas sous le jour ; “mardi après-midi” est traité comme “mardi”. » Repris au §9, hors périmètre MVP : « L'heure de la journée dans les disponibilités ». Mais FR-12 exige un événement d'agenda, et UJ-1 dit « il suggère plutôt le début de soirée » — le PRD ne dit jamais d'où sort une heure.
- **Côté UX :** *Key Flows*, parcours 1, étape 8 : « **L'heure se décide ici, et c'est la jouabilité qui l'amène.** Le vivier ne connaît que des jours, jamais des heures : le produit n'a donc aucune heure à proposer tant qu'il n'a pas de raison. […] **Sans alerte de jouabilité, le bot demande simplement l'heure en une phrase.** »
- **Nature :** PRD non couvert, comblé en UX. Le rubric l'avait relevé (« Aucun beat ne pose l'heure du créneau ») et le correctif n'a été appliqué que du côté UX.
- **Sens de la correction :** le PRD rattrape. La réponse de l'UX est bonne et doit être adoptée, pas défaite — mais telle quelle, le PRD dit « l'heure est hors périmètre » et l'UX dit « le bot demande l'heure ».
- **Correction proposée :** distinguer explicitement dans le PRD **l'heure de disponibilité** (hors périmètre, donnée du vivier) et **l'heure de la rencontre** (nécessaire à FR-12), et ajouter une conséquence testable à FR-10 ou FR-12 : l'heure est proposée par la jouabilité, ou demandée en une phrase à défaut.

### élevé — Le canal de notification est inventé en UX alors que le PRD savait qu'il manquait

- **Côté PRD :** FR-9 : « le bot propose d'enregistrer la demande et de **prévenir l'utilisateur** si un profil correspondant rejoint le vivier » — aucun canal. Même silence pour FR-13. Le memlog du PRD avait pourtant identifié le trou : « *(decision) Surface = web responsive uniquement (pas de mobile natif) -> consequence produit a traiter : pas de push natif, il faut un autre canal pour notifier qu'un adversaire a repondu* ». Cette conséquence n'a jamais été portée dans le PRD, ni en FR, ni en question ouverte.
- **Côté UX :** EXPERIENCE.md, *Information Architecture* : « `[ASSUMPTION: le canal d'alerte différée est l'e-mail, récupéré au moment de la connexion Google/Microsoft. Le PRD a identifié le trou […] sans le combler.]` » et *Responsive & Platform* : « **Pas de notification native.** […] Deux besoins en dépendent — l'alerte différée (FR-9) et la confirmation d'un partenaire (FR-13) — et tous deux sortent du produit vers un canal externe. »
- **Nature :** décision UX absente du PRD — posée honnêtement en hypothèse, mais c'est une capacité produit et une intégration tierce, pas un choix d'interface.
- **Sens de la correction :** le PRD rattrape.
- **Correction proposée :** nommer le canal dans FR-9 avec une conséquence testable, ajouter une septième question ouverte si l'arbitrage n'est pas mûr, et ajouter la ligne correspondante au tableau des intégrations de `addendum.md` (aujourd'hui : agenda, météo, terrains — pas d'e-mail sortant).

### élevé — « Trois candidats au maximum » est une règle produit inventée en UX, sans règle de sélection nulle part

- **Côté PRD :** FR-6, conséquence testable : « “Tennis, mardi, intermédiaire” renvoie **Anna, Iris et Tessa** avec leurs jours respectifs. » Aucun plafond, aucun critère d'ordre, aucun comportement au-delà de trois candidats.
- **Côté UX :** `Component Patterns`, carte de partenaire : « **Trois au maximum par proposition.** » Repris dans `DESIGN.md.Layout & Spacing` : « Les cartes de partenaires se rangent sur une ligne, **trois au maximum** ». Rien nulle part ne dit *lesquels* trois.
- **Nature :** UX a inventé — un plafond d'affichage est légitime, mais il produit mécaniquement une troncature, et une troncature sans règle d'ordre est une décision produit laissée au hasard de l'implémentation.
- **Sens de la correction :** le PRD rattrape (la règle de sélection), l'UX garde le plafond.
- **Correction proposée :** une conséquence testable dans FR-6 : critère d'ordre des candidats (proximité du jour demandé ? ordre du vivier ? aléatoire stable ?) et comportement au-delà de trois (le bot dit-il qu'il y en a d'autres ?). Sur un vivier de 86 profils la question est petite ; elle ne l'est plus quand le vivier grossit, ce qui est la promesse du produit.

### moyen — FR-4 et UJ-1 se contredisent dans le PRD ; l'UX a tranché en silence

- **Côté PRD :** FR-4, conséquences testables : « Rechercher, obtenir des propositions et consulter la jouabilité ne déclenche aucune demande de compte. **Retenir un partenaire la déclenche.** » Mais UJ-1 raconte l'inverse : Thomas répond mercredi, puis ville, puis terrains, puis météo, « Thomas valide. **C'est ici que le bot demande un compte.** »
- **Côté UX :** parcours 1 : étape 5 « Thomas clique la carte d'Anna » — pas de compte ; étapes 6 à 8, ville, lieux, jouabilité — pas de compte ; étape 9 seulement, « **Le moment du compte.** »
- **Nature :** contradiction interne au PRD, tranchée en douce par l'UX — dans le bon sens (celui de UJ-1 et du garde-fou « le compte arrive quand il devient nécessaire »), mais sans trace.
- **Sens de la correction :** le PRD rattrape.
- **Correction proposée :** reformuler la conséquence testable de FR-4 : « **Valider un créneau avec un partenaire** déclenche la demande de compte » — retenir une carte ne suffit pas.

### moyen — La question ouverte n° 3 est fermée en UX, mais le PRD la liste toujours et parle encore en tutoiement

- **Côté PRD :** §11.3 : « **Le ton du bot** n'a pas été discuté. C'est pourtant toute l'interface : tutoiement ou vouvoiement, concision ou chaleur, comment il annonce une mauvaise nouvelle. » Et le PRD fait parler le bot en tutoiement dans UJ-1 : « *Personne à **ton** niveau au tennis le mardi. […] Lequel **t'**arrange ?* »
- **Côté UX :** *Voice and Tone* : « Cette section répond à la question ouverte n° 3 du PRD » ; « **Le registre arrêté : vouvoiement, sympathique mais professionnel — pas un pote.** » Et un interdit absolu : « tout point d'exclamation dans une phrase du bot ».
- **Nature :** question ouverte tranchée — légitimement, le memlog UX indique qu'elle était « explicitement deleguee a l'UX » — mais non refermée côté PRD, dont les verbatims sont désormais faux.
- **Sens de la correction :** le PRD rattrape.
- **Correction proposée :** fermer §11.3 en renvoyant à `EXPERIENCE.md.Voice and Tone`, et réécrire au vouvoiement les répliques citées dans UJ-1 et UJ-2 — c'est le seul endroit du PRD où le produit parle, et c'est aujourd'hui le seul endroit qui parle faux.

### moyen — La deuxième demande d'une personne déjà inscrite n'existe nulle part

- **Côté PRD :** FR-3, conséquence testable : « **Le vivier ne contient pas deux profils pour la même personne.** » Le PRD ne dit pas ce que devient la première demande quand une seconde arrive, ni si un profil peut porter deux sports (les données d'amorçage n'en portent qu'un — 86 profils, un seul sport chacun).
- **Côté UX :** aucun moment, aucun état, aucun parcours. `State Patterns` a bien « Fil à froid, connu » — mais le bot « récapitule […] puis rend la parole. **Il ne relance pas, ne propose rien de lui-même** » — et le parcours 3 est bâti sur le fait que Thomas revient et **ne demande rien** : « Thomas ne demande rien. Il ferme. »
- **Nature :** PRD non couvert, et trou réel — pas un effet du périmètre des trois maquettes clés : EXPERIENCE.md revendique une fermeture d'IA (« Chaque besoin énoncé par le PRD atterrit dans un moment du fil ») avec une seule exception assumée, qui n'est pas celle-ci.
- **Sens de la correction :** arbitrage utilisateur, puis PRD, puis UX.
- **Correction proposée :** trancher si un profil porte un ou plusieurs sports, puis ajouter une conséquence testable à FR-3 (mise à jour du profil existant vs création) et une ligne d'état UX « nouvelle demande d'un profil connu ».

### moyen — Le contenu de l'événement d'agenda exigé par FR-12 n'est spécifié nulle part côté UX

- **Côté PRD :** FR-12, conséquence testable : « **L'événement porte le sport, le partenaire, le lieu et le statut de la rencontre.** »
- **Côté UX :** la seule phrase du dossier UX qui parle du contenu de l'événement est une interdiction : « Aucun numéro de téléphone n'apparaît nulle part dans l'interface. Ni dans la carte, ni dans le récapitulatif, **ni dans l'événement d'agenda**. » Le *Récapitulatif de rencontre* est spécifié en détail — mais il vit dans le fil, pas dans l'agenda. Le rubric l'avait relevé (« FR-12 est couvert à moitié ») et le correctif appliqué n'a porté que sur le bloc de choix d'agenda.
- **Nature :** PRD non couvert.
- **Sens de la correction :** l'UX complète — une ligne.
- **Correction proposée :** une entrée `Component Patterns` ou une ligne de `State Patterns` énumérant le contenu de l'événement, avec la microcopie de son titre. C'est la seule chose du produit qui survit hors du fil ; elle mérite une phrase.

### moyen — L'UX promet une persistance du fil que la NFR du PRD ne couvre pas

- **Côté PRD :** §6 : « **Reprise de conversation.** Un utilisateur **inscrit** qui revient retrouve ses demandes en cours et ses rencontres. » La promesse est bornée à l'inscrit.
- **Côté UX :** *Interaction Primitives* : « **Le fil ne se réinitialise jamais tout seul. Aucune expiration de session ne vide la conversation.** » Et *Charge cognitive* : « la seule mémoire du produit est le fil lui-même : il n'est donc **jamais purgé, jamais réinitialisé** ». Plus, dans `Component Patterns` : « **Le brouillon survit à une redirection OAuth.** »
- **Nature :** UX a inventé — l'extension de la reprise au visiteur **sans compte** est une promesse produit à conséquence directe pour l'architecture (identité anonyme persistante, durée de rétention, et une question de vie privée que le §7 n'aborde pas).
- **Sens de la correction :** le PRD rattrape, ou arbitrage utilisateur si la persistance anonyme n'est pas voulue.
- **Correction proposée :** préciser dans la NFR ce qui persiste pour un visiteur sans compte, et pendant combien de temps. Une conversation anonyme conservée indéfiniment est une donnée personnelle que le §7 ne mentionne pas.

### moyen — Les étapes narrées sont promues en garantie produit ; le PRD n'en dit rien

- **Côté PRD :** §6 : « **Latence conversationnelle.** Une réponse qui demande plusieurs étapes internes doit produire un signe de vie plutôt qu'un silence. » C'est une exigence d'attente, pas de transparence.
- **Côté UX :** *La grammaire de l'honnêteté* : « **Les étapes narrées sont une trace vérifiable.** Elles ne sont pas un habillage d'attente : **elles disent quelles sources ont réellement été consultées.** Quand la météo tombe, la ligne d'étape le montre. » Repris dans `Component Patterns` : « elles constituent la trace de ce que le bot a réellement consulté ».
- **Nature :** décision UX absente du PRD. Un signe de vie décoratif et une trace fidèle des appels d'outils ne sont pas la même exigence : la seconde contraint l'architecture agentique (chaque appel externe doit être observable et diffusé en temps réel dans le fil).
- **Sens de la correction :** le PRD rattrape.
- **Correction proposée :** une phrase dans le §7 (*Le bot n'invente rien*) plutôt que dans la NFR de latence : les étapes annoncées correspondent aux sources réellement interrogées, et une source qui n'a pas répondu est annoncée comme telle. Une note dans `addendum.md` pour l'orchestration.

### faible — Le droit de passer outre une alerte de jouabilité est décidé en UX

- **Côté PRD :** FR-10 : « Le bot propose une alternative (autre moment, autre jour) **plutôt que de se contenter d'alerter** » ; §5.3 précise que le contrôle a lieu avant validation « parce que le produit épargne un mauvais créneau plutôt que de le signaler une fois pris ». Rien sur le refus de la contre-proposition, alors que le PRD qualifie le sujet de question de **santé** et non de confort.
- **Côté UX :** `State Patterns`, *Jouabilité dangereuse* : « **La personne peut passer outre : le bot informe, il n'interdit pas.** » Matérialisé dans la maquette 3 par un bouton « **Garder 17 h** » à côté de « Retenir 19 h ».
- **Nature :** UX a inventé — élaboration défendable, mais c'est une règle produit sur le seul sujet que le PRD traite en termes de santé.
- **Sens de la correction :** le PRD rattrape, en une phrase.
- **Correction proposée :** ajouter à FR-10 une conséquence testable : l'alerte informe et n'interdit pas ; le créneau reste retenable après refus de la contre-proposition.

### faible — L'état « demande incomplète » oublie le jour

- **Côté PRD :** FR-2 : « Le bot extrait d'un message libre **le sport, les jours et le niveau**, et réclame les éléments manquants un par un. »
- **Côté UX :** `State Patterns` : « **Demande incomplète** | **Sport ou niveau manquant** | Le bot demande **un seul** élément manquant à la fois ». Le jour est absent du déclencheur, alors que c'est la dimension sur laquelle porte tout l'élargissement.
- **Nature :** PRD non couvert (omission d'un tiers de FR-2).
- **Sens de la correction :** l'UX complète — deux mots.
- **Correction proposée :** « Sport, jour ou niveau manquant ».

## Notes mécaniques

**Glossaire — dérive terme par terme.** Les dix termes du §3 sont tenus. Trois glissements mineurs, aucun bloquant :

- **« la personne »** est employé systématiquement côté UX pour désigner le visiteur (« Message de la personne », « la personne a remonté le fil »), là où le PRD dit « l'utilisateur ». Le choix est juste — un visiteur n'est pas encore un *utilisateur inscrit* — mais il n'existe pas au glossaire du PRD. À y inscrire si l'on veut que l'aval l'emploie sans hésiter.
- **PRD §6 « demandes en cours »** → UX « **rencontres et alertes** en cours » (`State Patterns`, *Fil à froid, connu* ; parcours 3). Une demande qui n'a produit ni rencontre ni alerte n'est donc pas reprise. Écart de couverture, pas de vocabulaire — mais il se lit comme un synonyme et n'en est pas un.
- **« Microsoft » (identité) vs « Outlook » (agenda)** cohabitent côté UX — cohérent avec `addendum.md` qui les distingue, mais aucun des deux documents ne l'écrit ; à inscrire au glossaire pour éviter qu'un troisième document les fusionne.

**Traçabilité des identifiants.**

- `EXPERIENCE.md` ne cite nommément que **FR-4** (l. 44), **FR-9** et **FR-13** (l. 252). Les dix autres FR n'ont aucune trace explicite : la vérification de couverture est entièrement manuelle et le restera à chaque évolution du PRD.
- **UJ-2 n'est jamais nommé** dans le dossier UX (seul `UJ-1` apparaît, l. 269, dans une balise `[ASSUMPTION]`), alors que le parcours 2 le réalise fidèlement.
- **Aucune référence FR/UJ dans `DESIGN.md` ni dans les trois maquettes.** Aucun identifiant inexistant ou périmé n'a en revanche été trouvé : rien ne référence un FR-14 ou un UJ-3 fantôme.

**Liens et statuts.**

- Les quatre `sources:` déclarées dans les frontmatters d'`EXPERIENCE.md` et `DESIGN.md` (prd.md, addendum.md, research-paysage.md, research-niveau.md) résolvent toutes sur le disque. Le `.memlog.md` du run PRD est déclaré hérité dans le memlog UX mais **absent des `sources:`** — c'est pourtant le seul document où vivent plusieurs décisions produit citées ci-dessus.
- **Asymétrie de statut :** `prd.md` est en `status: draft`, `EXPERIENCE.md` et `DESIGN.md` sont en `status: final`. Le document amont, non finalisé, est aujourd'hui moins à jour que les documents qui en dérivent. Aucun lien du PRD ne pointe vers le dossier UX.
- Le nom **« Ex Aequo » n'apparaît nulle part dans le dossier PRD**, et « Trouve-moi un partenaire » nulle part dans le dossier UX. Les deux moitiés de la chaîne ne partagent aucun nom de produit.

**Résidus et menues erreurs.**

- **Résidu intra-UX du pivot desktop :** `EXPERIENCE.md`, *Responsive & Platform*, dernière ligne du tableau, énonce encore « **Frappe au vol et Échap arment le champ** » alors qu'`Interaction Primitives` déclare cette règle **retirée** (« Une version antérieure de cette spine prescrivait une “frappe au vol” […] Elle est **retirée** »). C'est le seul endroit du couple où la règle supprimée survit.
- **Composant non déclaré :** la maquette 3 affiche une rangée de trois boutons de réponse (« Retenir 19 h » / « Garder 17 h » / « Un autre jour ») qui ne correspond à aucune entrée de `Component Patterns` ni de `DESIGN.md.Components`. C'est aussi la seule chose du produit qui ressemble à des puces de réponse rapide, que `Inspiration & Anti-patterns` rejette « comme interface dominante ».
- **Date fausse dans la maquette 3 :** « Mercredi 3 septembre » — le 3 septembre 2026 est un **jeudi** (le mercredi est le 2).
