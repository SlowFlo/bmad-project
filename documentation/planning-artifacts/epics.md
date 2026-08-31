---
stepsCompleted: [1, 2, 3, 4]
inputDocuments:
  - documentation/planning-artifacts/prds/prd-bmad-2026-08-26/prd.md
  - documentation/planning-artifacts/prds/prd-bmad-2026-08-26/addendum.md
  - documentation/planning-artifacts/prds/prd-bmad-2026-08-26/decisions-2026-08-26-niveau.md
  - documentation/planning-artifacts/prds/prd-bmad-2026-08-26/decisions-2026-08-27-statut-abandonnee.md
  - documentation/planning-artifacts/prds/prd-bmad-2026-08-26/decisions-2026-08-27-une-seule-recherche.md
  - documentation/planning-artifacts/architecture/architecture-bmad-2026-08-28/ARCHITECTURE-SPINE.md
  - documentation/planning-artifacts/architecture/architecture-bmad-2026-08-28/SOLUTION-DESIGN.md
  - documentation/planning-artifacts/architecture/architecture-bmad-2026-08-28/DECOUPAGE.md
  - documentation/planning-artifacts/ux-designs/ux-bmad-2026-08-26/DESIGN.md
  - documentation/planning-artifacts/ux-designs/ux-bmad-2026-08-26/EXPERIENCE.md
  - documentation/specs/spec-ex-aequo/SPEC.md
  - documentation/specs/spec-ex-aequo/glossaire.md
  - documentation/specs/spec-ex-aequo/criteres-acceptation.md
  - documentation/specs/spec-ex-aequo/criteres-reussite.md
  - documentation/specs/spec-ex-aequo/donnees-amorcage.md
  - documentation/specs/spec-ex-aequo/statuts-rencontre.md
  - documentation/implementation-artifacts/spec-e1-socle-du-vivier.md
  - documentation/implementation-artifacts/deferred-work.md
---

# Ex Aequo — Découpage en épiques et stories

## Overview

Ce document formalise en épiques et en stories le découpage déjà arbitré par
[DECOUPAGE.md](architecture/architecture-bmad-2026-08-28/DECOUPAGE.md), qui **fait autorité
sur la partition**. Les neuf lots E1 à E9 sont repris dans l'ordre établi ; le travail n'est
pas re-partitionné. Ce qui est produit ici, ce sont les stories *à l'intérieur* des lots et
la carte de couverture qui prouve qu'aucune exigence du PRD v5 n'est tombée entre eux.

Trois conventions gouvernent tout ce document.

**Le vocabulaire de [glossaire.md](../specs/spec-ex-aequo/glossaire.md) est employé
littéralement**, jusque dans les titres de stories et les critères d'acceptation. Jamais
*match*, *rendez-vous*, *booking*, *slot*. *Vivier*, *demande*, *candidat*, *partenaire*,
*créneau*, *rencontre*, *jour bloqué*, *recherche active*, *jouabilité* sont les mots du
produit et les mots du code.

**Les identifiants amont sont conservés sans renumérotation.** `FR-n` vient du PRD v5,
`CAP-n` du SPEC, `AD-n` de la spine d'architecture, `SM-n` des critères de réussite. Un
identifiant retiré n'est jamais réattribué : **FR-7** (élargissement au niveau voisin) et
**FR-15** (établissement du niveau par des faits) sont retirés, **SM-C1** aussi.

**Les « Fait quand » de DECOUPAGE.md sont des critères de démonstration, pas de complétude.**
Ils sont repris tels quels comme critères d'acceptation d'épique, mais ils ne closent pas un
lot : ils prouvent qu'il tient. La mesure est faite sur E1, le seul lot où l'on puisse comparer
un « Fait quand » aux critères réels du lot — il en couvre **deux sur quatre**, et les deux
absents (l'absence de dépendance sortante du domaine, l'ordre du vivier) sont précisément ceux
dont E2 dépend. **Une épique est close par les critères d'acceptation de ses stories** ; son
« Fait quand » est ce qu'on montre.

## Requirements Inventory

### Functional Requirements

Quatorze exigences fonctionnelles vivantes, issues du PRD v5 §5. Deux numéros sont retirés et
gardent leur place vide.

- **FR-1 — Dialoguer sans authentification.** Un visiteur peut ouvrir le site et dialoguer
  avec le bot sans compte ni inscription. La page d'entrée présente le chatbot utilisable
  sans écran d'authentification préalable, et un visiteur sans compte obtient des
  propositions de partenaires nommés. *(CAP-1)*

- **FR-2 — Extraire une demande du langage naturel.** Le bot extrait d'un message libre le
  sport, les jours et le niveau, et réclame ce qui manque **un élément à la fois**. Le niveau
  ne s'interprète pas : l'un des trois mots exacts est retenu tel quel, toute autre
  formulation ouvre les trois choix. La liste des sports est ouverte — un sport inconnu du
  vivier est un sport **vide**, jamais un sport refusé. Le bot ne demande **jamais** le
  niveau pendant la recherche. Un refus de répondre produit un *niveau inconnu*. *(CAP-2)*

- **FR-3 — Enregistrer l'utilisateur dans le vivier.** Un utilisateur devient trouvable par
  les recherches des autres **à la création de son compte**, et pas avant. Son profil porte
  **un sport, et un seul**. Une demande sur un autre sport remplace sport, niveau et jours
  **en une seule transaction**, après que le bot a annoncé ce que le remplacement coûte. Le
  compte est la clé d'identité du profil. *(CAP-3)*

- **FR-4 — Demander un compte au moment de la mise en relation.** Le bot demande la création
  d'un compte lorsqu'il va exposer l'utilisateur à une autre personne ou devra le recontacter
  — jamais avant. Chercher, obtenir des propositions, retenir un candidat et consulter la
  jouabilité ne la déclenchent pas ; **retenir un créneau** et accepter une alerte différée la
  déclenchent. Le bot énonce son motif et dit que le compte rend l'utilisateur trouvable. Le
  numéro de téléphone est facultatif. *(CAP-4)*

- **FR-5 — Recherche exacte.** Le bot renvoie les profils du vivier partageant le sport, au
  moins un jour disponible et le **niveau exact** de la demande. L'égalité de niveau est
  stricte, sans exception, à aucune étape. Un profil dont le jour demandé est bloqué n'est pas
  renvoyé **pour ce jour-là** ; un profil de *niveau inconnu* n'est jamais renvoyé ;
  l'utilisateur n'est jamais son propre partenaire. *(CAP-5)*

- **FR-6 — Élargir sur le jour.** Sans résultat exact, le bot relâche le jour — **et lui
  seul** — en conservant le niveau, et présente les candidats avec leurs jours. **Au plus
  trois candidats**, classés par **délai d'attente croissant** compté vers l'avant depuis le
  jour demandé, l'**ordre du vivier** départageant les ex æquo. Au-delà de trois, le bot dit
  combien il y en a d'autres et propose de les montrer. *(CAP-6)*

- **FR-7 — Retirée.** Élargissement au niveau voisin. Numéro non réattribué.

- **FR-8 — Annoncer l'absence de résultat sans broder.** Quand l'élargissement ne produit
  aucun candidat, la réponse **nomme le sport et le jour tentés**, dit que tous les autres
  jours ont été regardés, conclut qu'il n'y a personne **à ce niveau**, et enchaîne sur
  l'alerte différée. Jamais une personne absente du vivier, jamais quelqu'un d'un autre sport.
  *(CAP-7)*

- **FR-9 — Proposer une alerte différée.** Le bot propose d'enregistrer la demande et de
  prévenir par courriel si un profil correspondant rejoint le vivier. Déclenchement sur
  **correspondance exacte** — même sport, même niveau, au moins un jour commun — à
  **l'écriture d'un profil** et pas seulement à la création d'un compte. Notification dans
  l'heure, validité **60 jours** puis expiration annoncée par courriel. Plusieurs alertes
  coexistent ; chacune s'annule depuis la conversation. *(CAP-8)*

- **FR-10 — Évaluer la jouabilité d'un créneau.** Trois seuils : ressenti **> 28 °C**, rafales
  **> 40 km/h**, indice ATMO **≥ 4**. Le contrôle intervient **avant** que le créneau soit
  retenu. La jouabilité dépend du **lieu**, pas du sport : seul un équipement **pleinement
  intérieur** désactive les trois seuils, un équipement *extérieur couvert* y reste soumis. Le
  bot propose une heure alternative ; **l'alerte informe et n'interdit pas**, et accepter une
  heure **ne retient rien**. Les **deux horizons sont distincts** — météo à seize jours, air à
  environ un — et un créneau hors de portée de l'un rend les seuils établis en **nommant**
  celui qui ne l'a pas été. *(CAP-9)*

- **FR-11 — Proposer un lieu à Lyon.** Équipements lyonnais adaptés au sport, chacun portant
  **sa nature** — c'est elle qui décide de FR-10. Un secteur peut être demandé, jamais exigé,
  et un secteur donné est enregistré au profil et réutilisé. Sans donnée, le bot le dit : il
  n'invente aucun lieu plausible. *(CAP-10)*

- **FR-12 — Écrire la rencontre dans l'agenda.** Google ou Outlook, au choix. L'écriture n'a
  jamais lieu sans confirmation explicite. L'événement porte le sport, le prénom du
  partenaire, le lieu, le jour, l'heure et le statut — et **aucun numéro de téléphone**. Il est
  mis à jour à **chaque** changement de statut, *abandonnée* comprise. Le produit n'écrit
  jamais dans l'agenda de quelqu'un d'autre. *(CAP-11)*

- **FR-13 — Tenir le statut d'une rencontre.** Cinq statuts et un seul à la fois : *en
  attente*, *confirmée*, *déclinée*, *expirée*, *abandonnée*. Les effets sont attachés aux
  **transitions**, jamais aux statuts ; l'arête vers *abandonnée* met à jour l'agenda et
  **n'émet ni courriel ni message au partenaire**, et seul l'utilisateur la franchit. **Une
  seule recherche active à la fois** : le bot nomme le sport, le partenaire et le jour occupés,
  et donne la sortie dans la même phrase. Seules comptent les rencontres nées des demandes de
  la personne elle-même. Aucune rencontre n'est supprimée en silence. *(CAP-12)*

- **FR-14 — Prévenir le partenaire et lui permettre d'accepter.** **SMS** si la personne a un
  numéro, **courriel** si elle est inscrite et n'en a pas donné ; qui n'a ni l'un ni l'autre
  n'est jamais sollicitée. Le message énonce son motif, porte sport, jour, heure, lieu et
  prénom du demandeur, **aucune coordonnée**, et un moyen de **ne plus jamais être contacté**.
  Le lien est à usage unique, son jeton opaque et non devinable. **Aucun SMS ne part hors de la
  plage de fiction ARCEP `+336 39 98 XX XX`**, sauf vers un numéro qu'un utilisateur inscrit a
  lui-même saisi ; le filtre lit la **provenance enregistrée**, jamais le préfixe. La page rend
  l'un des **sept états terminaux** et jamais une erreur nue. *(CAP-13)*

- **FR-15 — Retirée.** Établissement du niveau par des questions de faits. Numéro non
  réattribué.

- **FR-16 — Tenir le cycle de vie d'un profil au vivier.** Un profil entre au vivier à la
  création du compte, y **reste après ses rencontres**, et n'en sort que s'il le demande. Une
  rencontre *en attente* ou *confirmée* bloque, pour les **deux** profils, **le seul jour** de
  la rencontre ; *déclinée*, *abandonnée* et *expirée* le libèrent, l'abandon pour les deux. Le
  profil conserve ses jours demandés **et le jour accepté**. Un profil sorti du vivier ne
  revient dans aucune recherche. *(CAP-14)*

Deux exigences du contrat n'ont pas de numéro `FR-n` d'origine et sont portées ici sous leur
identifiant `CAP-n`, faute de quoi elles tomberaient entre les lots.

- **CAP-15 — Reprendre une conversation.** *(exigence non fonctionnelle de reprise, PRD §6)*
  Le fil n'est jamais purgé ni réinitialisé. Un utilisateur inscrit retrouve ses demandes, ses
  alertes et sa rencontre ; le récapitulatif de reprise est **en prose**, porte **au plus une
  rencontre**, ouvre le tour du bot, s'insère **en bas du fil** et **ne re-rend aucun bloc**. Un
  visiteur sans compte retrouve son fil **30 jours** sur le même navigateur. La conversation
  **précède l'identité et lui survit** (AD-21).

- **CAP-16 — Rendre le travail du bot visible.** *(PRD §7, AD-3)* Chaque appel externe émet une
  **étape à l'entrée et à la sortie**, portant le service et son sort. Le **signe de vie part au
  premier appel d'outil, avant le premier jeton du modèle**. Une source en échec est annoncée
  nommément. **Le modèle ne dispose d'aucun outil lui permettant d'émettre une étape.** Les
  étapes sont persistées avec le tour.

### NonFunctional Requirements

Quatre exigences du PRD §6, plus les deux transversales que le SPEC ajoute.

- **NFR-1 — Latence conversationnelle.** Signe de vie **en moins de 2 secondes**, réponse
  complète **en moins de 20 secondes**. Au-delà, le bot dit ce qu'il fait et pourquoi c'est
  long. Bornes posées par défaut, là pour être vérifiables.

- **NFR-2 — Robustesse des services externes.** Météo, terrains et agenda peuvent être
  indisponibles ; le bot nomme le service qui n'a pas répondu et **le parcours reste terminable
  sans lui** : sans météo la rencontre se prend sans contrôle de jouabilité, sans terrains
  l'utilisateur indique le lieu, sans agenda la rencontre existe et l'écriture se réessaie plus
  tard. **Aucune valeur par défaut n'est jamais substituée.**

- **NFR-3 — Reprise de conversation.** Le fil n'est jamais purgé ni réinitialisé de lui-même.
  Un utilisateur inscrit retrouve tout ; un visiteur sans compte, **30 jours** sur le même
  navigateur. Le récapitulatif porte **au plus une rencontre**.

- **NFR-4 — Surface.** Site web responsive, **PC d'abord**, mobile à **parité fonctionnelle
  stricte**. Plancher **320 px** sans débordement horizontal — valeur d'EXPERIENCE.md, retenue
  contre les 360 px du PRD §6 parce qu'elle est la plus exigeante — y compris sous l'espacement
  forcé de WCAG 1.4.12. Pas d'application native, donc **pas de notification push** : les
  notifications différées passent par le courriel et le SMS.

- **NFR-5 — Panne du LLM.** *(SPEC § Robustesse et pannes ; AD-20)* Seul échec sans repli.
  Rendu comme un tour du fil qui **nomme la panne et dit ce qui n'est pas perdu**, avec un texte
  **arrêté et non généré**. **Aucune écriture de domaine n'est engagée par un tour interrompu.**

- **NFR-6 — Enveloppe technique.** *(SPEC § Constraints)* Un seul processus exécuté en local,
  base SQLite fichier à côté du dépôt, aucun conteneur, aucun hébergement, aucun environnement
  multiple. Les redirections OAuth sur `http://localhost:<port>` sont acceptées par les deux
  fournisseurs.

### Additional Requirements

Exigences techniques issues d'ARCHITECTURE-SPINE.md et de SOLUTION-DESIGN.md. Elles ne sont
pas des stories en elles-mêmes : ce sont les invariants que les stories des lots doivent
tenir, et que les critères d'acceptation citent nommément.

**Pas de starter template.** L'architecture n'en prescrit aucun. Le squelette du projet a été
posé par E1, déjà livré (commit `889ad43`) : `pyproject.toml` géré par uv, Python 3.13,
FastAPI, SQLAlchemy, SQLite fichier, pytest en groupe de développement.

**Les vingt-et-un invariants d'architecture (AD-1 à AD-21).**

- **AD-1** — Le LLM ne produit aucun fait : extraction d'une demande, choix de l'outil, prose.
  Aucun module du domaine n'importe le SDK Anthropic.
- **AD-2** — Un seul saut LLM par tour : une boucle de *tool runner*, aucun appel imbriqué, ni
  routeur ni agent spécialisé.
- **AD-3** — Les lignes d'étape sont émises par la couche d'appel d'outil, à l'entrée et à la
  sortie ; le modèle n'a aucun outil pour en émettre.
- **AD-4** — Un flux SSE par tour, quatre types d'événements : `etape`, `jeton`, `bloc`, `fin`.
  Un `bloc` est composé par l'adaptateur web à partir d'un résultat de domaine.
- **AD-5** — L'appariement porte sur la **clé de sport normalisée**, jamais sur le libellé. La
  table de synonymes redirige **à l'écriture**, jamais à la lecture ; un libellé inconnu fonde
  un sport.
- **AD-6** — La disponibilité et la recherche active sont **dérivées**, jamais stockées : ni
  champ `bloque`, ni champ `recherche_active`.
- **AD-7** — Le blocage par jour est **symétrique** ; la précondition d'une seule recherche
  active ne lit que le **côté demandeur**.
- **AD-8** — Retenir un créneau est une **transaction unique** : précondition, rencontre, jeton,
  inscription à la boîte d'envoi. L'acceptation côté partenaire en est une autre.
- **AD-9** — Les effets sont attachés aux **transitions**, pas aux statuts. Table d'arêtes
  explicite.
- **AD-10** — La validité du lien d'acceptation est la **conjonction** du statut de la rencontre
  et de l'état du jeton, résolus ensemble à la lecture.
- **AD-11** — La **provenance** de chaque numéro et la **population** de chaque profil sont
  portées dans le modèle, jamais déduites d'un préfixe.
- **AD-12** — Le **filtre de destinataire** (règle de domaine, active en production) et la
  **boîte d'envoi** (adaptateur persisté) sont deux couches distinctes qui ne se remplacent pas.
