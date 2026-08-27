# PRD Quality Review v2 — Ex Aequo (prd-bmad-2026-08-26)

Seconde relecture au rubric, après réécriture profonde. Porte sur `prd.md` (655 lignes),
`addendum.md`, `.memlog.md` et `SportsProfiles.csv` dans leur état du 26/08 19:48.
Les écarts avec le dossier UX ne sont pas traités ici — une relecture de dérive séparée s'en charge.

## Traitement des constats précédents

30 constats de la relecture précédente, repris un par un contre le texte actuel.

**Synthèse : 24 résolus, 4 partiellement résolus, 1 non traité, 1 devenu sans objet.**
Les 3 `critical` et les 9 `high` d'origine sont tous résolus.

| # | Constat d'origine | Sévérité | Statut | Note |
|---|---|---|---|---|
| 1 | « Anna est prévenue » n'est adossé à aucune exigence | critical | **résolu** | FR-14 crée l'exigence, nomme le canal, le contenu et le lien. §11.6 est fermée par un « oui » explicite. UJ-1 ne promet plus rien que le texte ne porte. |
| 2 | Le canal de notification n'existe nulle part | critical→high | **résolu** | E-mail du compte nommé en FR-4, FR-9, FR-13 ; SMS en FR-14 ; §6 *Surface* ferme la boucle en disant pourquoi il n'y a pas de push. |
| 3 | Rejoindre le vivier est imposé, pas consenti | high | **résolu** | L'arbitrage « entrée liée au compte » est pris et écrit : FR-3 (« et pas avant »), FR-4 (« dit que le compte rend l'utilisateur trouvable »), §7. Le consentement reste groupé avec la création de compte — c'est un choix, désormais visible. |
| 4 | Le modèle à deux populations en produit trois | medium | **résolu** | « Un visiteur sans compte ne sort jamais comme candidat » (FR-3) supprime la troisième population. |
| 5 | Quatre NFR, zéro borne | high | **résolu** | 2 s / 20 s, comportement par service tombé, 30 jours de fil anonyme, 360 px. Bornes réelles, pas des adjectifs déguisés. |
| 6 | FR-10 n'a pas de seuil et le sait | medium | **résolu** | Tableau à trois seuils. La *valeur* du seuil d'air pose un problème nouveau (voir N-7), mais le constat d'origine — l'absence — est traité. |
| 7 | La réponse à la cause de mort n°1 n'est jamais formulée | medium | **résolu** | §1 porte le paragraphe « conversation-inscription ». Le paragraphe ajouté contredit toutefois FR-3 (voir N-2) : le constat est traité, la rédaction retenue crée un défaut neuf. |
| 8 | Aucun critère ne teste le pari central | high | **résolu** | SM-5 mesure la thèse et dit franchement ce qu'un échec signifierait. |
| 9 | SM-3 est infalsifiable | high | **résolu** | « ≥ 85 % des 127 combinaisons », plafond 89 % cité. Recalculé : 127 vides, 113 récupérées par le jour, 89 % — exact. |
| 10 | SM-1 revendique une couverture qu'il n'a pas | medium | **partiellement résolu** | SM-1 renonce à FR-7/FR-8/FR-9 et SM-4 les reprend. Mais SM-1 revendique toujours FR-13 et FR-14, dont UJ-1 n'exerce ni l'acceptation, ni le passage à *confirmée*, ni le lien ; et SM-4 revendique FR-7 alors que UJ-2 est justement le cas où FR-7 **ne se déclenche pas**. Voir N-11. |
| 11 | Les deux contre-métriques ne sont pas observables | medium | **partiellement résolu** | Les bornes existent (20 %, 5 tours). SM-C1 est néanmoins structurellement inatteignable : FR-7 ne mord que sur 2 des 231 combinaisons. Voir N-10. |
| 12 | FR-8 : la conséquence Pilates est fausse contre le CSV | critical | **résolu** | « Pilates, avancé » — revérifié : Sarah André est la seule pratiquante, Débutant, et Débutant n'est pas adjacent d'Avancé. La conséquence est exacte. |
| 13 | L'heure est exclue du périmètre mais requise par la jouabilité | critical | **résolu** | FR-2 sépare explicitement disponibilité stockée et heure de la rencontre ; §5.3 dit qui amène l'heure ; §9 reprend la distinction. Traitement propre. |
| 14 | FR-13 : conséquence inexerçable en v1 | high | **résolu** | Le lien d'acceptation de FR-14 rend la transition atteignable. |
| 15 | FR-3 : la déduplication n'a aucun identifiant | high | **résolu** | « Le compte est la clé d'identité du profil ». Un cas résiduel neuf apparaît (profil d'amorçage ↔ compte de la même personne, N-20). |
| 16 | FR-8 n'a aucune conséquence positive | high | **résolu** | « La réponse nomme le sport et le jour tentés, et dit ce qui a été élargi ». |
| 17 | FR-7 est permissif, donc satisfaisable en ne faisant rien | medium | **résolu** | « cette descente n'est pas facultative ». |
| 18 | FR-9 est sans bornes | medium | **résolu** | Déclencheur exact, e-mail dans l'heure, 60 jours, alertes multiples, annulation. Un trou de déclenchement subsiste (N-28), mais les bornes demandées sont posées. |
| 19 | FR-11 est dans le périmètre avec une source non tranchée | medium | **résolu** | `[NOTE FOR PM]` au §5.4 + question ouverte 4 + ligne d'addendum. |
| 20 | « Niveau adjacent » n'est pas défini | low | **résolu** | Entrée de glossaire. |
| 21 | Un garde-fou contredit une question ouverte | medium | **résolu** | La question est fermée par « oui » et §7 est aligné. |
| 22 | L'inscription automatique au vivier n'est pas taguée | medium | **devenu sans objet** | L'arbitrage supprime l'inscription automatique ; il n'y a plus d'inférence à taguer. |
| 23 | L'addendum et le PRD divergent sur le niveau | medium | **résolu** | La section « Notation du niveau » dit désormais « Ce mécanisme n'est pas retenu en v1 » et renvoie à l'arbitrage du PRD. |
| 24 | Aucun `[NON-GOAL for MVP]` inline | low | **résolu** | Deux, aux deux endroits exacts qui étaient signalés : §5.4 (réservation) et §5.5 (agenda du partenaire). |
| 25 | Le profil d'un utilisateur inscrit n'est jamais défini | high | **résolu** | Entrée de glossaire champ par champ, symétrique de celle du profil d'amorçage. |
| 26 | « Candidat » et « créneau » manquent au glossaire | medium | **résolu** | Les deux sont entrés, et *créneau* gagne même la précision « l'heure n'existe nulle part dans le vivier ». |
| 27 | Trois étiquettes pour le même fichier | medium | **partiellement résolu** | Le glossaire déclare « la seule étiquette employée » et « jeu d'amorçage » disparaît du PRD — mais **« vivier d'amorçage » apparaît trois fois** (§4, FR-14, §7) comme quatrième étiquette, et « jeu d'amorçage » survit dans l'addendum. Le problème a changé de nom, pas de nature. |
| 28 | Collision de prénom entre protagoniste et profil d'amorçage | low | **résolu** | Nadia remplace Sarah. Vérifié : ni Thomas ni Nadia n'apparaissent dans le CSV. |
| 29 | « Rendez-vous », « rencontre » et « créneau » alternent | low | **partiellement résolu** | *Créneau* est glossé et employé correctement ; **« rendez-vous » subsiste trois fois** (§1, UJ-1, titre du §5.5) sans entrée de glossaire, dans un document dont le §0 promet « sans synonyme ». |
| 30 | Écart au format convenu (~2 pages visées, ~10 livrées) | low | **non traité** | Le document a encore grossi (37 Ko contre 30). L'écart est reconnu au memlog (« cible non tenue et assumée ») mais nulle part dans le PRD lui-même. |

## Overall verdict

La réécriture a fait son travail sur le fond : les trois `critical` et les neuf `high` de la
passe précédente sont réellement résolus — vérification faite, pas déclarée — et la
substitution des adjectifs par des bornes au §6, au §10 et en FR-9 est exemplaire. Le PRD
prend désormais quatre décisions qu'il esquivait, et les trace.

Ce qu'elle a cassé tient à la nature de ce qui a été ajouté : FR-14 introduit un cycle de
vie d'acceptation — un message qui part, un lien qui vit, un partenaire qui répond — et le
PRD n'en spécifie que le chemin heureux. Le refus, l'expiration, l'échec d'envoi,
l'annulation et la double réservation d'un même partenaire sont tous absents, et le refus
en particulier fait dire au bot quelque chose de faux, ce que le §7 lui interdit
frontalement. À cela s'ajoute une contradiction de la Vision elle-même : le paragraphe
ajouté pour combler le constat 7 décrit un mécanisme de croissance que FR-3 interdit
explicitement. Le document est plus juste qu'avant et moins terminable : il n'est pas prêt
à être découpé en épiques tant que le cycle de vie de la rencontre n'a pas d'états.

## Decision-readiness — adequate

Le PRD a nettement progressé sur cette dimension. Quatre questions sont fermées avec une
réponse et une trace (§11, « Questions fermées depuis la première rédaction »), les quatre
qui restent sont réellement ouvertes, et la `[NOTE FOR PM]` du §7 sur l'asymétrie de
consentement est le meilleur passage du document : elle nomme un problème que la solution
retenue *neutralise sans le résoudre*, dit exactement ce qui le neutralise (des numéros
fictifs), et pose la condition de réouverture. C'est le contraire du lissage.

Ce qui empêche de monter plus haut, c'est que la réécriture a créé une nouvelle catégorie
de non-décision : des cas qui ne sont ni traités, ni exclus, ni signalés comme ouverts.
L'annulation d'une rencontre par le demandeur en est le cas type — le §9 exclut « la
négociation entre deux utilisateurs inscrits — relance, contre-proposition de créneau,
annulation », ce qui ne couvre pas le cas majoritaire du produit, où le partenaire est un
profil d'amorçage. Le lecteur ne peut pas savoir si c'est un oubli ou une exclusion. Même
chose pour la double réservation. Ces sujets ne figurent nulle part : ni en FR, ni en hors
périmètre, ni en question ouverte.

Second point : le §9 a grossi de façon substantielle — une surface web hors conversation,
deux canaux sortants, un cycle de vie d'alerte de 60 jours, des profils multi-sports — et
le document ne le dit à aucun moment. Un décideur ne voit pas que le périmètre s'est
élargi, et n'a donc pas l'occasion de le refuser.

### Findings

- **high** L'annulation d'une rencontre n'est ni spécifiée, ni exclue (FR-13, FR-14, §9) — Une fois le SMS parti et l'événement écrit dans l'agenda, rien ne dit ce que Thomas peut faire s'il ne peut plus venir. Le hors-périmètre du §9 ne couvre que la négociation *entre deux utilisateurs inscrits*, donc pas le cas majoritaire. L'asymétrie est frappante : FR-9 donne explicitement le droit d'annuler une *alerte*, et rien ne permet d'annuler une *rencontre*. *Fix:* soit une conséquence en FR-13 (l'utilisateur annule ; le partenaire est prévenu par le même canal ; l'événement d'agenda est retiré), soit une ligne explicite au hors-périmètre disant que l'annulation n'existe pas en v1 et ce que le bot répond quand on la demande.
- **high** Un visiteur anonyme peut énumérer le vivier, et le PRD le promet (FR-1, FR-6, §7) — FR-1 garantit qu'« un visiteur sans compte peut formuler une demande et recevoir des propositions de partenaires nommés ». Rien ne borne le nombre de demandes : on peut balayer les 11 sports × 7 jours × 3 niveaux sans compte et reconstituer une large part du vivier (prénoms, sport, niveau, jours). Le §7 ne protège que le numéro de téléphone. Le caractère fictif des données neutralise le dommage aujourd'hui, exactement comme pour le SMS — mais contrairement au SMS, ce point n'est ni nommé ni assorti d'une condition de réouverture. *Fix:* une puce au §7 sur le même modèle que la `[NOTE FOR PM]` de l'asymétrie de consentement — l'exposition est admise parce que le vivier est fictif, à rouvrir avec des données réelles.
- **medium** La croissance du périmètre n'est reconnue nulle part (§9, §11) — Le MVP comprend maintenant huit dépendances externes (LLM, météo, indice d'air, terrains, Google Calendar, Microsoft Graph, envoi d'e-mail, envoi de SMS), deux parcours OAuth, une page hors conversation avec jetons, et un cycle de vie d'alerte. La seule faisabilité signalée comme un pari est FR-11. Le PRD ne dit à aucun endroit ce qui tomberait en premier si le temps manquait. *Fix:* une ligne au §9 nommant l'ordre de décrochage — par exemple terrains, puis SMS (l'e-mail suffit à FR-14 pour un utilisateur inscrit), puis Outlook.

