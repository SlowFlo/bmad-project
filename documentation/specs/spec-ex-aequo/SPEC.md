---
id: SPEC-ex-aequo
companions:
  - glossaire.md
  - criteres-acceptation.md
  - statuts-rencontre.md
  - criteres-reussite.md
  - donnees-amorcage.md
  - ../../planning-artifacts/architecture/architecture-bmad-2026-08-28/ARCHITECTURE-SPINE.md
  - ../../planning-artifacts/architecture/architecture-bmad-2026-08-28/DECOUPAGE.md
  - ../../planning-artifacts/ux-designs/ux-bmad-2026-08-26/EXPERIENCE.md
  - ../../planning-artifacts/ux-designs/ux-bmad-2026-08-26/DESIGN.md
sources:
  - ../../planning-artifacts/prds/prd-bmad-2026-08-26/prd.md
  - ../../planning-artifacts/prds/prd-bmad-2026-08-26/addendum.md
  - ../../planning-artifacts/prds/prd-bmad-2026-08-26/research-niveau.md
  - ../../planning-artifacts/prds/prd-bmad-2026-08-26/research-paysage.md
  - ../../planning-artifacts/architecture/architecture-bmad-2026-08-28/SOLUTION-DESIGN.md
---

> **Contrat canonique.** Ce SPEC et les fichiers de `companions:` forment le contrat complet et validé en préservation : quoi construire, quoi tester, quoi valider. Les documents de `sources:` servent la traçabilité — ne les consulter que pour le raisonnement narratif que ce contrat omet délibérément.

# Ex Aequo — chatbot de mise en relation sportive

## Why

**Une vision à réaliser, doublée d'un pari assumé.** Trouver quelqu'un avec qui pratiquer son sport, à son niveau, est pénible : on demande dans un groupe WhatsApp, on relance, personne ne répond, on n'y va pas. Ce que la personne cherche est fonctionnel — un créneau confirmé sans avoir à relancer trois personnes — mais aussi **émotionnel** : éviter l'humiliation douce du match trop déséquilibré, dans les deux sens, se faire écraser ou passer une heure à faire du renvoi de balle par politesse. C'est ce second registre qui rend l'égalité stricte de niveau non négociable. Les produits existants sont des places de marché de réservation de terrains où la mise en relation est annexe, et s'utilisent avec des listes, des cartes et des filtres. Ex Aequo fait le pari inverse — **une conversation** : l'utilisateur ouvre le site, dit « je veux jouer au tennis mardi », et le bot cherche quelqu'un de son niveau, négocie un jour jouable, vérifie que les conditions extérieures sont raisonnables, propose un endroit et pose la rencontre dans son agenda, en un seul fil, sans formulaire. Aucun produit grand public de mise en relation entre joueurs n'utilise le chat comme interface principale : c'est soit la différenciation du produit, soit le signe que la conversation n'est pas la bonne forme, et SM-5 se donne les moyens de savoir laquelle des deux lectures est la bonne. Le produit ne dessert que **Lyon** parce que la liquidité de cette catégorie est par lieu et non à l'échelle d'un pays. Sa raison d'être secondaire, pleinement assumée : servir de terrain d'apprentissage sur les systèmes agentiques à son constructeur, qui est aussi son unique utilisateur.

## Capabilities

Les conséquences testables de chaque capacité vivent dans [criteres-acceptation.md](criteres-acceptation.md). Le vocabulaire employé ici est contraignant et défini dans [glossaire.md](glossaire.md).

- **CAP-1** *(FR-1)*
  - **intent:** Un visiteur peut ouvrir le site et dialoguer avec le bot sans compte ni inscription.
  - **success:** La page d'entrée présente le chatbot utilisable sans écran d'authentification préalable, et un visiteur sans compte obtient des propositions de partenaires nommés.

