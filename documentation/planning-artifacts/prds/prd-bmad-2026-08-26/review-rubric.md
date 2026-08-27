# PRD Quality Review — Trouve-moi un partenaire (prd-bmad-2026-08-26)

## Overall verdict

Ce PRD tient largement au-dessus de la barre de ses enjeux : il a une thèse assumée, des décisions
prises et *justifiées par des chiffres tirés des données réelles* (§5.2), des non-objectifs qui font
un vrai travail (§8, §9), et une séparation exemplaire du « comment » vers l'addendum. La
différenciation revendiquée au §1 n'est pas du théâtre d'innovation : elle est gagnée par une
recherche qui a réellement passé le paysage en revue, et le PRD nomme le pari comme un pari, y
compris dans son interprétation défavorable.

Ce qui est à risque tient en trois points, tous localisés et tous réparables : une conséquence
testable est **factuellement fausse** contre le CSV qu'elle invoque (FR-8/Pilates, vérifié) ; la
jouabilité — une section entière — exige une granularité horaire que le PRD exclut explicitement
deux fois ailleurs ; et la promesse centrale de UJ-1, « Anna est prévenue », n'est portée par aucune
FR, n'a aucun canal, et entre en collision frontale avec le garde-fou le plus structurant du produit
(§7, *Le bot n'invente rien*). Le document est prêt à être découpé en épiques une fois ces trois
points tranchés ; il ne l'est pas avant.

## Decision-readiness — adequate

Le PRD prend des décisions et les affiche comme telles, ce qui est rare. Le §5.2 ne se contente pas
d'énoncer « le jour se négocie, le niveau se défend » : il donne le calcul qui a départagé les deux
options (113/127 contre 46/127) et nomme le perdant. Le §4 va plus loin en assumant explicitement le
coût de sa décision — « C'est moins satisfaisant qu'une fausse confirmation, et c'est délibéré ». Le
§7 *Sécurité des personnes* dit qu'il n'y a ni vérification d'identité, ni signalement, ni
réputation, et que ce serait inacceptable avec de vrais utilisateurs : c'est le contraire du
lissage. Les six questions du §11 sont réellement ouvertes — aucune ne porte sa réponse dans la
phrase suivante.

Ce qui empêche le verdict `strong`, c'est qu'une décision **porteuse** est traitée comme une
question de fin de document alors qu'elle contredit un garde-fou de milieu de document. La question
11.6 (« Les 86 personnes sont-elles contactées pour de bon ? ») n'est pas un détail à trancher plus
tard : toute la valeur du rendez-vous unilatéral décidé au memlog repose sur le fait que le
partenaire *est* prévenu. Si aucun message ne part, le bot annonce à Thomas quelque chose qui n'a pas
eu lieu — exactement ce que le §7 interdit. Le PRD ne voit pas cette collision.

Second angle mort : le §4 annonce **deux** populations et bâtit tout le produit dessus, mais les FR
en fabriquent une troisième. FR-3 enregistre l'utilisateur dans le vivier « à l'issue d'une
demande », alors que FR-4 ne réclame un compte qu'au moment de la mise en relation. Un visiteur qui
cherche, obtient des propositions et s'en va est donc un *utilisateur inscrit* au sens du glossaire —
lequel affirme qu'un utilisateur inscrit est « Joignable, et susceptible de répondre ». Il ne l'est
pas. Le modèle à deux populations, qui est la meilleure idée du document, est déjà faux à
l'intérieur du document.

### Findings

- **critical** « Anna est prévenue » n'est adossé à aucune exigence (§2.3 UJ-1, §7, §11.6) — Le parcours nominal, le garde-fou « aucune confirmation annoncée qui n'ait été donnée » et la question ouverte 6 disent trois choses incompatibles : le récit affirme que le partenaire est prévenu, la question demande si un message part vraiment, et aucune des 13 FR ne couvre la notification du partenaire. *Fix:* trancher la question 6 maintenant, puis créer une FR « prévenir le partenaire » (déclencheur, canal, contenu, et ce que le bot est autorisé à dire à l'utilisateur si rien ne part) — ou réécrire UJ-1 en « Anna sera contactée si… ».
- **high** Le canal de notification n'existe nulle part (§6, FR-9, FR-13) — Le memlog acte que la surface est web responsive et qu'il faut donc « un autre canal pour notifier qu'un adversaire a répondu » ; cette conséquence n'a jamais été portée dans le PRD. FR-9 (« déclenche une notification au demandeur ») et FR-13 (« passe à confirmée quand celui-ci accepte ») sont donc suspendus dans le vide. *Fix:* une ligne de NFR ou une conséquence de FR-4 nommant le canal (e-mail du compte) et le délai attendu.
- **high** Rejoindre le vivier est imposé, pas consenti (FR-3, §2.3, §7) — UJ-1 le dit franchement (« sans l'avoir demandé ») et FR-3 se contente d'informer. Le §7 promet pourtant que « le bot demande le minimum nécessaire, et à chaque fois qu'il demande quelque chose, il dit pourquoi » : ici il ne demande pas, il inscrit. Pour un produit qui expose des personnes à d'autres personnes, information ≠ opt-in, et la décision n'est prise nulle part. *Fix:* trancher explicitement (inscription automatique avec information, ou proposition acceptable et refusable), l'écrire dans FR-3, et taguer si c'est une inférence.
- **medium** Le modèle à deux populations en produit trois (§3, §4, FR-3, FR-4) — L'utilisateur enregistré mais sans compte n'est ni un profil d'amorçage (il a une ville, un vrai profil) ni un utilisateur inscrit joignable. Le glossaire affirme le contraire. *Fix:* soit conditionner FR-3 à l'existence d'un moyen de contact, soit ajouter au §3 la troisième population et dire comment le bot la traite quand elle sort en résultat de recherche.

## Substance over theater — adequate

La différenciation est **gagnée**, pas décorative. `research-paysage.md` passe en revue une quinzaine
de produits réels avec chiffres et sources, conclut au §3 qu'aucun n'utilise une interface
conversationnelle, et le §1 du PRD reprend ce constat en le retournant contre lui-même : « C'est soit
la différenciation du produit, soit le signe que la conversation n'est pas la bonne forme. » C'est
l'inverse du théâtre d'innovation. Même chose pour le non-objectif « pas de classement public », qui
cite `research-niveau.md` §4.7 — citation vérifiée, elle résout et dit bien ce que le PRD lui fait
dire. Et le §4 tout entier existe parce que la recherche a identifié le vide comme cause de mort ;
il n'est pas là parce qu'un gabarit prévoyait une section.

Le théâtre est ailleurs, et il est concentré au §6. Les quatre exigences non fonctionnelles sont des
paragraphes bien écrits sans une seule borne. « produire un signe de vie plutôt qu'un silence » — au
bout de combien de temps ? « ne bloque jamais le parcours entier » — quel est le comportement par
intégration tombée, et quelle partie du parcours survit ? « retrouve ses demandes en cours » — sur
quelle fenêtre ? « Responsive » est un adjectif seul. Ce sont exactement les phrases que la
dimension 4 demande de signaler, et elles sont ici dans la section censée poser les bornes.

Dernier point, plus subtil : le mécanisme le plus fort du produit n'est jamais énoncé comme tel. Le
memlog est explicite — « la conversation fait office d'inscription […] attaque directement le
problème de densité identifié comme mortel par la recherche ». Le PRD mentionne le vivier amorcé
(§4) et le profil-sans-formulaire (§5.1) dans deux sections différentes, sans jamais les joindre en
une réponse à la cause de mort n°1. La meilleure idée du document est dispersée.

### Findings

- **high** Quatre NFR, zéro borne (§6) — Latence, robustesse, reprise et responsive sont énoncées en prose sans seuil, sans fenêtre et sans comportement par service. Aucune n'est vérifiable, donc aucune ne contraindra l'implémentation. *Fix:* un chiffre chacune — signe de vie sous N secondes ; par intégration en panne, ce que le bot fait et ce qu'il dit ; durée de conservation d'une demande en cours ; largeur d'écran cible minimale.
- **medium** FR-10 n'a pas de seuil et le sait (§5.3) — Une section entière est justifiée par la santé (« chaleur excessive, vent dangereux ») et le `[NOTE FOR PM]` reconnaît qu'aucun seuil n'est fixé. Tant qu'ils manquent, la conséquence testable centrale de FR-10 est un adjectif. *Fix:* poser trois seuils provisoires maintenant (température ressentie, vitesse de vent, indice de qualité d'air) quitte à les réviser — un seuil faux est corrigeable, un seuil absent ne l'est pas.
- **medium** La réponse à la cause de mort n°1 n'est jamais formulée (§1, §4, §5.1) — Le vivier amorcé et l'inscription-par-conversation sont les deux moitiés d'une même réponse au problème de densité, et le PRD ne les rapproche jamais. Un lecteur aval y verra deux fonctionnalités, pas une stratégie. *Fix:* une phrase au §4 ou au §1 disant que la conversation-inscription est le mécanisme de croissance du vivier, et que c'est ce qui distingue ce produit des matchers purs morts du vide.

## Strategic coherence — adequate

Il y a une thèse, et elle est double sans être incohérente : la conversation comme forme, et
l'honnêteté comme contrainte. Les deux se tiennent — c'est parce que le bot n'invente rien (§7) que
la conversation reste utilisable, et c'est parce que le niveau est défendu (§5.2) que le produit a
quelque chose à vendre. Les 13 FR servent toutes UJ-1 ou UJ-2 ; aucune ne ressemble à une capacité
qui traînait dans un backlog. La priorisation suit la thèse et non la facilité : le comportement en
l'absence de résultat, qui serait un traitement d'erreur dans n'importe quel autre PRD, est promu au
rang de comportement principal (§2.3 UJ-2), sur la foi d'un chiffre — 55 % — que j'ai recalculé et
qui est exact.

Ce sont les critères de réussite qui décrochent. Le §10 valide l'honnêteté (SM-2), l'élargissement
(SM-3) et le bout-en-bout (SM-1) — mais **rien ne teste le pari du §1**. Le PRD affirme qu'aucun
concurrent grand public n'a fait de la conversation son interface, assume que c'est peut-être un
signal négatif, et ne se donne ensuite aucun moyen de savoir laquelle des deux lectures est la
bonne. SM-1 mesure que le tuyau ne fuit pas, pas que la forme conversationnelle vaut mieux qu'une
liste avec des filtres. La revendication la plus risquée du document est la seule qui ne soit pas
instrumentée.

Les contre-métriques sont bien choisies dans leur direction — SM-C1 nomme précisément la façon de
tricher SM-3, ce qui est le test d'une bonne contre-métrique — mais aucune des deux n'a de borne ni
d'observable. On ne peut pas constater qu'on a optimisé un taux qu'on ne mesure pas. Elles mordent
sur le papier, pas en exploitation.

### Findings

- **high** Aucun critère ne teste le pari central (§10 vs §1) — La thèse du produit est que la conversation est la bonne forme ; SM-1 à SM-3 mesurent la complétude du parcours, la non-invention et le taux de rattrapage, jamais la forme. *Fix:* ajouter un SM sur la conversation — par exemple le nombre de tours entre la première phrase et la première proposition de partenaire, ou la part de sessions où l'utilisateur réclame explicitement une liste, une carte ou un filtre (signal que la forme ne convient pas).
- **high** SM-3 est infalsifiable alors que la donnée fournit le seuil (§10) — « une proposition utilisable dans la grande majorité des cas » : ni échantillon, ni seuil, ni définition de « utilisable ». Le §5.2 a pourtant déjà le chiffre à opposer — l'élargissement sur le jour récupère 89 % des recherches vides. *Fix:* « ≥ 85 % des 127 combinaisons sans résultat exact du jeu d'amorçage produisent au moins un candidat du niveau exact demandé ».
- **medium** SM-1 revendique une couverture qu'il n'a pas (§10) — « Valide FR-1 à FR-13 » : le parcours UJ-1 n'exerce ni FR-7 (descente de niveau), ni FR-8 (absence totale), ni FR-9 hors cas limite, ni la transition vers *confirmée* de FR-13 — laquelle est de toute façon hors périmètre v1. *Fix:* restreindre la revendication de SM-1 aux FR réellement traversées et ajouter un SM adossé à UJ-2, qui couvre le cas majoritaire.
- **medium** Les deux contre-métriques ne sont pas observables (§10) — « à ne pas optimiser » sans borne ni mesure : rien ne permettra jamais de dire qu'elles ont été violées. *Fix:* donner une borne à SM-C2 (nombre maximal de tours avant la première proposition) et une observable à SM-C1 (part des mises en relation obtenues via FR-7, c'est-à-dire par descente de niveau — si elle monte, la promesse s'érode).

## Done-ness clarity — adequate

Le socle est bon et mérite d'être dit : les 13 FR ont chacune au moins une conséquence testable
réelle — je les ai reprises une par une — et plusieurs sont d'une qualité inhabituelle parce
qu'elles citent des données littérales vérifiables. FR-2 donne la phrase d'entrée et la structure de
sortie attendue. FR-5 nomme Emma Leroy : **vérifié**, elle est bien l'unique profil Tennis/Mardi/
Débutant du CSV. FR-6 nomme Anna, Iris et Tessa : **vérifié**, ce sont exactement les trois profils
Tennis/Intermédiaire, et l'union de leurs jours disponibles est bien {Lundi, Mercredi, Samedi}, ce
que UJ-1 restitue correctement en « mercredi, samedi ou lundi ». Un ingénieur peut écrire ces tests
tels quels.

Le socle est fissuré en trois endroits, et ce sont des fissures d'une autre nature qu'une simple
imprécision. **Une conséquence est fausse.** FR-8 affirme qu'« une demande de Pilates ne produit
jamais de nom de partenaire » ; c'est faux dans 9 des 21 combinaisons (niveau × jour) possibles pour
le Pilates. Sarah André *est* dans le vivier (Pilates, Mardi;Jeudi, Débutant) : toute demande de
Pilates par un Débutant la renvoie, exactement ou après élargissement du jour, et une demande
Intermédiaire mardi ou jeudi la renvoie via l'élargissement adjacent de FR-7. Seul un demandeur
Avancé ne trouve jamais rien. La cause est un télescopage de noms : le memlog notait Sarah André
comme piège de démonstration *en tant que chercheuse* (elle ne peut pas se matcher elle-même), et le
PRD en a fait une protagoniste homonyme dont le récit affirme qu'« elle est la seule pratiquante de
Pilates de tout le vivier » — ce qui ne peut être vrai que si la protagoniste **est** le profil
d'amorçage, hypothèse que le §4 exclut formellement puisque ces profils ne parlent jamais au bot.

**Une exclusion de périmètre contredit deux fonctionnalités.** FR-2 sort l'heure de la journée
(« mardi après-midi » est traité comme « mardi ») et le §9 la reconduit en hors périmètre MVP. Or
UJ-1 fait dire au bot que « mercredi s'annonce très chaud en fin d'après-midi » et qu'il vaut mieux
« le début de soirée », et FR-10 exige que le bot « propose une alternative (autre moment, autre
jour) ». La météo est intrinsèquement horaire : on ne peut pas évaluer la jouabilité d'un « mardi ».
Le PRD exclut la donnée dont sa propre section §5.3 a besoin.

**Une conséquence pointe vers un parcours qui n'existe pas.** FR-13 exige qu'« une rencontre avec un
utilisateur inscrit passe à *confirmée* quand celui-ci accepte », alors que le §9 place explicitement
le parcours d'acceptation hors périmètre. Cette conséquence n'est pas testable en v1, par
construction.

Enfin, la section la plus faible en bornes n'est pas une FR mais le §6 (voir dimension 2) : c'est là
que l'exigence « bounds, not adjectives » est la plus violée.

### Findings

- **critical** FR-8 : la conséquence Pilates est fausse contre le CSV qu'elle invoque (§5.2 FR-8, §2.3 UJ-2) — Vérification faite sur `SportsProfiles.csv` : Sarah André (Pilates, Mardi;Jeudi, Débutant) est dans le vivier, donc une demande de Pilates renvoie bien un nom dans 9 cas sur 21 (tous les Débutants quel que soit le jour, plus les Intermédiaires mardi et jeudi via FR-7). Le récit UJ-2 et sa conséquence testable confondent la protagoniste avec un profil d'amorçage homonyme. *Fix:* renommer la protagoniste de UJ-2, et remplacer la conséquence par un cas réellement vide — soit un sport absent du vivier (déjà couvert par FR-2), soit « Pilates, Avancé », qui est vide tous les jours et le reste après élargissement.
- **critical** L'heure est exclue du périmètre mais requise par la jouabilité (FR-2, FR-10, §2.3 UJ-1, §9) — Le PRD exclut deux fois l'heure de la journée et lui fait jouer un rôle central deux fois. Sans granularité horaire, FR-10 ne peut ni évaluer un créneau ni « proposer un autre moment », et le passage le plus concret de UJ-1 devient irréalisable. *Fix:* distinguer explicitement les deux usages — l'heure n'est **pas** une contrainte d'appariement (les données d'amorçage ne la portent pas) mais **est** fixée en fin de conversation entre les deux personnes, et c'est cette heure-là que la jouabilité évalue. Une phrase au §5.3 et un amendement au hors-périmètre du §9.
- **high** FR-13 : conséquence inexerçable en v1 (§5.5, §9) — « passe à *confirmée* quand celui-ci accepte » suppose un parcours d'acceptation que le §9 déclare hors périmètre. *Fix:* marquer cette conséquence v2, ou spécifier le minimum côté partenaire qui la rend atteignable (un lien d'acceptation à usage unique suffit).
- **high** FR-3 : la déduplication n'a aucun identifiant sur lequel s'appuyer (§5.1) — « Le vivier ne contient pas deux profils pour la même personne » alors que FR-4 garantit qu'aucun compte n'existe à ce stade. Un visiteur anonyme qui revient est indiscernable d'un nouveau. La conséquence n'est pas testable. *Fix:* nommer la clé d'identité et le moment où elle existe (compte via FR-4, ou fusion différée à la création de compte), et rattacher la conséquence à FR-4.
- **high** FR-8 n'a aucune conséquence positive (§5.2) — Ses trois conséquences sont des interdictions (ne jamais nommer, ne jamais inventer, ne jamais changer de sport). Rien ne dit ce que la réponse **contient**, alors que c'est le comportement majoritaire du produit à 55 % et que le PRD lui-même en fait un comportement principal. *Fix:* ajouter une conséquence sur le contenu du refus — nommer le sport et le jour tentés, dire ce qui a été élargi, et enchaîner sur l'alerte FR-9.
- **medium** FR-7 est permissif, donc satisfaisable en ne faisant rien (§5.2) — « le bot **peut** proposer un niveau adjacent » : une implémentation qui ne descend jamais respecte l'exigence et ses trois conséquences. *Fix:* énoncer l'obligation et sa condition de déclenchement, ou assumer que FR-7 est une autorisation et le dire.
- **medium** FR-9 est sans bornes (§5.2) — Durée de vie d'une alerte, critère de déclenchement (correspondance exacte ou élargie ?), nombre d'alertes simultanées, comportement si le profil correspondant est un profil d'amorçage : rien n'est fixé. *Fix:* au minimum le critère de déclenchement et une durée de validité.
- **medium** FR-11 est dans le périmètre MVP avec une source de données non tranchée (§5.4, §9, addendum) — L'addendum note « Terrains : non tranché ». Le PRD met la proposition de terrains dans le périmètre sans remonter le risque, si bien que la seule branche garantie atteignable est « le bot dit qu'il n'a pas de donnée ». *Fix:* une question ouverte ou un `[NOTE FOR PM]` au §5.4 signalant que la faisabilité de FR-11 dépend d'une source non identifiée.
- **low** « Niveau adjacent » n'est pas défini (§3, FR-7) — Le terme porte toute la logique de FR-7 et sa troisième conséquence l'utilise implicitement (« Débutant et Avancé ne sont jamais proposés l'un pour l'autre »), mais le glossaire s'arrête aux trois valeurs. *Fix:* une ligne au §3.

## Scope honesty — strong

C'est la dimension la mieux tenue. Les omissions ne sont jamais laissées à l'inférence : le §2.2 dit
qui n'est pas visé, le §8 donne cinq non-objectifs *avec leur raison* (dont un adossé à la
recherche), et le §9 liste six exclusions explicites en donnant à chaque fois la cause — l'heure
parce que les données ne la portent pas, le côté partenaire parce que les profils d'amorçage ne
peuvent pas répondre. Le §7 va jusqu'à dire que le traitement de la vie privée serait insuffisant
pour un vrai lancement, et pourquoi ce choix est cohérent avec un projet personnel. Le déscopage est
proposé, pas fait en silence.

Densité des items ouverts : 6 questions ouvertes + 2 `[ASSUMPTION]` + 3 `[NOTE FOR PM]` = 11. Pour un
projet personnel d'apprentissage sans jury de relecture, c'est proportionné — c'est même plutôt bas
au regard du nombre de sujets réellement non tranchés. Aucun de ces onze items n'est un
faux-semblant : les trois `[NOTE FOR PM]` sont posés à de vraies tensions (les seuils de jouabilité,
la conformité, le côté partenaire), pas à des points de contrôle confortables.

L'aller-retour du §12 est **complet** : deux `[ASSUMPTION]` inline (§2.3 UJ-1 et §5.1 FR-2), deux
entrées à l'index, correspondance exacte dans les deux sens, chacune préfixée de son emplacement.
Rien à signaler de ce côté.

Le reproche porte donc uniquement sur le sous-taggage : deux ou trois inférences réelles circulent
sans marque, et un garde-fou contredit une question ouverte.

### Findings

- **medium** Un garde-fou contredit une question ouverte (§7 vs §11.6) — Le §7 affirme comme acquis que « le bot les nomme et **les contacte** », pendant que la question 6 demande si un SMS part réellement. Le lecteur ne peut pas savoir lequel des deux fait foi. *Fix:* aligner — soit le §7 devient conditionnel jusqu'à l'arbitrage, soit la question 6 se ferme.
- **medium** L'inscription automatique au vivier n'est pas taguée (§2.3 UJ-1, FR-3) — Que l'utilisateur accepte d'être rendu trouvable par des inconnus au seul motif qu'il a parlé au bot est une inférence, non une chose confirmée. Elle est même mise en avant comme un bénéfice (« sans l'avoir demandé »). *Fix:* `[ASSUMPTION: l'inscription au vivier est automatique et signalée, non soumise à acceptation]` + entrée au §12.
- **medium** L'addendum et le PRD divergent sur le niveau (addendum, §9, §11.5) — L'addendum annonce que le PRD « n'énoncera que la capacité attendue et ses propriétés observables (le niveau se corrige avec l'usage, il est affiché comme une fourchette et non comme une valeur précise, il est distinct par sport) ». Le PRD fait l'inverse : niveau déclaratif à trois valeurs, correction par l'usage en hors périmètre. Un des deux documents est périmé et l'aval ne saura pas lequel. *Fix:* corriger le paragraphe de l'addendum pour refléter l'arbitrage réellement pris.
- **low** Aucun `[NON-GOAL for MVP]` inline (tout le document) — Les omissions sont concentrées en §8 et §9, ce qui est lisible, mais aucune n'est signalée là où elle pourrait être silencieusement supposée — notamment au §5.4 (le produit ne réserve rien) et au §5.5 (aucune écriture dans l'agenda du partenaire). *Fix:* deux callouts inline, ou rien du tout si le regroupement est assumé.

