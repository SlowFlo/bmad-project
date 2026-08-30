---
title: "Addendum — matière technique et décisions hors PRD"
status: living
created: 2026-08-26
updated: 2026-08-30
---

# Addendum

Ce document recueille ce qu'a apporté l'utilisateur et qui relève d'un document **aval**
(architecture, conception de solution, spec UX) plutôt que du PRD. Le PRD décrit des
capacités ; l'addendum garde le « comment ».

Chaque section suit la même forme : un constat, puis ses conséquences pour l'architecture.

## Contraintes d'entrée

### LLM

Le chatbot doit être branché sur **un LLM pour lequel l'utilisateur dispose déjà d'un
accès API**. C'est une contrainte, pas un choix à instruire : l'architecture s'appuie
dessus au lieu d'évaluer des alternatives.

*Conséquences pour l'architecture :*

- Trois points restent à préciser avec l'utilisateur, sans bloquer le PRD : le fournisseur
  et le modèle, les limites de débit et de quota, la pérennité de l'accès.
- Ces trois points commandent la conception de l'orchestration — budget de tokens par
  conversation, tolérance à la latence, stratégie de repli si l'API tombe.

### Architecture agentique

Le brief initial demande un **système multi-agents** pour orchestrer profils, matching,
planification, terrains et météo. C'est une décision d'architecture, délibérément tenue
hors du PRD : le PRD énonce les capacités attendues, l'architecture décide si elles sont
servies par des agents distincts, par des outils appelés depuis un agent unique, ou par un
mélange des deux.

*Conséquences pour l'architecture :*

- Le découpage « un agent par capacité » séduit sur le papier, mais il n'est pas gratuit :
  chaque saut inter-agents coûte de la latence dans une interface conversationnelle, où
  l'utilisateur attend devant un curseur.
- Ce découpage s'arbitre au moment de la conception, pas maintenant.

## Orchestration — les étapes annoncées engagent

Le PRD §7 érige les étapes annoncées par le bot en garantie produit : « les étapes que le
bot annonce correspondent aux sources qu'il a réellement interrogées ». Ce n'est pas une
exigence d'affichage, c'est une contrainte d'architecture.

*Conséquences pour l'architecture :*

- Chaque appel externe — météo, terrains, agenda — doit être **observable et diffusé au
  fil en temps réel**.
- Une source en échec remonte comme telle jusqu'à la conversation, sans repli silencieux.
- Une orchestration qui prépare une réponse complète avant de la rendre ne peut pas
  satisfaire cette contrainte.

## Persistance

Les profils ne sont **pas** lus depuis un CSV à chaud : le fichier
[SportsProfiles.csv](SportsProfiles.csv) (86 profils) sert de **données d'amorçage**,
chargé en base au premier lancement de l'application. Ensuite, la base est la source de
vérité et s'enrichit des utilisateurs qui passent par le chatbot.

*Conséquences pour l'architecture :*

- Le schéma en base doit accueillir **plus de colonnes que le CSV n'en a**. Les profils
  d'amorçage arriveront avec des champs vides — ni e-mail, ni secteur, ni heure de la
  journée — là où les profils créés par conversation seront plus complets. Prévoir la
  nullabilité plutôt que des valeurs par défaut trompeuses.
- Il faut pouvoir **distinguer un profil d'amorçage d'un utilisateur inscrit**, parce que
  le produit les traite différemment (PRD §4) : les 86 profils du CSV ne parlent jamais au
  bot et ne sont joignables que par SMS, là où un utilisateur inscrit a un compte, une
  adresse e-mail et une conversation.
- Le champ « jours disponibles » du CSV est une liste de jours de la semaine, pas des
  dates ni des heures. **L'heure de la rencontre** (FR-10, FR-12) est en revanche une
  donnée du produit : elle appartient à la rencontre, pas au profil, et n'a donc pas à
  s'ajouter au modèle de disponibilité.
- **Un profil porte un sport, et un seul** (FR-3), avec son niveau et ses jours
  disponibles. Le CSV est mono-sport et le modèle l'est aussi — mais une demande sur un
  autre sport **remplace** ces trois champs, donc le remplacement doit être une écriture
  atomique et annoncée, pas une accumulation. Si le multi-sport revient un jour, c'est une
  relation profil → sports qu'il faudra introduire ; ne pas la préparer aujourd'hui, la
  rendre possible suffit.
- **Le libellé de sport est une chaîne libre, pas une énumération** (FR-2, liste ouverte).
  C'est le point de fragilité du modèle : sans normalisation, « tennis », « Tennis » et
  « Tennis » sont trois sports distincts qui ne se rencontrent jamais, et le vivier se
  pulvérise silencieusement au fil des inscriptions. Prévoir une clé normalisée — casse,
  accents, espaces, éventuellement un dictionnaire de synonymes — distincte du libellé
  affiché. **Non tranché :** jusqu'où va la normalisation, et qui arbitre un sport
  réellement nouveau d'une variante orthographique.