- **CAP-2** *(FR-2)*
  - **intent:** Le bot extrait d'un message libre le sport, les jours et le niveau, et réclame ce qui manque un élément à la fois.
  - **success:** « je veux jouer au tennis mardi aprem, je suis intermédiaire » produit la demande {Tennis, [Mardi], Intermédiaire} sans aucune question ; « j'ai un niveau OK » n'est ni interprété ni stocké et ouvre les trois choix ; un sport absent du vivier reçoit la réponse d'un vivier vide et non un refus.

- **CAP-3** *(FR-3)*
  - **intent:** Un utilisateur devient trouvable par les recherches des autres à la création de son compte, avec un sport et un seul.
  - **success:** Après création de compte, une recherche « tennis, mardi, intermédiaire » renvoie le nouveau profil ; une demande sur un autre sport remplace sport, niveau et jours en une écriture atomique, après que le bot a annoncé le coût.

- **CAP-4** *(FR-4)*
  - **intent:** Le bot demande la création d'un compte lorsqu'il va exposer l'utilisateur à une autre personne ou devra le recontacter — jamais avant.
  - **success:** Chercher, obtenir des propositions, retenir un candidat et consulter la jouabilité ne déclenchent aucune demande de compte ; retenir un créneau la déclenche, et le bot énonce alors son motif et dit que le compte rend l'utilisateur trouvable.

- **CAP-5** *(FR-5)*
  - **intent:** Le bot renvoie les profils du vivier partageant le sport, au moins un jour disponible et le niveau exact de la demande.
  - **success:** « Tennis, mardi, débutant » renvoie Emma Leroy ; « Tennis, mardi, intermédiaire » ne renvoie aucun candidat ; aucun candidat renvoyé n'est d'un autre niveau, à aucune étape.

- **CAP-6** *(FR-6)*
  - **intent:** Sans résultat exact, le bot relâche le jour — et lui seul — en conservant le niveau, et présente les candidats avec leurs jours.
  - **success:** « Tennis, mardi, intermédiaire » renvoie Anna, Iris et Tessa avec leurs jours ; au plus trois candidats, classés par délai d'attente croissant, l'ordre du vivier départageant les ex æquo, de sorte que deux recherches identiques rendent le même trio dans le même ordre.

- **CAP-7** *(FR-8)*
  - **intent:** Quand l'élargissement ne produit aucun candidat, le bot le dit clairement plutôt que de broder.
  - **success:** La réponse nomme le sport et le jour tentés, dit que tous les autres jours ont été regardés, conclut qu'il n'y a personne à ce niveau, et enchaîne sur CAP-8 — sans jamais nommer une personne absente du vivier.

- **CAP-8** *(FR-9)*
  - **intent:** Faute de résultat, le bot propose d'enregistrer la demande et de prévenir l'utilisateur par courriel si un profil correspondant rejoint le vivier.
  - **success:** L'alerte se déclenche sur une correspondance **exacte** — même sport, même niveau, au moins un jour commun — notifie dans l'heure, vaut 60 jours puis expire avec un courriel ; plusieurs alertes coexistent et chacune s'annule depuis la conversation.

- **CAP-9** *(FR-10)*
  - **intent:** Avant qu'un créneau soit retenu, le bot évalue les conditions extérieures du lieu envisagé et fixe l'heure de la rencontre à ce moment.
  - **success:** Pour un lieu en extérieur, un dépassement de l'un des trois seuils — ressenti > 28 °C, rafales > 40 km/h, ATMO ≥ 4 — est signalé avant que l'utilisateur retienne, avec une heure alternative proposée ; pour un lieu pleinement intérieur, aucune condition extérieure n'est mentionnée ; l'alerte informe et n'interdit pas, et accepter une heure ne retient rien.

- **CAP-10** *(FR-11)*
  - **intent:** Le bot propose des équipements lyonnais adaptés au sport, en précisant pour chacun s'il est couvert ou en extérieur.
  - **success:** Chaque lieu proposé est à Lyon ou dans son agglomération, correspond au sport, et porte sa nature — c'est elle qui décide de CAP-9 ; un secteur peut être demandé mais jamais exigé, et sans donnée le bot le dit au lieu d'inventer un lieu plausible.

