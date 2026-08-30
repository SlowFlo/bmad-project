---
title: "Ex Aequo — chatbot de mise en relation sportive"
status: final
version: 5
created: 2026-08-26
updated: 2026-08-30
---

# PRD — Ex Aequo

## 0. Objet du document

Ce PRD décrit **ce que le produit fait**, pas comment il est construit. Il s'adresse à toi
en tant que constructeur, et aux workflows aval (UX, architecture, découpage en épiques).

Le « comment » — le LLM retenu, le découpage en agents, la base de données, les API
tierces — vit dans [addendum.md](addendum.md). Les deux recherches qui ont nourri les
décisions sont archivées dans [research-niveau.md](research-niveau.md) et
[research-paysage.md](research-paysage.md). Les données d'amorçage sont dans
[SportsProfiles.csv](SportsProfiles.csv). Le fil des décisions est dans `.memlog.md`, et
**les changements de fond d'une version à l'autre sont au §13** — les citer plutôt que de
supposer qu'une exigence n'a pas bougé.

L'expérience et le design dérivés de ce PRD vivent dans
[ux-designs/ux-bmad-2026-08-26/](../../ux-designs/ux-bmad-2026-08-26/) —
`EXPERIENCE.md` pour les moments et le ton, `DESIGN.md` pour la forme visuelle.

Le vocabulaire du §3 est contraignant : les exigences fonctionnelles l'emploient
littéralement, sans synonyme.

## 1. Vision

Trouver quelqu'un avec qui pratiquer son sport, à son niveau, est un problème
étonnamment pénible. On demande dans un groupe WhatsApp, on relance, personne ne répond,
et on finit par ne pas y aller. Les applications qui s'y attaquent sont des places de
marché de réservation de terrains où la mise en relation est une fonctionnalité annexe ;
elles s'utilisent avec des listes, des cartes et des filtres.

Ce produit fait le pari inverse : **une conversation.** L'utilisateur arrive sur le site,
un chatbot est là, et il dit ce qu'il veut — « je veux jouer au tennis mardi ». Le bot
cherche quelqu'un de son niveau, négocie une date jouable, vérifie que les conditions
sont raisonnables, propose un endroit où jouer et pose la rencontre dans son agenda.
En un seul fil de discussion, sans formulaire.

Le pari est réel : la recherche menée pour ce PRD n'a trouvé **aucun** produit grand
public de mise en relation entre joueurs utilisant une interface conversationnelle
(voir [research-paysage.md](research-paysage.md), §3). C'est soit la différenciation du
produit, soit le signe que la conversation n'est pas la bonne forme. Le projet assume ce
pari en connaissance de cause, et le §10 se donne les moyens de savoir laquelle des deux
lectures est la bonne.

**Ex Aequo ne dessert qu'une ville : Lyon.** Ce n'est pas une limite de départ qu'on
lèvera plus tard, c'est une décision de conception. La recherche montre que dans cette
catégorie la liquidité est **par lieu** et non à l'échelle d'un pays : les produits qui
survivent chevauchent un sport dense dans une géographie resserrée, et les matchers qui
s'éparpillent meurent du vide ([research-paysage.md](research-paysage.md), §2). Une seule
ville, c'est le seul moyen pour un vivier de cette taille d'avoir une chance d'être dense
quelque part.

**Le mécanisme de croissance du vivier est la conversation-inscription.** Un matcher sans
densité ne matche personne : c'est ce qui tue les petits produits de cette catégorie
(*ibid.*, §4). La même recherche décrit un second régime d'échec, l'intégrité du niveau,
qu'on rencontre une fois le premier franchi (voir §7). Ex Aequo répond au premier en
supprimant la marche : il n'y a pas de formulaire d'inscription, le profil se construit
en parlant, et **le compte demandé au moment de la mise en relation fait entrer son
auteur dans le vivier** (FR-3, FR-4). Une personne qui vient chercher un partenaire en
devient un.

Il faut être clair sur ce que cette réponse vaut : elle est **du PRD, pas de la
recherche**. Les 86 profils d'amorçage sont fictifs et ne jouent jamais — c'est du décor,
pas de la densité. Le pari est que la friction nulle suffise à convertir des chercheurs
en profils assez vite pour que le décor cède la place. Ce pari n'est validé par aucune
source ; c'est celui du projet.

La raison d'être secondaire du produit, elle aussi pleinement assumée : servir de terrain
d'apprentissage sur les systèmes agentiques.

## 2. Utilisateur cible

### 2.1 Ce que l'utilisateur cherche à faire

- **Fonctionnel** — obtenir un créneau confirmé, avec quelqu'un de son niveau, sans
  avoir à relancer trois personnes.
- **Émotionnel** — éviter l'humiliation douce du match trop déséquilibré, dans les deux
  sens : se faire écraser, ou passer une heure à faire du renvoi de balle par politesse.
- **Contextuel** — la demande naît d'une fenêtre de disponibilité, souvent tard, souvent
  pour dans quelques jours. Elle est courte et concrète.
- **Pour le constructeur** — disposer d'un système multi-agents non trivial mais fini,
  avec de vraies intégrations externes.

### 2.2 Qui n'est pas visé en v1

- **Les joueurs hors de Lyon.** Le produit ne dessert qu'une agglomération, et le dit à
  quiconque cherche ailleurs plutôt que de renvoyer un vivier vide.
- Les clubs et les gestionnaires d'équipements. Le produit ne s'adresse qu'aux joueurs.
- Les sports d'équipe pris comme tels : le produit met en relation **deux** personnes,
  jamais une équipe entière. Un footballeur peut y trouver un partenaire d'entraînement,
  pas un match.

### 2.3 Parcours utilisateur

> **UJ-1. Thomas trouve quelqu'un à son niveau, mais pas le jour qu'il voulait.**
> `[ASSUMPTION: le prénom du protagoniste est un substitut — à remplacer par une personne réelle. Il est choisi absent des données d'amorçage pour qu'aucun scénario de test ne le confonde avec un profil du vivier.]`
>
> Thomas, la trentaine, joue au tennis de façon régulière sans être classé. Mardi soir
> il regarde son agenda, voit un trou le mardi suivant, et ouvre le site sur son
> ordinateur. Pas de page d'accueil à traverser, pas d'inscription : **le chatbot est
> là**. Il écrit « je veux jouer au tennis mardi aprem, je suis intermédiaire ».
>
> **Le bot ne lui demande rien sur son niveau.** Thomas a employé le mot « intermédiaire »,
> qui est l'une des trois valeurs du produit : le bot le prend tel quel et passe à la suite.
> S'il avait écrit « j'ai un niveau correct », le bot n'aurait rien interprété — il lui
> aurait ouvert les trois choix, Débutant, Intermédiaire ou Avancé, en disant pourquoi il
> les pose.
>
> Personne. Aucun joueur de tennis de ce niveau n'est disponible le mardi. Plutôt que de
> s'excuser dans le vide, le bot revient avec ce qu'il a :
> *« Personne à votre niveau au tennis le mardi. En revanche Anna, Iris et Tessa jouent
> exactement à votre niveau — mercredi, samedi ou lundi. Lequel vous arrange ? »* Thomas
> répond mercredi et retient Anna.
>
> Le bot propose deux courts à Lyon, puis regarde les conditions : mercredi s'annonce à
> 31 °C ressentis en fin d'après-midi, au-dessus du seuil de 28 °C à partir duquel il
> alerte. Il propose plutôt 19 h, où il fera 24 °C. **C'est la jouabilité qui amène
> l'heure** : le vivier ne connaît que des jours, jamais des heures, et le bot n'a donc
> aucune heure à proposer tant qu'il n'a pas de raison. Thomas peut refuser et garder
> 17 h — le bot informe, il n'interdit pas.
>
> Thomas valide 19 h. **C'est ici que le bot demande un compte** : il va prévenir Anna,
> et il faudra pouvoir recontacter Thomas quand elle répondra. Le bot dit aussi ce que le
> compte implique — *« vous deviendrez trouvable par les autres personnes qui cherchent un
> partenaire de tennis »* — et Thomas signe avec son compte Google.
>
> **Le bot pose la rencontre dans son agenda** et envoie à Anna un SMS qui explique
> d'où il sort, ce qui est proposé, et comment accepter. La rencontre est créée **en
> attente** : Anna est prévenue, elle n'a pas encore répondu, et le bot le dit exactement
> comme ça. Thomas ferme l'onglet avec un créneau bloqué, un lieu, et une heure choisie
> pour ne pas jouer à 31 °C.
>
> **Cas limite —** si Thomas refuse tous les jours proposés, le bot lui propose de le
> prévenir par e-mail quand quelqu'un correspondra exactement à sa demande. C'est le seul
> moment où une demande sans résultat produit quand même quelque chose.

> **UJ-2. Nadia cherche un partenaire là où il n'y a personne.**
>
> Nadia fait du Pilates depuis dix ans et cherche quelqu'un pour mardi. Sa phrase ne porte
> aucun des trois mots du produit : le bot lui ouvre les trois choix, et elle prend
> **Avancé**. Il n'y a personne, et il n'y aura personne quel que soit le jour — le vivier
> compte une seule pratiquante de Pilates, et elle est débutante. **Le bot n'apparie qu'à
> niveau strictement égal** ; il ne proposera pas une débutante à une avancée, ni ne lui
> demandera si elle accepterait.
>
> Le bot le dit franchement, sans inventer un partenaire ni noyer le refus dans des
> formules : il nomme le sport et le jour tentés, dit qu'il a aussi regardé tous les autres
> jours, et qu'il n'a rien trouvé. Il propose de la prévenir si quelqu'un s'inscrit. Nadia
> accepte, crée un compte — et rejoint le vivier, de sorte que le prochain pratiquant de
> Pilates, lui, la trouvera.

**Ce parcours est rare, et c'est le chemin de UJ-1 qui est majoritaire.** Sur les 231
combinaisons de sport, jour et niveau des données d'amorçage, 55 % ne renvoient aucun
candidat *exact* — mais l'élargissement sur le jour en rattrape la quasi-totalité, et il
ne reste que **14 combinaisons, soit 6,1 %, où il n'y a réellement personne**. Toutes sont
du Pilates.
Ce que ces chiffres disent au produit : le comportement principal n'est pas le refus,
c'est **l'élargissement et son explication** (UJ-1) ; le refus total est un cas rare qui,
sur les données d'amorçage, tient tout entier à un seul profil sur 86. Il doit être
irréprochable parce qu'il est le moment où le bot est le plus tenté de broder, pas parce
qu'il est fréquent.

## 3. Glossaire

- **Données d'amorçage** — le fichier des 86 profils chargés au premier lancement. C'est
  la seule étiquette employée dans ce document pour désigner ce fichier.