- **AD-13** — Un échec de service externe est une **valeur typée**, jamais une exception. Aucune
  valeur par défaut substituée.
- **AD-14** — La jouabilité se décide sur une **projection explicite** de `equip_nature` vers un
  booléen *jouabilité applicable*, qui vit **dans le domaine**.
- **AD-15** — Le temps qui passe est un **adaptateur primaire idempotent** : passage à *expirée*,
  expiration des alertes à 60 jours. Il ne franchit jamais l'arête vers *abandonnée*.
- **AD-16** — L'amorçage est **idempotent**, sur une clé naturelle stable. *(tenu par E1)*
- **AD-17** — Le fil est **append-only** ; seuls le récapitulatif de rencontre et le
  récapitulatif de profil mutent sur place, uniques par entité.
- **AD-18** — L'autorisation OAuth est **incrémentale** : identité et adresse d'abord, portée
  d'écriture agenda au second consentement.
- **AD-19** — Météo et qualité de l'air sont **deux ports séparés aux horizons déclarés
  distincts** — seize jours contre environ un — et le plus court commande.
- **AD-20** — La panne du LLM est le seul échec sans repli, et elle se dit avec un texte arrêté.
- **AD-21** — Le fil **précède l'identité et lui survit** : cookie signé de 30 jours,
  attachement au compte à la connexion, ni rejeu ni duplication.

**Conventions de cohérence** *(spine, § Consistency Conventions)* — vocabulaire du glossaire
littéral jusque dans les noms de tables et de fonctions ; ports nommés `Port<Capacité>` et
adaptateurs nommés par le service ; **UUIDv7** pour toute entité et jeton d'acceptation de
**256 bits d'aléa cryptographique** distinct de l'identifiant de rencontre ; jours de la semaine
en **énumération**, heures en `Europe/Paris` stockées en **UTC**, sérialisation ISO 8601 ;
**nullabilité** plutôt que valeurs par défaut trompeuses ; `Resultat[T]` en retour de tout port ;
seul le domaine mute ; variables d'environnement pour les secrets, `.env.example` sans valeurs ;
les étapes persistées avec le tour, distinctes de la journalisation technique.

**Stack épinglée** — Python 3.13, fastapi 0.141.1, uvicorn 0.52.4, sqlalchemy 2.0.52, anthropic
1.2.0, modèle `claude-opus-5`, SQLite fourni par Python. Services tiers : **Open-Meteo** (API v1,
sans clé, horizon 16 jours), **API ATMO Auvergne-Rhône-Alpes** (identifiant requis, gratuit sur
inscription, horizon ~1 jour — **seule démarche du projet**), **Data ES** (Opendatasoft Explore
v2.1, sans clé, champs `equip_nature` et `aps_name`), **Google Calendar / Microsoft Graph**.

**Arbre source** *(spine, § Structural Seed)* — `exaequo/domaine/` sans dépendance sortante
(`vivier`, `sports`, `recherche`, `rencontre`, `jouabilite`, `alerte`, `envoi`, `ports`) ;
`exaequo/adaptateurs/primaires/{web,agent,horloge}` ; `exaequo/adaptateurs/secondaires/{persistance,meteo,air,lieux,agenda,envois}` ;
`exaequo/amorcage/`.

**Deux reports d'E1 explicitement renvoyés à l'aval** *(deferred-work.md)*, intégrés en critères
d'acceptation dans les lots qui les tranchent.

- **DW-1 — Index sur `profil.sport_id`.** SQLite n'indexe pas automatiquement les clés
  étrangères ; « chercher les profils d'un sport » est l'usage central d'E2. **À trancher dans
  E2**, qui connaîtra ses accès.
- **DW-2 — Lecture du fichier `.env`.** `.env.example` documente six clés mais aucun code ne lit
  de fichier `.env` ; `python-dotenv` n'est pas dans la table *Stack*, donc l'ajouter relève du
  « Ask First ». **À trancher dans E3**, premier lot à consommer réellement une clé (Anthropic).

*Les cinq autres reports de deferred-work.md restent hors épique* : l'empaquetage du CSV par
hatchling, la contrainte symétrique population *inscrit* / `cle_amorcage`, la cellule « Sports
pratiqués » multi-valuée, les garde-fous de `poser_synonyme`, et l'intégration continue.

### UX Design Requirements

Extraites de [DESIGN.md](ux-designs/ux-bmad-2026-08-26/DESIGN.md) — identité visuelle — et
d'[EXPERIENCE.md](ux-designs/ux-bmad-2026-08-26/EXPERIENCE.md) — comportement, états,
accessibilité, parcours. Le contrat UX est un document d'entrée de premier rang, au même titre
que le PRD. Sauf mention contraire, ces exigences atterrissent dans **E3**, qui construit
l'adaptateur web ; celles qui portent sur une surface d'un autre lot le disent.

**Fondations visuelles**