- **CAP-11** *(FR-12)*
  - **intent:** L'utilisateur peut faire ajouter la rencontre à son agenda Google ou Outlook.
  - **success:** Les deux fournisseurs sont proposés au choix, l'écriture n'a jamais lieu sans confirmation explicite, et l'événement porte le sport, le prénom du partenaire, le lieu, le jour, l'heure et le statut — et **aucun numéro de téléphone**.

- **CAP-12** *(FR-13)*
  - **intent:** Une rencontre porte un statut et un seul, qui détermine seul ce que le bot a le droit de dire ; tant qu'une rencontre est *en attente* ou *confirmée*, aucune nouvelle recherche n'est lancée.
  - **success:** Les cinq statuts, leurs transitions et les effets attachés à chaque arête se comportent comme [statuts-rencontre.md](statuts-rencontre.md) le spécifie ; une demande formulée pendant qu'une rencontre occupe la place n'est pas lancée, et le bot nomme le sport, le partenaire et le jour occupés en proposant l'abandon dans la même phrase.

- **CAP-13** *(FR-14)*
  - **intent:** Quand l'utilisateur retient un créneau, le bot prévient le partenaire par un message auto-explicatif portant un lien d'acceptation à usage unique.
  - **success:** Le message part par SMS si la personne a un numéro, par courriel si elle est inscrite et n'en a pas donné ; il énonce son propre motif, porte sport, jour, heure, lieu et prénom du demandeur, aucune coordonnée, et un moyen de ne plus jamais être contacté ; la page rend l'un des **sept états terminaux** d'EXPERIENCE.md et jamais une erreur nue.

- **CAP-14** *(FR-16)*
  - **intent:** Un profil entre au vivier à la création du compte, y reste après ses rencontres, et n'en sort que s'il le demande ; ce qu'une rencontre produit est un jour bloqué, pas une sortie.
  - **success:** Une rencontre *en attente* ou *confirmée* bloque, pour les **deux** profils, le seul jour de la rencontre ; *déclinée*, *abandonnée* et *expirée* le libèrent immédiatement, l'abandon pour les deux profils ; le jour accepté est conservé au profil ; un profil sorti du vivier ne revient dans aucune recherche.

- **CAP-15** *(exigence non fonctionnelle de reprise)*
  - **intent:** Un utilisateur qui revient retrouve son fil, ses demandes, ses alertes et sa rencontre.
  - **success:** Le fil n'est jamais purgé ni réinitialisé ; un utilisateur inscrit reçoit en ouverture du tour du bot un récapitulatif **en prose** portant au plus une rencontre, inséré en bas du fil comme tout autre tour et ne re-rendant aucun bloc ; un visiteur sans compte retrouve son fil 30 jours sur le même navigateur, après quoi il est effacé.

- **CAP-16** *(PRD §7, AD-3)*
  - **intent:** Pendant que le bot travaille, l'utilisateur voit quelles sources sont réellement interrogées et le sort de chacune.
  - **success:** Chaque port qui peut échouer d'une façon que la personne doit connaître émet une étape à l'entrée et à la sortie, portant le service et son sort ; le signe de vie part au premier appel d'outil, avant le premier jeton du modèle ; une source en échec est annoncée nommément, ce qui rend cohérente l'absence de sa donnée dans la réponse ; le modèle ne dispose d'aucun moyen d'émettre une étape lui-même.

## Constraints