- **Vivier** — l'ensemble des profils parmi lesquels le bot cherche. Contient des
  *profils d'amorçage* et des *utilisateurs inscrits*. Il grossit à chaque compte créé
  (FR-3) et ne diminue que par une **sortie définitive** demandée depuis un SMS (FR-14).
  Un profil n'en sort pas parce qu'il a joué : ce qu'une rencontre produit, c'est un *jour
  bloqué*, et le cycle de vie complet d'un profil est en FR-16.
- **Profil d'amorçage** — un des 86 profils issus des *données d'amorçage*. Possède un
  prénom, un nom, un téléphone, un sport, des *jours disponibles* et un *niveau*. N'a ni
  compte, ni e-mail, ni ville. **Ne parle jamais au bot** — mais peut accepter une
  rencontre en suivant le lien de son SMS (FR-14).
- **Utilisateur inscrit** — une personne qui a parlé au bot et créé un compte. Son profil
    porte : un prénom, l'adresse e-mail du compte, **un sport** avec son *niveau* et ses
  *jours disponibles*, et facultativement un secteur de Lyon et un
  numéro de téléphone. Il n'a ni nom de famille, ni téléphone, ni secteur tant qu'il ne
  les donne pas. Joignable par e-mail, et susceptible de répondre.
- **Partenaire** — la personne que le bot propose. Quelqu'un avec qui pratiquer le même
  sport : un adversaire au tennis, un binôme en escalade, un partenaire de rythme en
  course à pied, quelqu'un au même cours de yoga. Pas nécessairement un adversaire.
- **Candidat** — un profil du vivier que la recherche a retenu et que le bot présente,
  avant que l'utilisateur en retienne un. Un candidat retenu devient un *partenaire*.
- **Niveau** — Débutant, Intermédiaire ou Avancé. **Valeur déclarée par la personne,
  demandée une fois, jamais vérifiée.** Le bot la retient telle quelle si la personne a
  employé l'un des trois mots ; sinon il lui ouvre les trois choix (FR-2). Il ne l'infère
  jamais d'autre chose, et rien ne la corrige ensuite. Un profil dont la personne a refusé
  de répondre porte un **niveau inconnu**, qui n'est pas une quatrième valeur mais une
  absence : ce profil ne sort d'aucune recherche.
- **Jour bloqué** — un jour de la semaine pendant lequel un profil cesse d'être renvoyé par
  les recherches, parce qu'une *rencontre* y est posée. Le blocage porte sur ce jour seul,
  jamais sur le profil entier (FR-16).
- **Jour disponible** — un jour de la semaine, sans heure. Le vocabulaire des *données
  d'amorçage* et des profils.
- **Demande** — ce que l'utilisateur exprime : un sport, un ou plusieurs jours, un niveau.
- **Élargissement** — la relaxation d'une contrainte de la *demande* pour obtenir des
  *candidats* quand la recherche exacte ne renvoie rien.
- **Créneau** — un jour et une heure précise, proposés pour une *rencontre*. Le jour vient
  de la *demande* et des *jours disponibles* ; l'heure est fixée en fin de conversation et
  n'existe nulle part dans le vivier.
- **Rencontre** — un *créneau* retenu entre l'utilisateur et un *partenaire*, dans un lieu
  donné. Elle porte un statut et un seul : **en attente**, **confirmée**, **déclinée**,
  **expirée** ou **abandonnée** (FR-13). Les quatre premiers disent la réponse du
  *partenaire* ; le cinquième dit que l'utilisateur a renoncé. C'est le seul mot du
  glossaire pour cet objet : le document ne dit ni « rendez-vous » ni « match ».
- **Recherche active** — une *demande* qui a produit une *rencontre* encore
  **en attente** ou **confirmée** (FR-13). Une demande qui n'a produit aucune rencontre
  — faute de candidat, ou parce qu'elle est devenue une *alerte différée* (FR-9) —
  n'est **jamais** active. Une personne n'en porte **qu'une seule à la fois**, et seules
  comptent les rencontres nées de ses propres demandes : être sollicité par quelqu'un
  d'autre (FR-14) n'occupe pas la place.
- **Retenir un créneau** — le geste par lequel l'utilisateur arrête un *créneau* et
  déclenche la mise en relation. C'est **le seul geste du produit qui engage quelqu'un
  d'autre** : à partir de là un message part vers le *partenaire* (FR-14) et la
  *rencontre* existe (FR-13). **Rien n'est retenu tant qu'il n'a pas eu lieu.** C'est ce
  que le document désignait auparavant par « la validation du créneau ».
- **Jouabilité** — l'appréciation des conditions extérieures d'un *créneau* : température
  ressentie, vent, qualité de l'air.

## 4. Le vivier et ses deux populations

Cette section précède les fonctionnalités parce qu'elle les conditionne presque toutes.

Les données d'amorçage contiennent 86 personnes qui n'ont jamais entendu parler du
produit. Elles ont un numéro de téléphone et rien d'autre : pas de compte, pas d'e-mail,
pas de ville. Elles peuplent le vivier pour qu'il ne soit pas vide au démarrage. Le
diagnostic vient de la recherche — un matcher vide meurt
([research-paysage.md](research-paysage.md), §2) — mais **pas ce remède** : le §2 de cette
recherche recense quatre stratégies d'amorçage réellement observées, et charger des
profils fictifs n'en est aucune. C'est du décor destiné à tenir le temps que la
conversation-inscription produise de vrais profils (§1).

**Ces 86 personnes sont fictives, et leurs numéros aussi.** Tous appartiennent à la plage
`+336 39 98 XX XX`, réservée par l'ARCEP aux œuvres de fiction et garantie non attribuée à
un abonné. C'est une propriété dont le produit dépend : FR-14 envoie de vrais SMS, et le
les données d'amorçage doivent donc être incapables d'en faire parvenir un à quelqu'un.

**Les utilisateurs inscrits**, eux, sont venus par le bot et ont créé un compte.

**Ce qui sépare les deux populations n'est pas la capacité de répondre — c'est le canal
et l'initiative.** Un profil d'amorçage ne parle jamais au bot : il ne fait jamais de
demande, ne cherche jamais de partenaire, n'a pas de conversation. Il reçoit un SMS quand
quelqu'un le retient, et peut accepter en suivant le lien (FR-14). Un utilisateur inscrit
fait tout le reste : il demande, il cherche, il retient, il est prévenu par e-mail.

**Sur un point les deux populations sont identiques : un profil porte un sport, et un
seul.** Les 86 profils d'amorçage n'en portent qu'un parce que la donnée est ainsi ; les
utilisateurs inscrits n'en portent qu'un parce que le modèle est ainsi (FR-3). Il n'y a
donc pas deux qualités de profil dans le vivier.

Le produit **ne fait pas semblant** que ces deux populations sont équivalentes. Une
rencontre reste *en attente* tant que le partenaire n'a pas accepté, et l'utilisateur le
sait — quelle que soit la population dont vient ce partenaire. Le bot n'annonce jamais
qu'un partenaire a confirmé avant qu'il l'ait fait : voir §7, *Le bot n'invente rien*.

## 5. Fonctionnalités

### 5.1 Conversation et création de profil

**Description.** Le chatbot est l'interface unique. Il est accessible immédiatement, sans
authentification. L'utilisateur exprime sa demande en langage naturel ; le bot en extrait
sport, jours et niveau, et demande uniquement ce qui manque. Réalise UJ-1, UJ-2.

Ce même échange constitue le profil. L'utilisateur ne remplit jamais de formulaire : il a
décrit son besoin, et cette description *est* son profil.

#### FR-1 : Dialoguer sans authentification

Un visiteur peut ouvrir le site et dialoguer avec le bot sans compte ni inscription.

**Conséquences testables :**
- La page d'entrée présente le chatbot utilisable, sans écran d'authentification préalable.
- Un visiteur sans compte peut formuler une demande et recevoir des propositions de
  partenaires nommés.

#### FR-2 : Extraire une demande du langage naturel

Le bot extrait d'un message libre le sport, les jours et le *niveau*, et réclame ce qui
manque un élément à la fois.

**Le niveau ne s'interprète pas.** Si la personne a employé l'un des trois mots exacts —
Débutant, Intermédiaire, Avancé — le bot le retient et ne demande rien. Toute autre
formulation ouvre les trois choix, avec son motif attaché : c'est ce qui permettra de la
trouver. Le LLM n'a jamais le droit d'improviser sur cette donnée, parce que c'est elle
qui structure l'appariement.

**La liste des sports est ouverte.** Les 11 sports des données d'amorçage sont un jeu
d'amorçage, pas un catalogue. Un sport que le vivier ne connaît pas est un sport **vide**,
pas un sport refusé, et le premier pratiquant à le demander le fonde.

**Conséquences testables :**
- « je veux jouer au tennis mardi aprem, je suis intermédiaire » produit la demande
  {sport: Tennis, jours: [Mardi], niveau: Intermédiaire} sans qu'aucune question soit posée.
- « j'ai un niveau OK » n'est ni interprété ni stocké : le bot ouvre les trois choix.
- Si le sport, le jour **ou** le niveau manque, le bot réclame un seul élément à la fois
  avant de lancer la recherche.
- Une demande sur un sport absent du vivier — le squash, le badminton — reçoit la réponse
  d'un vivier vide (FR-8) et non un refus.
- Une demande qui vise explicitement une autre ville que Lyon reçoit une réponse explicite
  (§2.2) plutôt qu'une recherche vide.
- Une demande complète formulée alors qu'une *recherche active* occupe déjà la place
  n'est pas lancée : le bot nomme ce qui occupe et donne la sortie dans la même phrase
  (FR-13).
- **Le bot ne demande jamais le niveau pendant la recherche** : ni pour élargir, ni après
  avoir montré des candidats, ni pour rattraper un résultat vide.
- Un refus de répondre est accepté : le profil portera un *niveau inconnu*, et le bot dit
  ce que ça coûte avant que la personne tranche.

**Notes :** `[NOTE FOR PM]` un *niveau inconnu* rend un profil inerte des deux côtés — ni
trouvable, ni capable de chercher. C'est un état légal du modèle et un cul-de-sac produit.
S'il devient fréquent, c'est le premier signe que la question tombe au mauvais moment.

`[NOTE FOR PM]` **une liste de sports ouverte fragmente le vivier si les libellés ne sont
pas normalisés** : « tennis », « Tennis » et « tennis en simple » ne se rencontreraient
jamais. La normalisation est un point d'architecture, pas de produit — voir
[addendum.md](addendum.md).

**Hors périmètre :** l'heure de disponibilité. Les données d'amorçage ne descendent pas
sous le jour ; « mardi après-midi » est traité comme « mardi ». Cette exclusion ne porte
que sur la disponibilité stockée dans le vivier — **l'heure de la rencontre**, elle, est
dans le périmètre et se fixe en fin de conversation (FR-10, FR-12).
`[ASSUMPTION: l'heure de disponibilité est ignorée en v1 plutôt que collectée pour les seuls nouveaux profils, afin de ne pas créer deux qualités de données dans le vivier.]`