## Downstream usability — adequate

Le PRD est un chain-top et il s'est équipé pour l'être : le §0 nomme ses consommateurs aval, déclare
le vocabulaire du §3 **contraignant**, et renvoie le « comment » à l'addendum plutôt que de le
mélanger aux capacités. Les identifiants sont propres — FR-1 à FR-13 contigus et uniques, UJ-1/UJ-2,
SM-1 à SM-3 plus SM-C1/SM-C2, aucun trou, aucun doublon. Les annotations « Réalise UJ-x » couvrent
toutes les sections de fonctionnalités, donc chaque FR est rattachable à un parcours. Les renvois
externes résolvent : j'ai ouvert `research-niveau.md` §4.7 et `research-paysage.md` §2 et §3, ils
disent bien ce que le PRD leur fait dire. Les deux UJ ont un protagoniste nommé qui porte son
contexte inline — l'entrée Journey-led est correctement tenue.

Deux problèmes limitent quand même l'extraction aval. D'abord une asymétrie de définition : le §3
décrit le *profil d'amorçage* champ par champ (prénom, nom, téléphone, sport, jours, niveau, et ce
qu'il n'a pas) et ne dit **rien** des champs d'un *utilisateur inscrit*. Or FR-11 lui ajoute une
ville, FR-4 un compte, FR-9 un moyen d'être notifié : l'aval devra inventer un modèle que le PRD
avait toutes les cartes pour poser. Ensuite le glossaire est incomplet là où il compte : « candidat »
(7 occurrences) et « créneau » (12 occurrences) sont deux noms de domaine porteurs, employés jusque
dans les conséquences testables, et absents du §3 — alors que le §0 promet un vocabulaire sans
synonyme.