- **UX-DR1 — Jetons de couleur.** Palette délibérément pauvre, **thème sombre unique**, pas de
  bascule clair/sombre. `surface-base` `#0B1220`, `surface-raised` `#111C2E`, `surface-overlay`
  `#18263C`, `surface-user` `#1B2C46` ; `accent` `#2DD4A7` (l'acquis, et lui seul) ;
  `status-pending` `#E8A33D` (*en attente*, et rien d'autre) ; `status-danger` `#F0637A` (la
  jouabilité dangereuse, et rien d'autre) ; `focus-ring` `#7DD3FC` ; encres `ink-primary`,
  `ink-secondary`, `ink-primary-soft` `#D6DEE9`, `ink-disabled` `#55677F` (bouton d'envoi
  `disabled` natif, seul usage) ; filets `border-interactive` `#6B82A6` et `border-strong`.
  **Aucun gris sourd pour dire l'inconnu.**
- **UX-DR2 — Table de contraste contractuelle.** Les vingt paires chiffrées de DESIGN.md sont un
  contrat : toute composition qui les enfreint est un défaut. Les douze « compositions à
  surveiller » sont admises **parce qu'un filet ou un mot porte l'information**, jamais la marche
  tonale seule. Deux dépendances sont nommées et doivent survivre à toute retouche : la marge la
  plus fine du système (`ink-secondary` sur `surface-raised-pressed`, **4,513:1**) et
  l'`outlineOffset: 2px` sans lequel l'anneau de focus du bouton primaire n'est pas conforme.
- **UX-DR3 — Typographie.** Une seule famille, `Inter` avec repli sur la pile système. Rôles :
  `display`, `message` (1,0625 rem, interligne 1,6), `card-name`, `meta`, `meta-unknown`
  (italique, **seul marqueur typographique du système**), `label`. **Toutes les tailles en
  `rem`**, aucune hauteur de conteneur fixe, tenue sous l'espacement forcé de WCAG 1.4.12.
- **UX-DR4 — Layout et espacement.** `message-gap` 24 px, `turn-gap` 32 px, `thread-max-width`
  45 rem, `gutter-desktop` 32 px, `gutter-mobile` 16 px, `breakpoint` **49 rem** exprimé une seule
  fois et écrit en `em` dans la requête média. Une colonne centrée, le **vide latéral assumé** :
  ni panneau, ni grille, ni carte pour le remplir.
- **UX-DR5 — Élévation et formes.** **Aucune ombre portée**, y compris pour l'anneau de focus.
  Trois marches tonales et pas davantage ; un seul filet porteur, `border-interactive`, à 3:1 sur
  les cinq fonds où il est posé. Rayons `sm` 8 px, `md` 12 px, `lg` 18 px, `full` (pastilles
  seulement). **Les messages du bot n'ont pas de forme** — ni bulle, ni fond, ni contour : geste
  visuel le plus important du produit, obligatoirement doublé par UX-DR20.
- **UX-DR6 — Mode contraste forcé.** Sous `forced-colors: active`, toute la hiérarchie de fonds
  disparaît : chaque surface qui compte porte un **filet réel** et chaque pastille porte **son
  mot**. Le produit reste lisible sans une seule de ses couleurs.

**Composants** — vingt-trois composants nommés, chacun avec ses états.

- **UX-DR7 — `message-bot` et `message-user`.** Texte nu sur `surface-base` aligné à gauche,
  pleine largeur de colonne, sans avatar ni horodatage / bulle `surface-user` alignée à droite,
  `rounded/lg`, 80 % de la colonne au plus. Le message du bot **arrive en un bloc**, pas
  caractère par caractère, et pas de points de suspension imitant un indicateur de frappe.
- **UX-DR8 — `step-line` et ses trois états.** Ligne en `meta` / `ink-secondary` précédée d'un
  point `accent` de 6 px. *Franchie* : phrase à l'accompli, point plein. *En cours* : pulsation
  **bornée à 5 secondes** (WCAG 2.2.2) **plus une suspension typographique**, et un marqueur
  textuel « en cours » qui existe **toujours**, masqué visuellement quand la pulsation joue.
  *Échouée* : **encre `ink-primary`**, seule ligne d'étape à quitter `ink-secondary`, aucune
  teinte, et une phrase qui dit ce qui n'a pas pu être fait. **Les étapes franchies et échouées
  restent dans la pile.**
- **UX-DR9 — `partner-card`.** `surface-raised`, filet `border-interactive`, `rounded/md`.
  Prénom en `card-name`, **jours et délai d'attente** en `meta`. **Le niveau n'y figure pas** —
  il vit dans `candidate-group-label`. **Identique pour les deux populations du vivier** : aucun
  badge « profil d'amorçage », aucune mention de second rang. Trois états : active, survolée
  (filet `border-strong`), pressée, **inerte avec son sort écrit en toutes lettres**.
- **UX-DR10 — Pastille de statut, cinq valeurs.** `rounded/full`, fond sourd, texte de la même
  famille : *en attente* (ambre), *confirmée* (vert), *déclinée*, *expirée*, *abandonnée*
  (neutres). **Le statut est un mot, jamais une couleur seule.**
- **UX-DR11 — `meeting-recap`.** `surface-raised`, filet, `rounded/md`. Non interactif mais
  **porte un rôle réel et un nom accessible**. Point de vérité du parcours : persiste, **mute sur
  place**, gagne la ligne du **jour bloqué** puis la perd, et porte les dates de changement de
  statut. Unique par rencontre — jamais un second bloc divergent.
- **UX-DR12 — `profile-recap`.** **Jeton pour jeton identique à `meeting-recap`.** Sport, jours,
  niveau. **Posé au seul refus du niveau**, portant *« Niveau : je ne sais pas encore »* en
  `unknown-value` **suivi de la phrase qui dit ce que ce trou empêche**. Mute sur place.
- **UX-DR13 — `auth-block`.** *(E4)* Coque `surface-raised` + filet, motif écrit **au-dessus et
  hors du bloc, en prose de message**. Deux `button-quiet` de rang égal, Google et Microsoft.
- **UX-DR14 — `agenda-choice`.** *(E8)* Même anatomie. Google et Outlook au même rang, aucune
  mise en avant. **Le consentement d'écriture est un troisième temps**, distinct du choix.
- **UX-DR15 — `level-choice`.** Trois `button-quiet` **empilés en colonne** — jamais alignés,
  l'œil y lirait une échelle dont le centre est le défaut. Chacun porte **le mot et une ligne de
  fait** générique. Motif en prose au-dessus et hors du bloc. **Un seul tour, jamais deux.**
  **N'apparaît jamais pendant ni après une recherche.**
- **UX-DR16 — `sport-replace`.** *(E4)* Même coque, et **le seul bloc qui contient une zone de
  lecture seule** : rappel de ce qui sera perdu — sport, niveau, jours — séparé des deux boutons
  par un filet. Deux choix de rang égal, **aucun `button-primary`** : le produit ne pousse vers
  aucune des deux issues.
- **UX-DR17 — `candidate-group-label`.** Une ligne en `meta` / `ink-secondary` au-dessus des
  cartes, portant le niveau **une seule fois**. Une salve supplémentaire pose **son propre**
  intitulé.
- **UX-DR18 — `playability-callout`.** *(E7 pour la donnée, E3 pour le rendu)* Fond
  `status-danger-quiet`, **filet gauche de 3 px** en `status-danger` — seul composant à filet
  latéral de l'interface — texte en encre primaire, **un mot en tête**. Contre-proposition portée
  par un `button-quiet` réel, cliquable ou dicible. Elle **fixe l'heure et ne retient rien**,
  **annonce ce qu'elle vient de changer** et **laisse une trace visible** dans le fil.
- **UX-DR19 — `composer`.** `<textarea>`, jamais un `<input>` : la croissance sur quatre lignes
  et Maj+Entrée l'exigent. `surface-overlay`, filet, `rounded/lg`, ancré en bas. **Toujours
  active, même pendant que le bot travaille.** Focalisée au chargement et re-focalisée après
  chaque envoi. **Entrée envoie, Maj+Entrée passe à la ligne.** **Aucune règle `outline: none`,
  sous aucun prétexte.** Le brouillon est conservé à travers une redirection OAuth quand c'est
  possible, et **s'il est perdu, le bot le dit**.
- **UX-DR20 — `new-message-pill`, `button-primary`, `button-quiet`, `unknown-value`,
  `service-notice`, message non envoyé, `focus-indicator`.** La pastille « nouveau message »
  apparaît quand le fil change alors que la personne a remonté. **Un seul `button-primary` dans
  tout le produit** — *« Retenir ce créneau »* — le bouton d'envoi étant hors du compte. La valeur
  inconnue est en `meta-unknown`, **à la même lisibilité que tout autre texte**. `service-notice`
  porte le hors-ligne et l'indisponibilité du bot, **sans couleur de statut**. Un message non
  envoyé garde sa bulle, porte le mot « Non envoyé » et un bouton « Renvoyer », **jamais effacé
  en silence**. L'indicateur de focus est un `outline` opaque de 3 px décalé de 2 px, **identique
  partout, jamais supprimé**.
- **UX-DR21 — Bloc de récapitulatif d'alerte.** *(E9)* Distinct de `meeting-recap`, qui n'est pas
  interactif : celui-ci porte **un bouton d'annulation qui reste actif aussi longtemps que
  l'alerte vit** — seule exception du produit à l'inertie du passé.
- **UX-DR22 — `acceptance-page`.** *(E6)* Seule surface hors du fil. Mêmes jetons, une colonne
  bornée à `thread-max-width`, **sans en-tête, sans navigation, sans pied de page**. Deux
  `button-quiet` de rang égal, **aucun `button-primary`**. **Sept états terminaux** : invitation
  ouverte, acceptée, refusée, lien déjà utilisé, lien expiré, profil désinscrit, **rencontre
  abandonnée** — plus la variante de **conflit de créneaux** où l'acceptation échoue. **Jamais une
  erreur nue.** Le cadre réel de cette surface est le téléphone.

**Comportement et voix**

- **UX-DR23 — Cliquer ou écrire, toujours les deux.** Toute carte cliquable a un équivalent en
  langage naturel ; aucun choix n'existe uniquement en bouton. **Aucun raccourci à touche de
  caractère unique**, aucun raccourci actif hors focus (WCAG 2.1.4). Survol réservé aux cartes
  actives, aucune information portée uniquement par le survol. **Défilement automatique
  conditionnel.**
- **UX-DR24 — Le passé est inerte, et « tour résolu » a une définition.** Un tour est **une
  question**, pas un message ; une salve supplémentaire **l'agrandit sans le résoudre** ; un tour
  sans question ne se résout jamais. Dès qu'un tour est résolu, **tout** ce qu'il contenait de
  cliquable devient inerte : cartes, contre-proposition, boutons de connexion, choix d'agenda,
  choix de niveau, remplacement de sport. Chacun reste lisible, perd son rôle, sort de l'ordre de
  tabulation et **porte son sort en toutes lettres**. Trois exceptions, les seules :
  `meeting-recap`, `profile-recap`, et le bouton d'annulation du bloc d'alerte.
- **UX-DR25 — Voix et ton.** Vouvoiement, registre de **secrétariat compétent**. Six règles dans
  l'ordre : la mauvaise nouvelle en premier sans coussin ; le bot ne se félicite jamais ; chaque
  demande énonce son motif au moment où elle est faite ; tout message d'échec dit **ce qui n'est
  pas perdu** ; aucun message d'échec ne s'ouvre sur une excuse ; **l'inconnu se conjugue** — « je
  ne sais pas encore », jamais « non déterminé ». Interdits absolus : « adversaire » hors sport de
  duel, « réservé » / « réservation », « confirmé » sur une rencontre qui ne l'est pas, « pas
  encore » et tout adverbe qui promet une réponse. Les formulations arrêtées et les textes
  sortants de EXPERIENCE.md sont contractuels.
- **UX-DR26 — La grammaire de l'honnêteté.** Quatre mécanismes : le trou a un style qui n'est pas
  un effacement ; les étapes narrées sont une **trace vérifiable** ; le statut est un mot ; **le
  produit écrit les conséquences qu'il s'inflige au moment où il se les inflige** — jour bloqué,
  jour gagné, sport remplacé, aucune ne peut se produire en silence. Règle dérivée : **aucun
  composant ne rend un champ obligatoire à l'affichage**, et toute donnée affichable a un état
  « inconnu » rendu.
- **UX-DR27 — Demande de liste, de carte ou de filtre.** Traitée à l'inverse d'une demande hors
  périmètre : le bot **ne répond pas qu'il ne sait pas faire**, il donne ce qu'il peut sous une
  forme plus dense et **note la demande**. C'est le symptôme que SM-5 surveille.

**Plancher d'accessibilité** — contractuel : chaque règle double un parti visuel d'un équivalent
non visuel.

- **UX-DR28 — Le fil visible n'est pas une région live.** C'est une `<section>` nommée — un
  `region` réel, jamais un `<div>` étiqueté — **sans aucun attribut live**. Ce qu'on voit et ce
  qu'on entend sont produits par deux chemins distincts.
- **UX-DR29 — Trois régions live, hors du flux visuel, présentes et vides dès le premier octet.**
  **Satellite de tour** `role="log" aria-relevant="additions" aria-atomic="false"` — le texte
  complet d'un tour du bot **en un seul ajout**, ni les étapes ni les tours de la personne.
  **Satellite d'étapes** `role="status" aria-atomic="true"` — **une phrase à la fois**.
  **Région de statut** `role="status"` — **toute mutation d'un bloc persistant**, en phrase
  complète et autonome. **Jamais démontées ni remontées pendant la vie de la page.**
- **UX-DR30 — L'ordre écrire-puis-vider est contractuel.** Le texte du tour est **ajouté** dans
  un satellite vide, puis le satellite est **vidé** après un délai fixe — jamais l'inverse, jamais
  dans la même tâche. Vider puis écrire serait un **remplacement**, et le mode de défaillance
  serait le **silence, tour après tour, invisible à toute recette visuelle**. Cet échec doit être
  détectable : les trois satellites sont le seul chemin sonore du produit.
- **UX-DR31 — Aucune annonce n'est mise en attente.** Aucune minuterie ne s'interpose entre
  l'événement et l'écriture dans un satellite. Aucun état ne peut être retenu — ni échec d'envoi,
  ni perte de réseau, ni indisponibilité du bot.
- **UX-DR32 — Structure et attribution.** **Étiquette de locuteur visuellement masquée** sur
  chaque tour, sans quoi le geste « pas de bulle » rend la conversation muette. Un seul `main`,
  `form` pour la saisie, satellites **hors des repères**. `<h1>` **visuellement masqué et
  permanent** — l'accroche `display` disparaît au premier message. `lang="fr"`, `<title>` stable.
  Les cartes sont de **vrais `<button>`** dont le **nom accessible contient le texte visible mot
  pour mot** (WCAG 2.5.3). Bouton d'envoi `<button>` nommé, `disabled` **natif** et jamais
  `aria-disabled`. Erreurs identifiées **en texte** (WCAG 3.3.1). **`aria-label` prohibé sur
  `role=generic`.**
- **UX-DR33 — Clavier, focus et pointeur.** Anneau de focus toujours visible, en `outline`
  opaque. Le composer ancré **ne recouvre jamais l'élément focalisé** (WCAG 2.4.11), la pastille
  « nouveau message » entrant dans le calcul de la zone exclue. Ordre de tabulation = ordre de
  lecture ; focus au composer après envoi ; **à l'arrivée d'un tour le focus ne bouge pas**. **Le
  focus n'est jamais laissé dans le vide** — élément devenu inerte **ou retiré du DOM**. Retour
  d'OAuth : focus sur le message de reprise, `tabindex="-1"`, **et cette règle prime sur la
  focalisation automatique du champ**. Cibles **24 × 24 px** plancher normatif, **48 px imposé**
  hors cible en ligne dans du texte.
- **UX-DR34 — Perception et préférences.** **Aucune information portée par la couleur seule** —
  statut, jouabilité, jour bloqué, sort d'une carte résolue portent tous leur mot.
  `prefers-reduced-motion` : plus de fondu, plus de pulsation, marqueur textuel visible.
  `prefers-contrast: less` : `ink-primary-soft` pour la prose longue — **seul assouplissement du
  produit**. Zoom **200 %**, redistribution **400 %**, espacement forcé WCAG 1.4.12 : rien n'est
  perdu ni chevauché.
- **UX-DR35 — Charge cognitive.** « On le redit au bot » a un coût, compensé par le fil qui
  n'est jamais purgé pour un utilisateur inscrit. **Le bot restitue ce qu'il a retenu avant de
  relancer** (WCAG 3.3.7, *Saisie redondante*). Le mot **« vivier »** est glosé à sa première
  occurrence, sans être remplacé par un synonyme.
- **UX-DR36 — Responsive.** Un seul point de rupture, plancher **320 px**, **parité fonctionnelle
  stricte** — aucune capacité d'un côté et pas de l'autre. Cartes sur une ligne au-delà du point
  de rupture, empilées en deçà ; une ou deux cartes gardent la largeur d'une carte et ne
  s'étirent pas. Pas de survol au tactile : l'**état pressé le remplace, et il porte un filet**.
  **Clavier virtuel** : la saisie reste visible, le fil se réduit, la dernière ligne reste
  lisible.

### FR Coverage Map

C'est cette carte qui prouve qu'aucune exigence du PRD v5 n'est tombée entre les lots. Elle
couvre les **neuf** épiques, E1 comprise : un lot déjà livré doit rendre des comptes au même
titre que les autres, sans quoi la couverture d'E2 et d'E5 repose sur un socle que rien ne
relie aux exigences.

Chaque exigence porte **un lot propriétaire** — celui qui la rend vraie et dont le « Fait
quand » la vérifie — et, le cas échéant, les lots qui en portent une **part nommée**. Une part
sans lot propriétaire serait une exigence orpheline ; un propriétaire sans parts serait une
exigence que le découpage ne traverse pas.

| Exigence | Propriétaire | Parts portées par d'autres lots |
|---|---|---|
| **FR-1** — dialoguer sans authentification | **E3** — la page d'entrée présente le fil utilisable, sans écran d'authentification préalable | **E2** : c'est elle qui rend les propositions de partenaires nommés qu'un visiteur sans compte doit obtenir |
| **FR-2** — extraire une demande, niveau non interprété | **E3** — extraction, réclamation d'un élément à la fois, moment « niveau », hors zone, refus du niveau | **E1** : clé de sport normalisée, synonymes à l'écriture, fondation d'un libellé inconnu — les 11 libellés produisent 11 clés. **E5** : la précondition qui empêche de lancer une demande complète pendant qu'une *recherche active* occupe la place |
| **FR-3** — enregistrer l'utilisateur dans le vivier | **E4** — entrée au vivier à la création du compte, remplacement de sport en écriture atomique et annoncée | **E1** : modèle mono-sport, population portée, niveau nullable, compte optionnel. **E2** : le nouveau profil ressort effectivement d'une recherche, et un *niveau inconnu* n'en ressort jamais |
| **FR-4** — demander un compte au moment de la mise en relation | **E4** — les deux parcours OAuth, première portée seulement, motif énoncé | **E5** : *retenir un créneau* est le geste qui la déclenche. **E9** : accepter une alerte différée la déclenche également |
| **FR-5** — recherche exacte | **E2** — égalité stricte de niveau, exclusion du niveau inconnu, exclusion de soi-même | **E1** : le schéma et l'*ordre du vivier* sur lesquels la jointure porte. **E5** : la dérivation du *jour bloqué* qui retire un profil pour ce jour-là seulement. **E6** : la *sortie définitive du vivier* que la recherche doit filtrer |
| **FR-6** — élargir sur le jour | **E2** — élargissement sur le jour et lui seul, plafond de trois candidats, tri par délai d'attente croissant, ordre du vivier à égalité | **E1** : l'ordre du vivier porté par l'identifiant UUIDv7 monotone. **E3** : les cartes, l'intitulé de groupe et « montrer les autres » |
| **FR-7** | *retirée* | — |
| **FR-8** — annoncer l'absence de résultat sans broder | **E3** — la réponse qui nomme le sport et le jour tentés, dit ce qui a été élargi, conclut qu'il n'y a personne à ce niveau | **E2** : le résultat vide du domaine, et les deux paires Pilates qui le produisent. **E9** : l'enchaînement sur la proposition d'alerte différée |
| **FR-9** — alerte différée | **E9** — déclenchement à l'écriture d'un profil, correspondance exacte, alertes multiples, annulation, expiration à 60 jours | **E4** : le compte exigé et l'adresse qui devient le canal. **E6** : la boîte d'envoi qui porte réellement le courriel |
| **FR-10** — jouabilité | **E7** — les trois seuils, la projection de `equip_nature`, les deux horizons, la contre-proposition d'heure | **E3** : l'encadré rendu dans le fil, la contre-proposition qui fixe l'heure sans rien retenir, et la trace qu'elle laisse |
| **FR-11** — proposer un lieu à Lyon | **E7** — Data ES, filtrage lyonnais, nature de l'équipement, absence de donnée dite plutôt qu'inventée | **E1** : la colonne de secteur posée et laissée nulle. **E4** : l'écriture du secteur au profil de l'utilisateur inscrit, pour réemploi |
| **FR-12** — écrire la rencontre dans l'agenda | **E8** — second consentement OAuth, choix Google ou Outlook, écriture après confirmation explicite, aucun numéro dans l'événement | **E4** : la première portée OAuth, dont celle-ci est l'incrément. **E5** : les arêtes de la table de transitions qui commandent la mise à jour de l'événement |
| **FR-13** — cinq statuts, une seule recherche active | **E5** — les cinq statuts, la table de transitions et ses effets, la précondition et son asymétrie, la transaction unique | **E3** : les pastilles, la phrase qui nomme le sport, le partenaire et le jour occupés, et la sortie donnée dans la même phrase. **E6** : les arêtes franchies depuis la page d'acceptation, conflit de créneaux compris. **E8** : la mise à jour de l'événement à chaque changement de statut |
| **FR-14** — prévenir le partenaire, lien d'acceptation | **E6** — filtre de destinataire, boîte d'envoi et page locale, jeton opaque, sept états terminaux, sortie définitive du vivier | **E1** : la provenance du numéro portée dans le modèle, que le filtre lit au lieu du préfixe (AD-11). **E5** : la transaction de *retenir un créneau*, qui crée la rencontre, le jeton et l'inscription à la boîte d'envoi |
| **FR-15** | *retirée* | — |
| **FR-16** — cycle de vie d'un profil au vivier | **E5** — dérivation du jour bloqué et sa symétrie, libération par *déclinée*, *expirée* et *abandonnée*, conservation du jour accepté | **E1** : l'absence assumée de tout champ `bloque`, et la colonne de sortie du vivier posée sans être lue. **E2** : la recherche qui lit la dérivation et exclut un profil sorti du vivier. **E6** : la sortie définitive exercée depuis le message |
| **CAP-15** — reprendre une conversation | **E3** — fil append-only, cookie signé de 30 jours, récapitulatif de reprise en prose qui ne re-rend aucun bloc | **E4** : l'attachement de la conversation en cours au compte, sans rejeu ni duplication (AD-21). **E5** : la garantie d'au plus une rencontre à récapituler |
| **CAP-16** — rendre le travail du bot visible | **E3** — les quatre événements du flux, l'émission des étapes par la couche d'outil, le signe de vie avant le premier jeton | **E7** : les trois adaptateurs tiers qui émettent leurs étapes et nomment leur échec. **E8** : l'adaptateur d'agenda, au même titre. **E6** : la boîte d'envoi, **cinquième port émetteur** — son filtre échoue bruyamment, et la personne doit le savoir *(arbitrage B)* |

**Exigences non fonctionnelles et UX — où elles atterrissent.**

| Exigence | Lots |
|---|---|
| **NFR-1** — latence 2 s / 20 s | **E3** (propriétaire, via CAP-16) ; **E7** et **E8** tiennent leur part en n'ajoutant pas de saut LLM |
| **NFR-2** — robustesse des services externes | **E7** (météo, air, lieux) et **E8** (agenda) sont les seuls lots à en avoir ; le `Resultat[T]` et l'étape échouée sont posés par **E3** |
| **NFR-3** — reprise de conversation | **E3**, avec la part d'**E4** (attachement au compte) |
| **NFR-4** — surface responsive, plancher 320 px | **E3** pour le fil, **E6** pour la page d'acceptation — les deux seules surfaces du produit |
| **NFR-5** — panne du LLM | **E3** |
| **NFR-6** — enveloppe technique locale | **E1** (posée), tenue par tous |
| **UX-DR1 → UX-DR12, UX-DR15, UX-DR17, UX-DR19, UX-DR20, UX-DR23 → UX-DR36** | **E3** |
| **UX-DR13, UX-DR16** — `auth-block`, `sport-replace` | **E4** |
| **UX-DR14** — `agenda-choice` | **E8** |
| **UX-DR18** — `playability-callout` | **E7** pour la donnée, **E3** pour le rendu |
| **UX-DR21** — bloc de récapitulatif d'alerte | **E9** |
| **UX-DR22** — `acceptance-page` et ses sept états | **E6** |
| **DW-1** — index sur `profil.sport_id` | **E2** |
| **DW-2** — lecture du fichier `.env` | **E3** |

### Ce que la carte a fait remonter, et comment c'est tranché

La carte a révélé un trou et une ambiguïté. Les deux sont arbitrés ci-dessous ; **ni l'un ni
l'autre ne modifie la partition**.

**A — Trois lots déclarent des courriels, aucun n'en vérifiait un.** E5 attache un courriel à
quatre de ses six arêtes, E9 en émet deux — notification et expiration — et E6 construit la
boîte d'envoi. Or les « Fait quand » de ces trois lots portent respectivement sur la
concurrence, sur le déclenchement d'alerte et sur la page d'acceptation : **aucun ne teste un
envoi**. Chaque lot pouvait donc être déclaré terminé sans qu'un seul courriel soit jamais
parti.

*Arbitrage.* `AD-12` a déjà tranché que **la boîte d'envoi est le transport** — il n'y a ni
fournisseur SMS ni serveur de courriel dans l'enveloppe. « Le courriel est parti » signifie
donc « une ligne existe dans la boîte d'envoi, avec son destinataire, son corps rendu et son
sort ». Le partage qui en découle :

- **E5 et E9 gardent l'assertion**, parce que l'effet appartient à la transition (`AD-9`).
  Elles assertent **contre le port**, au moyen d'un double de test implémentant `PortEnvois` —
  donc sans dépendre d'E6.
- **`PortEnvois` est déclaré dans la première story d'E5**, dans `domaine/ports.py`. C'est la
  condition pour que l'arête E6 → E9 reste inutile : si le protocole naissait dans E6, les deux
  lots amont n'auraient rien contre quoi asserter.
- **E6 porte une story de plus, et une seule** : l'adaptateur réel honore le même contrat que
  le double.

**B — `AD-3` et le SPEC ne désignent pas la même liste de ports.** `AD-3` écrit « chaque **port
secondaire** émet un événement `etape` » ; l'*intent* de CAP-16 écrit « chaque **appel
externe** ». La persistance et la boîte d'envoi sont des ports secondaires **locaux** : selon
la phrase qu'on lit, le fil affiche ou n'affiche pas une étape pour une écriture en base.

*Arbitrage — par principe, pas par liste de répertoires :*

> **Un port émet une étape s'il peut échouer d'une façon que la personne doit connaître.**

Ce qui donne **cinq ports émetteurs** et non quatre :

| Port | Émet une étape | Pourquoi |
|---|---|---|
| `meteo`, `air`, `lieux`, `agenda` | **oui** | leur échec change ce que le bot a le droit de dire |
| `envois` | **oui** | le filtre de destinataire **échoue bruyamment** par conception (CAP-13) ; ne pas avoir pu prévenir le partenaire est une conséquence que le produit s'inflige, donc qu'il écrit (UX-DR26) |
| `persistance` | **non** | son échec n'est pas un fait mais un **défaut** — « une exception qui remonte au fil est un défaut », § *Forme des erreurs* |

**Correction à remonter à la spine :** la phrase d'`AD-3` doit dire *« chaque port qui peut
échouer d'une façon que la personne doit connaître »*, et non *« chaque port secondaire »*.
Elle est appliquée ici et signalée en amont plutôt que contournée en silence dans une story.

**C — Ce que les « Fait quand » ne couvrent pas, et qui doit donc devenir une story.** Le
balayage des neuf critères a montré qu'ils sont étroits par construction — ils démontrent, ils
ne closent pas *(voir l'Overview)*. Trois familles y échappent systématiquement, et l'écriture
des stories doit les rattraper nommément.

1. **Les règles d'ordre de FR-6 ne sont mesurées par rien.** SM-3 mesure le **taux de
   récupération** — 85 % des 127 combinaisons vides. Une recherche qui renverrait *tous* les
   candidats, non triés, passerait SM-3 à 89 %. Le plafond de trois, le tri par délai d'attente
   croissant et l'ordre du vivier à égalité sont invisibles à ce critère — et le PRD dit
   lui-même que ces règles ne mordent presque jamais sur les données actuelles, donc rien ne les
   révélera par accident. **E2 doit porter une story dédiée à l'ordre.**
2. **Trois règles de production n'ont aucun critère de lot** : le **remplacement de sport**
   *(E4, « le geste le plus destructeur du produit »)*, le **filtre de destinataire**
   *(E6, cœur d'`AD-11` et `AD-12`)*, et l'**expiration** *(E5, « le seul mécanisme qui rend au
   vivier les jours immobilisés »)*. Chacune prend sa story.
3. **Les interdits ne se testent jamais par un parcours nominal.** Le produit en vit — *jamais
   demander le niveau pendant la recherche*, *ne pas demander de compte avant le geste qui
   engage*, *accepter une heure ne retient rien*, *aucun numéro de téléphone nulle part*. Aucun
   des neuf « Fait quand » n'en attrape un seul. **Chaque interdit porte sa propre story
   négative.**

**D — Deux confirmations, sans conséquence.** FR-1 n'est pleinement vraie qu'avec E2 —
« un visiteur sans compte obtient des propositions de partenaires nommés » n'est pas rendu par
le fil seul — et l'ordre E1 → E2 → E3 la satisfait d'office. Et **E1 couvre sept parts de
manière rétroactive** : son critère vérifie par exemple que la colonne de provenance *existe*,
pas qu'un filtre la lise. C'est E6 qui apportera cette seconde assertion.

**Deux corrections remontées en amont le 2026-08-31**, appliquées aux documents sources plutôt
que contournées en silence dans une story. Chacune vivait à deux endroits :

| Document | Ancienne formulation | Formulation corrigée |
|---|---|---|
| `ARCHITECTURE-SPINE.md`, `AD-3` | « chaque **port secondaire** émet un événement `etape` » | « chaque port qui peut **échouer d'une façon que la personne doit connaître** », suivi des cinq ports concernés |
| `SPEC.md` et `criteres-acceptation.md`, CAP-16 | « chaque **appel externe** » / « chaque **port secondaire** » | même critère de principe, aligné sur `AD-3` |
| `DECOUPAGE.md`, E7, *Fait quand* | « un lieu **couvert** ne déclenche aucune mention météo » | « un lieu **pleinement intérieur** » — la formulation d'origine était l'inverse d'`AD-14` |

Les quatre fichiers portent une note datée expliquant ce qui a changé et pourquoi ; les
`updated:` de la spine et du découpage sont bumpés au 2026-08-31.

## Epic List

Neuf épiques, dans l'ordre arbitré par DECOUPAGE.md. Les cinq premières ne contiennent
**aucun appel au LLM** : elles sont testables au sens strict, contre les chiffres que le PRD
compte lui-même. Le critère d'acceptation de chaque épique est le **« Fait quand »** du lot,
repris tel quel.

### Epic 1 : Socle du vivier

**Statut : livré** — `documentation/implementation-artifacts/spec-e1-socle-du-vivier.md`,
commit `889ad43`.

Le vivier existe : les entités, le schéma, la clé de sport normalisée et sa table de
synonymes, la distinction des deux populations, la provenance des numéros, et les 86 profils
d'amorçage en base. Rien ne peut être construit avant lui — ni la recherche d'E2, ni le fil
d'E3.

**Gouverné par :** AD-1, AD-5, AD-11, AD-16
**Touche :** `domaine/vivier`, `domaine/sports`, `adaptateurs/secondaires/persistance`, `amorcage/`
**Exigences couvertes :** FR-2 *(part)*, FR-3 *(part)*, FR-5 *(part)*, FR-6 *(part)*, FR-11 *(part)*, FR-14 *(part)*, FR-16 *(part)*, NFR-6

**Fait quand :** relancer l'application ne duplique rien, et les 11 sports du fichier
produisent 11 clés — pas 12.

### Epic 2 : Recherche

Le moteur d'appariement complet, sans une ligne de LLM ni de web. À son terme, **SM-3 devient
mesurable directement** : les 231 combinaisons se parcourent en boucle, les 127 vides se
comptent, et le plancher de 85 % que le PRD fixe se vérifie. C'est le seul critère de réussite
du produit qui soit chiffrable par un test, et il est atteignable en premier.

**Gouverné par :** AD-1, AD-5, AD-6
**Touche :** `domaine/recherche`
**Exigences couvertes :** FR-5, FR-6, FR-3 *(part)*, FR-8 *(part)*, FR-16 *(part)*, DW-1

**Fait quand :** SM-3 se mesure et passe. Les deux paires Pilates ressortent vides, et le
scénario « Tennis, mardi, débutant » renvoie Emma Leroy.

### Epic 3 : Le fil

Le seul lot vraiment nouveau. Tout le reste est du logiciel ordinaire ; l'agent, le flux SSE
et le contrat d'événements sont l'endroit où le projet apprend quelque chose. Le placer après
E1–E2 fait qu'il arrive sur un domaine déjà juste, donc qu'un comportement étrange s'impute
au câblage et non aux règles.

**Gouverné par :** AD-2, AD-3, AD-4, AD-17, AD-20, AD-21
**Touche :** `adaptateurs/primaires/web`, `adaptateurs/primaires/agent`
**Exigences couvertes :** FR-1, FR-2, FR-8, CAP-15, CAP-16, NFR-1, NFR-3, NFR-4 *(le fil)*, NFR-5, FR-6 *(part)*, FR-10 *(part)*, FR-13 *(part)*, DW-2, et l'essentiel des UX-DR

**Fait quand :** une recherche complète se déroule dans le fil, le signe de vie part en moins
de deux secondes, et couper le réseau au milieu d'un tour produit un message qui nomme la
panne et dit ce qui n'est pas perdu.

> **Une story de ce lot n'a pas d'autre objet que le chemin sonore.** `UX-DR30` décrit son
> propre mode de panne — **le silence, tour après tour, invisible à toute recette visuelle** :
> le fil s'affiche parfaitement pendant que les trois satellites sont morts. Aucune story
> fonctionnelle ne l'attrapera. Le poids d'E3 n'est pas un problème de découpage ; l'absence
> d'assertion sur ce tiers-là en serait un.

### Epic 4 : Identité et compte

Le compte arrive au moment où le bot va exposer l'utilisateur à quelqu'un d'autre, et pas
avant. C'est aussi le lot où un utilisateur entre au vivier et devient trouvable.

**Gouverné par :** AD-18, AD-21
**Touche :** `adaptateurs/primaires/web`, `domaine/vivier`
**Exigences couvertes :** FR-3, FR-4, CAP-15 *(part)*, FR-11 *(part)*, FR-12 *(part)*, UX-DR13, UX-DR16

**Fait quand :** se connecter en milieu de fil ne perd rien et n'ouvre pas un second fil.

### Epic 5 : Cycle de vie des rencontres

Les cinq statuts et ce qu'ils autorisent le bot à dire. C'est ici que la machine à états, ses
effets par arête et les deux dérivations — jour bloqué, recherche active — deviennent vraies.

**Gouverné par :** AD-6, AD-7, AD-8, AD-9, AD-15
**Touche :** `domaine/rencontre`, `adaptateurs/primaires/horloge`
**Exigences couvertes :** FR-13, FR-16, FR-2 *(part)*, FR-4 *(part)*, FR-5 *(part)*, FR-12 *(part)*, FR-14 *(part)*, CAP-15 *(part)*

**Fait quand :** deux onglets ne produisent pas deux rencontres ; un abandon libère le jour
des **deux** profils ; être sollicité par un autre demandeur n'empêche pas de chercher.

> **La première story de ce lot déclare `PortEnvois` dans `domaine/ports.py`** — arbitrage A.
> Sans ce protocole posé ici, E5 et E9 n'ont rien contre quoi asserter leurs courriels et
> l'arête E6 → E9 redevient nécessaire.

### Epic 6 : Partenaire et envois

Le seul geste du produit qui engage quelqu'un d'autre trouve son destinataire. C'est aussi la
seule surface du produit qui vit hors du fil, et le seul endroit où un partenaire peut
apprendre un abandon.

**Gouverné par :** AD-8, AD-10, AD-11, AD-12
**Touche :** `domaine/envoi`, `adaptateurs/secondaires/envois`, `adaptateurs/primaires/web`
**Exigences couvertes :** FR-14, FR-5 *(part)*, FR-9 *(part)*, FR-13 *(part)*, FR-16 *(part)*, NFR-4 *(la page d'acceptation)*, UX-DR22

**Fait quand :** le scénario de démonstration de l'addendum s'exécute — le lien ouvert dans un
second onglet, rechargé après un abandon, affiche l'état *rencontre abandonnée* et propose la
sortie du vivier.

> **Une story de plus, et une seule, au titre de l'arbitrage A** : l'adaptateur réel de la
> boîte d'envoi honore le contrat `PortEnvois` que les doubles d'E5 et d'E9 ont utilisé. C'est
> le seul endroit du produit où le vrai et le faux se rencontrent. Ce lot apporte aussi la
> seconde assertion que la part d'E1 n'avait pas : le filtre **lit** réellement la provenance
> enregistrée.

### Epic 7 : Lieux et jouabilité

Le seul lot substantiel qui se détache du chemin critique : **il ne dépend que d'E1** et
s'écrit sans le fil, sans compte et sans rencontre. Utile si l'inscription à l'API ATMO
traîne, puisqu'elle est la seule démarche du projet.

**Gouverné par :** AD-13, AD-14, AD-19
**Touche :** `domaine/jouabilite`, `adaptateurs/secondaires/{lieux,meteo,air}`
**Exigences couvertes :** FR-10, FR-11, CAP-16 *(part)*, NFR-2, UX-DR18 *(la donnée)*

**Fait quand :** un lieu **pleinement intérieur** ne déclenche aucune mention météo ; un créneau
à cinq jours rend les deux premiers seuils et **nomme** celui qu'il n'a pas pu établir.

> **Correction, à remonter en amont.** DECOUPAGE.md écrit ici *« un lieu **couvert** »*. Lu avec
> le vocabulaire du produit, ce critère dit l'**inverse** d'`AD-14` : « couvert » ne suffit
> précisément pas à désactiver la jouabilité, et Data ES retourne littéralement la valeur
> `Extérieur couvert`. Un constructeur qui ne lirait que ce critère implémenterait l'inversion
> que l'invariant a été écrit pour empêcher, et son test passerait. Le mot est corrigé ici en
> *pleinement intérieur*.

### Epic 8 : Agenda

La rencontre sort du produit et entre dans l'agenda de l'utilisateur — le sien seulement, et
après un second consentement demandé au moment où il sert.

**Gouverné par :** AD-9, AD-13, AD-18
**Touche :** `adaptateurs/secondaires/agenda`
**Exigences couvertes :** FR-12, FR-13 *(part)*, CAP-16 *(part)*, NFR-2 *(part)*, UX-DR14

**Fait quand :** un abandon met l'événement à jour **sans** envoyer de courriel.

### Epic 9 : Alertes différées

Ce qui reste à faire quand le vivier n'a personne : enregistrer la demande, et prévenir quand
quelqu'un arrive. Le chemin rare — 14 combinaisons sur 231 — et celui où le bot est le plus
tenté de broder.

**Gouverné par :** AD-5, AD-12, AD-15
**Touche :** `domaine/alerte`
**Exigences couvertes :** FR-9, FR-4 *(part)*, FR-8 *(part)*, UX-DR21

**Fait quand :** un utilisateur existant qui change de sport déclenche l'alerte de quelqu'un
d'autre, au même titre qu'une inscription.

> Ce « Fait quand » teste le **déclenchement**, pas la **remise** — c'est ce qui permet à E9 de
> se clore sans E6. Ses deux courriels, notification et expiration à 60 jours, s'assertent
> contre `PortEnvois` (arbitrage A).

### Ce qui n'est dans aucune épique

Hors périmètre MVP : le parcours conversationnel côté partenaire (QO-2), la réservation de
terrain, la calibration du niveau, le multi-sport, le signal d'équilibre après rencontre, et
tout ce qui suit le créneau. Hors enveloppe technique : le déploiement, les secrets managés et
un fournisseur SMS réel. Hors épique côté outillage : les cinq reports de `deferred-work.md`
qui ne sont pas DW-1 et DW-2.

---

## Epic 1 : Socle du vivier

Le vivier existe : les entités, le schéma, la clé de sport normalisée et sa table de synonymes,
la distinction des deux populations, la provenance des numéros, et les 86 profils d'amorçage en
base.

**Une seule story.** Ce lot est **livré** (commit `889ad43`) et son contenu vient de la section
*Tasks & Acceptance* de `spec-e1-socle-du-vivier.md`, pas du PRD. Le décomposer a posteriori en
stories qui n'ont jamais été écrites produirait une fiction de traçabilité.

### Story 1.1 : Le vivier existe et se recharge sans se dupliquer

En tant que **bot**,
je veux un vivier peuplé et un vocabulaire de sport stable,
afin de pouvoir chercher quelqu'un sans que le vivier se pulvérise en silence.

**Périmètre livré** — `pyproject.toml` et l'enveloppe uv / Python 3.13 ; `.env.example` et
`.gitignore` ; `domaine/identifiants.py` (UUIDv7 monotone) ; `domaine/sports.py` (`cle_sport` et
la résolution d'un libellé : synonyme, puis sport existant, puis fondation) ; `domaine/vivier.py`
(les quatre énumérations et les quatre types) ; `adaptateurs/secondaires/persistance/{base,modeles,depots}.py` ;
`amorcage/{lecture,chargement}.py` ; `application.py` et `__main__.py` ; la suite `tests/`.

**Exigences :** FR-2, FR-3, FR-5, FR-6, FR-11, FR-14, FR-16 *(parts)* · NFR-6 · AD-1, AD-5, AD-11, AD-16

**Acceptance Criteria :**

**Étant donné** une base vide
**Quand** l'application démarre deux fois de suite
**Alors** le vivier compte **86 profils** aux deux passages
**Et** aucun jour disponible n'est dupliqué.

**Étant donné** les 86 profils chargés
**Quand** on compte les sports
**Alors** il y en a **11**, chacun portant une clé distincte et son libellé d'origine.

**Étant donné** le domaine
**Quand** on inspecte ses imports
**Alors** aucun module de `exaequo/domaine/` n'importe `sqlalchemy`, `fastapi`, `anthropic` ni
`exaequo.adaptateurs`
**Et** la vérification est faite par un test, pas par relecture.

**Étant donné** les profils chargés dans l'ordre du fichier
**Quand** on les trie par identifiant
**Alors** l'ordre du fichier est restitué — c'est l'**ordre du vivier** dont CAP-6 a besoin pour
départager les ex æquo.

> **Statut : done.** Les deux critères que le « Fait quand » d'E1 ne portait pas — l'absence de
> dépendance sortante du domaine et l'ordre du vivier — sont précisément ceux dont E2 dépend.

---

## Epic 2 : Recherche

Le moteur d'appariement complet, sans une ligne de LLM ni de web. À son terme, **SM-3 devient
mesurable** : les 231 combinaisons se parcourent en boucle et le plancher de 85 % se vérifie.

Ce lot écrit `domaine/recherche` et rien d'autre. La dérivation du **jour bloqué** appartient à
E5 : la recherche est donc écrite pour accepter un ensemble de jours indisponibles en paramètre,
afin qu'E5 la branche sans la réécrire.

### Story 2.1 : Chercher des candidats du niveau exact

En tant que **personne qui cherche un partenaire**,
je veux que le bot ne me propose que des profils exactement de mon niveau, dans mon sport, un
jour où je suis disponible,
afin de ne me retrouver ni écrasée, ni à faire du renvoi de balle par politesse.

**Exigences :** FR-5 · AD-5, AD-6 · DW-1

**Acceptance Criteria :**

**Étant donné** le vivier d'amorçage
**Quand** on cherche « Tennis, mardi, débutant »
**Alors** **Emma Leroy** est renvoyée
**Et** aucun candidat d'un autre niveau ne l'est.

**Étant donné** la même demande formulée en **intermédiaire**
**Quand** on cherche
**Alors** **aucun candidat** n'est renvoyé — la recherche exacte rend vide et n'élargit jamais
d'elle-même.

**Étant donné** un profil qui correspond par le sport et le jour mais porte un **niveau inconnu**
**Quand** on cherche
**Alors** il n'est **jamais** renvoyé
**Et** un profil dont la sortie du vivier est valuée ne l'est pas davantage, quel que soit le
statut de ses rencontres passées.

**Étant donné** un utilisateur présent au vivier avec le même sport et le même niveau que sa
propre demande
**Quand** il cherche
**Alors** il n'est jamais renvoyé comme son propre partenaire.

**Étant donné** les libellés « tennis », « Tennis » et «  TENNIS  »
**Quand** on cherche avec chacun d'eux
**Alors** la comparaison porte sur la **clé de sport normalisée** et les trois demandes rendent
le même ensemble
**Et** la table de synonymes n'est **jamais** consultée à la lecture (AD-5).

**Étant donné** que « chercher les profils d'un sport » est l'accès central de ce lot
**Quand** la requête est écrite
**Alors** le report **DW-1** est clos explicitement : un index sur `profil.sport_id` est posé, ou
son absence est justifiée par une mesure sur les 86 profils
**Et** `deferred-work.md` est mis à jour dans les deux cas.

### Story 2.2 : Élargir sur le jour, et sur lui seul

En tant que **personne dont le jour voulu ne donne rien**,
je veux que le bot cherche les autres jours en gardant mon niveau,
afin d'obtenir quand même quelqu'un plutôt qu'un refus.

**Exigences :** FR-6 · AD-1

**Acceptance Criteria :**

**Étant donné** une recherche exacte qui n'a rien rendu
**Quand** l'élargissement s'applique
**Alors** le jour est la **seule** contrainte relâchée
**Et** le sport et le niveau sont conservés à l'identique.

**Étant donné** « Tennis, mardi, intermédiaire » sur le vivier d'amorçage
**Quand** l'élargissement s'applique
**Alors** **Anna, Iris et Tessa** sont rendues, chacune avec ses jours disponibles.

**Étant donné** un élargissement qui a produit des candidats
**Quand** le résultat est rendu
**Alors** il porte l'information que **le jour demandé n'était pas disponible** — comme donnée du
résultat, la prose appartenant à E3.

**Étant donné** une recherche exacte qui a rendu au moins un candidat
**Quand** on l'exécute
**Alors** l'élargissement n'est **pas** tenté.

### Story 2.3 : Ordonner et plafonner les candidats

En tant que **personne à qui on propose des gens**,
je veux les voir dans un ordre stable, le plus tôt disponible d'abord,
afin de pouvoir choisir sans que la liste change entre deux fois où je pose la même question.

> Story exigée par la contrainte d'écriture **C1** : **SM-3 ne mesure aucune de ces règles**. Une
> recherche qui renverrait tous les candidats, non triés, passerait SM-3 à 89 %.

**Exigences :** FR-6 · CAP-6 · contrainte d'écriture C1

**Acceptance Criteria :**

**Étant donné** un candidat et un jour demandé
**Quand** son délai d'attente est calculé
**Alors** il compte le nombre de jours **vers l'avant** depuis le jour demandé jusqu'à sa
prochaine disponibilité — depuis mardi : mercredi = 1, jeudi = 2, … lundi = 6.

**Étant donné** plus de trois candidats correspondants
**Quand** le résultat est rendu
**Alors** il en porte **trois au maximum**
**Et** il porte le nombre de candidats restants, pour que le bot puisse dire combien il y en a
d'autres et proposer de les montrer.

**Étant donné** plusieurs candidats à **délai d'attente égal** — le cas le plus fréquent sur les
données d'amorçage
**Quand** ils sont ordonnés
**Alors** l'**ordre du vivier** les départage, c'est-à-dire l'ordre croissant d'identifiant.

**Étant donné** la même demande exécutée deux fois de suite
**Quand** on compare les deux résultats
**Alors** ils portent **le même trio dans le même ordre**.

### Story 2.4 : Mesurer SM-3 sur les 231 combinaisons

En tant que **constructeur**,
je veux un test qui parcourt la grille entière et rend le taux de récupération,
afin de savoir, sans une ligne de LLM ni de web, si le produit tient sa seule promesse
chiffrable.

**Exigences :** FR-5, FR-6, FR-8 *(part)* · SM-3

**Acceptance Criteria :**

**Étant donné** le vivier d'amorçage
**Quand** un test parcourt les **231 combinaisons** — 11 sports × 7 jours × 3 niveaux
**Alors** **127** d'entre elles ne rendent aucun candidat exact.

**Étant donné** ces 127 combinaisons
**Quand** l'élargissement sur le jour s'applique à chacune
**Alors** **au moins 85 %** produisent au moins un candidat du niveau exact demandé
**Et** le plafond atteignable de **89 %** n'est pas dépassé — le dépasser signalerait une fuite
de niveau.

**Étant donné** le résidu réellement vide
**Quand** on l'inspecte
**Alors** il compte **14 combinaisons**, toutes du **Pilates**, réparties sur les deux seules
paires sport × niveau vides du fichier.

**Étant donné** l'ensemble des candidats rendus sur les 231 combinaisons
**Quand** on vérifie leur niveau
**Alors** **aucun** n'est d'un autre niveau que celui demandé — zéro exception.

### Story 2.5 : Aucun élargissement de niveau, à aucune étape

En tant que **personne qui a déclaré son niveau**,
je veux que le produit n'ait aucun moyen de me proposer quelqu'un d'un autre niveau,
afin que l'égalité stricte soit une propriété du code et non une intention.

> Story négative, exigée par la contrainte d'écriture **C3** : un interdit ne se vérifie jamais
> par un parcours nominal.

**Exigences :** FR-5, FR-6 · contrainte « égalité stricte de niveau » · contrainte d'écriture C3

**Acceptance Criteria :**

**Étant donné** l'interface publique de `domaine/recherche`
**Quand** on l'inspecte
**Alors** aucune fonction n'accepte de paramètre de tolérance, d'adjacence ou de relaxation de
niveau
**Et** la vérification est faite par un test, pas par relecture.

**Étant donné** une demande qui réclamerait explicitement d'élargir le niveau
**Quand** elle atteint le domaine
**Alors** aucun chemin ne la satisfait : il n'existe pas de fonction à appeler.

**Étant donné** les 231 combinaisons parcourues par la story 2.4
**Quand** on agrège tous les candidats rendus, élargissement compris
**Alors** la distribution de leurs niveaux est exactement celle des niveaux demandés.

---

## Epic 3 : Le fil

Le seul lot vraiment nouveau. L'agent, le flux SSE et le contrat d'événements sont l'endroit où
le projet apprend quelque chose ; il arrive sur un domaine déjà juste, donc un comportement
étrange s'impute au câblage et non aux règles.

Treize stories, parce que ce lot porte trente des trente-six UX-DR, le contrat de rendu d'un
tour, la reprise de conversation et la seule panne sans repli du produit. Ce n'est pas un problème
de découpage — c'est la raison pour laquelle les stories 3.4, 3.12 et 3.13 existent.

> **Portée des blocs persistants dans ce lot.** E3 possède les **règles** du fil — append-only,
> unique par entité, toute mutation annoncée — mais le **récapitulatif de rencontre** n'existe
> qu'une fois qu'une rencontre existe, c'est-à-dire avec E5. Les règles sont donc assertées ici
> sur le **récapitulatif de profil**, seul bloc persistant qu'E3 produit par elle-même (story
> 3.6), et E5 les étend au récapitulatif de rencontre sans les réécrire. Aucune story de ce lot
> ne dépend d'un lot aval.

### Story 3.1 : Le fil à froid, ouvert sans authentification

En tant que **visiteur**,
je veux ouvrir le site et pouvoir écrire tout de suite,
afin de dire ce que je cherche sans qu'on me demande d'abord qui je suis.

**Exigences :** FR-1 · NFR-4 · UX-DR1 à UX-DR6, UX-DR19, UX-DR32 *(part)*, UX-DR36

**Acceptance Criteria :**

**Étant donné** un navigateur qui n'a jamais visité le site
**Quand** la page s'ouvre
**Alors** l'accroche en `display` et la zone de saisie s'affichent, **sans aucun écran
d'authentification préalable**
**Et** le champ est **focalisé** avant que le reste du fil ait fini de se peindre.

**Étant donné** la zone de saisie
**Quand** on l'inspecte
**Alors** c'est un `<textarea>` — jamais un `<input>` — qui croît jusqu'à quatre lignes puis
défile
**Et** **Entrée** envoie, **Maj+Entrée** passe à la ligne
**Et** aucune règle `outline: none` n'existe sur cet élément, ni sur aucun autre du produit.

**Étant donné** les jetons de `DESIGN.md`
**Quand** la page est rendue
**Alors** la palette, la typographie en `rem`, les trois marches tonales et le filet unique
`border-interactive` sont ceux du contrat
**Et** aucune ombre portée n'est posée, y compris pour l'anneau de focus.

**Étant donné** la page à **320 px** de large
**Quand** on la mesure, y compris sous la feuille d'espacement forcé de WCAG 1.4.12
**Alors** il n'y a **aucun débordement horizontal**
**Et** à 200 % de zoom et 400 % de redistribution, le fil reste utilisable en défilement vertical
seul.

**Étant donné** le document
**Quand** on inspecte sa structure
**Alors** il porte `lang="fr"`, un `<title>` stable, un seul `main`, une `<section>` nommée pour
le fil et un `<h1>` **visuellement masqué et permanent**.

### Story 3.2 : Un tour de parole, du message posté au flux d'événements

En tant que **personne qui vient d'écrire**,
je veux voir le bot travailler pendant qu'il travaille,
afin que l'attente ne se lise pas comme une panne.

**Exigences :** CAP-16 *(part)* · NFR-1 · AD-2, AD-4 · DW-2

**Acceptance Criteria :**

**Étant donné** un message posté
**Quand** le tour démarre
**Alors** le client reçoit **un flux SSE unique pour le tour**, portant quatre types
d'événements — `etape`, `jeton`, `bloc`, `fin`.

**Étant donné** un tour de parole
**Quand** on trace les appels au modèle
**Alors** il y a **exactement une** boucle de *tool runner*, aucun appel LLM imbriqué, ni routeur
ni agent spécialisé (AD-2).

**Étant donné** un événement `bloc`
**Quand** on en cherche l'auteur
**Alors** il est **composé par l'adaptateur web** à partir d'un résultat de domaine
**Et** le modèle ne choisit jamais un gabarit ni ne compose un bloc (AD-4).

**Étant donné** un tour qui appelle au moins un outil
**Quand** on mesure le délai jusqu'au premier événement reçu
**Alors** il est **inférieur à 2 secondes**
**Et** la réponse complète arrive en moins de 20 secondes, au-delà de quoi le bot dit ce qu'il
fait et pourquoi c'est long.

**Étant donné** que ce lot est le premier à consommer réellement une clé d'API
**Quand** la configuration est lue
**Alors** le report **DW-2** est clos explicitement : soit `python-dotenv` est ajouté à la table
*Stack* de la spine après accord, soit `.env.example` est corrigé pour ne documenter que des
variables d'environnement de shell
**Et** `deferred-work.md` est mis à jour.

### Story 3.3 : Les lignes d'étape, émises par les ports et non par le modèle

En tant que **personne qui lit ce que le bot annonce**,
je veux que chaque étape corresponde à un appel qui a réellement eu lieu,
afin que « j'ai regardé la météo » soit une observation et non une affirmation.

**Exigences :** CAP-16 · AD-3, AD-13 · arbitrage B · UX-DR8

**Acceptance Criteria :**

**Étant donné** un port qui **peut échouer d'une façon que la personne doit connaître**
**Quand** il est appelé
**Alors** il émet un événement `etape` **à l'entrée et à la sortie**, portant le service et son
sort.

**Étant donné** la liste des ports du produit
**Quand** on vérifie lesquels émettent
**Alors** ce sont les **cinq** suivants : `meteo`, `air`, `lieux`, `agenda` et `envois`
**Et** `persistance` n'émet pas — son échec est un défaut, pas un fait *(arbitrage B)*.

**Étant donné** l'outillage remis au modèle
**Quand** on l'inspecte
**Alors** **aucun outil ne permet au modèle d'émettre une étape**.

**Étant donné** un appel externe qui échoue
**Quand** le tour se poursuit
**Alors** la ligne d'étape **reste dans la pile**, en encre primaire, et dit à l'accompli ce qui
n'a pas pu être fait
**Et** aucune teinte ne la distingue — le rose-rouge appartient à la seule jouabilité.

**Étant donné** un tour terminé
**Quand** on inspecte la base
**Alors** ses étapes sont **persistées avec le tour**, distinctes de la journalisation technique.

### Story 3.4 : Le chemin sonore — trois satellites qui ne se taisent jamais

En tant que **personne qui utilise un lecteur d'écran**,
je veux entendre chaque tour du bot une fois, complet, et chaque mutation d'un bloc,
afin que le produit me soit utilisable au même titre qu'à quelqu'un qui le voit.

> Story dédiée, exigée par le mode de panne que `UX-DR30` décrit lui-même : **le silence, tour
> après tour, invisible à toute recette visuelle.** Aucune story fonctionnelle ne l'attrapera —
> le fil s'affichera parfaitement pendant que le chemin sonore est mort.

**Exigences :** CAP-16 *(part)* · UX-DR28 à UX-DR32

**Acceptance Criteria :**

**Étant donné** le premier octet de HTML servi
**Quand** on inspecte le document
**Alors** les **trois satellites** sont déjà présents et **vides** : satellite de tour
(`role="log" aria-relevant="additions" aria-atomic="false"`), satellite d'étapes
(`role="status" aria-atomic="true"`), région de statut (`role="status"`)
**Et** le fil visible ne porte **aucun attribut live**.

**Étant donné** un tour du bot qui se termine
**Quand** il est annoncé
**Alors** son texte complet est **ajouté** au satellite de tour **en un seul ajout**
**Et** le satellite est **vidé ensuite**, après un délai fixe — jamais l'inverse, jamais dans la
même tâche.

**Étant donné** un test qui pilote un tour complet
**Quand** il observe le satellite de tour
**Alors** il **échoue** si le satellite est vidé avant d'être écrit, ou si l'écriture et le
vidage tombent dans la même tâche — c'est la seule assertion qui distingue le produit correct du
produit muet.

**Étant donné** la vie entière de la page
**Quand** on observe les trois satellites
**Alors** ils ne sont **jamais démontés ni remontés**
**Et** aucun tour de la personne n'y est jamais écrit.

**Étant donné** un bloc persistant qui mute — pastille de statut, ligne de jour bloqué, valeur
inconnue remplacée, alerte annulée, heure retenue par la contre-proposition
**Quand** la mutation a lieu
**Alors** la **région de statut** porte une **phrase complète et autonome** : un sujet, un verbe,
la valeur qui a changé.

### Story 3.5 : Extraire une demande du langage naturel

En tant que **personne qui écrit une phrase**,
je veux que le bot en tire mon sport, mes jours et mon niveau,
afin de ne jamais remplir de formulaire.

**Exigences :** FR-2

**Acceptance Criteria :**

**Étant donné** « je veux jouer au tennis mardi aprem, je suis intermédiaire »
**Quand** le tour se déroule
**Alors** la demande {sport: Tennis, jours: [Mardi], niveau: Intermédiaire} est produite **sans
qu'aucune question soit posée**
**Et** le bot **répète le niveau dans sa phrase suivante**, sans le commenter ni le valider.

**Étant donné** un message où le sport, le jour **ou** le niveau manque
**Quand** le bot répond
**Alors** il réclame **un seul élément à la fois**, en prose, et jamais trois questions
d'affilée.

**Étant donné** « j'ai un niveau OK », « bon niveau », « ça va » ou toute formulation approchante
**Quand** le bot la traite
**Alors** elle n'est **ni interprétée ni stockée** — seuls les trois mots exacts sont retenus tels
quels.

**Étant donné** une demande sur un sport que le vivier ne connaît pas
**Quand** elle est traitée
**Alors** le bot **cherche**, ne trouve rien, et le dit — jamais un refus, et sans annoncer à la
personne qu'elle fonde le sport.

### Story 3.6 : Déclarer son niveau, ou refuser de le dire

En tant que **personne qui n'a pas employé l'un des trois mots**,
je veux qu'on me les propose une fois, avec le motif attaché,
afin de savoir pourquoi on me le demande et de pouvoir refuser.

**Exigences :** FR-2 · UX-DR12, UX-DR15

**Acceptance Criteria :**

**Étant donné** une demande qui se complète sans que le niveau ait été dit
**Quand** le bot répond
**Alors** le bloc `level-choice` s'affiche : **trois choix empilés en colonne**, chacun portant
le mot et une ligne de fait générique, le motif en prose **au-dessus et hors du bloc**
**Et** il apparaît **une seule fois**, jamais deux.

**Étant donné** le bloc de niveau affiché
**Quand** la personne écrit, au lieu de cliquer, un mot que le bot ne sait pas lire
**Alors** le bloc **reste en place, actif, et n'est jamais dupliqué**
**Et** le bot répond **une seule** phrase courte, **différente** de celle qui avait ouvert le
bloc, nommant le mot non lu et rappelant les deux sorties.

**Étant donné** un deuxième mot illisible sur le même bloc
**Quand** le bot répond
**Alors** il **n'ajoute rien**
**Et** le **focus est déplacé sur le `role="group"` du bloc**, dont le nom accessible et les trois
options se réénoncent — la question est reposée sans qu'un mot soit ajouté.

**Étant donné** une personne qui écrit qu'elle ne veut pas dire son niveau
**Quand** le bot répond
**Alors** il l'accepte, **dit ce que ça coûte avant qu'elle tranche** — le profil devient inerte
des deux côtés — et pose le `profile-recap`, portant « Niveau : je ne sais pas encore » en
`unknown-value` **suivi de la phrase qui dit ce que ce trou empêche**
**Et** il ne redemande jamais.

### Story 3.7 : Rendre les candidats dans le fil

En tant que **personne à qui on propose des gens**,
je veux comparer trois prénoms et leurs jours d'un coup d'œil,
afin de choisir sans lire ligne à ligne.

**Exigences :** FR-6 *(part)* · UX-DR9, UX-DR17, UX-DR23

**Acceptance Criteria :**

**Étant donné** un résultat de recherche portant des candidats
**Quand** le fil les rend
**Alors** chaque carte porte le prénom en `card-name` et **les jours et le délai d'attente** en
`meta`
**Et** le **niveau n'y figure pas** : il vit une seule fois dans l'intitulé de groupe.

**Étant donné** les deux populations du vivier
**Quand** on compare les cartes
**Alors** elles sont **identiques** — aucun badge « profil d'amorçage », aucune mention de second
rang.

**Étant donné** une carte de partenaire
**Quand** on l'inspecte
**Alors** c'est un **vrai `<button>`**, et son **nom accessible contient le texte visible mot pour
mot**
**Et** « Anna » tapé au clavier vaut le clic sur la carte d'Anna.

**Étant donné** plus de trois candidats et une demande de voir les autres
**Quand** la salve suivante arrive
**Alors** elle porte **son propre intitulé de groupe**
**Et** les cartes précédentes **restent actives** — une salve agrandit le tour, elle ne le résout
pas.

### Story 3.8 : Annoncer un vivier vide sans broder

En tant que **personne pour qui il n'y a vraiment personne**,
je veux qu'on me le dise en nommant ce qui a été tenté,
afin de savoir que la recherche a eu lieu plutôt que d'être renvoyée à un message générique.

**Exigences :** FR-8

**Acceptance Criteria :**

**Étant donné** un élargissement qui n'a produit aucun candidat
**Quand** le bot répond
**Alors** la réponse **nomme le sport et le jour tentés**, dit que **tous les autres jours** ont
été regardés, et conclut qu'il n'y a personne **à ce niveau**.

**Étant donné** « Pilates, avancé » ou « Pilates, intermédiaire »
**Quand** le bot répond
**Alors** il dit « personne à votre niveau » et **jamais** « personne ne fait de Pilates » — une
pratiquante existe.

**Étant donné** cette réponse
**Quand** elle se termine
**Alors** elle **enchaîne** sur la proposition d'alerte différée
**Et** aucun nom de personne absente du vivier, ni d'un autre sport, n'y figure jamais.

### Story 3.9 : Le passé est inerte, et le fil ne se réécrit pas

En tant que **personne qui a fait un choix il y a dix tours**,
je veux que ce choix reste lisible sans redevenir cliquable,
afin de ne jamais me demander si mon action d'il y a dix minutes vient de repartir.

**Exigences :** AD-17 · UX-DR11, UX-DR20 *(part)*, UX-DR24, UX-DR33 *(part)*

**Acceptance Criteria :**

**Étant donné** un tour résolu — sa question a reçu sa réponse, par un clic ou par une phrase
**Quand** on l'inspecte
**Alors** **tout** ce qu'il contenait de cliquable est inerte : cartes, contre-proposition,
boutons de connexion, choix d'agenda, choix de niveau, remplacement de sport
**Et** chacun reste lisible, perd son rôle, sort de l'ordre de tabulation et **porte son sort en
toutes lettres**, jamais par un filet seul.

**Étant donné** un tour déjà écrit
**Quand** l'état du produit change
**Alors** il ne change plus jamais — seuls le **récapitulatif de rencontre** et le
**récapitulatif de profil** mutent sur place, et ils sont **uniques par entité**.

**Étant donné** un élément focalisé qui devient inerte **ou qui est retiré du DOM**
**Quand** la transition a lieu
**Alors** le focus est déplacé **avant**, jamais après — il n'est jamais laissé dans le vide.

**Étant donné** le fil entier
**Quand** on compte les boutons primaires actifs
**Alors** il y en a **au plus un**, et le produit n'en pose qu'une seule instance : *« Retenir ce
créneau »*
**Et** le bouton d'envoi est hors du compte.

### Story 3.10 : Reprendre une conversation

En tant que **personne qui revient trois jours plus tard**,
je veux retrouver mon fil et savoir où en sont mes affaires,
afin de ne pas avoir à tout redire.

**Exigences :** CAP-15 · NFR-3 · AD-21 *(part)* · UX-DR35 *(part)*

**Acceptance Criteria :**

**Étant donné** un visiteur **sans compte** revenu sur le même navigateur
**Quand** la page s'ouvre
**Alors** son fil est là, porté par un **cookie signé de 30 jours**
**Et** au 31ᵉ jour il trouve un **fil à froid ordinaire**, sans message d'expiration ni trace
d'une conversation perdue.

**Étant donné** un **utilisateur inscrit** qui revient
**Quand** le bot ouvre son tour
**Alors** il récapitule **en prose**, en tête de son tour, la rencontre et les alertes en cours,
chaque rencontre nommée portant sa **pastille en ligne dans la phrase**
**Et** ce tour **s'insère en bas du fil** comme tous les autres.

**Étant donné** un récapitulatif de rencontre déjà posé plus haut dans le fil
**Quand** la reprise a lieu
**Alors** elle **ne le re-rend pas** : le bloc existant reste l'unique point de vérité et
continue de muter sur place.

**Étant donné** un utilisateur inscrit
**Quand** le temps passe
**Alors** son fil n'est **jamais** purgé ni réinitialisé de lui-même.

**Étant donné** un récapitulatif pas encore prêt au retour
**Quand** la page s'affiche
**Alors** une **ligne d'attente explicite** est rendue plutôt qu'un fil vide.

### Story 3.11 : Les pannes, dites sans excuse et sans couleur

En tant que **personne dont le réseau vient de tomber**,
je veux savoir ce qui a échoué et ce qui n'est pas perdu,
afin de ne pas croire que ma rencontre a disparu.

**Exigences :** NFR-5 · NFR-2 *(part)* · AD-20 · UX-DR20 *(part)*

**Acceptance Criteria :**

**Étant donné** un appel au modèle qui échoue
**Quand** le tour se rend
**Alors** c'est un tour du fil qui **nomme la panne et dit ce qui n'est pas perdu**, avec un
texte **arrêté et non généré**
**Et** **aucune écriture de domaine** n'a été engagée par ce tour interrompu.

**Étant donné** une perte de connexion
**Quand** la personne continue
**Alors** le fil reste lisible et défilable, la zone de saisie reste active, le message est mis
en file
**Et** une `service-notice` non modale, **sans couleur de statut**, dit que l'envoi attend le
réseau.

**Étant donné** un message qui n'est pas parti
**Quand** il s'affiche
**Alors** il garde sa bulle et sa pleine lisibilité, précédé du mot « Non envoyé » et suivi d'un
bouton « Renvoyer »
**Et** il n'est **jamais** effacé silencieusement.

**Étant donné** l'ensemble des états de panne du produit — envoi, réseau, OAuth, permission
d'agenda
**Quand** on les rend
**Alors** aucun n'est signalé par la seule couleur : encre primaire, filet réel et **mot écrit**
**Et** aucun message d'échec ne s'ouvre sur une excuse.

### Story 3.12 : Les interdits du fil

En tant que **personne qui a déclaré son niveau une fois**,
je veux que le bot ne me le redemande jamais et ne me pousse jamais à créer un compte trop tôt,
afin que les garde-fous du produit soient vérifiés plutôt que promis.

> Story négative, exigée par la contrainte d'écriture **C3**.

**Exigences :** FR-2 *(les interdits)* · UX-DR25 *(part)*, UX-DR27 · contrainte d'écriture C3

**Acceptance Criteria :**

**Étant donné** une recherche en cours, des candidats affichés, ou un résultat vide
**Quand** le bot répond
**Alors** le bloc de niveau **n'apparaît jamais** — ni pour élargir, ni après avoir montré des
candidats, ni pour rattraper un vide.

**Étant donné** une demande qui vise explicitement une autre agglomération que Lyon
**Quand** le bot répond
**Alors** il le dit **avant toute recherche**, jamais par une recherche vide déguisée en absence
de partenaire
**Et** c'est le **seul** état qui court-circuite la recherche.

**Étant donné** une question sans rapport avec la pratique sportive
**Quand** le bot répond
**Alors** il dit en une phrase ce qu'il fait et ce qu'il ne fait pas, sans s'excuser et sans
tenter de répondre.

**Étant donné** « montre-moi tous les joueurs », « t'as une carte ? » ou « filtre par niveau »
**Quand** le bot répond
**Alors** il **ne dit pas qu'il ne sait pas faire** : il donne ce qu'il peut sous une forme plus
dense — davantage de candidats en une fois, les jours côte à côte — et **note la demande**.

**Étant donné** le vocabulaire produit par le bot sur un échantillon de tours
**Quand** on le vérifie
**Alors** il ne contient ni « adversaire » hors sport de duel, ni « réservé », ni « réservation »,
ni « pas encore » ou tout autre adverbe qui promet une réponse.

### Story 3.13 : Le plancher de perception, et ce que le bot restitue

En tant que **personne qui lit mal les contrastes, ou qui a désactivé les animations**,
je veux que le produit reste entièrement lisible et utilisable,
afin que les partis visuels du produit ne soient jamais la condition de son usage.

> Story de couverture : elle porte les six UX-DR qu'aucune story fonctionnelle n'assertait —
> forme des messages, pastilles de statut, pastille « nouveau message », formulations arrêtées,
> préférences de perception, charge cognitive.

**Exigences :** UX-DR7, UX-DR10, UX-DR20 *(part)*, UX-DR25, UX-DR34, UX-DR35

**Acceptance Criteria :**

**Étant donné** un message du bot
**Quand** il arrive
**Alors** c'est du **texte nu** sur `surface-base`, sans bulle, sans avatar, sans horodatage, et
il arrive **en un bloc** — pas caractère par caractère, pas de points de suspension imitant un
indicateur de frappe
**Et** le message de la personne est une bulle `surface-user` alignée à droite, bornée à 80 % de
la colonne.

**Étant donné** une pastille de statut
**Quand** elle se rend
**Alors** elle porte **son mot écrit** à côté de sa couleur — *en attente* (ambre), *confirmée*
(vert), *déclinée*, *expirée*, *abandonnée* (neutres)
**Et** **aucune information du produit n'est portée par la couleur seule** : statut, jouabilité,
jour bloqué et sort d'une carte résolue portent tous leur mot, visiblement.

**Étant donné** une personne qui a remonté le fil pour relire
**Quand** le fil change
**Alors** il **ne défile pas** et la pastille « nouveau message » apparaît au-dessus de la zone de
saisie
**Et** son activation ramène le fil en bas, puis **le focus part vers le dernier tour**, qui porte
`tabindex="-1"`, **avant** que la pastille disparaisse.

**Étant donné** `prefers-reduced-motion`
**Quand** la page se rend
**Alors** le fondu d'arrivée cesse, la pulsation de l'étape en cours cesse, et le **marqueur
textuel « en cours » reste visible**
**Et** en toute circonstance la pulsation s'arrête au bout de **5 secondes** (WCAG 2.2.2).

**Étant donné** `prefers-contrast: less`
**Quand** la page se rend
**Alors** `ink-primary-soft` remplace `ink-primary` pour la prose longue — **seul assouplissement
du produit**
**Et** sous `forced-colors: active`, chaque surface qui compte reste identifiée par son **filet
réel** et chaque pastille par **son mot**.

**Étant donné** le bot qui relance après avoir déjà reçu une information
**Quand** il formule sa question
**Alors** il **restitue ce qu'il a retenu** avant de relancer (WCAG 3.3.7, *Saisie redondante*)
**Et** il **glose le mot « vivier »** à sa première occurrence, sans le remplacer par un synonyme.

**Étant donné** un échantillon de tours du bot
**Quand** on vérifie sa voix
**Alors** la mauvaise nouvelle arrive **en premier, sans coussin** ; le bot **ne se félicite
jamais** ; tout message d'échec **dit ce qui n'est pas perdu** ; et l'inconnu se conjugue à la
première personne — « je ne sais pas encore », jamais « non déterminé ».

---

## Epic 4 : Identité et compte

Le compte arrive au moment où le bot va exposer l'utilisateur à quelqu'un d'autre, et pas avant.
C'est aussi le lot où un utilisateur entre au vivier et devient trouvable.

### Story 4.1 : Se connecter avec Google ou Microsoft

En tant que **personne à qui le bot vient de demander un compte**,
je veux me connecter avec un compte que j'ai déjà,
afin de ne pas inventer un mot de passe pour un service que je découvre.

**Exigences :** FR-4 · AD-18 · UX-DR13

**Acceptance Criteria :**

**Étant donné** le moment où le bot demande un compte
**Quand** le bloc `auth-block` s'affiche
**Alors** il porte **deux `button-quiet` de rang égal**, Google et Microsoft, et le motif de la
demande est écrit **au-dessus du bloc, en prose de message**, jamais à l'intérieur
**Et** le motif dit **que le compte rend l'utilisateur trouvable par les autres**.

**Étant donné** le parcours OAuth de ce moment
**Quand** on inspecte les portées demandées
**Alors** elles se limitent à **l'identité et l'adresse électronique** — la portée d'écriture
agenda n'y figure pas (AD-18).

**Étant donné** une connexion réussie
**Quand** le compte est créé
**Alors** l'adresse fournie devient le **canal des notifications différées**
**Et** le numéro de téléphone n'est jamais exigé pour terminer un parcours.

**Étant donné** un fournisseur qui refuse
**Quand** le bot répond
**Alors** il nomme l'échec sans jargon, propose l'autre fournisseur, et énonce ce qui reste
possible sans compte : chercher, comparer, consulter la jouabilité.

### Story 4.2 : Revenir d'OAuth au même endroit

En tant que **personne qui vient de quitter le produit pour se connecter**,
je veux retrouver ma conversation exactement où je l'ai laissée,
afin que me connecter ne me coûte pas ce que j'avais déjà fait.

**Exigences :** CAP-15 *(part)* · AD-21 · UX-DR33 *(part)*

**Acceptance Criteria :**

**Étant donné** une conversation en cours portée par le cookie de visiteur
**Quand** la personne se connecte
**Alors** la conversation **s'attache** au compte : ni rejouée, ni dupliquée, ni recommencée
**Et** **aucun second fil** n'est ouvert (AD-21).

**Étant donné** un brouillon de saisie non envoyé
**Quand** la personne revient d'OAuth
**Alors** le brouillon est intact quand c'est possible
**Et** s'il est perdu, **le bot le dit** — ce qui est promis n'est pas qu'il survive toujours,
c'est qu'il ne disparaisse jamais en silence.

**Étant donné** le retour d'OAuth
**Quand** la page se rend
**Alors** le focus est placé sur le message qui reprend la conversation, qui porte
`tabindex="-1"`, et le statut du retour — réussi, annulé, refusé — est annoncé
**Et** cette règle **prime sur la focalisation automatique du champ**.

**Étant donné** une personne qui a fermé la fenêtre du fournisseur sans se connecter
**Quand** elle revient
**Alors** le fil reprend exactement où il était, **sans reproche et sans redemander**
**Et** le bot rappelle en une phrase ce que la connexion débloquait, puis se tait.

### Story 4.3 : Entrer au vivier à la création du compte

En tant que **personne qui vient de créer son compte**,
je veux devenir trouvable par les recherches des autres,
afin que le vivier grossisse de moi comme il m'a servi.

**Exigences :** FR-3 · FR-16 *(part)*

**Acceptance Criteria :**

**Étant donné** un visiteur sans compte
**Quand** quelqu'un cherche un partenaire
**Alors** il ne sort **jamais** comme candidat.

**Étant donné** un compte qui vient d'être créé à partir d'une demande « tennis, mardi,
intermédiaire »
**Quand** une autre personne lance la même recherche
**Alors** le nouveau profil est renvoyé.

**Étant donné** un profil et une nouvelle demande **sur le sport déjà porté**
**Quand** elle est traitée
**Alors** ses jours et son niveau sont mis à jour, sans que le sport change.

**Étant donné** deux conversations d'une même personne connectée au même compte
**Quand** on compte ses profils
**Alors** il y en a **un seul** — le compte est la clé d'identité du profil.

**Étant donné** une personne qui demande à sortir du vivier depuis la conversation
**Quand** le bot exécute
**Alors** elle en sort définitivement, exactement comme un profil d'amorçage l'obtient depuis son
message.

### Story 4.4 : Remplacer son sport, annoncé avant d'être appliqué

En tant que **personne inscrite qui veut changer de sport**,
je veux savoir ce que je perds avant de le perdre,
afin de ne pas découvrir après coup que je ne suis plus trouvable au tennis.

> Story exigée par la contrainte d'écriture **C2** : le geste le plus destructeur du produit
> n'avait aucun critère de lot.

**Exigences :** FR-3 · AD-5 · UX-DR16 · contrainte d'écriture C2

**Acceptance Criteria :**

**Étant donné** un utilisateur inscrit qui demande un sport **autre** que celui de son profil
**Quand** le bot répond
**Alors** le bloc `sport-replace` s'affiche : un **rappel en lecture seule** de ce qui sera perdu
— sport, niveau, jours — séparé des deux boutons par un filet
**Et** le coût est écrit **dans la prose au-dessus**, jamais dans un libellé de bouton.

**Étant donné** ce bloc
**Quand** on l'inspecte
**Alors** les deux choix sont de **rang égal** et **aucun n'est un `button-primary`** — le
produit ne pousse vers aucune des deux issues.

**Étant donné** le remplacement accepté
**Quand** il s'applique
**Alors** **sport, niveau et jours** sont réécrits **en une seule transaction**
**Et** jamais une accumulation, jamais un second profil sous le même compte.

**Étant donné** le remplacement appliqué
**Quand** la personne est recherchée sur son sport précédent
**Alors** elle ne sort plus
**Et** l'écriture du profil passe par le **point d'entrée unique d'écriture de profil** du
domaine — c'est ce point que E9 branchera pour déclencher ses alertes, sans que cette story ait
rien à asserter d'E9.

**Étant donné** l'ordre des opérations
**Quand** on le vérifie
**Alors** le bot **annonce avant d'appliquer**, jamais après.

### Story 4.5 : Le compte n'est jamais demandé avant le geste qui engage

En tant que **visiteur qui veut juste voir**,
je veux chercher, comparer et consulter la jouabilité sans qu'on me demande qui je suis,
afin que le produit ne ressemble pas au paywall dont il se démarque.

> Story négative, exigée par la contrainte d'écriture **C3**.

**Exigences :** FR-4 · UX-DR25 *(part)* · contrainte d'écriture C3

**Acceptance Criteria :**

**Étant donné** un visiteur sans compte
**Quand** il formule une demande, obtient des propositions, retient un candidat et consulte la
jouabilité
**Alors** **aucune demande de compte** n'est déclenchée à aucune de ces étapes.

**Étant donné** le même visiteur
**Quand** il **retient un créneau**
**Alors** la demande de compte est déclenchée, et à ce moment-là seulement.

**Étant donné** le même visiteur devant une proposition d'alerte différée
**Quand** il l'accepte
**Alors** la demande de compte est déclenchée également.

**Étant donné** toute demande faite par le bot — secteur, compte, accès agenda, niveau
**Quand** elle est formulée
**Alors** son **motif est énoncé au moment où elle est faite**, jamais après ni ailleurs.

---

## Epic 5 : Cycle de vie des rencontres

Les cinq statuts et ce qu'ils autorisent le bot à dire. C'est ici que la machine à états, ses
effets par arête et les deux dérivations — jour bloqué, recherche active — deviennent vraies.

### Story 5.1 : Les cinq statuts et leurs effets, attachés aux arêtes

En tant que **personne qui attend une réponse**,
je veux que le bot ne dise que ce que le statut l'autorise à dire,
afin qu'il ne me présente jamais un refus comme une absence de réponse.

**Exigences :** FR-13 · AD-9 · arbitrage A

**Acceptance Criteria :**

**Étant donné** `domaine/rencontre`
**Quand** on l'inspecte
**Alors** il porte **cinq** statuts — *en attente*, *confirmée*, *déclinée*, *expirée*,
*abandonnée* — et une **table de transitions explicite** portant, pour chaque arête, ses effets
**Et** il n'existe **aucun** déclencheur générique « statut changé → prévenir » (AD-9).

**Étant donné** `domaine/ports.py`
**Quand** on l'inspecte
**Alors** il déclare les deux protocoles que les effets de la table touchent — **`PortEnvois`**
et **`PortAgenda`** — que les adaptateurs d'E6 et d'E8 implémenteront
*(arbitrage A, étendu à l'agenda : sans ces déclarations ici, E5 et E9 n'ont rien contre quoi
asserter leurs courriels, et E5 rien contre quoi asserter la mise à jour de l'événement)*.

**Étant donné** un double de test implémentant `PortEnvois`
**Quand** chaque arête de la table est franchie
**Alors** les effets assertés sont exactement ceux de `statuts-rencontre.md` : courriel au
demandeur sur *confirmée*, *déclinée* et *expirée* ; message au partenaire sur la seule création ;
mise à jour de l'événement d'agenda sur **toutes** les arêtes — cette dernière assertée contre un
double de `PortAgenda`, l'adaptateur réel arrivant avec la story 8.3.

**Étant donné** l'arête vers *abandonnée*
**Quand** elle est franchie
**Alors** **aucun courriel** n'est demandé au port, **aucun message au partenaire** non plus
**Et** la mise à jour de l'agenda l'est.

**Étant donné** une rencontre *déclinée*, *expirée* ou *abandonnée*
**Quand** on la cherche
**Alors** elle existe toujours et reste consultable avec son statut — **jamais supprimée en
silence**.

### Story 5.2 : Retenir un créneau, en une seule transaction

En tant que **personne qui vient de choisir quelqu'un**,
je veux que mon geste engage une fois et une seule,
afin que deux onglets ouverts ne fassent pas partir deux messages.

**Exigences :** FR-13, FR-14 *(part)* · AD-7, AD-8, AD-20 *(part)*

**Acceptance Criteria :**

**Étant donné** le geste de retenir un créneau
**Quand** il s'exécute
**Alors** la vérification de la précondition, la création de la **rencontre**, la création du
**jeton** et l'inscription à la **boîte d'envoi** se font dans **une seule transaction** (AD-8).

**Étant donné** deux onglets d'un même utilisateur qui retiennent simultanément
**Quand** les deux transactions s'exécutent
**Alors** **une seule rencontre** existe, et la seconde échoue proprement.

**Étant donné** une rencontre qui vient d'être créée
**Quand** on lit son statut
**Alors** il est **en attente**, quelle que soit la population dont vient le partenaire.

**Étant donné** le **premier** récapitulatif de rencontre posé dans le fil
**Quand** il apparaît
**Alors** le bot dit **une fois**, sans désigner personne, qu'une partie des personnes qu'il
propose ne sont pas encore inscrites et peuvent ne jamais répondre
**Et** il ne le redit plus — c'est la seule manière de tenir la promesse d'honnêteté sans créer
une mention de second rang sur les profils d'amorçage.

**Étant donné** une rencontre
**Quand** on inspecte son modèle
**Alors** elle porte **deux liens distincts** vers un profil — un **côté demandeur** et un **côté
partenaire** (AD-7).

**Étant donné** la génération d'un tour interrompue par une panne
**Quand** on inspecte la base
**Alors** aucune transaction de retenue n'a été engagée — elle est **postérieure** à la
génération, jamais concurrente (AD-20).

### Story 5.3 : Dériver le jour bloqué, symétriquement

En tant que **personne dont la rencontre est posée un mercredi**,
je veux rester trouvable les autres jours,
afin qu'une rencontre ne me retire pas du vivier pour la semaine.

**Exigences :** FR-16, FR-5 *(part)* · AD-6, AD-7 · UX-DR26 *(part)*

**Acceptance Criteria :**

**Étant donné** une rencontre *en attente* ou *confirmée*
**Quand** on dérive la disponibilité
**Alors** **le seul jour** de la rencontre est bloqué, **pour les deux profils**
**Et** chacun continue de sortir des recherches portant sur ses autres jours.

**Étant donné** le modèle de données
**Quand** on cherche un champ `bloque`
**Alors** il n'en existe **aucun** : la disponibilité se dérive par jointure sur les rencontres
bloquantes (AD-6).

**Étant donné** une rencontre qui passe *déclinée*, *expirée* ou *abandonnée*
**Quand** on dérive à nouveau
**Alors** le jour est **libéré immédiatement**, et l'abandon le libère **pour les deux profils**.

**Étant donné** un partenaire qui accepte un jour qu'il n'avait pas demandé
**Quand** l'acceptation est enregistrée
**Alors** ce jour **entre au profil et y reste**
**Et** le bot l'écrit dans le fil — c'est une mutation de la fiche de quelqu'un, elle ne peut pas
se produire en silence.

**Étant donné** une rencontre passée sans incident
**Quand** on cherche le profil le lendemain
**Alors** il est trouvable exactement comme la veille.

### Story 5.4 : Une seule recherche active, côté demandeur seulement

En tant que **personne sollicitée par un inconnu**,
je veux garder le droit de chercher quelqu'un moi-même,
afin qu'un tiers ne me gèle pas alors que je n'ai rien demandé.

**Exigences :** FR-13 · AD-6, AD-7

**Acceptance Criteria :**

**Étant donné** une rencontre *en attente* ou *confirmée* née de **ses propres** demandes
**Quand** la personne formule une demande complète
**Alors** la recherche **n'est pas lancée**
**Et** la réponse **nomme le sport, le partenaire et le jour occupés**, et propose l'abandon
**dans la même phrase**.

**Étant donné** une personne **sollicitée** par un autre demandeur
**Quand** elle formule une demande complète
**Alors** la recherche **est lancée** — être sollicité n'occupe pas la place (AD-7)
**Et** son jour reste néanmoins bloqué par la story 5.3.

**Étant donné** le modèle de données
**Quand** on cherche un champ `recherche_active`
**Alors** il n'en existe **aucun** : l'état se dérive de la même jointure, filtrée sur le côté
demandeur.

**Étant donné** une ou plusieurs **alertes différées** en cours
**Quand** la personne lance une recherche
**Alors** elles n'y font **aucun** obstacle — une alerte n'occupe aucun créneau.

### Story 5.5 : Abandonner une rencontre

En tant que **personne qui veut chercher autre chose**,
je veux pouvoir renoncer à ma rencontre en cours,
afin que la règle d'une seule recherche ne mange pas la porte de sortie qu'elle promet.

**Exigences :** FR-13, FR-16 · AD-9

**Acceptance Criteria :**

**Étant donné** une rencontre *en attente* ou *confirmée*
**Quand** l'utilisateur y renonce
**Alors** elle passe en **abandonnée**, le jour se libère aussitôt pour les deux profils, et la
recherche redevient possible.

**Étant donné** l'arête vers *abandonnée*
**Quand** on cherche qui peut la franchir
**Alors** **seul l'utilisateur** le peut — ni la tâche périodique, ni le partenaire (AD-15).

**Étant donné** un abandon
**Quand** on inspecte les effets
**Alors** **aucun courriel** ne part au demandeur et **aucun message** au partenaire
**Et** l'événement d'agenda **est** mis à jour.

**Étant donné** un changement de créneau sur une rencontre déjà écrite dans l'agenda
**Quand** il s'exécute
**Alors** il emprunte ce même chemin — *abandonnée*, puis une nouvelle rencontre retenue. Ce
n'est **pas un cas particulier**.

### Story 5.6 : Expirer les rencontres et rendre les jours

En tant que **personne dont le partenaire n'a jamais répondu**,
je veux que mon jour me revienne quand le créneau est passé,
afin qu'une rencontre restée sans réponse ne m'immobilise pas indéfiniment.

> Story exigée par la contrainte d'écriture **C2** : le seul mécanisme qui rend au vivier les
> jours immobilisés n'avait aucun critère de lot.

**Exigences :** FR-13, FR-16 · AD-15 · contrainte d'écriture C2

**Acceptance Criteria :**

**Étant donné** une tâche d'arrière-plan attachée au cycle de vie de l'application
**Quand** elle s'exécute
**Alors** elle appelle le domaine comme n'importe quel adaptateur primaire, sans logique propre
(AD-15).

**Étant donné** une rencontre *en attente* dont le créneau est passé
**Quand** la tâche s'exécute
**Alors** elle bascule en **expirée**, le jour est libéré, et un courriel est demandé au port
pour le demandeur.

**Étant donné** la même tâche exécutée deux fois de suite
**Quand** on compare les états
**Alors** rien n'a changé au second passage — elle est **rejouable sans effet**.

**Étant donné** une rencontre *confirmée* dont le créneau est passé, ou une rencontre déjà
*abandonnée*
**Quand** la tâche s'exécute
**Alors** elle n'y touche pas — elle ne franchit **jamais** l'arête vers *abandonnée*.

---

## Epic 6 : Partenaire et envois

Le seul geste du produit qui engage quelqu'un d'autre trouve son destinataire. C'est aussi la
seule surface du produit qui vit hors du fil, et le seul endroit où un partenaire peut apprendre
un abandon.

### Story 6.1 : Filtrer les destinataires avant tout envoi

En tant que **personne inscrite dans les données d'amorçage sans l'avoir demandé**,
je veux que le produit soit structurellement incapable de m'atteindre,
afin qu'une campagne de test ne compose pas 86 numéros réels.

> Story exigée par la contrainte d'écriture **C2** : le filtre est une **règle de production**,
> et le « Fait quand » d'E6 ne le touchait pas.

**Exigences :** FR-14 · AD-11, AD-12 · arbitrage B · contrainte d'écriture C2

**Acceptance Criteria :**

**Étant donné** un numéro de la plage de fiction ARCEP `+336 39 98 XX XX`
**Quand** un envoi est demandé
**Alors** il est **autorisé**.

**Étant donné** un numéro dont la **provenance enregistrée** est *saisie par un utilisateur
inscrit*
**Quand** un envoi est demandé
**Alors** il est **autorisé**.

**Étant donné** un numéro qui ne satisfait **ni l'une ni l'autre** condition
**Quand** un envoi est demandé
**Alors** il **échoue bruyamment** et **n'entre pas** dans la boîte d'envoi.

**Étant donné** le code du filtre
**Quand** on l'inspecte
**Alors** il lit la **provenance portée dans le modèle** et **jamais le préfixe du numéro**
(AD-11) — c'est la seconde assertion que la part d'E1 ne portait pas
**Et** la vérification est faite par un test qui construit un numéro de la plage de fiction avec
une provenance *saisie par un utilisateur inscrit*, et l'inverse.

**Étant donné** le filtre et le mode « journaliser sans envoyer »
**Quand** on les inspecte
**Alors** ce sont **deux couches distinctes** : le filtre décide si un message a le *droit* de
partir, la boîte d'envoi s'il part *réellement* — l'un ne remplace jamais l'autre (AD-12).

**Étant donné** un échec du filtre pendant un tour
**Quand** le fil se rend
**Alors** une **ligne d'étape échouée** le dit — la boîte d'envoi est le cinquième port émetteur
*(arbitrage B)*.

### Story 6.2 : La boîte d'envoi persiste tout message sortant

En tant que **constructeur qui n'a aucun fournisseur SMS**,
je veux que chaque message sortant devienne une ligne consultable,
afin de pouvoir suivre le lien d'acceptation et démontrer le parcours du partenaire.

**Exigences :** FR-14, FR-9 *(part)* · AD-12

**Acceptance Criteria :**

**Étant donné** un envoi autorisé par le filtre
**Quand** il est remis à la boîte d'envoi
**Alors** une ligne persiste, portant le **destinataire**, le **corps rendu**, le **lien** et son
**sort**
**Et** la boîte ne remet rien à un opérateur : elle **est** le transport (AD-12).

**Étant donné** la boîte d'envoi
**Quand** on ouvre sa page locale
**Alors** elle liste les envois, et le lien d'acceptation y est suivable
**Et** cette page sert sur le même hôte que le fil.

**Étant donné** un envoi de type **courriel** — changement de statut, alerte, expiration
**Quand** il est remis
**Alors** il produit une ligne de la même forme, distinguée par son canal.

### Story 6.3 : L'adaptateur réel honore le contrat `PortEnvois`

En tant que **constructeur**,
je veux un seul test où le vrai adaptateur et le double se rencontrent,
afin que les assertions d'E5 et d'E9 vaillent pour le produit et pas seulement pour leurs
doubles.

> Story exigée par l'**arbitrage A**. C'est le seul endroit du produit où le vrai et le faux se
> rencontrent.

**Exigences :** FR-14 · arbitrage A

**Acceptance Criteria :**

**Étant donné** le protocole `PortEnvois` déclaré par la story 5.1
**Quand** l'adaptateur de boîte d'envoi est inspecté
**Alors** il l'implémente intégralement.

**Étant donné** la suite de contrat
**Quand** elle s'exécute contre le double de test **et** contre l'adaptateur réel
**Alors** les deux passent les **mêmes** assertions
**Et** un écart entre les deux fait échouer la suite.

### Story 6.4 : Prévenir le partenaire, par un message qui explique d'où il sort

En tant que **personne qu'on vient de retenir**,
je veux comprendre pourquoi je reçois ce message et pouvoir ne plus jamais être contactée,
afin de ne pas subir un service dont je n'ai jamais entendu parler.

**Exigences :** FR-14

**Acceptance Criteria :**

**Étant donné** un partenaire qui a un numéro de téléphone
**Quand** la rencontre est créée
**Alors** il est prévenu par **SMS**
**Et** un partenaire **inscrit sans numéro** est prévenu par **courriel**
**Et** une personne qui n'a ni l'un ni l'autre n'est **jamais** sollicitée.

**Étant donné** le message sortant
**Quand** on le lit
**Alors** il **énonce son propre motif** — que la personne figure dans le vivier d'Ex Aequo et que
quelqu'un cherche un partenaire — **avant** de présenter la proposition.

**Étant donné** le même message
**Quand** on en inspecte le contenu
**Alors** il porte le **sport, le jour, l'heure, le lieu et le prénom du demandeur**
**Et** **aucune coordonnée** du demandeur
**Et** un moyen de **ne plus jamais être contacté**.

**Étant donné** le lien d'acceptation
**Quand** on inspecte son jeton
**Alors** il porte **256 bits d'aléa cryptographique** encodés URL-safe, il est **distinct de
l'identifiant de rencontre**, et il n'en est jamais dérivé
**Et** il ne fonctionne **qu'une fois**.

**Étant donné** un même partenaire sollicité par plusieurs demandeurs
**Quand** on inspecte les envois
**Alors** chaque sollicitation a **son propre message et son propre lien**.

### Story 6.5 : La page d'acceptation et ses sept états

En tant que **personne qui suit un lien depuis son téléphone**,
je veux comprendre en une page ce qu'on me demande et y répondre,
afin de ne pas avoir à créer un compte pour dire oui ou non.

**Exigences :** FR-14, FR-13 *(part)* · AD-10 · NFR-4 *(part)* · UX-DR22

**Acceptance Criteria :**

**Étant donné** un lien suivi
**Quand** la page se rend
**Alors** son sort se dérive du **statut de la rencontre et de l'état du jeton, résolus ensemble
à la lecture** (AD-10)
**Et** la page rend **l'un des sept états terminaux** et **jamais une erreur nue**.

**Étant donné** les sept états
**Quand** on les énumère
**Alors** ce sont : *invitation ouverte*, *acceptée*, *refusée*, *lien déjà utilisé*, *lien
expiré*, *profil désinscrit*, *rencontre abandonnée*.

**Étant donné** l'état **rencontre abandonnée**
**Quand** la page se rend
**Alors** elle le dit en une phrase, **sans excuse et sans reproche**, ne le présente **jamais
comme un refus du demandeur**, et propose la **sortie définitive du vivier**
**Et** c'est le **seul endroit** du produit où le partenaire peut l'apprendre.

**Étant donné** une acceptation qui entre en conflit avec une rencontre déjà **confirmée** du même
partenaire
**Quand** elle s'exécute
**Alors** elle **échoue**, la page le lui dit sans lui proposer d'arbitrer, et la rencontre
concernée passe en **déclinée**.

**Étant donné** la page
**Quand** on l'inspecte
**Alors** c'est une colonne bornée à `thread-max-width`, **sans en-tête, sans navigation, sans
pied de page**, avec **deux `button-quiet` de rang égal** et **aucun `button-primary`**
**Et** elle tient à **320 px** sans débordement horizontal.

**Étant donné** un refus
**Quand** il est enregistré
**Alors** la rencontre passe en **déclinée**, sans qu'aucun motif soit demandé
**Et** l'absence de réponse la laisse *en attente* jusqu'au créneau, jamais annulée d'office,
jamais requalifiée en confirmée.

### Story 6.6 : Sortir définitivement du vivier

En tant que **personne qui ne veut plus jamais recevoir ça**,
je veux un moyen d'en sortir qui ne se reprenne pas d'un clic,
afin que « définitif » veuille dire définitif.

**Exigences :** FR-14, FR-16 *(part)* · CAP-13

**Acceptance Criteria :**

**Étant donné** le moyen de sortie porté par le message ou par la page
**Quand** il est exercé
**Alors** le profil sort **définitivement** du vivier
**Et** il ne revient dans **aucune** recherche, quel que soit le statut de ses rencontres
passées.

**Étant donné** l'état **profil désinscrit** de la page
**Quand** il se rend
**Alors** il confirme que la personne ne sera plus contactée
**Et** il ne porte **aucun bouton pour revenir en arrière**.

**Étant donné** les deux populations du vivier
**Quand** on vérifie ce droit
**Alors** il vaut pour les deux — un profil d'amorçage l'obtient par son message, un utilisateur
inscrit par une phrase dans la conversation.

---

## Epic 7 : Lieux et jouabilité

Le seul lot substantiel qui se détache du chemin critique : il ne dépend que d'E1 et s'écrit sans
le fil, sans compte et sans rencontre. Utile si l'inscription à l'API ATMO traîne, puisqu'elle est
la seule démarche du projet.

### Story 7.1 : Proposer un lieu lyonnais adapté au sport

En tant que **personne qui a retenu quelqu'un**,
je veux qu'on me propose un endroit où pratiquer,
afin de ne pas avoir à chercher un terrain moi-même.

**Exigences :** FR-11 · AD-13 · NFR-2 *(part)*

**Acceptance Criteria :**

**Étant donné** un sport et l'agglomération lyonnaise
**Quand** Data ES est interrogée
**Alors** les lieux rendus sont à **Lyon ou dans son agglomération** et correspondent au sport
**Et** l'appel se fait **sans clé d'API**.

**Étant donné** chaque lieu rendu
**Quand** on l'inspecte
**Alors** il porte **sa nature**, projetée depuis `equip_nature` — c'est elle qui décidera de la
jouabilité.

**Étant donné** un secteur ou un arrondissement
**Quand** le bot le demande
**Alors** il ne l'**exige jamais** : sans réponse, il propose quand même
**Et** un secteur donné est **enregistré au profil** de l'utilisateur inscrit et réutilisé la fois
suivante.

**Étant donné** une interrogation qui ne rend aucun lieu
**Quand** le bot répond
**Alors** il **le dit** et poursuit le parcours — aucun lieu plausible n'est inventé
**Et** le créneau reste retenable sans lieu.

**Étant donné** Data ES indisponible
**Quand** l'appel échoue
**Alors** le port rend un **résultat typé** nommant le service et son motif, jamais une exception
**Et** le parcours reste terminable : l'utilisateur indique le lieu lui-même.

### Story 7.2 : Projeter la nature d'un équipement vers *jouabilité applicable*

En tant que **personne qui pratique sous un préau**,
je veux que le bot vérifie quand même la chaleur, le vent et l'air,
afin qu'un toit ne me protège pas de ce dont il ne protège pas.

**Exigences :** FR-10, FR-11 · AD-14

**Acceptance Criteria :**

**Étant donné** un équipement classé **pleinement intérieur**
**Quand** la projection s'applique
**Alors** *jouabilité applicable* est **faux** et les trois seuils sont désactivés.

**Étant donné** un équipement classé **`Extérieur couvert`** — la valeur que Data ES retourne
réellement
**Quand** la projection s'applique
**Alors** *jouabilité applicable* est **vrai** : les trois seuils ne comportent **aucune notion de
pluie**, et un toit n'abrite ni de la chaleur, ni du vent, ni de l'air (AD-14).

**Étant donné** cette projection
**Quand** on cherche où elle vit
**Alors** elle est dans **`domaine/jouabilite`**, jamais dans l'adaptateur
**Et** elle est **nommée**, pas incluse dans une condition.

**Étant donné** un équipement dont l'attribut de nature est **absent**
**Quand** le bot répond
**Alors** il le dit **en une clause** plutôt que de supposer.

**Étant donné** **aucun lieu**
**Quand** la jouabilité est demandée
**Alors** **aucune évaluation** n'a lieu.

### Story 7.3 : Évaluer les trois seuils

En tant que **personne qui va courir dehors**,
je veux savoir si les conditions sont mauvaises avant de m'engager,
afin que ce soit une question de santé et non de confort découvert sur place.

**Exigences :** FR-10 · AD-13 · NFR-2 · CAP-16 *(part)*

**Acceptance Criteria :**

**Étant donné** un créneau sur un lieu où la jouabilité s'applique
**Quand** l'évaluation s'exécute
**Alors** elle compare la **température ressentie à 28 °C**, les **rafales à 40 km/h** et
l'**indice ATMO à 4** sur l'échelle à six degrés
**Et** un dépassement de l'un des trois est signalé.

**Étant donné** Open-Meteo
**Quand** il est appelé
**Alors** il rend `apparent_temperature` et `wind_gusts_10m` en prévision horaire, **sans clé
d'API**.

**Étant donné** l'API ATMO Auvergne-Rhône-Alpes
**Quand** elle est appelée
**Alors** elle rend l'indice pour Lyon, avec l'identifiant d'accès obtenu sur inscription.

**Étant donné** un lieu **pleinement intérieur**
**Quand** le bot répond
**Alors** il **ne mentionne aucune condition extérieure** et ne propose aucune alternative pour ce
motif — pas d'encadré, et pas non plus de mention rassurante.

**Étant donné** l'un des deux services indisponible
**Quand** l'appel échoue
**Alors** le port rend un résultat typé nommant le service, **aucune valeur par défaut n'est
substituée**, et le parcours reste terminable sans lui.

### Story 7.4 : Deux horizons distincts, et le plus court commande

En tant que **personne qui prend un créneau dans cinq jours**,
je veux qu'on me dise ce qu'on ne sait pas plutôt qu'on me le devine,
afin qu'une absence de donnée ne se lise pas comme une bonne nouvelle.

**Exigences :** FR-10 · AD-19

**Acceptance Criteria :**

**Étant donné** les deux ports
**Quand** on les inspecte
**Alors** ce sont **deux ports séparés** aux horizons **déclarés** distincts — seize jours pour la
météo, environ un pour la qualité de l'air (AD-19).

**Étant donné** un créneau **à cinq jours**
**Quand** l'évaluation s'exécute
**Alors** elle rend les **deux premiers seuils** — chaleur et vent — et **nomme** le troisième
comme **non établi**
**Et** aucune valeur n'est inventée pour lui.

**Étant donné** un créneau hors de portée des **deux** horizons
**Quand** le bot répond
**Alors** il annonce qu'il ne sait pas encore et propose de revérifier plus tard.

**Étant donné** que cette branche est le **cas courant** pour l'air et non l'exception
**Quand** le bot en parle
**Alors** il le dit comme une **propriété du produit**, jamais comme une panne.

### Story 7.5 : Contre-proposer une heure, sans rien retenir

En tant que **personne à qui on propose 19 h au lieu de 15 h**,
je veux que choisir l'heure et décider d'y aller restent deux décisions,
afin qu'accepter une heure n'engage jamais quelqu'un d'autre à mon insu.

> Porte l'un des interdits du produit, au titre de la contrainte d'écriture **C3**.

**Exigences :** FR-10 · UX-DR18 · contrainte d'écriture C3

**Acceptance Criteria :**

**Étant donné** un créneau qui dépasse l'un des trois seuils
**Quand** le bot répond
**Alors** le contrôle intervient **avant** que le créneau soit retenu, jamais après
**Et** le bot propose une **heure alternative** dans la même journée, ou un autre jour, plutôt que
de se contenter d'alerter.

**Étant donné** une contre-proposition acceptée
**Quand** elle s'applique
**Alors** elle **fixe l'heure** et **ne retient rien** : le geste de *retenir un créneau* reste à
faire, et **aucun message ne part avant lui**.

**Étant donné** cette même contre-proposition
**Quand** elle s'applique
**Alors** elle **annonce ce qu'elle vient de changer** par la région de statut
**Et** l'heure retenue **s'écrit dans le fil**, à la suite de l'encadré.

**Étant donné** une personne qui refuse la contre-proposition
**Quand** elle poursuit
**Alors** le **créneau initial reste retenable** — l'alerte informe et n'interdit pas.

**Étant donné** l'absence de tout dépassement de seuil
**Quand** le bot poursuit
**Alors** il demande l'heure de la rencontre **en une phrase**.

---

## Epic 8 : Agenda

La rencontre sort du produit et entre dans l'agenda de l'utilisateur — le sien seulement, et
après un second consentement demandé au moment où il sert.

### Story 8.1 : Choisir son fournisseur et consentir à l'écriture

En tant que **personne qui vient de retenir un créneau**,
je veux choisir Google ou Outlook et autoriser l'écriture à ce moment-là,
afin qu'on ne m'ait pas demandé l'accès à mon agenda pour me connecter.

**Exigences :** FR-12 · AD-18 · UX-DR14

**Acceptance Criteria :**

**Étant donné** une rencontre qui vient d'être retenue
**Quand** le bloc `agenda-choice` s'affiche
**Alors** **Google et Outlook** sont présentés **au même rang**, aucune n'étant mise en avant
**Et** le motif de la demande est écrit **au-dessus du bloc, en prose**.

**Étant donné** un fournisseur choisi
**Quand** le consentement est demandé
**Alors** c'est un **troisième temps**, distinct du choix
**Et** la **portée d'écriture agenda** est demandée **à ce moment**, pour ce fournisseur, et
jamais lors de la connexion de FR-4 (AD-18).

**Étant donné** le retour de ce second parcours OAuth
**Quand** la page se rend
**Alors** le fil se rouvre **au même endroit**, brouillon intact — la règle vaut aux deux
passages.

**Étant donné** un consentement d'écriture **refusé**
**Quand** le bot répond
**Alors** le créneau **reste retenu** et le récapitulatif est posé dans le fil ; seule l'écriture
n'a pas lieu
**Et** le bot le dit et propose de réessayer plus tard — un refus de permission **n'annule jamais
la rencontre**.

### Story 8.2 : Écrire la rencontre, sans aucun numéro

En tant que **personne qui a autorisé l'accès**,
je veux voir la rencontre apparaître dans mon agenda,
afin de ne pas avoir à la recopier moi-même.

**Exigences :** FR-12

**Acceptance Criteria :**

**Étant donné** un consentement explicite
**Quand** l'écriture s'exécute
**Alors** l'événement porte le **sport**, le **prénom du partenaire**, le **lieu**, le **jour**,
l'**heure** et le **statut** de la rencontre.

**Étant donné** l'événement écrit
**Quand** on inspecte son contenu
**Alors** il ne contient **aucun numéro de téléphone**, nulle part.

**Étant donné** l'absence de confirmation explicite
**Quand** on inspecte l'agenda
**Alors** **aucune** écriture n'a eu lieu.

**Étant donné** l'agenda d'une personne autre que celle qui a donné l'accès
**Quand** on cherche une écriture du produit
**Alors** il n'y en a **aucune**, jamais — l'agenda du partenaire est hors périmètre.

### Story 8.3 : Mettre à jour l'événement à chaque changement de statut

En tant que **personne dont le partenaire vient de décliner**,
je veux que mon agenda le sache,
afin de ne pas garder un créneau qui n'a plus lieu d'être.

**Exigences :** FR-12, FR-13 *(part)* · AD-9

**Acceptance Criteria :**

**Étant donné** chacune des arêtes de la table de transitions d'E5
**Quand** elle est franchie
**Alors** l'événement d'agenda est **mis à jour**, sans exception — *abandonnée* comprise.

**Étant donné** l'arête vers **abandonnée**
**Quand** elle est franchie
**Alors** l'événement **est** mis à jour **et aucun courriel ne part**
**Et** c'est le « Fait quand » de ce lot : un abandon met l'événement à jour **sans** envoyer de
courriel.

**Étant donné** la mise à jour
**Quand** on cherche ce qui l'a déclenchée
**Alors** c'est la **transition**, jamais le statut d'arrivée seul (AD-9)
**Et** il n'existe aucun déclencheur générique « statut changé → écrire ».

### Story 8.4 : Un agenda indisponible n'annule jamais la rencontre

En tant que **personne dont l'agenda ne répond pas**,
je veux que ma rencontre existe quand même,
afin qu'une panne technique ne se lise pas comme la perte de la rencontre.

**Exigences :** FR-12 · NFR-2 · AD-13 · CAP-16 *(part)*

**Acceptance Criteria :**

**Étant donné** le fournisseur d'agenda indisponible
**Quand** l'écriture est tentée
**Alors** le port rend un **résultat typé** nommant le service et son motif, **jamais une
exception** (AD-13)
**Et** aucune valeur par défaut n'est substituée.

**Étant donné** cet échec
**Quand** le fil se rend
**Alors** une **ligne d'étape échouée** le dit nommément
**Et** le bot nomme ce qu'il n'a pas pu faire, **dit ce qui n'est pas perdu** — la rencontre
existe — et propose de réessayer l'écriture plus tard.

**Étant donné** ce même échec
**Quand** on inspecte l'état du domaine
**Alors** la rencontre existe, son statut est intact, et le partenaire a été prévenu.

---

## Epic 9 : Alertes différées

Ce qui reste à faire quand le vivier n'a personne : enregistrer la demande, et prévenir quand
quelqu'un arrive. Le chemin rare — 14 combinaisons sur 231 — et celui où le bot est le plus tenté
de broder.

### Story 9.1 : Poser une alerte quand le vivier est vide

En tant que **personne pour qui il n'y a personne aujourd'hui**,
je veux qu'on me prévienne si quelqu'un arrive,
afin de ne pas avoir à revenir vérifier chaque semaine.

**Exigences :** FR-9, FR-4 *(part)* · UX-DR21

**Acceptance Criteria :**

**Étant donné** un élargissement qui n'a produit aucun candidat
**Quand** le bot a fini d'annoncer le vide
**Alors** il **propose l'alerte différée** dans le même tour.

**Étant donné** une proposition d'alerte acceptée
**Quand** la personne n'a pas de compte
**Alors** la demande de compte est déclenchée (E4)
**Et** l'adresse du compte devient le canal de la notification.

**Étant donné** une alerte posée
**Quand** le bloc de récapitulatif d'alerte s'affiche
**Alors** il porte la demande, la validité de **60 jours** que le bot annonce à la pose, et **un
bouton d'annulation**
**Et** ce bouton **reste actif aussi longtemps que l'alerte vit** — seule exception du produit à
l'inertie du passé.

**Étant donné** une personne qui pose plusieurs alertes
**Quand** on les compte
**Alors** elles **coexistent** — la règle d'une seule *recherche active* ne s'y applique pas, une
alerte n'occupant aucun créneau
**Et** enchaîner Pilates → vide → alerte → squash → vide → alerte reste possible.

**Étant donné** une alerte posée
**Quand** le bot en parle
**Alors** il ne promet **aucun délai de réponse**.

### Story 9.2 : Déclencher sur correspondance exacte, à l'écriture d'un profil

En tant que **personne qui attend depuis trois semaines**,
je veux être prévenue dès que quelqu'un correspond vraiment,
afin de ne pas recevoir un courriel pour quelqu'un que la recherche ne m'aurait pas proposé.

**Exigences :** FR-9 · AD-5 *(part)* · arbitrage A

**Acceptance Criteria :**

**Étant donné** un profil écrit au vivier
**Quand** les alertes sont évaluées
**Alors** le déclenchement a lieu à **l'écriture d'un profil**, pas seulement à la création d'un
compte
**Et** un **utilisateur existant qui change de sport** déclenche l'alerte de quelqu'un d'autre au
même titre qu'une inscription — c'est le « Fait quand » de ce lot.

**Étant donné** un profil qui correspond
**Quand** la correspondance est évaluée
**Alors** elle est **exacte** : même clé de sport normalisée, **même niveau**, **au moins un jour
commun**.

**Étant donné** un profil qui ne correspondrait **qu'après élargissement sur le jour**
**Quand** la correspondance est évaluée
**Alors** l'alerte **ne se déclenche pas**.

**Étant donné** une correspondance exacte trouvée
**Quand** la notification est demandée
**Alors** un envoi de type courriel est demandé à **`PortEnvois`**, à l'adresse du compte, **dans
l'heure** qui suit l'inscription du profil correspondant *(arbitrage A — asserté contre le
double)*.

**Étant donné** le courriel
**Quand** on en inspecte le contenu
**Alors** il porte le strict nécessaire — qu'un partenaire correspond, et pour quel sport — et
**aucune donnée du partenaire** ; tout le reste se lit en revenant dans le fil.

### Story 9.3 : Annuler une alerte depuis la conversation

En tant que **personne qui a trouvé autrement**,
je veux annuler mon alerte en le disant,
afin de ne pas être prévenue pour quelque chose que je ne cherche plus.

**Exigences :** FR-9 · UX-DR21 *(part)*

**Acceptance Criteria :**

**Étant donné** une alerte en cours
**Quand** la personne l'annule — en cliquant le bouton du bloc, ou en le disant
**Alors** l'alerte cesse et ne se déclenchera plus.

**Étant donné** cette annulation
**Quand** elle a lieu
**Alors** la **région de statut** l'annonce en phrase complète et autonome, comme toute mutation
d'un bloc persistant.

**Étant donné** plusieurs alertes en cours
**Quand** l'une est annulée
**Alors** les autres sont intactes
**Et** le fil garde la trace de celle qui a été annulée, jamais supprimée en silence.

### Story 9.4 : Expirer une alerte à 60 jours

En tant que **personne dont l'alerte n'a jamais servi**,
je veux qu'on me le dise plutôt qu'elle s'éteigne en silence,
afin de savoir que je peux la reposer.

**Exigences :** FR-9 · AD-15

**Acceptance Criteria :**

**Étant donné** la tâche périodique d'E5
**Quand** elle s'exécute
**Alors** elle porte sa **seconde charge** : l'expiration des alertes à **60 jours** (AD-15).

**Étant donné** une alerte qui atteint 60 jours sans correspondance
**Quand** la tâche s'exécute
**Alors** l'alerte expire
**Et** un envoi de type courriel est demandé à `PortEnvois` pour le dire.

**Étant donné** une alerte expirée
**Quand** on la cherche dans le fil
**Alors** elle **reste visible avec son statut**, jamais supprimée en silence
**Et** elle est reconductible en une phrase.

**Étant donné** la même tâche exécutée deux fois de suite
**Quand** on compare les états
**Alors** rien n'a changé au second passage — elle est **rejouable sans effet**.