#### FR-15 : retirée en v2

L'exigence établissait le *niveau* par des questions de faits — ancienneté, fréquence,
club, compétition — plutôt qu'en le demandant. **Elle est retirée parce que la précision
du niveau est sortie du périmètre** (§9) : un mécanisme d'inférence n'a plus d'objet dès
lors que le produit assume la valeur déclarée telle quelle. La seule contrainte qui
survit — *le bot ne demande jamais le niveau pendant la recherche* — est passée en FR-2 et
au §7.

*Son numéro n'est pas réattribué. Une exigence retirée garde son identifiant, pour que les
documents qui la citaient trouvent ce qui lui est arrivé plutôt qu'une autre exigence à sa
place (§13).*

#### FR-3 : Enregistrer l'utilisateur dans le vivier

Un utilisateur devient trouvable par les recherches des autres **à la création de son
compte**, et pas avant. Son profil porte **un sport, et un seul** — celui de la demande
qui l'a amené là, avec son niveau et ses jours.

**Conséquences testables :**
- Un visiteur sans compte ne sort jamais comme candidat d'une recherche.
- Après que Thomas a créé son compte, une recherche « tennis, mardi, intermédiaire »
  renvoie Thomas.
- Une nouvelle demande sur le sport déjà porté met à jour ses jours et son niveau.
- Une demande sur un **autre** sport remplace le sport du profil, son niveau et ses jours.
  Le bot annonce le remplacement avant de l'appliquer et dit ce qu'il coûte : la personne
  cesse d'être trouvable sur le sport précédent.
  `[ASSUMPTION: le remplacement est la conséquence retenue du profil mono-sport. Refuser la seconde demande, ou tenir deux profils sous un même compte, sont les deux autres issues possibles ; aucune des trois n'a été mesurée.]`
- Un profil de *niveau inconnu* (FR-2) n'est jamais renvoyé par une recherche.
- Le compte est la clé d'identité du profil : deux conversations d'une même personne
  connectée au même compte ne produisent jamais deux profils.

**Note :** les 86 profils d'amorçage ne portent qu'un sport chacun. Ce n'est plus une
propriété de la seule donnée — c'est le modèle, et les deux populations du vivier s'y
conforment (§4).

#### FR-4 : Demander un compte au moment de la mise en relation

Le bot demande la création d'un compte lorsqu'il va exposer l'utilisateur à une autre
personne ou devra le recontacter — jamais avant. Réalise UJ-1, UJ-2.

**Conséquences testables :**
- Rechercher, obtenir des propositions, retenir un candidat et consulter la jouabilité ne
  déclenchent aucune demande de compte.
- **Valider un créneau avec un partenaire** la déclenche. Accepter une alerte différée
  (FR-9) la déclenche également.
- Le bot énonce la raison de la demande au moment où il la formule, **et dit que le compte
  rend l'utilisateur trouvable par les autres** (FR-3).
- La connexion Google ou Microsoft fournit l'adresse e-mail du compte, qui devient le
  canal des notifications différées.
- Le numéro de téléphone est facultatif et n'est jamais exigé pour terminer un parcours.

### 5.2 Recherche de partenaire

**Description.** Le bot cherche d'abord une correspondance exacte. En l'absence de
résultat — le cas majoritaire — il élargit sur **un seul axe** : le jour. **Le jour se
négocie ; le niveau, jamais.** Réalise UJ-1, UJ-2.

Cette règle n'est pas arbitraire. Sur les 231 combinaisons possibles des données
d'amorçage, relâcher le jour en conservant le niveau récupère 113 des 127 recherches vides
(89 %). Le jour est le facteur limitant — 83 des 86 profils d'amorçage ne déclarent que
deux jours — et le niveau est la promesse du produit.

**Ce que coûte le refus de négocier le niveau, chiffré.** Un élargissement vers le niveau
voisin aurait récupéré 46 des 127 recherches vides (36 %) et fait tomber le résidu de
6,1 % à 3,0 %. Ces **3,1 points** ne sont pas nuls et ils sont refusés en connaissance de
cause : ils correspondent tous à *Pilates Intermédiaire*, c'est-à-dire au droit de
proposer la seule pratiquante de Pilates du fichier — débutante — à quelqu'un qui ne l'est
pas. Le produit préfère un refus honnête.

Ce que cette rigueur n'achète pas, il faut le dire ici : le niveau est **déclaré et jamais
vérifié** (FR-2). Défendre une valeur que personne ne contrôle protège l'appariement
contre le laxisme du produit, pas contre l'optimisme de l'utilisateur. Voir §7,
*L'intégrité du niveau*.

Le plafond de trois candidats de FR-6 est, lui, une règle tournée vers un vivier qui a
grossi : sur les 33 paires sport × niveau possibles, 31 sont peuplées, la **médiane est de
3 profils** et seules **4 paires en comptent plus de trois** ; 19 % des combinaisons n'en
renvoient qu'un. Le plafond ne mord donc presque jamais aujourd'hui — et c'est précisément
pour cela que sa règle d'ordre doit être écrite maintenant, pendant qu'elle ne coûte rien,
plutôt que découverte quand elle comptera.

`[NOTE FOR PM]` Les 231 combinaisons sont comptées uniformément (11 sports × 7 jours ×
3 niveaux) et ne sont pas pondérées par la demande réelle. « 55 % ne renvoient aucun
candidat » est donc un fait sur la grille, pas une prévision du taux d'échec que vivront
les utilisateurs — lequel dépendra des sports réellement demandés.

#### FR-5 : Recherche exacte

Le bot renvoie les profils du vivier partageant le sport, au moins un jour disponible et
le **niveau exact** de la demande. L'égalité de niveau est stricte, pour tous les sports,
et ne souffre aucune exception à aucune étape.

**Conséquences testables :**
- « Tennis, mardi, débutant » renvoie Emma Leroy.
- « Tennis, mardi, intermédiaire » ne renvoie aucun candidat.
- Aucun candidat renvoyé n'est d'un autre niveau que celui demandé — ni après
  élargissement, ni sur proposition, ni sur demande de l'utilisateur.
- Un profil dont le jour demandé est **bloqué** par une rencontre n'est pas renvoyé pour ce
  jour-là, mais continue de l'être pour ses autres jours (FR-16).
- Un profil de *niveau inconnu* n'est jamais renvoyé.
- L'utilisateur lui-même n'est jamais renvoyé comme son propre partenaire.

#### FR-6 : Élargir sur le jour

Sans résultat exact, le bot relâche le jour — **et lui seul** — en conservant le niveau, et
présente les candidats avec leurs jours. C'est le seul élargissement du produit. Réalise
UJ-1.

**Conséquences testables :**
- « Tennis, mardi, intermédiaire » renvoie Anna, Iris et Tessa avec leurs jours respectifs.
- Les candidats proposés sont exactement du niveau demandé.
- La proposition indique explicitement que le jour demandé n'était pas disponible.
- **Le bot présente au plus trois candidats**, classés par **délai d'attente croissant** :
  pour chaque candidat, le nombre de jours à attendre depuis le jour demandé jusqu'à sa
  prochaine disponibilité, en tournant vers l'avant sur la semaine (depuis mardi :
  mercredi = 1, jeudi = 2, … lundi = 6). Le plus tôt d'abord.
- À délai égal — le cas le plus fréquent sur les données d'amorçage — l'ordre est celui du
  vivier, de sorte que deux recherches identiques renvoient toujours le même trio dans le
  même ordre.
- Au-delà de trois candidats, le bot dit combien il y en a d'autres et propose de les
  montrer.


#### FR-8 : Annoncer l'absence de résultat sans broder

Si l'élargissement sur le jour ne produit aucun candidat, le bot le dit clairement.
Réalise UJ-2.

**Conséquences testables :**
- « Pilates, avancé » ne produit aucun nom de partenaire, quel que soit le jour : le vivier
  ne compte qu'une pratiquante de Pilates, et elle est débutante. « Pilates,
  intermédiaire » ne produit rien non plus, pour la même raison — ce sont les deux seules
  paires sport × niveau vides des données d'amorçage.
- **La réponse nomme le sport et le jour tentés, et dit ce qui a été élargi** — tous les
  autres jours — avant de conclure qu'il n'y a personne **à ce niveau**.
- Un sport que le vivier ne connaît pas encore reçoit cette même réponse et non un refus
  (FR-2) : le bot dit qu'il n'a encore personne dans ce sport.
- La réponse enchaîne sur la proposition d'alerte différée de FR-9.
- Le bot ne propose jamais une personne absente du vivier.
- Le bot ne propose jamais quelqu'un d'un autre sport que celui demandé.

#### FR-9 : Proposer une alerte différée

Faute de résultat satisfaisant, le bot propose d'enregistrer la demande et de prévenir
l'utilisateur par e-mail si un profil correspondant rejoint le vivier. Réalise UJ-1
(cas limite), UJ-2.

**Conséquences testables :**
- L'acceptation d'une alerte exige un compte (FR-4).
- Une alerte se déclenche sur une **correspondance exacte** — même sport, même niveau, au
  moins un jour commun. Un profil qui ne correspondrait qu'après élargissement ne la
  déclenche pas.
- La notification part par e-mail à l'adresse du compte, dans l'heure qui suit
  l'inscription du profil correspondant.
- Une alerte vaut **60 jours**, puis expire ; le bot prévient par e-mail lors de
  l'expiration.
  `[ASSUMPTION: 60 jours de validité et une notification dans l'heure — durées posées par défaut, à confronter au rythme réel des inscriptions.]`
- Un utilisateur peut porter plusieurs alertes simultanées, une par demande.
- L'utilisateur peut annuler une alerte à tout moment, depuis la conversation.

### 5.3 Jouabilité

**Description.** Avant qu'un créneau soit retenu, le bot vérifie que les conditions
extérieures sont raisonnables. Il ne s'agit pas de confort mais de **santé** : chaleur
excessive, vent dangereux, alerte de qualité de l'air. Réalise UJ-1.

Le contrôle intervient **avant** que le créneau soit **retenu** (§3, *retenir un créneau*), pas après : le produit épargne
un mauvais créneau plutôt que de le signaler une fois pris.

C'est aussi le moment où **l'heure de la rencontre se décide** : le vivier ne connaît que
des jours, et le bot n'a donc aucune heure à proposer tant qu'il n'a pas de raison. Quand
la jouabilité en fournit une, il propose une heure ; sinon, il la demande en une phrase.

**Choisir une heure et décider d'y aller sont deux décisions distinctes.** La
contre-proposition de jouabilité fixe l'heure ; **elle ne retient rien**. Le produit ne
déduit jamais un engagement d'une réponse à une question d'horaire ou de jouabilité :
seul le geste du §3 engage, et c'est pourquoi le contrôle paraît toujours **avant** lui.