## Substance over theater — adequate

Les seuils ne sont plus du théâtre : le §6 a des chiffres, FR-9 a un cycle de vie complet,
FR-10 a un tableau. Le §5.2 va plus loin qu'avant en versant deux chiffres nouveaux — les
83 profils sur 86 à deux jours, les 19 % de combinaisons à candidat unique — qui sont l'un
et l'autre exacts (recalculés). Et l'ajout au §7 des « étapes annoncées correspondent aux
sources réellement interrogées » est une idée forte, pas un ornement : l'addendum en tire
correctement une contrainte d'architecture.

Le théâtre s'est déplacé. Il n'est plus dans l'absence de chiffres mais dans des chiffres
qui ne mesurent pas ce qu'ils prétendent mesurer. « Indice supérieur à 100 » ne désigne
aucune échelle nommée, et l'addendum renvoie pour la France aux indices ATMO, qui sont
gradués de 1 à 6 : le seuil est inapplicable tel quel. Le paragraphe qui justifie le
plafond de trois candidats de FR-6 invoque un chiffre qui porte sur autre chose. Et la
garantie la plus forte du document — la fidélité des étapes narrées — n'a aucune
conséquence testable, aucun SM, et vit donc entièrement en prose.

### Findings

- **high** « Indice supérieur à 100 » ne nomme aucune échelle et contredit l'addendum (§5.3 FR-10, addendum *Intégrations*) — Un indice de qualité de l'air n'a de valeur que relativement à son échelle : 100 est la frontière « modéré / médiocre » de l'AQI américain, mais l'addendum indique « en France, les indices ATMO sont régionaux » — et l'ATMO comme l'indice européen sont gradués de 1 à 6. Sur l'échelle que l'addendum désigne, le seuil de 100 n'est jamais atteignable ; la conséquence testable de FR-10 est donc inerte pour un tiers de son objet. C'est le seul des trois seuils arbitrés qui ne survit pas à sa propre source de données. *Fix:* nommer l'échelle dans le tableau (« indice européen EAQI ≥ 4 (*Poor*) », ou « AQI US > 100 ») et aligner la ligne Météo de l'addendum.
- **medium** La garantie la plus forte du §7 n'a aucune conséquence testable (§7, §10) — « Les étapes que le bot annonce correspondent aux sources qu'il a réellement interrogées » est la nouveauté la plus structurante du document et la seule qui contraigne l'orchestration. Aucune FR ne la porte, aucun SM ne la vérifie : SM-2 teste que le bot n'invente ni nom, ni lieu, ni météo — pas qu'il n'invente pas *avoir regardé*. Un système qui affiche « je regarde la météo… » avant d'appeler l'API satisferait SM-2. *Fix:* une conséquence en FR-10 ou une extension de SM-2 — pour un échantillon de conversations, chaque étape annoncée correspond à un appel externe effectivement émis, et toute source en échec est annoncée.
- **medium** La justification chiffrée du plafond de trois est un non-sequitur (§5.2, FR-6) — « 19 % des combinaisons ne renvoient qu'un seul candidat, et le plafond n'y mord donc presque jamais » : les 19 % portent sur la recherche **exacte**, alors que le plafond s'applique aux résultats **élargis**, qui sont par construction plus fournis. Le chiffre pertinent est ailleurs et il est encore plus favorable — seules 4 des 33 paires sport × niveau comptent plus de trois profils (Football/Intermédiaire, Natation/Intermédiaire, Rugby/Avancé, Yoga/Avancé). Le paragraphe donne un chiffre exact au service d'une conclusion qu'il n'établit pas. *Fix:* remplacer par le décompte des paires sport × niveau au-dessus de trois.
- **medium** La jouabilité se réclame de la santé et ignore l'orage, le froid et la pluie (§5.3) — « Il ne s'agit pas de confort mais de **santé** », puis trois seuils : chaleur, vent, air. L'orage — le risque de santé le plus aigu d'une pratique extérieure — n'est ni un seuil ni un non-objectif ; le froid et la pluie non plus. Le tableau définit implicitement la jouabilité comme un triplet, sans le dire. *Fix:* soit un quatrième seuil (alerte orage = créneau signalé), soit une phrase assumant que la v1 se limite à trois conditions et pourquoi.