- **Le bot n'invente rien.** Aucun nom de partenaire hors du vivier, aucune donnée météo, aucun terrain, aucune disponibilité, aucune confirmation qui n'ait été donnée. Les étapes annoncées correspondent aux sources réellement interrogées. En cas de doute, le bot dit qu'il ne sait pas. C'est la contrainte la plus structurante, en tension permanente avec le fait que l'interface est un LLM.
- **Le LLM est un adaptateur primaire, jamais le noyau** *(AD-1)*. Il ne produit que trois choses : l'extraction d'une demande, le choix de l'outil, et la prose. Aucun nom, aucune valeur météo, aucun lieu, aucun statut ne vient de la génération. Aucun module du domaine n'importe le SDK du modèle.
- **Un seul saut LLM par tour de parole** *(AD-2)*. Un tour est une seule boucle de *tool runner* ; aucun outil n'émet d'appel LLM imbriqué, et il n'existe ni routeur ni agent spécialisé en amont.
- **Égalité stricte de niveau, sans exception, à aucune étape.** Le jour est le seul axe d'élargissement du produit. Le coût est chiffré et refusé en connaissance de cause : élargir au niveau voisin ferait tomber le résidu de combinaisons vides de 6,1 % à 3,0 %.
- **Le niveau est déclaré, demandé une fois, jamais vérifié, jamais corrigé** — et **jamais demandé pendant la recherche** : ni pour élargir, ni après avoir montré des candidats, ni pour rattraper un résultat vide. Un refus de répondre produit un *niveau inconnu*, état légal qui rend le profil inerte des deux côtés.
- **Lyon uniquement.** Décision de conception fondée sur la liquidité par lieu, pas une limite de départ à lever.
- **Un profil porte un sport, et un seul.** Une demande sur un autre sport le remplace — sport, niveau et jours dans une seule transaction — après que le bot a annoncé ce que le remplacement coûte. Jamais une accumulation, jamais un second profil sous le même compte.
- **L'appariement porte sur la clé de sport normalisée, jamais sur le libellé** *(AD-5)*. Sans elle, « tennis » et « Tennis » sont deux sports qui ne se rencontrent jamais et le vivier se pulvérise en silence. La table de synonymes redirige à l'écriture, jamais à la lecture ; un libellé inconnu fonde un sport.
- **Une seule recherche active à la fois**, et le bot nomme ce qui occupe la place en donnant la sortie dans la même phrase. Seules comptent les rencontres nées des demandes de la personne elle-même : être sollicité par quelqu'un d'autre n'occupe pas la place. Les alertes différées ne sont pas concernées.
- **La disponibilité et la recherche active sont dérivées, jamais stockées** *(AD-6, AD-7)*. Ni champ « bloqué », ni champ « recherche en cours » : les deux se dérivent d'une jointure sur les rencontres *en attente* ou *confirmée*. Le blocage par jour est **symétrique** ; la précondition de recherche ne lit que le **côté demandeur**.
- **Les effets sont attachés aux transitions, jamais aux statuts** *(AD-9)*. Un déclencheur générique « statut changé → prévenir » viole le produit dès sa première ligne : l'arête vers *abandonnée* met à jour l'événement d'agenda et n'émet ni courriel ni SMS.
- **Retenir un créneau est une transaction unique** *(AD-8)*. Vérification de la précondition, création de la rencontre, création du jeton et inscription à la boîte d'envoi dans une seule transaction. L'acceptation côté partenaire en est une autre, qui échoue bruyamment sur une rencontre *confirmée* conflictuelle.
- **Aucun SMS ne part vers un numéro hors de la plage de fiction ARCEP `+336 39 98 XX XX`, sauf vers un numéro qu'un utilisateur inscrit a lui-même saisi.** Tout autre numéro fait échouer l'envoi bruyamment. C'est une règle de production, pas un interrupteur de test, et elle lit la **provenance portée dans le modèle**, jamais le préfixe *(AD-11, AD-12)*.
- **Aucun numéro de téléphone n'apparaît nulle part** : ni dans l'interface, ni dans un message sortant, ni dans l'événement d'agenda. Le bot nomme ces personnes et les contacte lui-même ; il ne diffuse pas leurs coordonnées.
- **La validité du lien d'acceptation est une conjonction** *(AD-10)* : le sort affiché se dérive du statut de la rencontre **et** de l'état du jeton, résolus ensemble à la lecture. Le jeton est opaque, non devinable, à usage unique.
- **Un échec de service externe est une valeur, jamais une exception** *(AD-13)*. Tout port retourne un résultat typé nommant le service et son motif ; aucune valeur par défaut n'est jamais substituée, et le parcours reste terminable sans le service tombé. Le LLM est le seul échec sans repli, et il se dit avec un texte arrêté et non généré *(AD-20)*.
- **Météo et qualité de l'air sont deux ports aux horizons déclarés distincts** *(AD-19)* — seize jours contre environ un. Un créneau hors de portée de l'un rend les seuils qu'il a pu établir et **nomme** celui qu'il n'a pas pu.
- **Signe de vie en moins de 2 s, réponse complète en moins de 20 s.** Au-delà, le bot dit ce qu'il est en train de faire et pourquoi c'est long. Dans une conversation, l'attente muette se lit comme une panne.
- **Le fil est l'application entière côté demandeur**, et il est *append-only* : un tour écrit ne change plus, tout contrôle d'un tour résolu devient inerte, et seuls le récapitulatif de rencontre et le récapitulatif de profil mutent sur place, uniques par entité *(AD-17)*. Le produit a exactement deux surfaces hors du fil, et aucune ne sert le demandeur : la redirection OAuth et la page d'acceptation.
- **L'autorisation OAuth est incrémentale** *(AD-18)*. La connexion de CAP-4 ne demande qu'identité et adresse ; la portée d'écriture agenda fait l'objet d'un second consentement au moment de CAP-11, pour le fournisseur choisi alors. Au retour, le fil se rouvre au même endroit, brouillon intact.
- **Web responsive, PC d'abord, parité fonctionnelle stricte**, plancher **320 px** sans débordement horizontal, y compris sous l'espacement forcé de WCAG 1.4.12. Pas d'application native, donc pas de notification push : les notifications différées passent par le courriel et le SMS.
- **Thème sombre unique.** Pas de bascule clair/sombre en v1. Un seul assouplissement existe, sous `prefers-contrast: less`.
- **Vouvoiement, registre de secrétariat compétent.** La mauvaise nouvelle arrive en premier sans coussin ; le bot ne se félicite jamais ; chaque demande énonce son motif au moment où elle est faite ; tout message d'échec dit ce qui n'est pas perdu et ne s'ouvre jamais sur une excuse ; l'inconnu se conjugue à la première personne — « je ne sais pas encore », jamais « non déterminé ». Vocabulaire interdit et formulations arrêtées : voir EXPERIENCE.md, *Voice and Tone*.
- **Le bot rend la main plutôt que de la retenir.** Le seul verbatim du corpus qui porte sur l'interface choisie est hostile — « aucun moyen de parler à un vrai humain, toujours renvoyé vers un chatbot ». Ce que les gens détestent n'est pas le chat, c'est de ne pas pouvoir en sortir : quand quelqu'un demande une liste, une carte ou un filtre, le bot ne répond pas qu'il ne sait pas faire — il donne ce qu'il peut sous une forme plus dense, et note la demande. SM-5 surveille ce symptôme.
- **Vie privée : le bot demande le minimum nécessaire et dit pourquoi à chaque fois.** L'accès à l'agenda sert à écrire la rencontre convenue, rien d'autre. Le message envoyé au partenaire explique toujours pourquoi il arrive et porte un moyen de ne plus jamais être contacté — droit qui vaut pour les deux populations du vivier. Le numéro d'un utilisateur inscrit est facultatif : sans numéro, il est prévenu par courriel et ne reçoit aucun SMS.
- **Le vocabulaire de [glossaire.md](glossaire.md) est employé littéralement, sans synonyme**, jusque dans les noms de types, de champs et de fonctions.
- **Enveloppe technique : un seul processus exécuté en local**, base SQLite fichier à côté du dépôt, aucun conteneur, aucun hébergement, aucun environnement multiple. Les redirections OAuth sur `http://localhost:<port>` sont acceptées par les deux fournisseurs.