#### FR-10 : Évaluer la jouabilité d'un créneau

Le bot évalue température ressentie, vent et qualité de l'air pour le créneau et le lieu
envisagés, et restitue le résultat en langage clair.

**Seuils d'alerte :**

| Condition | Seuil |
|---|---|
| Chaleur | température ressentie **supérieure à 28 °C** |
| Vent | rafales **supérieures à 40 km/h** |
| Qualité de l'air | indice **ATMO ≥ 4** sur l'échelle à six degrés (*Mauvais*, *Très mauvais*, *Extrêmement mauvais*) |

**La jouabilité dépend du *lieu retenu* (FR-11), pas du sport — et « couvert » ne suffit
pas à la désactiver.** Les trois seuils ci-dessus portent sur la chaleur, le vent et
l'air, et ne comportent **aucune notion de pluie**. Un équipement **pleinement intérieur**
met à l'abri des trois, et lui seul désactive l'évaluation. Un équipement **extérieur
couvert** n'abrite que de ce que le produit ne vérifie pas : il **reste soumis aux trois
seuils**, au même titre qu'un cours de yoga en plein air. Sans lieu, aucune évaluation.
*Précisé en v5 : la distinction n'est pas théorique, la source de terrains classe
réellement des équipements en « extérieur couvert » (§11, QO-4).*

**Conséquences testables :**
- Pour un lieu soumis aux seuils, un créneau dépassant l'un des trois est signalé avant
  que l'utilisateur le retienne.
- Pour un lieu **pleinement intérieur**, le bot ne mentionne aucune condition extérieure
  et ne propose aucune alternative pour ce motif.
- Un équipement **extérieur couvert** est traité comme un lieu en extérieur : les trois
  seuils s'y appliquent, et le bot en parle.
- Le bot propose une heure alternative dans la même journée, ou un autre jour, plutôt que
  de se contenter d'alerter.
- **L'alerte informe et n'interdit pas** : le créneau initial reste retenable si
  l'utilisateur refuse la contre-proposition.
- **Accepter une heure alternative ne retient pas le créneau** : le geste du §3 reste à
  faire, et aucun message ne part avant lui.
- En l'absence d'alerte, le bot demande l'heure de la rencontre en une phrase.
- Un créneau hors de portée des prévisions est annoncé comme tel, sans valeur inventée.
- **Les deux horizons de prévision sont distincts, et le plus court commande.** La chaleur
  et le vent se prévoient à une quinzaine de jours ; la qualité de l'air à environ un jour.
  Un créneau au-delà rend les seuils qui ont pu être établis et **nomme** celui qui n'a pas
  pu l'être ; jamais une valeur par défaut, jamais un silence.

**Notes :** `[NOTE FOR PM]` **la branche « hors de portée des prévisions » est le cas
courant pour l'air, pas l'exception.** Le produit prend des rencontres quelques jours à
l'avance (§2.1) et l'indice ATMO ne porte qu'à environ un jour : dès le lendemain,
l'évaluation rendra la chaleur et le vent en nommant l'air comme non établi. C'est une
propriété du produit et non une panne, et le bot doit le dire comme telle. Si la qualité de
l'air doit réellement peser sur le choix d'un créneau, c'est une **source à horizon plus
long** qu'il faut, pas un correctif d'affichage.

### 5.4 Terrains

**Description.** Le bot propose un endroit où jouer, à Lyon. Le produit ne desservant
qu'une agglomération (§1), il n'y a pas de ville à demander. Réalise UJ-1.

#### FR-11 : Proposer un lieu à Lyon

Le bot propose des équipements lyonnais adaptés au sport, et précise pour chacun **sa
nature** : pleinement intérieur, ou exposé aux conditions extérieures.

**Conséquences testables :**
- Les lieux proposés sont à Lyon ou dans son agglomération, et correspondent au sport de
  la demande.
- Chaque lieu proposé indique **sa nature** — c'est elle qui détermine si la jouabilité
  s'applique, selon la projection que FR-10 définit : un équipement *extérieur couvert*
  y reste soumis, seul un équipement pleinement intérieur y échappe.
- Le bot peut demander un secteur ou un arrondissement pour affiner, mais ne l'exige
  jamais : sans réponse, il propose quand même.
- Un secteur donné est enregistré au profil de l'utilisateur inscrit et réutilisé la fois
  suivante.
- Sans donnée disponible, le bot le dit — il ne propose pas de lieu plausible inventé.

**Hors périmètre :** la réservation. `[NON-GOAL for MVP]` Le produit propose un endroit ;
il ne réserve rien, ne connaît pas les disponibilités et ne gère aucun paiement.

**Notes :** `[NOTE FOR PM]` **la source des données de terrains est identifiée depuis la
v5, et FR-11 cesse d'être un pari** (§11, QO-4) : elle s'interroge sans clé et porte
l'attribut de nature dont FR-10 dépend autant que FR-11 — voir [addendum.md](addendum.md),
« Terrains ». Ce que la fermeture déplace : la question n'est plus *aura-t-on des
terrains* mais *comment la nature d'un équipement se projette sur la jouabilité*, et elle
est tranchée sous FR-10.

### 5.5 Rencontre et agenda

**Description.** Une fois le créneau retenu, le bot pose la rencontre dans l'agenda de
l'utilisateur — Google ou Outlook, au choix — et prévient le partenaire. Le statut de la
rencontre est explicite. Réalise UJ-1.

#### FR-12 : Écrire la rencontre dans l'agenda de l'utilisateur

L'utilisateur peut faire ajouter la rencontre à son agenda Google ou Outlook.

**Conséquences testables :**
- Les deux fournisseurs sont proposés au choix.
- L'écriture n'a jamais lieu sans confirmation explicite de l'utilisateur.
- L'événement porte le sport, le prénom du partenaire, le lieu, le jour, l'heure et le
  statut de la rencontre.
- L'événement ne contient **aucun numéro de téléphone**.

**Hors périmètre :** l'agenda du partenaire. `[NON-GOAL for MVP]` Le produit n'écrit
jamais dans l'agenda de quelqu'un d'autre que l'utilisateur qui lui a donné accès au sien.

#### FR-13 : Tenir le statut d'une rencontre

Une rencontre a **cinq** statuts, et un seul à la fois. C'est le statut, et lui seul,
qui détermine ce que le bot a le droit de dire.

| Statut | Ce qui l'a produit | Ce que le bot dit |
|---|---|---|
| **En attente** | le partenaire a été prévenu, il n'a pas répondu | « prévenu, pas encore de réponse » |
| **Confirmée** | le partenaire a accepté | « c'est confirmé » |
| **Déclinée** | le partenaire a refusé | « il / elle a décliné » — jamais « pas encore répondu » |
| **Expirée** | le créneau est passé sans réponse | « personne n'a répondu à temps » |
| **Abandonnée** | l'utilisateur a renoncé à la rencontre | « j'ai laissé tomber » |

Les quatre premiers décrivent tous, sans exception, la **réponse du partenaire**.
*Abandonnée* est le seul que produit l'utilisateur lui-même, et c'est la raison de son
existence : router un abandon vers *déclinée* ferait dire au bot qu'une personne **a
refusé** alors qu'elle n'a rien répondu ; vers *expirée*, qu'une **échéance est passée**
alors que rien ne l'a été. Dans un produit dont le §7 tient « le bot n'invente rien » pour
sa contrainte la plus structurante, ni l'un ni l'autre n'est disponible.

**Conséquences testables :**
- Une rencontre naît *en attente*, quelle que soit la population dont vient le partenaire.
- Une rencontre n'est jamais annoncée comme confirmée avant que le partenaire ait accepté.
- **Un refus produit le statut *déclinée* et jamais *en attente*** : le bot ne présente
  jamais un refus comme une absence de réponse.
- Une rencontre passe à *confirmée* ou *déclinée* quand le partenaire suit le lien de son
  message (FR-14) ou, s'il est utilisateur inscrit, répond depuis sa conversation.
- Une rencontre *en attente* dont le créneau est passé bascule en *expirée*.
- Une rencontre *en attente* ou *confirmée* que l'utilisateur abandonne bascule en
  *abandonnée*. **C'est le seul chemin vers ce statut** : rien d'automatique ne le produit,
  et personne d'autre que l'utilisateur ne peut le déclencher.
- Tout changement de statut déclenche une notification à l'utilisateur par e-mail et met à
  jour l'événement d'agenda (FR-12). **Une seule exception : *abandonnée*.** L'événement
  d'agenda est bien mis à jour, mais aucun courriel ne part — la personne vient elle-même
  de demander l'abandon, l'en informer serait lui apprendre ce qu'elle vient de faire.
- **Le passage à *abandonnée* n'envoie aucun message au partenaire non plus.** Son lien
  cesse de fonctionner, et c'est la page d'acceptation qui le lui dit s'il la rouvre
  (FR-14). Nulle part ailleurs.
- Une rencontre *déclinée*, *expirée* ou *abandonnée* n'est jamais supprimée en silence :
  elle reste consultable dans le fil avec son statut.

**Une seule recherche active à la fois.** Tant qu'une rencontre est *en attente* ou
*confirmée*, aucune nouvelle recherche n'est lancée. Le bot **nomme ce qui occupe la
place et donne la sortie dans la même phrase** :

> « Une recherche à la fois. Anna n'a pas encore répondu pour mercredi. Dites-moi si
> vous préférez laisser tomber le tennis — je cherche le badminton ensuite. »

**Conséquences testables :**
- Une demande complète formulée pendant qu'une rencontre est *en attente* ou *confirmée*
  n'est pas lancée ; la réponse nomme le sport, le partenaire et le jour occupés, et
  propose d'abandonner la rencontre en cours.
- Abandonner la rencontre en cours la fait passer en ***abandonnée***. Le jour se libère
  aussitôt (FR-16), la recherche redevient possible, et la rencontre reste consultable
  dans le fil. **C'est ce qui rend la sortie exécutable** : sans statut d'arrivée, la
  rencontre resterait *en attente*, le jour resterait bloqué et la nouvelle recherche
  resterait refusée — la règle mangerait la porte de sortie que sa propre phrase promet.
- Revenir sur un choix déjà fait — « en fait, Iris » après avoir retenu Anna — emprunte
  ce chemin : ce n'est pas un cas concurrent, **c'est le chemin normal**.
- Changer le créneau d'une rencontre déjà écrite dans l'agenda (FR-12) l'emprunte aussi :
  la rencontre passe en *abandonnée*, puis une nouvelle est retenue. **Ce n'est pas un cas
  particulier** — c'est le chemin normal, emprunté une fois de plus.
- **Seules comptent les rencontres nées des demandes de la personne elle-même.** Être
  sollicité par un autre demandeur (FR-14) n'occupe pas la place : la personne sollicitée
  garde le droit de chercher, son jour étant déjà bloqué par FR-16.