### Findings

- **high** Le profil d'un utilisateur inscrit n'est jamais défini (§3, FR-4, FR-9, FR-11) — Le glossaire donne les champs exacts du profil d'amorçage et laisse l'autre population sans schéma, alors que trois FR lui ajoutent des attributs. Toute dérivation aval (UX, architecture, stories) devra reconstruire ce modèle de mémoire, et le fera différemment. *Fix:* symétriser l'entrée du §3 — champs hérités de la demande, ville (FR-11), moyen de contact (FR-4/FR-9), et ce qui reste vide.
- **medium** « Candidat » et « créneau » manquent au glossaire déclaré contraignant (§0, §3) — 7 et 12 occurrences respectivement, y compris dans les conséquences testables de FR-5, FR-6, FR-8 et FR-10. Un extracteur aval ne saura pas si « candidat » est un synonyme de « partenaire » (avant retenue ?) ni si « créneau » est une *rencontre* avant confirmation. *Fix:* deux entrées au §3, ou remplacement systématique par les termes déjà définis.
- **medium** Trois étiquettes pour le même fichier (§0, §2.3, §3, §4, §5.2) — « données d'amorçage », « jeu d'amorçage » et « les 86 profils » désignent la même chose dans cinq sections. *Fix:* n'en garder qu'une, de préférence celle du glossaire.
- **low** Collision de prénom entre une protagoniste et un profil d'amorçage (§2.3 UJ-2, CSV) — Au-delà de l'erreur factuelle relevée en dimension 4, la coexistence de deux Sarah piégera toute génération automatique de scénarios de test à partir du PRD. *Fix:* choisir pour les protagonistes des prénoms absents du CSV.
- **low** « Rendez-vous », « rencontre » et « créneau » alternent au §5.5 — Le glossaire ne définit que *rencontre*, et le titre de section comme la description utilisent les deux autres. *Fix:* uniformiser sur *rencontre*.