## Strategic coherence — thin

La thèse est plus visible qu'avant et le §10 la teste enfin (SM-5). Mais le paragraphe
même qui a été ajouté pour énoncer le mécanisme central affirme le contraire de ce que les
exigences prescrivent : « **chaque personne qui parle au bot rejoint le vivier par le
simple fait d'avoir parlé**. Il n'y a pas de formulaire d'inscription à franchir, donc pas
de marche à laquelle le vivier cesse de grossir. » Or FR-3 dit « à la création de son
compte, **et pas avant** », FR-4 place cette création à la mise en relation, et FR-3 ajoute
« un visiteur sans compte ne sort jamais comme candidat ». Il y a une marche, elle est
nommée, et c'est exactement la marche à laquelle le vivier cesse de grossir. Le §1 décrit
le produit d'avant l'arbitrage.

Ce n'est pas une maladresse de rédaction : c'est l'affirmation de différenciation du
produit — « c'est ce qui distingue Ex Aequo des matchers purs morts du vide » — assise sur
un mécanisme que le document interdit trois pages plus loin. Un lecteur aval qui part de la
Vision construira le mauvais produit.

Le §10 souffre par ailleurs d'un défaut de la même famille que celui relevé la fois
précédente, transposé sur du matériel neuf : les SM revendiquent des couvertures que les
parcours n'exercent pas, et la contre-métrique la plus importante ne peut pas se
déclencher.