- **Les alertes différées ne sont pas concernées** (FR-9). Une alerte n'occupe aucun
  créneau et n'attend la réponse de personne : enchaîner Pilates → vide → alerte →
  squash → vide → alerte reste possible, et « plusieurs alertes simultanées » reste
  vrai mot pour mot.

**Notes :** `[NOTE FOR PM]` **c'est le plus restrictif des trois arbitrages possibles, et
c'est délibéré** : c'est le seul qui se lève sans rien casser le jour où l'usage
prouverait qu'il gêne. Les deux autres étaient d'autoriser plusieurs demandes en
acceptant plusieurs récapitulatifs dans le fil, ou d'autoriser sans limite en renonçant
au récapitulatif de reprise en prose. **Rien ne mesure aujourd'hui si la restriction
gêne** — voir QO-8.

`[NOTE FOR PM]` **le cinquième statut est uniforme, et il se paie.** Un simple décalage
d'heure produit lui aussi une rencontre *abandonnée* : le fil en garde la trace pour ce qui
n'était qu'un report, et la page d'acceptation du partenaire affiche son état d'abandon
pour la même raison (FR-14). L'alternative — exempter le changement de créneau — a été
écartée : elle réintroduit exactement le cas particulier que cette règle avait fermé, et
laisse à nouveau une rencontre sans statut d'arrivée.
`[ASSUMPTION: l'usage visé — un trou dans un agenda, quelques jours à l'avance — ne produit pas de file d'attente, donc la restriction ne gêne personne. Posé par défaut, jamais observé.]`

#### FR-14 : Prévenir le partenaire et lui permettre d'accepter

Quand l'utilisateur **retient** un créneau (§3), le bot prévient le partenaire par un message qui
explique d'où il sort, et qui porte un lien d'acceptation à usage unique.

**Conséquences testables :**
- Le partenaire est prévenu par **SMS** s'il a un numéro de téléphone, par **e-mail** s'il
  est utilisateur inscrit et n'en a pas donné.
- Le message énonce son propre motif — que la personne figure dans le vivier d'Ex Aequo et
  que quelqu'un cherche un partenaire — avant de présenter la proposition.
- Le message porte le sport, le jour, l'heure, le lieu et le prénom du demandeur.
- Le message ne contient **aucune coordonnée** du demandeur.
- Le lien permet d'accepter ou de refuser, et ne fonctionne qu'une fois.
- Le message porte un moyen de **ne plus jamais être contacté** ; l'exercer retire le
  profil du vivier définitivement.
- Tant que les données d'amorçage sont fictives, **aucun SMS ne part vers un numéro hors de la
  plage de fiction** `+336 39 98 XX XX`, sauf vers un numéro qu'un utilisateur inscrit a
  lui-même donné. Un numéro qui ne satisfait ni l'une ni l'autre condition fait échouer
  l'envoi bruyamment plutôt que de partir.
- Un refus fait passer la rencontre en *déclinée* (FR-13) ; l'absence de réponse la laisse
  *en attente* jusqu'au créneau, puis *expirée*. Jamais annulée d'office, jamais
  requalifiée en confirmée.
- **La page dit aussi qu'une rencontre a été abandonnée par le demandeur** quand c'est le
  cas. C'est **le seul endroit** où le partenaire peut l'apprendre : aucun message ne part
  (FR-13). Elle ne le présente **jamais comme un refus du demandeur** — il a renoncé à
  chercher, il n'a pas jugé la personne. Elle propose la sortie définitive du vivier, seule
  action qui reste utile.
- Aucun message n'est envoyé à une personne qui n'a ni numéro de téléphone ni compte.
- **Un même partenaire peut être sollicité par plusieurs demandeurs.** Chaque sollicitation
  a son propre message et son propre lien. Le message énonce le créneau proposé, et le
  partenaire peut accepter les deux s'ils ne se chevauchent pas — en pratique, sur des jours
  différents, puisqu'une rencontre *en attente* bloque déjà son jour (FR-16).
- **Deux acceptations qui se chevauchent sont impossibles :** accepter un créneau qui
  entre en conflit avec une rencontre déjà *confirmée* du même partenaire échoue, la page
  le lui dit, et la rencontre concernée passe en *déclinée*.
- Un lien déjà utilisé, expiré, portant une rencontre abandonnée, ou appartenant à un
  profil désinscrit, affiche la raison plutôt qu'une erreur technique.

**Notes :** `[NOTE FOR PM]` **le silence sur l'abandon repose sur un invariant que le
produit s'impose déjà : le SMS est le seul contact qu'un profil d'amorçage aura jamais avec
Ex Aequo.** Envoyer un second message pour annoncer un abandon le romprait — pour la
population **majoritaire** du vivier, et au profit de gens qui n'avaient rien fait.
Écartés : prévenir toujours, et prévenir seulement si la rencontre était *confirmée*.
`[ASSUMPTION: celui qui rouvre son lien apprend l'abandon à temps, et celui qui ne le rouvre pas ne perdait rien. Déduit de l'invariant du contact unique, jamais observé — c'est QO-9.]`

#### FR-16 : Tenir le cycle de vie d'un profil au vivier

Un profil entre au vivier à la création du compte (FR-3), y **reste après ses rencontres**,
et n'en sort que s'il le demande (FR-14). Ce qu'une rencontre produit n'est pas une sortie :
c'est un **jour bloqué**.

*Le numéro de cette exigence reflète son ajout tardif ; sa place dans le parcours est ici,
après FR-13 dont elle emploie les cinq statuts.*

**Conséquences testables :**
- Une rencontre *en attente* ou *confirmée* bloque, pour les deux profils, **le seul jour
  de la rencontre**. Chacun continue de sortir des recherches portant sur ses autres jours.
- Une rencontre *déclinée* libère le jour **immédiatement**. Une rencontre *abandonnée*
  aussi, et **pour les deux profils** : le partenaire qui n'avait rien fait retrouve son
  jour en même temps que le demandeur qui a renoncé.
- Une rencontre *expirée* libère le jour. C'est le seul mécanisme qui rend au vivier les
  jours immobilisés par une rencontre restée sans réponse — un ramasse-miettes, pas une
  politesse.
- Le profil conserve **ses jours demandés et le jour accepté**. Accepter un mercredi qu'on
  n'avait pas demandé est une information sur sa disponibilité, et elle est gardée.
- Un profil sorti du vivier (FR-14) ne revient dans aucune recherche, quel que soit le
  statut de ses rencontres passées.
- Une rencontre passée sans incident ne retire rien : le lendemain, le profil est trouvable
  exactement comme la veille.

**Notes :** `[NOTE FOR PM]` **le blocage est volontairement trop large.** Le vivier ne
connaît que des jours, jamais des heures (FR-2) : une rencontre à 19 h retire la personne de
toute la journée. C'est le prix du choix de ne pas stocker d'heures, et il se paie en
disponibilité perdue, jamais en propositions fausses.

`[NOTE FOR PM]` **Cette règle absorbe une partie de FR-14.** Puisqu'un jour se bloque dès
l'état *en attente*, deux demandeurs ne peuvent plus retenir la même personne le même jour
par la recherche. La règle de non-chevauchement de FR-14 ne protège donc plus que la
fenêtre de course entre deux validations quasi simultanées — elle reste nécessaire, mais
elle ne décrit plus le cas courant.

## 6. Exigences non fonctionnelles

`[ASSUMPTION: les bornes chiffrées de cette section — 2 s, 20 s, 30 jours, 360 px — sont posées par défaut faute d'exigence exprimée. Elles sont là pour être vérifiables, pas parce qu'elles ont été mesurées.]`

- **Latence conversationnelle.** Toute action du bot produit un signe de vie **en moins de
  2 secondes**, et la réponse complète arrive en moins de 20 secondes. Au-delà, le bot dit
  ce qu'il est en train de faire et pourquoi c'est long. Dans une conversation, l'attente
  muette se lit comme une panne.
- **Robustesse des services externes.** Météo, terrains et agenda peuvent être
  indisponibles. Le bot poursuit la conversation en annonçant nommément le service qui n'a
  pas répondu, et le parcours reste terminable sans lui : sans météo la rencontre se prend
  sans contrôle de jouabilité et le bot le dit ; sans données de terrains l'utilisateur
  indique le lieu lui-même ; sans agenda la rencontre existe et le bot propose de
  réessayer l'écriture plus tard.
- **Reprise de conversation.** Le fil n'est jamais purgé ni réinitialisé de lui-même. Un
  utilisateur inscrit qui revient retrouve ses demandes, ses alertes et ses rencontres.
  Le récapitulatif de reprise porte **au plus une rencontre**, ce que la règle d'une
  seule *recherche active* garantit (FR-13) : au-delà de deux ou trois, un
  récapitulatif en prose devient illisible.
  Un visiteur **sans compte** retrouve son fil pendant **30 jours** sur le même
  navigateur, après quoi il est effacé.
- **Surface.** Le produit est un site web responsive. **Le navigateur d'un ordinateur est
  le cas d'usage principal** ; le mobile est servi à parité fonctionnelle complète, à
  partir de 360 px de large. Il n'y a pas d'application native, donc pas de notification
  push : les notifications différées passent par l'e-mail (FR-9, FR-13) et le SMS (FR-14).

## 7. Contraintes et garde-fous

### Le bot n'invente rien

C'est la contrainte la plus structurante du produit, et elle est en tension permanente
avec le fait que l'interface est un LLM, dont la pente naturelle est de faire plaisir.

- Aucun nom de partenaire qui ne vienne du vivier.
- Aucune donnée météo, aucun terrain, aucune disponibilité inventés.
- Aucune confirmation annoncée qui n'ait été donnée.
- **Les étapes que le bot annonce correspondent aux sources qu'il a réellement
  interrogées.** Ce n'est pas un habillage d'attente : quand le bot dit qu'il regarde la
  météo, il la regarde ; une source qui n'a pas répondu est annoncée comme telle.
- En cas de doute, le bot dit qu'il ne sait pas.

### L'intégrité du niveau

C'est le second risque du produit, et il vise sa promesse centrale : le niveau. La
recherche décrit deux régimes d'échec successifs pour cette catégorie : le vide d'abord,
puis **l'intégrité de la note de niveau et le match déséquilibré qui s'ensuit**
([research-paysage.md](research-paysage.md), §4). Ex Aequo doit traverser le premier pour
rencontrer le second ; ce n'est pas une raison pour l'ignorer.

**Le produit prend ici le contre-pied de sa propre recherche, et l'assume.**
[research-niveau.md](research-niveau.md) §4.1 déconseille nommément la saisie
Débutant / Intermédiaire / Avancé et prescrit d'établir le niveau à partir de faits
vérifiables. C'est exactement ce que faisait FR-15, et c'est exactement ce qui a été retiré
(§13). La raison n'est pas que la recherche aurait tort : c'est que **toute forme de
calibration est hors périmètre** (§9), et qu'une inférence sans calibration produit une
fausse précision plutôt qu'une vraie. Le produit préfère une valeur franchement déclarée à
une valeur devinée avec l'air d'avoir été mesurée.