- **Le niveau peut être absent.** Un profil de *niveau inconnu* (FR-2) est un état légal :
  la colonne est nullable, et l'absence exclut le profil de toute recherche — ce n'est pas
  une quatrième valeur de l'énumération.
- **Le statut d'une rencontre a cinq valeurs, et la cinquième n'oblige à rien de neuf**
  (FR-13, v4). *Abandonnée* n'étant ni *en attente* ni *confirmée*, les deux dérivations
  ci-dessous — le jour bloqué de FR-16 et la précondition d'une seule *recherche active*
  — la traitent correctement **sans être modifiées** : le jour se libère et la recherche
  redevient possible par le seul fait que le statut a changé. **Ce qui exige du soin est
  ailleurs, et à trois endroits.** *Premier :* la notification de changement de statut
  n'est pas uniforme — *abandonnée* met à jour l'événement d'agenda (FR-12) mais **n'envoie
  aucun courriel**, et un déclencheur générique « statut changé → prévenir » viole le
  produit dès sa première ligne. *Deuxième :* le lien d'acceptation du partenaire doit
  cesser de fonctionner quand la rencontre est abandonnée, donc sa validité se dérive du
  **statut de la rencontre** et pas seulement de l'état de son propre jeton. *Troisième :*
  seul l'utilisateur peut produire ce statut, jamais une tâche périodique ni le partenaire
  — c'est l'inverse exact d'*expirée*.
- **Le cycle de vie d'un profil se lit dans les rencontres, pas dans le profil** (FR-16).
  Un profil n'a pas de champ « bloqué » : sa disponibilité un jour donné se dérive des
  rencontres *en attente* ou *confirmée* qui portent ce jour. Deux conséquences — la
  recherche de FR-5 est une jointure, pas un filtre sur colonne ; et le passage à *expirée*
  doit être déclenché par le temps qui passe, donc par une tâche périodique, sans quoi les
  jours immobilisés ne sont jamais rendus. **Non tranché :** dérivation à la volée ou
  colonne dénormalisée tenue à jour.
- **La règle d'une seule *recherche active* (FR-13) exige de savoir qui a demandé
  quoi.** Elle ne mord que sur les rencontres nées des demandes de la personne
  elle-même : une rencontre porte donc un **côté demandeur** et un **côté partenaire**,
  là où le blocage par jour de FR-16 est au contraire **symétrique** et s'applique aux
  deux profils sans les distinguer. Les deux règles lisent le même état — les statuts
  *en attente* et *confirmée* — mais pas selon le même axe, et les confondre inverse le
  produit : ce serait laisser un inconnu geler quelqu'un qui n'a rien demandé.
- **C'est une précondition à l'entrée d'une demande, pas un statut de plus.** Aucune
  colonne « recherche en cours » : l'état se dérive de la même jointure que ci-dessus,
  filtrée sur le côté demandeur. Prévoir en revanche l'**atomicité** de la vérification
  et de la création — deux demandes quasi simultanées du même utilisateur, deux onglets
  ouverts, ne doivent pas produire deux rencontres. C'est la même fenêtre de course que
  celle décrite en FR-14 pour deux demandeurs, cette fois pour un seul.
- **La fraîcheur d'une fiche n'est pas modélisée** (PRD §11, QO-6). Le vivier ne diminuant
  jamais, un profil inactif depuis des mois reste proposé. Une date de dernière activité
  suffirait à ouvrir l'option plus tard ; la poser maintenant coûte une colonne, la poser
  après coup coûte une reprise de données. **Non tranché :** produit ou architecture.
- **La clé d'identité d'un utilisateur inscrit est son compte** (FR-3, FR-4). Un visiteur
  sans compte n'entre pas dans le vivier ; la déduplication n'a donc pas à traiter le cas
  du visiteur anonyme récurrent. Le fil de conversation, lui, doit survivre 30 jours sans
  compte (PRD §6).
- **Le lien d'acceptation** (FR-14) est à usage unique et porte aussi la sortie définitive
  du vivier. Prévoir un jeton opaque, non devinable, et un état terminal explicite :
  accepté, refusé, désinscrit, expiré, **abandonné par le demandeur**. Ce dernier est le
  seul qu'aucune action du porteur du lien ne produit : il **survient sous ses pieds**,
  entre l'envoi du SMS et la réouverture du lien, sans qu'aucun message l'ait annoncé. La
  page est donc **le seul canal** par lequel l'information peut lui parvenir — la rendre
  correctement n'est pas un raffinement.
- Le chargement d'amorçage doit être idempotent : relancer l'application ne duplique pas
  les 86 profils.