## Shape fit — strong

La forme correspond au produit. Produit grand public avec une UX porteuse : les parcours utilisateur
sont là, nommés, et ils sont réellement load-bearing — UJ-2 ne décore pas, il porte le comportement
majoritaire du système. L'absence de section persona autonome est un choix de méthode assumé
(entrée Journey-led) et le contexte est effectivement porté inline dans les deux récits : Thomas a
un âge, une pratique, un déclencheur et un agenda ; Sarah a une pratique et une contrainte. Rien ne
manque de ce côté.

La rigueur allégée du projet personnel est visible aux bons endroits et *nommée* : le §10 s'ouvre sur
« Projet personnel : la mesure est qualitative et volontairement courte », le §7 explique pourquoi la
vie privée est traitée en garde-fous et non en section de conformité, et le §7 *Sécurité des
personnes* dit franchement que le compromis ne tiendrait pas avec de vrais utilisateurs. C'est la
bonne façon d'alléger : en disant qu'on allège et pourquoi.

Le document n'est pas sur-formalisé — pas de matrice de responsabilités, pas de dix personas, pas de
tableau de risques décoratif — et pas sous-formalisé non plus. Le seul écart de calibrage est la
longueur : le memlog visait « ~2 pages » et le résultat en fait quatre à cinq fois plus. L'essentiel
de ce surplus est de la substance (le §4 et le raisonnement chiffré du §5.2 valent leur place), mais
le §6 et le §7 sont les deux endroits où le ratio prose / contenu vérifiable est le plus défavorable.