- **La sur-évaluation est acceptée, pas réduite.** Le biais est bidirectionnel et
  documenté : gonflement de 0,5 à 1,0 point d'un côté, *sandbagging* de l'autre
  ([research-niveau.md](research-niveau.md), §1). Rien, dans le produit, ne le corrige.
- **Une déclaration se croit brièvement et lâchement.** Le bot emploie le niveau, il ne le
  traite pas comme un fait acquis et ne le présente jamais comme une mesure. Il ne
  l'affiche pas non plus sur les cartes de partenaires : à niveau strictement égal il y
  serait identique partout, et se lirait comme une garantie qu'il n'est pas.
- **Le produit n'a aucun instrument pour constater qu'un match était déséquilibré.** Le
  signal d'équilibre après rencontre existe dans la recherche (§4.5) et a été écarté du
  périmètre v1 (§9).
- **Il n'a plus de contre-métrique non plus.** SM-C1 surveillait la part de mises en
  relation obtenues par descente de niveau ; la descente de niveau n'existe plus, et la
  contre-métrique est retirée avec elle (§10).

`[NOTE FOR PM]` **Il faut voir cette accumulation pour ce qu'elle est.** Trois garde-fous
étaient prévus sur la promesse centrale du produit : l'établissement du niveau par des
faits, le signal d'équilibre après rencontre, et la contre-métrique de descente de niveau.
Les trois ont été retirés, chacun pour une raison défendable prise séparément. Ce qui reste
est un niveau déclaré, jamais vérifié, jamais corrigé, et dont rien ne mesure la justesse —
**le risque est accepté sans aucune contrepartie.** C'est le premier endroit où regarder si
les retours d'usage se dégradent : la plainte prendra la forme « je ne trouve pas de
partenaire à mon niveau » alors que la cause sera un niveau mal déclaré, pas un vivier trop
petit.

### L'enfermement dans la conversation

Le seul verbatim du corpus qui porte sur l'interface qu'Ex Aequo a choisie est hostile :
« aucun moyen de parler à un vrai humain, toujours renvoyé vers un chatbot »
([research-paysage.md](research-paysage.md), §3). Ce que les gens détestent n'est pas le
chat, c'est de ne pas pouvoir en sortir.

Le bot doit donc rendre la main plutôt que la retenir : quand quelqu'un demande une liste,
une carte ou un filtre, le bot ne répond pas qu'il ne sait pas faire — il donne ce qu'il
peut sous une forme plus dense, et note la demande. SM-5 (§10) surveille ce symptôme.

### Vie privée

- Le numéro de téléphone d'un profil d'amorçage **n'est jamais communiqué** à
  l'utilisateur, ni affiché, ni écrit dans l'événement d'agenda. Le bot nomme ces
  personnes et les contacte lui-même ; il ne diffuse pas leurs coordonnées.
- Le message envoyé au partenaire (FR-14) explique toujours pourquoi il arrive, et porte
  un moyen de ne plus jamais être contacté.
- Le numéro de téléphone d'un utilisateur inscrit est **facultatif**. Sans numéro, il est
  prévenu par e-mail et ne reçoit aucun SMS.
- Le bot demande le minimum nécessaire, et chaque fois qu'il demande quelque chose, il dit
  pourquoi. La création du compte annonce explicitement qu'elle rend l'utilisateur
  trouvable par d'autres (FR-3, FR-4).
- L'accès à l'agenda sert à écrire la rencontre convenue, rien d'autre.
- **Aucun SMS ne peut atteindre une personne réelle par les données d'amorçage.** Les 86
  numéros sont dans la plage de fiction de l'ARCEP (§4), et FR-14 refuse d'envoyer vers un
  numéro qui ne serait ni dans cette plage, ni donné par un utilisateur inscrit. C'est un
  garde-fou de conception, pas une précaution de test : il tient aussi en production.

`[NOTE FOR PM]` **Asymétrie de consentement, neutralisée mais pas résolue.** Un utilisateur
inscrit choisit de donner son numéro ; un profil d'amorçage, lui, a déjà le sien dans les
données et recevrait un SMS sans l'avoir demandé. Le fait que ces numéros soient fictifs
supprime le dommage, pas le principe : le jour où le vivier serait amorcé avec de vraies
coordonnées, la conception actuelle enverrait des SMS à des gens qui n'ont rien demandé.
Le message est auto-explicatif et porte une sortie définitive, mais cela ne fait pas un
consentement préalable. Le sujet est traité en garde-fou et non en section de conformité,
ce qui est cohérent avec un projet personnel à vivier fictif. **À rouvrir impérativement
avant tout amorçage par des données réelles.**

### Sécurité des personnes

Le produit organise des rencontres physiques entre inconnus. En v1 il n'y a ni
vérification d'identité, ni signalement, ni réputation. C'est acceptable pour un projet
d'apprentissage à vivier fictif ; ça ne le serait pas avec de vrais utilisateurs.

## 8. Non-objectifs

- **Ce n'est pas une plateforme de réservation.** Le produit propose des terrains, il n'en
  réserve aucun et ne gère aucun paiement.
- **Ce n'est pas un réseau social sportif.** Pas de fil, pas d'abonnements, pas de profils
  publics à parcourir.
- **Pas de classement public.** La recherche montre qu'un classement visible crée des
  incitations à la manipulation impossibles à contrôler à cette échelle
  ([research-niveau.md](research-niveau.md), §4.7).
- **Pas d'organisation de matchs à plusieurs.** Deux personnes, jamais une équipe.
- **Le bot n'est pas un assistant généraliste.** Il fait ce produit, et le dit quand on
  lui demande autre chose.

## 9. Périmètre du MVP

### Dans le périmètre

- Chatbot web responsive, pensé pour l'ordinateur d'abord, accessible sans compte.
- **Lyon uniquement.**
- Niveau **déclaré** parmi trois valeurs, demandé une seule fois et jamais pendant la
  recherche (FR-2).
- **Liste de sports ouverte** : un sport que le vivier ne connaît pas est vide, pas refusé
  (FR-2).
- Recherche de partenaire à **niveau strictement égal**, avec élargissement sur le jour et
  sur lui seul (FR-5, FR-6).
- **Une seule *recherche active* à la fois**, et le bot dit comment en sortir (FR-13).
- **Cycle de vie d'un profil au vivier** : blocage par jour, libération, sortie définitive
  (FR-16).
- Refus honnête et alerte différée quand il n'y a personne.
- Vérification de la jouabilité **partout où les trois seuils gardent un sens** — tout lieu
  qui n'est pas pleinement intérieur, un équipement *extérieur couvert* compris — avant que
  le créneau soit retenu, et heure de la rencontre fixée à ce moment.
- Proposition d'équipements lyonnais, avec leur **nature**, dont dépend la jouabilité.
- Écriture de la rencontre dans l'agenda Google ou Outlook.
- Vivier amorcé par les 86 profils, enrichi des utilisateurs qui créent un compte.
- **Notification du partenaire et lien d'acceptation à usage unique** (FR-14) : une page
  hors conversation, qui accepte ou refuse, et rien d'autre.

### Hors périmètre du MVP

- L'heure de disponibilité dans les profils — les données d'amorçage ne la portent pas.
  L'heure de la rencontre, elle, est dans le périmètre.
- La réservation de terrain et tout paiement.
- **Le parcours conversationnel côté partenaire.** Un profil d'amorçage accepte ou refuse
  par un lien, sans conversation. La négociation entre deux utilisateurs inscrits — relance,
  contre-proposition de créneau, annulation — n'est pas spécifiée ici.
  `[NOTE FOR PM]` C'est le premier candidat pour la v2.
- **Toute autre ville que Lyon.**
- **Le signal d'équilibre après rencontre** (« trop facile / équilibré / trop dur »).
  `[NOTE FOR PM]` Il ne coûte aucun algorithme et c'est le seul instrument qui dirait si la
  promesse du produit tient — voir §7, *L'intégrité du niveau*. Écarté sciemment pour tenir
  le périmètre, pas parce qu'il serait cher.
- **Ce qui se passe après le créneau.** Ni annulation, ni relance, ni no-show, alors que
  le no-show est le mode d'échec terminal documenté du parcours nominal
  ([research-paysage.md](research-paysage.md), §4). Le produit s'arrête à l'écriture dans
  l'agenda.
- **Toute forme de calibration du niveau** : questionnaire comportemental, inférence à
  partir de faits déclarés, correction par les résultats. Le niveau est déclaré une fois et
  ne bouge plus. Les mécanismes existent et sont documentés dans
  [research-niveau.md](research-niveau.md) §4 pour plus tard ; la sur-évaluation qui en
  résulte est assumée (§7).
- **Plusieurs sports par profil.** Un profil porte un sport ; une demande sur un autre
  sport le remplace (FR-3).
- **La fraîcheur d'une fiche.** Un profil resté inactif des mois est proposé comme les
  autres, et le vivier fabrique ainsi ses propres partenaires injoignables (§11, QO-6).
- Vérification d'identité, signalement, réputation.
- Sports d'équipe en tant que tels.

## 10. Critères de réussite

Projet personnel : la mesure est qualitative et volontairement courte.

`[ASSUMPTION: les seuils de cette section — 85 %, une session sur cinq, 4 tours — sont posés par défaut. Seul le 85 % est adossé à un calcul, le plafond de 89 % établi au §5.2. Le seuil de SM-C2 descend de 5 à 4 tours pour compenser le retrait de FR-15, sans que la longueur réelle des conversations ait jamais été mesurée.]`

Ces critères mesurent **la tenue du produit sur les données d'amorçage**, pas son succès
auprès de vrais utilisateurs. La distinction n'est pas une coquetterie : le vivier de
départ est fictif, il compte 7,8 profils par sport en moyenne, et sa répartition de niveaux
est presque uniforme — là où la recherche établit qu'une population réelle s'entasse dans
« intermédiaire » ([research-niveau.md](research-niveau.md), §1). Les taux ci-dessous sont
donc calibrés sur une distribution qui n'existe pas dans la nature. Ils disent que la
mécanique fonctionne ; ils ne disent rien de l'utilité.

- **SM-1** — Le parcours complet de UJ-1 se déroule de bout en bout, en une conversation,
  sans intervention manuelle. Valide FR-1, FR-2, FR-3, FR-4, FR-5, FR-6, FR-10,
  FR-11, FR-12, FR-13, FR-14, FR-16.
- **SM-2** — Sur un échantillon de demandes couvrant les 11 sports, le bot ne produit
  jamais un nom, un lieu ou une météo qui ne vienne pas d'une source réelle. Valide FR-8,
  FR-10, FR-11.