## Non-goals

- **Pas de réservation ni de paiement.** Le produit propose un endroit ; il ne réserve rien et ne connaît aucune disponibilité de terrain.
- **Pas de réseau social sportif.** Pas de fil d'actualité, pas d'abonnements, pas de profils publics à parcourir.
- **Pas de classement public.** Un classement visible crée des incitations à la manipulation impossibles à contrôler à cette échelle.
- **Pas de matchs à plusieurs.** Deux personnes, jamais une équipe. Un footballeur y trouve un partenaire d'entraînement, pas un match.
- **Le bot n'est pas un assistant généraliste.** Il fait ce produit, et le dit quand on lui demande autre chose.
- **Aucune autre ville que Lyon.**
- **Aucune forme de calibration du niveau** : ni questionnaire comportemental, ni inférence à partir de faits déclarés, ni correction par les résultats. Aucune colonne ne l'anticipe — ni `mu`, ni `sigma`, ni historique de résultats : un schéma qui la préparerait laisserait croire qu'elle est prévue.
- **Pas de signal d'équilibre après rencontre** (« trop facile / équilibré / trop dur »). Écarté sciemment pour tenir le périmètre, pas parce qu'il serait cher — voir QO-5.
- **Pas de parcours conversationnel côté partenaire.** Un profil d'amorçage accepte ou refuse par un lien, sans conversation. La relance, la contre-proposition de créneau et l'annulation entre deux utilisateurs inscrits ne sont pas spécifiées — voir QO-2.
- **Plusieurs sports par profil.** Un profil porte un sport ; une demande sur un autre le remplace.
- **L'heure de disponibilité dans les profils.** Les données d'amorçage ne descendent pas sous le jour ; « mardi après-midi » est traité comme « mardi ». L'heure **de la rencontre**, elle, est dans le périmètre.
- **Rien de ce qui suit le créneau** : ni annulation après coup, ni relance, ni no-show. Le produit s'arrête à l'écriture dans l'agenda.
- **La fraîcheur d'une fiche.** Une colonne de dernière activité est posée et n'est jamais lue en v1 ; le seuil et son usage restent du produit — voir QO-6.
- **Pas de vérification d'identité, de signalement ni de réputation.** Acceptable pour un projet d'apprentissage à vivier fictif ; ça ne le serait pas avec de vrais utilisateurs.
- **Pas de déploiement, d'hébergement, de secrets managés ni d'observabilité de production.** À rouvrir entièrement avant toute exposition publique.
- **Pas de fournisseur SMS réel.** Les 86 numéros d'amorçage sont dans une plage garantie non attribuée : aucun opérateur ne les délivrera jamais. La boîte d'envoi persistée est le transport, et le filtre de destinataire reste une règle de production sans lui.
- **Pas de stratégie de compaction du contexte.** À ouvrir sur la première conversation qui approche la fenêtre du modèle, pas avant.