### Findings

- **low** Écart au format convenu (tout le document vs memlog) — Cible actée à ~2 pages, document livré à ~10. Ce n'est pas un défaut en soi puisque le contenu est dense, mais l'écart mérite d'être conscient plutôt que subi. *Fix:* si compression il doit y avoir, comprimer le §6 (en le remplaçant par des seuils, ce qui le raccourcira) et le §7, pas le §4 ni le §5.2.

## Mechanical notes

**Identifiants.** FR-1 à FR-13 contigus, uniques, sans doublon. UJ-1 et UJ-2 idem. SM-1 à SM-3 plus
SM-C1 et SM-C2 idem. Toutes les références croisées internes (« FR-4 » depuis FR-9, « §7 » depuis
§4, « FR-10 » depuis §11.2, « research-niveau.md §4 » depuis §9) résolvent.

**Aller-retour de l'index des hypothèses : complet.** Deux `[ASSUMPTION]` inline — §2.3 UJ-1 (prénom
substitut) et §5.1 FR-2 (heure ignorée) — et exactement deux entrées au §12, chacune préfixée de son
emplacement, chacune reprenant fidèlement le texte inline. Aucune orpheline dans un sens ni dans
l'autre.

**Chiffres vérifiés contre `SportsProfiles.csv`** (recalcul complet) : 86 profils ✓ ; 11 sports ✓ ;
231 combinaisons sport × jour × niveau ✓ ; 127 combinaisons vides, soit 55 % ✓ ; élargissement sur
le jour récupère 113 des 127, soit 89 % ✓ ; Emma Leroy unique sur Tennis/Mardi/Débutant ✓ ;
Tennis/Mardi/Intermédiaire vide ✓ ; Anna Perrot, Iris Payet et Tessa Armand sont exactement les
trois profils Tennis/Intermédiaire, union de leurs jours = Lundi, Mercredi, Samedi, restituée
correctement par UJ-1 ✓.