- **SM-3** — **Au moins 85 % des 127 combinaisons sans résultat exact des données
  d'amorçage produisent au moins un candidat du niveau exact demandé.** Le §5.2 donne le
  plafond atteignable : 89 %. Valide FR-6.
- **SM-4** — Le parcours de UJ-2 se déroule sans que le bot invente un partenaire, et
  aboutit à une alerte différée acceptée. Il se vérifie sur les 14 combinaisons réellement
  vides — les deux paires Pilates, tous jours confondus. Valide FR-8, FR-9.
- **SM-5** — **Le pari de la conversation tient** : sur un échantillon de sessions,
  moins d'une sur cinq voit l'utilisateur réclamer explicitement une liste, une carte, des
  filtres ou un catalogue de profils. Au-delà, c'est le signe que la forme conversationnelle
  n'est pas la bonne pour ce problème, et il faut le savoir. Valide la thèse du §1.

**Contre-métriques — à ne pas optimiser :**

- **SM-C1 — retirée en v2.** Elle mesurait la part des mises en relation obtenues par
  descente de niveau (FR-7). La descente de niveau n'existe plus, et la contre-métrique
  disparaît avec elle. **Il ne reste donc aucune contre-métrique sur l'intégrité du
  niveau** — c'est une perte, pas un nettoyage, et le §7 la nomme. Son identifiant n'est
  pas réattribué.
- **SM-C2** — Le nombre de tours de conversation avant la première proposition de
  partenaire. Un bot qui pose beaucoup de questions paraît attentif et devient pénible.
  **Au-delà de 4 tours**, la forme conversationnelle coûte plus qu'elle ne rapporte. Le
  seuil descend de 5 à 4 parce que le retrait de FR-15 retire jusqu'à deux questions du
  parcours : le garder à 5 aurait rendu la contre-métrique plus facile à satisfaire
  qu'avant, ce qui est l'inverse de ce qu'on attend d'un garde-fou. Contrebalance SM-1 et
  SM-5.

## 11. Questions ouvertes

Les identifiants `QO-n` sont **stables**. Une question fermée garde son numéro et sa
place ; aucun numéro n'est réattribué. C'est ce qui permet à un document aval de citer une
question sans qu'une renumérotation lui fasse désigner autre chose.

- **QO-1 — Le protagoniste de UJ-1 n'a pas de nom réel.** À remplacer par une personne
  concrète. Les prénoms des deux parcours ont été choisis absents des données d'amorçage
  pour éviter toute confusion avec un profil du vivier.
- **QO-2 — Que se passe-t-il quand deux utilisateurs inscrits négocient ?** L'acceptation
  simple est couverte par FR-14 ; la relance, la contre-proposition de créneau et
  l'annulation restent hors périmètre v1 et deviendront nécessaires.
- **QO-3 — fermée en v2.** Elle demandait ce que valait le niveau tant qu'il restait une
  inférence non vérifiée. FR-15 est retirée : le niveau n'est plus inféré du tout, il est
  déclaré, et la sur-évaluation est assumée sans contrepartie (§7). La question ne se pose
  plus dans ces termes ; ce qui la remplace est QO-7.
- **QO-4 — fermée en v5.** Elle demandait quelle source fournirait les données de terrains,
  et notait que tant qu'elle manquait, la présence de FR-11 dans le périmètre MVP était un
  pari. La source existe : le **Recensement des Équipements Sportifs** du ministère des
  Sports, interrogeable sans clé, qui porte l'attribut de nature dont FR-10 dépend autant
  que FR-11 (voir [addendum.md](addendum.md), « Terrains »). **Le pari est levé** — c'était
  l'un des deux bloquants de phase recensés depuis la première rédaction. Ce que la
  fermeture a fait apparaître à sa place n'est pas une question mais un arbitrage, traité
  sous FR-10 : « couvert » ne veut pas dire « à l'abri des trois seuils ».
- **QO-5 — Aucun critère ne mesure la qualité d'une rencontre**, seulement son existence.
  Le signal d'équilibre après rencontre est écarté du périmètre (§9) ; tant qu'il manque,
  le produit ne peut pas savoir s'il tient sa promesse. **Aggravée en v2** par le retrait
  de SM-C1 : il n'existe plus non plus de contre-métrique sur le niveau (§7).
- **QO-6 — La fraîcheur d'une fiche n'est pas traitée.** Le vivier ne diminue jamais
  (FR-16), donc quelqu'un qui a joué une fois en septembre est encore proposé en mars : le
  produit fabrique ses propres partenaires injoignables. Une date de dernière activité et
  un seuil suffiraient ; reste à trancher si c'est du produit ou de l'architecture. Voir
  [addendum.md](addendum.md).
- **QO-7 — Rien ne corrige jamais un niveau déclaré.** Le MVP ne produit aucun résultat de
  match, donc aucun signal de retour. Deux signaux gratuits existent pourtant : le **jour**
  que la personne choisit est propre et exploitable ; la **personne** qu'elle choisit ne
  l'est pas, parce que ce choix est confondu avec la disponibilité. À reprendre avant toute
  v2 touchant au niveau.
- **QO-8 — Rien ne dit si la restriction d'une seule *recherche active* gêne.** L'usage
  que décrit ce PRD — un trou dans un agenda, quelques jours à l'avance — ne produit
  pas de file d'attente, mais c'est une **hypothèse, pas une observation**. Aucun
  critère du §10 ne la mesure, et le §10 ne le peut pas : il évalue la tenue sur les
  *données d'amorçage*, or les 86 profils ne cherchent jamais. **Condition de levée :**
  si l'hypothèse est fausse, c'est le premier arbitrage à lever, et il se lève sans
  rien casser (FR-13). C'est le **troisième** endroit laissé sans instrument, après le
  signal d'équilibre (§9) et SM-C1 (§10).
- **QO-9 — Rien ne dit ce que coûte le silence sur l'abandon.** Le partenaire d'une
  rencontre *confirmée* n'apprend qu'elle a été abandonnée que s'il rouvre son lien
  (FR-13, FR-14) : c'est le prix assumé de l'invariant du contact unique. Il est faible
  tant que les rencontres se prennent à quelques jours d'avance ; il ne l'est plus si
  l'usage réel les prend à plusieurs semaines, quelqu'un gardant alors un créneau qui
  n'existe plus. **Aucune mesure ne le dit**, et le §10 ne le peut pas plus que pour QO-8 :
  les 86 profils d'amorçage ne rouvrent jamais leur lien. **Condition de levée :** la
  première rencontre confirmée puis abandonnée à plus d'une semaine de son créneau. C'est
  le **quatrième** endroit laissé sans instrument, après le signal d'équilibre (§9),
  SM-C1 (§10) et QO-8.

**Questions fermées depuis la première rédaction :**

- *Le nom du produit* — **Ex Aequo**, arrêté en conception UX.
- *La géographie* — **Lyon uniquement**, et c'est une décision de conception, pas une
  limite de départ (§1, §2.2).
- *Comment le niveau est obtenu* — **déclaré** parmi trois valeurs, pris tel quel si la
  personne emploie l'un des trois mots, demandé par trois choix sinon, et jamais pendant la
  recherche (FR-2). Arbitré en v2 **contre** la prescription de
  [research-niveau.md](research-niveau.md) §4.1, en connaissance de cause (§7, §13).
- *L'appariement tolère-t-il un écart de niveau ?* — **non**, égalité stricte pour tous les
  sports. Le jour est le seul axe d'élargissement (FR-6).
- *Combien de sports par profil ?* — **un seul** (FR-3).
- *Peut-on mener plusieurs recherches de front ?* — **non**, une seule *recherche
  active* à la fois (FR-13). Arbitré en v3 pendant la conception d'interface. La
  question n'a jamais été posée sous forme numérotée : elle ne consomme donc aucun
  `QO-n`.
- *Que devient une rencontre que son demandeur abandonne ?* — elle passe en
  ***abandonnée***, cinquième statut (FR-13). Arbitré en v4, la règle d'une seule recherche
  active s'étant révélée sans porte de sortie exécutable. Jamais posée sous forme
  numérotée non plus : aucun `QO-n` consommé.
- *Les seuils de jouabilité* — 28 °C ressentis, 40 km/h de rafales, indice ATMO ≥ 4, et
  seulement là où ils gardent un sens : tout lieu qui n'est pas pleinement intérieur, un
  équipement *extérieur couvert* compris (FR-10, précisé en v5).
- *Le ton du bot* — vouvoiement, sympathique mais professionnel. Voir
  [EXPERIENCE.md](../../ux-designs/ux-bmad-2026-08-26/EXPERIENCE.md), *Voice and Tone*.
- *Les 86 personnes sont-elles contactées pour de bon ?* — **oui**, par un SMS
  auto-explicatif portant un lien d'acceptation et un moyen de sortir du vivier (FR-14).

## 12. Index des hypothèses

- **§2.3 UJ-1** — le prénom du protagoniste est un substitut, à remplacer ; il est choisi
  absent des données d'amorçage pour qu'aucun scénario de test ne le confonde avec un
  profil du vivier.
- **§5.1 FR-2** — l'heure de disponibilité est ignorée en v1 plutôt que collectée pour les
  seuls nouveaux profils, afin de ne pas créer deux qualités de données dans le vivier.
- **§5.1 FR-3** — une demande sur un second sport **remplace** le sport du profil. Refuser
  la demande ou tenir deux profils sous un même compte étaient les deux autres issues ;
  aucune des trois n'a été mesurée.
- **§5.2 FR-9** — 60 jours de validité d'une alerte et une notification dans l'heure :
  durées posées par défaut, à confronter au rythme réel des inscriptions.
- **§5.5 FR-13** — l'usage visé ne produit pas de file d'attente, donc la restriction
  d'une seule *recherche active* ne gêne personne. Rien ne l'a mesuré ; c'est QO-8.
- **§5.5 FR-14** — celui qui rouvre son lien apprend l'abandon à temps, celui qui ne le
  rouvre pas ne perdait rien. Déduit de l'invariant du contact unique plutôt qu'observé ;
  c'est QO-9.
- **§6** — les bornes chiffrées des exigences non fonctionnelles (2 s, 20 s, 30 jours,
  360 px) sont posées par défaut faute d'exigence exprimée ; elles sont là pour être
  vérifiables, pas parce qu'elles ont été mesurées.
- **§10** — les seuils des critères de réussite (85 %, une session sur cinq, 4 tours) sont
  posés par défaut. Seul le 85 % est adossé à un calcul, le plafond de 89 % établi au §5.2.
  Le passage de 5 à 4 tours pour SM-C2 compense le retrait de FR-15 par un raisonnement,
  pas par une mesure.

## 13. Journal des modifications