## Success signal

Le parcours complet de **UJ-1** — de « je veux jouer au tennis mardi » à une rencontre *en attente* écrite dans l'agenda, le partenaire prévenu — se déroule de bout en bout, en une seule conversation, sans intervention manuelle ; et **au moins 85 % des 127 combinaisons sans résultat exact** des données d'amorçage produisent au moins un candidat du niveau exact demandé, contre un plafond atteignable de 89 %. Le second critère est mesurable par un test dès que le moteur d'appariement existe, sans une ligne de LLM. Les six critères complets, leur contre-métrique et la mise en garde sur ce qu'ils ne mesurent pas vivent dans [criteres-reussite.md](criteres-reussite.md).

## Assumptions

- Le prénom du protagoniste de UJ-1 est un substitut, à remplacer par une personne réelle ; il est choisi absent des données d'amorçage pour qu'aucun scénario de test ne le confonde avec un profil du vivier.
- L'heure de disponibilité est ignorée en v1 plutôt que collectée pour les seuls nouveaux profils, afin de ne pas créer deux qualités de données dans le vivier.
- Le remplacement du sport est la conséquence retenue du profil mono-sport. Refuser la seconde demande, ou tenir deux profils sous un même compte, étaient les deux autres issues ; aucune des trois n'a été mesurée.
- Les 60 jours de validité d'une alerte et la notification dans l'heure sont posés par défaut, à confronter au rythme réel des inscriptions.
- L'usage visé — un trou dans un agenda, quelques jours à l'avance — ne produit pas de file d'attente, donc la restriction d'une seule recherche active ne gêne personne. Jamais observé ; c'est QO-8.
- Le partenaire qui rouvre son lien apprend l'abandon à temps, et celui qui ne le rouvre pas ne perdait rien. Déduit de l'invariant du contact unique plutôt qu'observé ; c'est QO-9.
- Les bornes chiffrées des exigences non fonctionnelles — 2 s, 20 s, 30 jours — sont posées par défaut faute d'exigence exprimée : elles sont là pour être vérifiables, pas parce qu'elles ont été mesurées.
- Les seuils des critères de réussite — 85 %, une session sur cinq, 4 tours — sont posés par défaut. Seul le 85 % est adossé à un calcul.
- Le plancher de largeur retenu est **320 px** (EXPERIENCE.md) et non 360 px (PRD §6) : l'écart est délibéré et va dans le sens du plus exigeant. Les maquettes ont été mesurées à 320 px sans débordement horizontal.