**Une précision de reproductibilité (§5.2).** « Relâcher le niveau en conservant le jour n'en
récupère que 46 (36 %) » n'est vrai qu'en se limitant aux niveaux **adjacents**, conformément à
FR-7. Sans cette contrainte, le chiffre est 61 (48 %). La phrase ne dit pas « adjacent » ; qui
referait le calcul trouverait un autre nombre et croirait à une erreur. Ajouter le mot.

**Une nuance sur les 231 combinaisons (§2.3, §5.2).** Le décompte est uniforme (11 × 7 × 3) et non
pondéré par la demande réelle. « 55 % ne renvoient aucun candidat » est donc un fait sur la grille,
pas une prévision du taux d'échec vécu par les utilisateurs — lequel dépendra de la distribution des
sports demandés. Le PRD s'appuie fortement sur ce chiffre ; une incise d'une ligne le mettrait à
l'abri.

**Titre.** « Trouve-moi un partenaire » est marqué « Titre de travail, à confirmer » au §0 mais ne
figure pas parmi les questions ouvertes du §11, qui recense pourtant des points bien moins ouverts.

**Sections requises.** Pour les enjeux convenus et le type de produit, rien ne manque : vision,
utilisateur cible, parcours, glossaire, fonctionnalités, NFR, contraintes, non-objectifs, périmètre
MVP, critères de réussite, questions ouvertes, index des hypothèses. L'absence de section persona
autonome est conforme à l'entrée Journey-led et n'est pas comptée comme un manque.