## Intégrations tierces pressenties

| Besoin | Piste | Remarque |
|---|---|---|
| Agenda | Google Calendar **et** Outlook / Microsoft Graph | Deux parcours OAuth distincts ; « Sign in with Google / Microsoft » peut servir à la fois l'identité et l'accès agenda |
| Météo | API météo + **indice ATMO** | Le besoin dépasse la pluie : chaleur ressentie, rafales, qualité de l'air — voir ci-dessous |
| Terrains | **Data ES** — Recensement des Équipements Sportifs du ministère des Sports, API Opendatasoft Explore v2.1, sans clé | **Tranché en v5.** Porte `equip_nature` et `aps_name`, les deux champs dont FR-11 et FR-10 dépendent. Dans le périmètre MVP — voir ci-dessous |
| E-mail sortant | Fournisseur d'envoi transactionnel | Deux usages : l'alerte différée de FR-9 et la notification de confirmation de FR-13. L'adresse vient de la connexion Google / Microsoft : ni saisie, ni vérification à prévoir |
| SMS sortant | Fournisseur d'envoi SMS | Sert FR-14. Chaque message a un coût réel : prévoir une limite de débit et un garde-fou contre les envois en boucle. Filtre de destinataire obligatoire — voir ci-dessous |
| Lien d'acceptation | Page web hors conversation | Sert FR-14. Seule surface du produit qui vit en dehors du fil ; le jeton et ses états sont décrits en « Persistance » |

### Météo — jouabilité et qualité de l'air

Le besoin dépasse la pluie : le PRD (FR-10) demande la chaleur ressentie, les rafales et
la qualité de l'air, et fixe le seuil sur l'échelle ATMO à six degrés, ≥ 4.

*Conséquences pour l'architecture :*

- Pour Lyon, c'est ATMO Auvergne-Rhône-Alpes qui fait foi.
- **Seul un équipement pleinement intérieur n'appelle aucune requête.** Un équipement
  *extérieur couvert* reste soumis aux trois seuils, qui ne comportent aucune notion de
  pluie : le classer « couvert » désactiverait la jouabilité là où elle reste pertinente.
  La projection de la nature du lieu vers un booléen *jouabilité applicable* est une règle
  de domaine, pas un détail d'adaptateur. **Corrigé en v5** — la formulation antérieure
  disait l'inverse.
- **Deux ports séparés, aux horizons déclarés distincts.** La chaleur ressentie et les
  rafales se prévoient à une quinzaine de jours ; l'indice ATMO à environ un. Un appel
  « météo » unique effacerait en silence un écart d'un ordre de grandeur et produirait soit
  un trou muet, soit une valeur inventée. Le créneau hors de portée de l'un des deux emprunte
  la branche que FR-10 prévoit déjà, en **nommant** le seuil non établi.

### Terrains : tranché en v5

La source est **Data ES**, le Recensement des Équipements Sportifs du ministère des Sports,
interrogeable anonymement en une requête. **QO-4 est fermée** et FR-11 cesse d'être un pari :
le `[NOTE FOR PM]` du §5.4 qui limitait l'exigence à sa branche « pas de donnée » est retiré.

*Conséquences pour l'architecture :*

- La source porte les deux champs dont le produit dépend : `equip_nature` pour la nature de
  l'équipement, `aps_name` pour l'activité pratiquée.
- **`equip_nature` n'est pas un booléen**, et c'est la découverte qui a produit une règle :
  la valeur observée est « Extérieur couvert ». La projection vers *jouabilité applicable*
  vit donc dans le domaine et se décide sur la lettre de FR-10 — trois seuils, pas de pluie.
- Le filtrage lyonnais se fait à l'interrogation ; une ville unique garde par ailleurs
  envisageable, en repli, la saisie manuelle des principaux équipements.

### SMS — filtre de destinataire

FR-14 envoie de vrais SMS, et les données d'amorçage portent des personnes qui n'ont rien
demandé. Le risque n'est pas théorique : une campagne de test qui parcourrait le vivier
composerait 86 numéros.