Ce journal existe parce que son absence a coûté cher : le 2026-08-26, le PRD a été réécrit
après que les spines UX ont été finalisées, et les documents aval ont cité pendant des
heures une version qui n'existait plus. Toute modification de fond s'inscrit ici, avec sa
raison. **Un identifiant retiré — exigence, critère, question — n'est jamais réattribué.**

**Deux conventions de tenue**, adoptées en v4 :

- **Seule la version courante est narrée en entier.** Les antérieures se replient sur un
  paragraphe dès qu'une version nouvelle s'ouvre. Le journal cesse ainsi de grossir
  indéfiniment — il pesait 11 % du PRD en v3 — sans rien perdre : le fil complet des
  décisions vit dans `.memlog.md`, et chaque entrée nomme le fichier de décisions dont
  elle est issue.
- **Ce qui est *porté depuis l'aval* et ce qui est *ajouté en le portant* sont
  distingués.** Seul le second a besoin de redescendre. C'est la leçon de la v3, qui s'est
  déclarée soldée côté aval en comptant la décision d'origine sans voir qu'elle avait
  elle-même ajouté de la matière — il a fallu une resynchronisation de plus pour s'en
  apercevoir.

### v5 — 2026-08-30

Origine : passe `bmad-architecture` du 2026-08-28, dont le §8 de
[SOLUTION-DESIGN.md](../../architecture/architecture-bmad-2026-08-28/SOLUTION-DESIGN.md)
renvoie trois points en amont. **Première fois qu'une décision remonte depuis
l'architecture** ; les trois versions précédentes venaient toutes de la conception
d'interface.

**« Couvert » ne veut pas dire « à l'abri » (FR-10).** La source de terrains classe des
équipements en *extérieur couvert*, et les trois seuils de FR-10 — chaleur, rafales, air —
ne comportent **aucune notion de pluie**. « Un tennis couvert n'est pas concerné » était juste
sur son exemple et faux sur sa règle : appliqué à un équipement extérieur couvert, il
désactivait la jouabilité là où elle reste pertinente, au moment précis où le produit dit
s'occuper de la santé de quelqu'un. Seul un équipement **pleinement intérieur** la désactive.

**La correction touchait sept endroits, pas un.** Le point renvoyé ne signalait que le
paragraphe de FR-10 ; la même affirmation vivait aussi dans une conséquence testable de
FR-10, à deux endroits de FR-11, sur deux lignes du §9, dans une question fermée du §11 et à
deux endroits de l'addendum. N'en corriger qu'un aurait laissé six occurrences dire l'inverse
— le mode d'échec que ce journal existe pour empêcher.

**QO-4 est fermée (FR-11).** La source des données de terrains est identifiée et porte
l'attribut de nature dont FR-10 dépend autant que FR-11. Le `[NOTE FOR PM]` du §5.4 qui
limitait FR-11 à sa branche « pas de donnée » tombe : **la présence de FR-11 dans le périmètre
MVP cesse d'être un pari**, l'un des deux bloquants de phase ouverts depuis la première
rédaction.

**L'horizon de l'air (FR-10).** La qualité de l'air se prévoit à environ un jour, la chaleur
et le vent à une quinzaine. La branche « hors de portée des prévisions », que FR-10 tenait
pour un cas limite, devient le **cas courant pour l'air** dès que la rencontre est à plus
d'un jour — l'usage même que décrit le §2.1. C'est une propriété du produit, pas une panne ;
et si l'air doit réellement peser sur le choix d'un créneau, il faut une **source à horizon
plus long**, pas un correctif d'affichage.

**Autres changements.** §9 : la jouabilité couvre tout lieu qui n'est pas pleinement
intérieur. §11 : QO-4 garde son numéro et sa place selon le précédent de QO-3, et la question
fermée sur les seuils est précisée. **QO-6 n'a pas bougé** — l'architecture a posé une colonne
de dernière activité qu'elle ne lit jamais ; le seuil et son usage restent du produit. Aucun
identifiant réattribué, aucune exigence ajoutée ni retirée.

**Porté depuis l'aval / ajouté en le portant.** *Porté* : la projection de la nature du lieu,
la fermeture de QO-4, l'écart des horizons. *Ajouté, donc à redescendre* : la portée réelle
de la correction — six occurrences que l'aval ne signalait pas — et l'implication produit de
l'horizon de l'air, que l'architecture nommait comme une limite de fait sans en tirer la
conséquence. **Reliquat de la v4, soldé :** l'observation « cinq états de lien contre sept
états de page » est fermée par AD-10.

### v4 — 2026-08-27 *(résumé)*

Origine : passe `bmad-ux` v3.4, consignée dans
[decisions-2026-08-27-statut-abandonnee.md](decisions-2026-08-27-statut-abandonnee.md).
**Un cinquième statut de rencontre : *abandonnée* (FR-13).** La v3 promettait qu'abandonner
la rencontre en cours la fasse passer « par ses statuts ordinaires, jamais par un cinquième
état ». Aucun des quatre ne pouvait recevoir un abandon : tous décrivent la réponse du
partenaire, et router l'abandon vers *déclinée* aurait fait dire au bot qu'une personne
**a refusé** alors qu'elle n'avait rien répondu ; vers *expirée*, qu'une échéance était
passée alors que rien ne l'était. La phrase n'était pas imprécise, elle était
**inexécutable** — et le trou désarmait la règle qui l'avait créé : sans statut d'arrivée,
la rencontre restait *en attente*, le jour restait bloqué et la nouvelle recherche restait
refusée pour toujours. Le cinquième statut n'assouplit la règle d'aucun pouce, il la rend
applicable. **L'arbitrage retenu le rend uniforme** — un simple décalage d'heure produit lui
aussi une rencontre *abandonnée* ; exempter le changement de créneau réintroduisait le cas
particulier que la v3 avait fermé. **Personne n'est prévenu, et c'est délibéré** (FR-13,
FR-14) : ni courriel à l'utilisateur, qui vient de demander l'abandon, ni message au
partenaire, parce que **le SMS est le seul contact qu'un profil d'amorçage aura jamais avec
Ex Aequo** ; un état terminal de plus sur la page d'acceptation l'annonce à qui rouvre son
lien, et ce que ce silence coûte devient **QO-9**. Aussi : *rencontre* passe à cinq valeurs
au §3, *recherche active* n'a **pas** bougé, **FR-16** fait libérer le jour par *abandonnée*
immédiatement et **pour les deux profils**, et ce journal adopte ses deux conventions de
tenue. Deuxième correction de suite d'un fichier de décisions : la clause « aucun cinquième
état » meurt aux **trois** endroits où elle se trouvait, et non au seul signalé.

### v3 — 2026-08-27 *(résumé)*

Origine : passe `bmad-ux` v3.2, consignée dans
[decisions-2026-08-27-une-seule-recherche.md](decisions-2026-08-27-une-seule-recherche.md).
**Une seule recherche active à la fois (FR-13)** : lancer une recherche pendant qu'une
rencontre est *en attente* ou *confirmée* est refusé, et le bot nomme ce qui occupe la place
en donnant la sortie dans la même phrase. C'est le plus restrictif des trois arbitrages
possibles, et le seul qui se lève sans rien casser — **QO-8** en est la contrepartie : rien
ne mesure si la restriction gêne. **La définition venue de l'aval a été corrigée avant
d'être écrite** : ancrée sur la *demande*, elle rendait active à vie toute demande sans
rencontre — or 55 % des recherches exactes n'en produisent aucune — et tuait FR-9 au
passage, une alerte différée étant précisément une demande complète sans rencontre ;
réancrée sur les **deux statuts bloquants**, FR-9 survit par construction. Deux points
laissés indéterminés ont été arbitrés : la règle ne mord que sur les rencontres **nées de
ses propres demandes**, sans quoi un inconnu gelait quelqu'un qui n'avait rien demandé, de
façon cumulable ; et l'absence de mesure devient QO-8 plutôt qu'une contre-métrique que le
§10 ne pourrait pas valider. **« La validation du créneau » devient un geste défini** au §3,
*retenir un créneau* — expression employée sans jamais l'être, alors que FR-10 et toute la
§5.3 s'y adossaient. Aussi : le §6 gagne le récapitulatif d'au plus une rencontre, et
*Peut-on mener plusieurs recherches de front ?* rejoint les questions fermées sans consommer
de numéro. Conséquence aval déclarée : un désaccord de vocabulaire — sous-estimation dont la
v4 est la correction.

### v2 — 2026-08-27 *(résumé)*

Origine : séance `bmad-party-mode` du 2026-08-26, consignée dans
[decisions-2026-08-26-niveau.md](decisions-2026-08-26-niveau.md). **Le modèle du niveau est
renversé.** **FR-15 retirée** : le niveau n'est plus établi à partir de faits vérifiables,
il est **déclaré** parmi Débutant / Intermédiaire / Avancé — pris tel quel si la personne
emploie l'un des trois mots, demandé par trois choix sinon, jamais pendant la recherche
(FR-2) — et le produit prend ainsi sciemment le contre-pied de
[research-niveau.md](research-niveau.md) §4.1 (§7). **FR-7 retirée** : appariement à niveau
strictement égal pour tous les sports, le jour restant le seul axe d'élargissement (FR-6).
**SM-C1 retirée** avec elle, ne laissant plus aucune contre-métrique sur l'intégrité du
niveau ; **SM-C2 abaissée de 5 à 4 tours**. **Un écart assumé avec la décision d'origine :**
le fichier plaçait la question du niveau « à l'entrée au vivier, à la toute fin du parcours,
après le récapitulatif », ce qui n'était pas tenable puisque FR-5 cherche au niveau exact ;
elle est donc posée **au moment où la demande se complète** (FR-2), et la contrainte « jamais
pendant la recherche » se lit désormais comme jamais comme levier d'élargissement, jamais
après avoir montré des candidats, jamais pour rattraper un résultat vide. **Ce que le
renversement coûte, chiffré :** le résidu de combinaisons sans personne passe de **3,0 % à
6,1 %** (7 → 14 sur 231), tous en *Pilates Intermédiaire* — et un **5,2 % périmé**, porté
depuis la première rédaction au §2.3 et dans SM-4, a été corrigé au passage. Aussi :
**FR-2** ouvre la liste des sports, **FR-3** revient à **un seul sport par profil**,
**FR-16 est créée** (cycle de vie d'un profil : jour bloqué et jamais le profil entier,
*déclinée* libère immédiatement, *expirée* sert de ramasse-miettes), le §3 est réécrit
(*niveau adjacent* supprimé, *jour bloqué* ajouté) et le §11 reçoit des identifiants stables
`QO-n`, deux questions neuves (QO-6, QO-7) et la fermeture de QO-3. Conséquence aval : le
passage des deux spines UX en v3, soldé depuis.

### v1 — 2026-08-26

Première rédaction complète, puis réécriture sur les 46 constats de la passe de validation
([validation-report.md](validation-report.md)), puis finalisation. Le fil complet des
décisions est dans `.memlog.md`.