## Open Questions

- **QO-1 —** Le protagoniste de UJ-1 n'a pas de nom réel ; à remplacer par une personne concrète.
- **QO-2 —** Que se passe-t-il quand deux utilisateurs inscrits négocient ? L'acceptation simple est couverte par CAP-13 ; la relance, la contre-proposition de créneau et l'annulation restent hors périmètre v1 et deviendront nécessaires.
- **QO-5 —** Aucun critère ne mesure la qualité d'une rencontre, seulement son existence. Tant que le signal d'équilibre manque, le produit ne peut pas savoir s'il tient sa promesse — aggravé par le retrait de la contre-métrique SM-C1.
- **QO-6 —** Le seuil de fraîcheur d'une fiche et son usage restent à trancher côté produit. L'architecture a posé la colonne de dernière activité et ne la lit jamais en v1.
- **QO-7 —** Rien ne corrige jamais un niveau déclaré. Deux signaux gratuits existent : le **jour** choisi est propre et exploitable, la **personne** choisie ne l'est pas, ce choix étant confondu avec la disponibilité. À reprendre avant toute v2 touchant au niveau.
- **QO-8 —** Rien ne dit si la restriction d'une seule recherche active gêne. Condition de levée : la première file d'attente observée. Elle se lève sans rien casser.
- **QO-9 —** Rien ne dit ce que coûte le silence sur l'abandon. Condition de levée : la première rencontre confirmée puis abandonnée à plus d'une semaine de son créneau.
> **Fermé le 2026-08-30.** Ce contrat portait ici une question — quatre décisions prises en aval que le SPEC tenait pour acquises sans qu'elles soient redescendues au PRD. Le **PRD v5** en a absorbé trois : la projection de la nature du lieu vers *jouabilité applicable* (FR-10), la fermeture de QO-4 (§5.4 et §11), et l'horizon de la qualité de l'air (FR-10, conséquence testable et `[NOTE FOR PM]`). La quatrième, QO-6, **reste ouverte des deux côtés par décision** et figure ci-dessus. Amont et contrat disent désormais la même chose ; aucune capacité n'a bougé.