Les numéros de [SportsProfiles.csv](SportsProfiles.csv) ont donc été **remplacés par des
numéros de la plage `+336 39 98 XX XX`**, réservée par l'ARCEP aux œuvres de fiction et
garantie non attribuée à un abonné
([décision ARCEP, art. 2.5.12](https://www.legifrance.gouv.fr/jorf/article_jo/JORFARTI000037263033)).
Les 86 profils portent `+3363998 0001` à `+3363998 0086`, uniques et dans l'ordre du
fichier.

*Conséquences pour l'architecture :*

- Le filtre de destinataire est une **règle de production, pas un interrupteur de test** :
  un envoi n'est autorisé que vers un numéro de la plage de fiction, ou vers un numéro
  qu'un utilisateur inscrit a lui-même saisi. Tout autre numéro fait échouer l'envoi avec
  une erreur explicite.
- Le filtre suppose de savoir, pour chaque numéro, **d'où il vient** : donnée d'amorçage
  ou saisie utilisateur. Cette provenance se porte dans le modèle, au même titre que la
  distinction entre profil d'amorçage et utilisateur inscrit, au lieu de se déduire du
  préfixe — la règle survit ainsi à un futur amorçage par d'autres données.
- Prévoir un mode « journaliser sans envoyer » pour le développement, en plus du filtre :
  les deux ne se remplacent pas.

## Notation du niveau — mécanisme écarté en v1

Le détail algorithmique — schéma `mu` / `sigma` / `last_played` par joueur et par sport,
mise à jour à pas proportionnel à l'incertitude, ancres humaines, appariement par
intervalles qui se recouvrent — est documenté dans
[research-niveau.md](research-niveau.md), section 4.

**Ce mécanisme n'est pas retenu en v1, et l'écart s'est creusé en v2.** L'arbitrage du PRD
est que le niveau est **déclaratif**, à trois valeurs (Débutant, Intermédiaire, Avancé),
demandé une seule fois, et que **toute forme de calibration est hors périmètre** — y compris
l'inférence à partir de faits déclarés, qui existait en v1 sous FR-15 et a été retirée
(PRD §13). Il n'y a donc aucun calcul de niveau à implémenter : ni notation, ni inférence,
ni correction. Une énumération à trois valeurs, nullable, écrite une fois.

Deux conséquences pour l'architecture :

- **Ne pas anticiper le mécanisme.** Pas de colonne `mu`, pas de `sigma`, pas d'historique
  de résultats. Le PRD assume la sur-évaluation sans contrepartie (PRD §7) ; un schéma qui
  prépare la correction laisserait croire qu'elle est prévue.
- **Garder les rencontres exploitables.** Le seul signal de retour gratuit identifié est le
  **jour** que la personne choisit parmi ceux proposés (PRD §11, QO-7). Il est déjà conservé
  par FR-16. C'est suffisant, et c'est tout ce qu'il faut préserver aujourd'hui.

Le détail algorithmique ci-dessus reste de la matière pour une v2 éventuelle, pas une
capacité attendue.

## Pièges de démonstration

Matière opérationnelle, pas une exigence : ce qu'il faut savoir avant de montrer le
produit en direct.

- **Sarah André ne peut jamais trouver personne.** Elle est la seule pratiquante de
  Pilates des données d'amorçage : si on la prend comme *demandeuse*, aucun élargissement
  ne produira de candidat. Excellent cas pour montrer FR-8, très mauvais pour montrer le
  parcours nominal.
- **Le scénario « Tennis, mardi » est étroit.** Il ne renvoie qu'une personne, Emma Leroy,
  et seulement si le demandeur est Débutant. En Intermédiaire ou Avancé, le résultat exact
  est vide — soit le scénario de UJ-1, où l'élargissement sur le jour prend le relais. À
  choisir sciemment selon ce qu'on veut démontrer.
- **Le Pilates est le seul sport entièrement mort, et il l'est deux fois depuis la v2.**
  L'égalité stricte de niveau (FR-5) fait que *Pilates Intermédiaire* rejoint *Pilates
  Avancé* parmi les paires sans aucun candidat : ce sont les deux seules des 33, soit
  14 combinaisons sur 231. Tout le reste du vivier trouve quelqu'un après élargissement sur
  le jour.
- **Une démonstration du cycle de vie demande deux demandeurs et deux jours.** Le blocage de
  FR-16 porte sur le jour de la rencontre seulement : pour le montrer, il faut retenir une
  personne un mercredi, puis la rechercher sur un autre de ses jours — où elle doit encore
  apparaître.
- **Démontrer l'abandon demande de préparer deux surfaces, pas une.** Le cinquième statut
  (FR-13) se voit dans le fil du demandeur *et* sur la page d'acceptation du partenaire,
  et **aucun message ne relie les deux** : pour le montrer en direct, il faut garder le
  lien d'acceptation ouvert dans un second onglet et le recharger après l'abandon. Une
  démonstration qui ne montre que le fil laisse croire que le partenaire n'apprend jamais
  rien.
- **La moitié du vivier pratique un sport sans appariement en duel** (yoga, pilates,
  danse, natation, course à pied, escalade), et 34 profils font un sport d'équipe qui
  demanderait 10 à 30 personnes. C'est la décision « partenaire de pratique » plutôt
  qu'« adversaire » (PRD §3) qui rend ces profils exploitables. Une démonstration qui
  ignorerait cette nuance donnerait l'impression d'un vivier absurde.