### Findings

- **critical** Le mécanisme central annoncé au §1 est interdit par FR-3 et FR-4 (§1, FR-3, FR-4) — « Chaque personne qui parle au bot rejoint le vivier par le simple fait d'avoir parlé […] pas de marche à laquelle le vivier cesse de grossir » contre « à la création de son compte, et pas avant » et « un visiteur sans compte ne sort jamais comme candidat ». Le paragraphe rédigé pour combler le constat 7 de la passe précédente porte le modèle d'avant l'arbitrage. C'est la phrase de différenciation du produit, et elle est fausse contre sa propre spécification. *Fix:* réécrire le paragraphe autour du mécanisme réellement retenu — il reste fort : il n'y a pas de formulaire, le profil se constitue en parlant, et la seule marche est un bouton de connexion posé au moment où il rend service à l'utilisateur, pas au moment où il protège le produit.
- **medium** SM-C1 ne peut pas mordre sur les données d'amorçage (§10, FR-7) — Recalcul complet : dans l'ordre imposé par FR-7 (le niveau ne se relâche qu'après l'échec de l'élargissement sur le jour), la descente de niveau ne se déclenche que sur **2 des 231 combinaisons** — Pilates/Intermédiaire, mardi et jeudi, qui renvoient toutes deux Sarah André. La part maximale des mises en relation obtenues par descente de niveau est donc de l'ordre de 1 %, contre un seuil d'alerte fixé à 20 %. La seule garde-fou chiffré de la promesse centrale du produit ne peut pas se déclencher. *Fix:* soit abaisser le seuil à une valeur que la donnée rend franchissable (5 %), soit changer d'observable — par exemple la part des propositions **acceptées** qui portaient un écart de niveau annoncé.
- **medium** SM-1 et SM-4 revendiquent des FR que leurs parcours n'exercent pas (§10, §2.3) — SM-1 revendique FR-13 et FR-14 alors que UJ-1 s'arrête sur « Thomas ferme l'onglet » : ni l'acceptation, ni le passage à *confirmée*, ni la notification de confirmation, ni le lien à usage unique ne sont traversés. SM-4 revendique FR-7 alors que UJ-2 (Pilates/Avancé) est précisément le cas où FR-7 **ne se déclenche pas**. Résultat : le comportement positif de FR-7 — la descente obligatoire avec annonce de l'écart — n'est validé par aucun critère, et la moitié de FR-14 non plus. *Fix:* un SM-6 adossé au cycle d'acceptation (le partenaire suit le lien, la rencontre passe à *confirmée*, le demandeur est notifié, l'agenda est mis à jour), et retirer FR-7 de SM-4.
- **medium** SM-5 ne détecte qu'un seul mode d'échec de la thèse (§10) — « Moins d'une session sur cinq voit l'utilisateur réclamer une liste, une carte ou des filtres » suppose que l'utilisateur à qui la conversation ne convient pas le dise. Le mode d'échec le plus probable est qu'il parte sans rien réclamer, et SM-5 comptera cela comme un succès. *Fix:* adjoindre une observable d'abandon — part des sessions closes avant la première proposition de partenaire — qui est la lecture négative du même pari.

## Done-ness clarity — thin

C'est la dimension qui a le plus gagné et le plus perdu. Gagné : les treize FR héritées
sont franchement meilleures — FR-3 a une clé d'identité, FR-6 a un plafond et une règle
d'ordre, FR-7 est obligatoire, FR-8 a une conséquence positive et un contre-exemple
désormais **exact** (revérifié contre le CSV), FR-9 a cinq bornes, FR-10 a trois seuils. Un
ingénieur peut écrire ces tests.

Perdu : FR-14 est une machine à états déguisée en liste de conséquences. Elle fait partir
un message, ouvre un lien, et attend une réponse — donc elle crée au moins cinq états
terminaux (accepté, refusé, expiré, désinscrit, non délivré) là où le glossaire n'en
connaît que deux, *confirmée* et *en attente*. La conséquence « un refus, ou l'absence de
réponse, laisse la rencontre *en attente* » n'est pas une simplification acceptable : elle
oblige le bot à dire à l'utilisateur ce que FR-13 lui fait dire — « le partenaire a été
prévenu et n'a pas encore répondu » — alors que le partenaire a répondu non. Le §7 interdit
au bot d'annoncer une confirmation non donnée ; il devrait tout autant lui interdire
d'annoncer un silence qui n'a pas eu lieu.

Le même angle mort touche FR-10 sous une autre forme : le glossaire définit un *créneau*
comme « un jour et **une heure précise** », FR-10 évalue « le créneau et le lieu
envisagés », et sa dernière conséquence est « en l'absence d'alerte, le bot demande l'heure
de la rencontre ». L'évaluation précède donc son entrée. Le passage de UJ-1 laisse
comprendre l'intention réelle — le bot regarde la journée entière et n'ouvre le sujet de
l'heure que s'il y trouve un dépassement — mais FR-10 ne le dit pas, et c'est FR-10 qui
sera découpée en stories.

Enfin, la question posée par le mandat — que se passe-t-il aux limites de FR-14 — reçoit
zéro réponse sur cinq : lien expiré (aucune durée de vie), partenaire qui refuse (état
absent), partenaire désinscrit (contredit le glossaire, sort des rencontres en cours non
traité), deux demandeurs sur le même partenaire (absent), utilisateur qui annule (absent).

### Findings

- **critical** Le refus du partenaire n'existe pas dans le modèle d'état (FR-13, FR-14, §3, §7) — « Un refus, ou l'absence de réponse, laisse la rencontre *en attente* » range dans le même état une réponse négative et un silence. Trois conséquences en découlent, toutes fausses pour l'utilisateur : le bot lui dit que le partenaire « n'a pas encore répondu » (FR-13) alors qu'il a dit non ; aucune notification ne part, puisque FR-13 n'en déclenche que sur le passage à *confirmée* ; et l'événement reste dans son agenda pour une rencontre qui n'aura pas lieu. Le §7 interdit d'annoncer une confirmation non donnée — annoncer une attente qui n'existe plus est la même faute. *Fix:* ajouter l'état *refusée* au glossaire et à FR-13, avec sa notification, le sort de l'événement d'agenda, et ce que le bot propose ensuite (relancer la recherche, ou basculer sur l'alerte différée de FR-9).
- **high** Deux demandeurs peuvent retenir le même partenaire sur le même créneau (FR-5, FR-6, FR-13, FR-14) — Rien n'exclut un candidat déjà retenu par quelqu'un d'autre, rien ne réconcilie deux rencontres *en attente* portant la même personne. Anna peut recevoir deux SMS avec deux liens valides et accepter les deux : le produit crée alors deux rencontres *confirmées* au même moment, en écrit deux dans deux agendas, et n'a aucun moyen d'en défaire une. Sur un vivier de 86 profils dont un seul est disponible dans 19 % des combinaisons, la collision n'est pas un cas d'école. *Fix:* une conséquence en FR-14 — un partenaire ne porte qu'une rencontre *en attente* par créneau, la seconde demande le retire des candidats ou la propose en file — et le comportement du bot quand cela arrive.
- **high** Le lien d'acceptation n'a pas de durée de vie (FR-14, addendum *Persistance*) — « Ne fonctionne qu'une fois » borne le nombre d'usages, pas la fenêtre. Rien ne dit ce qui se passe si le lien est suivi après la date de la rencontre, ni combien de temps une rencontre peut rester *en attente*. L'écart est d'autant plus visible que FR-9, qui est moins critique, a reçu ses 60 jours et sa notification d'expiration — et que l'addendum prévoit un état terminal « expiré » que le PRD ne crée jamais. *Fix:* une durée de validité en FR-14 (par exemple jusqu'à 24 h avant le créneau), l'état *expirée* au glossaire, et ce que le bot dit au demandeur à l'expiration.
- **high** L'échec d'envoi du SMS ou de l'e-mail n'a aucun comportement (FR-13, FR-14, §6) — Le §6 nomme trois services faillibles — météo, terrains, agenda — et omet les deux canaux sortants sur lesquels reposent désormais FR-9, FR-13 et FR-14. Or FR-13 fait affirmer au bot que « le partenaire a été prévenu » sans conditionner cette affirmation à un envoi réussi, et FR-14 ne prévoit d'échec explicite que pour le filtre de destinataire, pas pour l'indisponibilité du fournisseur. Le bot peut donc annoncer un envoi qui n'a pas eu lieu — la faute même que le §7 est censé rendre impossible. *Fix:* ajouter l'envoi sortant à la liste des services faillibles du §6 avec son comportement, et conditionner la conséquence de FR-13 (« l'utilisateur est informé que le partenaire a été prévenu ») à la confirmation d'envoi.
- **high** La jouabilité s'applique indistinctement aux sports d'intérieur (§5.3, FR-10) — Sur les 11 sports des données d'amorçage, la majorité se pratique couramment en salle : Yoga, Pilates, Danse, Natation, Basket-ball, Volley-ball, Escalade. FR-10 n'a aucune notion d'intérieur / extérieur : une séance de Pilates serait signalée « non jouable » parce qu'il fait 29 °C dehors et que les rafales atteignent 45 km/h. Le bot deviendrait absurde sur plus de la moitié de son catalogue, et le §7 lui interdit par ailleurs d'inventer — il ne peut donc pas décider tout seul de se taire. *Fix:* une propriété *sport d'extérieur* portée par le sport, et une conséquence de FR-10 disant que la jouabilité n'est évaluée que pour ceux-là ; ou, si la donnée manque, une conséquence disant que le bot demande où se déroule la pratique avant d'évaluer.
- **high** FR-10 évalue un créneau avant que son heure existe (§3, §5.3, FR-10) — Le glossaire définit un créneau comme « un jour et une heure précise » ; FR-10 évalue « le créneau et le lieu envisagés » ; sa dernière conséquence est « en l'absence d'alerte, le bot demande l'heure de la rencontre ». L'exigence consomme donc une donnée qu'elle produit. UJ-1 laisse deviner l'intention — évaluer la journée, n'ouvrir le sujet de l'heure qu'en cas de dépassement — mais FR-10 ne la porte pas, et c'est FR-10 qui sera découpée en story. *Fix:* dire ce qui est évalué en l'absence d'heure — les prévisions horaires de la journée sur une plage de pratique plausible — et faire du choix de l'heure une conséquence de ce balayage plutôt qu'une entrée.
- **medium** FR-9 ne se déclenche pas dans le cas que FR-3 vient de rendre courant (FR-3, FR-9) — L'alerte se déclenche « si un profil correspondant **rejoint le vivier** ». Depuis l'arbitrage multi-sports, le cas fréquent n'est plus l'arrivée d'un profil neuf mais l'**ajout d'un sport** à un profil déjà présent — FR-3 en fait une conséquence testable explicite. Un utilisateur déjà inscrit qui déclare le Pilates ne « rejoint » rien, et l'alerte de Nadia ne partirait donc jamais : le parcours de UJ-2 n'aboutit pas. *Fix:* reformuler le déclencheur en « lorsqu'un profil du vivier devient correspondant », ce qui couvre l'arrivée comme l'enrichissement.
- **medium** « Classés par proximité au jour demandé » n'a pas de métrique, et UJ-1 ne respecte pas la conséquence (FR-6, §2.3 UJ-1) — La proximité entre deux jours de la semaine n'est pas définie : circulaire ou non, vers l'avant seulement ou dans les deux sens, et pour un candidat qui porte plusieurs jours, lequel compte. Vérification faite, les trois candidates de UJ-1 sont toutes à distance 1 de mardi, donc l'ordre affiché est celui du vivier — le récit n'exerce pas la règle. Par ailleurs FR-6 exige de présenter « les candidats **avec leurs jours respectifs** » tandis que UJ-1 restitue une union (« mercredi, samedi ou lundi ») sans dire qui joue quand — ce qui rend d'ailleurs le choix de Thomas ambigu : mercredi désigne Anna ou Iris. *Fix:* définir la distance entre jours, et corriger la réplique de UJ-1 pour qu'elle attribue les jours aux personnes.
- **medium** UJ-1 fusionne connexion et accès agenda, ce que FR-12 interdit (§2.3 UJ-1, FR-12, addendum) — Thomas « signe avec son compte Google » puis « le bot pose le rendez-vous dans son agenda », sans moment de consentement intermédiaire. FR-12 exige que « l'écriture n'ait jamais lieu sans confirmation explicite de l'utilisateur », et l'addendum note que ce sont deux périmètres OAuth distincts. Le parcours nominal viole la conséquence la plus protectrice de FR-12. *Fix:* une phrase dans UJ-1 séparant les deux demandes, ou une conséquence de FR-12 précisant que la confirmation d'écriture peut être portée par le consentement OAuth lui-même.
- **low** La mise à jour différée de l'agenda suppose un accès conservé (FR-13, §7) — « Le passage à *confirmée* […] met à jour l'événement d'agenda » a lieu potentiellement des jours après la fin de la conversation, donc suppose la conservation du jeton d'accès. Le §7 dit « l'accès à l'agenda sert à écrire la rencontre convenue, rien d'autre » sans dire pendant combien de temps il est conservé. *Fix:* une incise au §7.

## Scope honesty — adequate

Recul depuis `strong`, pour une raison précise : le rapport entre ce que le PRD affirme et
ce qu'il marque comme non confirmé s'est dégradé. La version précédente portait deux
`[ASSUMPTION]` pour un document essentiellement qualitatif. La version actuelle est
truffée de chiffres — 2 s, 20 s, 30 jours, 360 px, 60 jours, une heure, trois candidats,
85 %, une session sur cinq, 20 %, 5 tours — dont **trois seulement** (28 °C, 40 km/h,
indice 100) ont été arbitrés par l'utilisateur, les autres étant des propositions du
rédacteur. L'index des hypothèses en compte toujours deux, dont aucune ne porte sur un
seuil. Un lecteur ne peut pas distinguer ce qui a été décidé de ce qui a été suggéré, et
c'est précisément la distinction que le §11 fait par ailleurs très bien pour les quatre
questions fermées.

Le reste tient. Les deux `[NON-GOAL for MVP]` sont posés aux bons endroits, la
`[NOTE FOR PM]` du §7 est un modèle du genre, le §8 garde ses cinq non-objectifs motivés,
et la section *Sécurité des personnes* continue de dire franchement que le compromis ne
tiendrait pas avec de vrais utilisateurs. Densité des items ouverts : 4 questions ouvertes
+ 2 `[ASSUMPTION]` + 3 `[NOTE FOR PM]` = 9, en baisse alors que le périmètre a grossi — ce
qui est le symptôme du problème ci-dessus plutôt qu'un progrès.

### Findings

- **high** Une dizaine de seuils neufs, aucun tagué ni indexé (§6, §10, FR-6, FR-9, §12) — Trois seuils viennent de l'utilisateur et sont tracés au §11 ; tous les autres — 2 s et 20 s de latence, 30 jours de fil anonyme, 360 px, 60 jours d'alerte, notification « dans l'heure », plafond de trois candidats, 85 %, une session sur cinq, 20 % et 5 tours — sont des inférences du rédacteur présentées avec la même autorité. L'index des hypothèses reste à deux entrées, dont aucune n'est un seuil. C'est exactement le cas que le tag `[ASSUMPTION]` existe pour couvrir, et le PRD sait l'utiliser puisqu'il le fait ailleurs. *Fix:* un `[ASSUMPTION]` groupé au §6 et au §10 (« les bornes chiffrées de cette section sont proposées, non arbitrées ») avec les deux entrées correspondantes au §12 — c'est deux lignes et cela rétablit la distinction.
- **medium** La désinscription d'un utilisateur inscrit n'est pas traitée (FR-14, §3) — « L'exercer retire le profil du vivier définitivement » s'applique aussi à un utilisateur inscrit prévenu par SMS ou par e-mail. Que devient alors son compte, ses alertes en cours, ses rencontres à venir, son historique ? Un « retrait définitif du vivier » qui coexiste avec un compte actif n'a pas de sens décrit. *Fix:* distinguer les deux cas en FR-14 — pour un profil d'amorçage, retrait ; pour un utilisateur inscrit, ce qui est vraisemblablement voulu est « ne plus être proposé comme candidat », qui est réversible et ne détruit pas le compte.
- **medium** Le §9 décrit la page d'acceptation autrement que FR-14 (§9, FR-14) — « Une page hors conversation, qui accepte ou refuse, **et rien d'autre** » : or la même page porte, d'après FR-14, la sortie définitive du vivier, qui est la fonction la plus lourde de conséquences du produit. Le périmètre MVP sous-décrit ce qu'il contient. *Fix:* ajouter la désinscription à la ligne du §9.

## Downstream usability — adequate

Le PRD reste bien équipé pour l'aval — §0 nomme ses consommateurs, le glossaire s'est
enrichi de cinq entrées demandées (*données d'amorçage*, *candidat*, *niveau adjacent*,
*créneau*, et le profil de l'utilisateur inscrit décrit champ par champ), les identifiants
sont propres (FR-1 à FR-14 contigus, UJ-1/UJ-2, SM-1 à SM-5 plus SM-C1/SM-C2), et les
renvois internes résolvent tous.

Mais le glossaire a une contradiction frontale avec une exigence, et la vague de termes
neufs de FR-14 n'y est pas entrée. Le §0 promet un vocabulaire « employé littéralement,
sans synonyme » — c'est la promesse la plus facile à tenir du document et elle s'est
dégradée sur du matériel neuf pendant qu'elle se réparait sur l'ancien.

### Findings

- **high** Le glossaire déclare le vivier append-only, FR-14 le vide (§3, FR-14) — « **Il grossit ; il ne diminue pas.** » contre « l'exercer retire le profil du vivier définitivement ». C'est l'entrée du nom le plus central du document, et elle contredit une conséquence testable. Un extracteur aval — architecture ou stories — modélisera un ensemble sans suppression, et FR-14 exigera une suppression. *Fix:* réécrire l'entrée : le vivier grossit par les créations de compte et ne perd un profil que par désinscription explicite (FR-14) ; c'est de toute façon plus vrai et plus intéressant que la formule actuelle.
- **medium** « Alerte » désigne deux choses, aucune n'est au glossaire (FR-9, FR-10, §5.3) — L'*alerte différée* de FR-9 (un e-mail, 60 jours, annulable) et l'*alerte* de jouabilité de FR-10 (« un créneau dépassant l'un des trois seuils est signalé », « l'alerte informe et n'interdit pas », « en l'absence d'alerte ») sont deux objets sans rapport portant le même nom, tous deux dans des conséquences testables. *Fix:* deux entrées au §3, ou renommer la seconde en *signalement de jouabilité*.
- **medium** Les termes centraux de FR-14 ne sont pas au glossaire (§3, FR-14, §9, addendum) — *Lien d'acceptation*, *désinscription* / *sortie du vivier* et *alerte différée* sont employés dans les conséquences testables, dans le périmètre MVP et dans l'addendum, et sont absents d'un glossaire déclaré contraignant — dans le même document où *candidat* et *créneau* viennent d'y être ajoutés pour la même raison. *Fix:* trois entrées.
- **medium** La fusion d'un profil d'amorçage avec le compte de la même personne n'est pas traitée (FR-3, §4) — La clé d'identité est le compte ; les 86 profils n'en ont pas. Si Anna Perrot venait créer un compte, elle produirait un second profil et pourrait être proposée deux fois, une fois joignable par SMS et une fois par e-mail. Le caractère fictif des données rend le cas théorique aujourd'hui — mais §4 insiste précisément sur le fait que le filtre de destinataire est « une règle de production, pas un interrupteur de test », c'est-à-dire que le modèle est censé survivre à un amorçage réel. *Fix:* une phrase au §4 ou une conséquence en FR-3 — soit le cas est reconnu comme non traité en v1, soit la fusion est décrite.
- **low** §4 et FR-14 divergent sur le canal d'un partenaire inscrit (§4, FR-14, §7) — Le §4 énonce sans condition qu'un utilisateur inscrit « est prévenu par e-mail » ; FR-14 dit « par SMS s'il a un numéro de téléphone, par e-mail s'il est utilisateur inscrit et n'en a pas donné ». *Fix:* aligner le §4 sur la règle réelle, qui dépend du numéro et non de la population.
- **low** « Profil » n'est pas défini alors qu'il porte la structure multi-sports (§3, FR-3) — Le glossaire définit *profil d'amorçage* et *utilisateur inscrit* mais pas *profil*, qui est pourtant le mot employé dans « un profil porte plusieurs sports », « les profils du vivier », « la clé d'identité du profil ». *Fix:* une entrée chapeau.

## Shape fit — strong

La forme continue de correspondre au produit, et la réécriture n'a rien abîmé de ce
côté : deux parcours utilisateur à protagoniste nommé qui portent leur contexte inline,
pas de section persona autonome (entrée Journey-led, conforme), pas de sur-formalisation.
Le §10 s'ouvre toujours sur « projet personnel : la mesure est qualitative et
volontairement courte », et la nouvelle `[NOTE FOR PM]` du §7 est un exemple de rigueur
allégée bien faite — elle allège en disant qu'elle allège, et pose la condition de
réouverture.

UJ-2 gagne même en force : le parcours de Nadia porte désormais l'ensemble du comportement
en l'absence de résultat, il est adossé à un SM propre (SM-4), et le contre-exemple qu'il
utilise est exact. Le seul écart de calibrage reste la longueur, aggravée — et la migration
de matière d'implémentation dans le corps du PRD.

### Findings

- **low** Le §4 et le §7 portent du « comment » que le §0 renvoie à l'addendum (§0, §4, §7) — La plage ARCEP, sa référence réglementaire implicite, et le fonctionnement du filtre de destinataire occupent maintenant deux paragraphes du PRD tout en figurant intégralement dans l'addendum. La justification produit tient en une phrase (« le vivier d'amorçage est incapable d'atteindre une personne réelle, et c'est une propriété dont FR-14 dépend ») ; le reste est de l'implémentation. Le document a par ailleurs encore grossi par rapport à une cible de ~2 pages que le memlog reconnaît comme non tenue, sans que le PRD le dise. *Fix:* réduire le §4 à la propriété produit et laisser la plage, la référence et le filtre à l'addendum, qui les porte déjà.

## Mechanical notes

**Identifiants.** FR-1 à FR-14 contigus, uniques, sans doublon. UJ-1 et UJ-2 idem. SM-1 à
SM-5 plus SM-C1 et SM-C2 idem. Toutes les références croisées internes résolvent
(FR-3 ↔ FR-4, FR-9 → FR-4, FR-13 → FR-14, §5.4 → addendum, §11.2 → FR-14, §10 → §5.2).
Les renvois externes vers `research-niveau.md` §4 et §4.7 et `research-paysage.md` §2 et §3
résolvent également. Le lien vers `ux-designs/ux-bmad-2026-08-26/` ajouté au §0 est un
progrès pour la chaîne aval.

**Chiffres revérifiés contre `SportsProfiles.csv`** (recalcul complet, 86 lignes) :
86 profils ✓ ; 11 sports ✓ ; 231 combinaisons ✓ ; 104 combinaisons servies et 127 vides,
soit 55 % ✓ ; élargissement sur le jour : 113 des 127, soit 89 % ✓ ; élargissement sur le
niveau adjacent à jour tenu : 46, soit 36 % ✓ ; 45 combinaisons à candidat unique,
soit 19 % ✓ ; 83 profils sur 86 à deux jours ✓ ; Emma Leroy unique sur
Tennis/Mardi/Débutant ✓ ; Anna Perrot, Iris Payet et Tessa Armand sont exactement les trois
Tennis/Intermédiaire ✓ ; Sarah André unique pratiquante de Pilates, niveau Débutant, donc
« Pilates avancé » est bien vide après tout élargissement ✓ ; les 86 numéros sont uniques et
tous dans `+3363998 0001`–`0086` ✓ ; ni « Thomas » ni « Nadia » n'apparaissent dans le
fichier ✓.

**Deux nombres que le PRD ne donne pas et qui l'aideraient.** Dans l'ordre imposé par
FR-7, la descente de niveau ne se déclenche que sur 2 combinaisons sur 231 (Pilates /
Intermédiaire, mardi et jeudi) et 12 restent définitivement vides. Et seules 4 des 33
paires sport × niveau comptent plus de trois profils. Ces deux chiffres soutiennent
directement SM-C1 et FR-6, là où les chiffres actuellement cités ne les soutiennent pas.

**Aller-retour de l'index des hypothèses : complet mais appauvri.** Deux `[ASSUMPTION]`
inline (§2.3 UJ-1, §5.1 FR-2), deux entrées au §12, correspondance exacte dans les deux
sens. Aucune orpheline. Voir toutefois le constat `high` de *Scope honesty* : le
périmètre a doublé et l'index n'a pas bougé. À noter aussi que la question ouverte 1
revendique un choix de prénom « pour les deux parcours » alors que seul UJ-1 porte le tag ;
UJ-2 n'en a pas.

**Dérive de vocabulaire résiduelle.** « Vivier d'amorçage » apparaît 3 fois (§4, FR-14, §7)
à côté de *données d'amorçage*, déclaré au glossaire « la seule étiquette employée dans ce
document » ; « jeu d'amorçage » survit dans l'addendum. « Rendez-vous » subsiste 3 fois
(§1, UJ-1, titre du §5.5) sans entrée de glossaire, pour ce que le §3 appelle *rencontre*.

**Cohérence PRD ↔ addendum.** Le désaccord sur le niveau est réparé. Il en reste deux
mineurs : l'addendum prévoit un état terminal « expiré » pour le lien d'acceptation que le
PRD ne crée jamais (voir le constat `high` correspondant), et sa ligne *Météo* renvoie aux
indices ATMO régionaux (échelle 1–6) là où FR-10 fixe un seuil à 100. La nouvelle
section *Pièges de démonstration* est un bon versement : elle recueille la matière
opérationnelle du memlog sans la faire remonter dans le PRD.

**Sections requises.** Rien ne manque pour les enjeux et le type de produit. L'absence de
section persona autonome reste conforme à l'entrée Journey-led et n'est pas comptée comme
un manque.
