# Critères d'acceptation — Ex Aequo

Companion de [SPEC.md](SPEC.md). Une entrée par capacité : les conséquences testables que le contrat exige. Le vocabulaire est celui de [glossaire.md](glossaire.md), employé littéralement.

Les identifiants `FR-n` d'origine sont conservés pour la traçabilité vers le PRD.

---

## CAP-1 — Dialoguer sans authentification *(FR-1)*

- La page d'entrée présente le chatbot utilisable, sans écran d'authentification préalable.
- Un visiteur sans compte peut formuler une demande et recevoir des propositions de partenaires nommés.

## CAP-2 — Extraire une demande du langage naturel *(FR-2)*

- « je veux jouer au tennis mardi aprem, je suis intermédiaire » produit la demande {sport: Tennis, jours: [Mardi], niveau: Intermédiaire} sans qu'aucune question soit posée.
- « j'ai un niveau OK » n'est ni interprété ni stocké : le bot ouvre les trois choix, avec son motif attaché.
- Si le sport, le jour **ou** le niveau manque, le bot réclame un seul élément à la fois avant de lancer la recherche.
- Une demande sur un sport absent du vivier — le squash, le badminton — reçoit la réponse d'un vivier vide (CAP-7) et non un refus : le premier pratiquant à le demander fonde ce sport.
- Une demande qui vise explicitement une autre ville que Lyon reçoit une réponse explicite plutôt qu'une recherche vide.
- Une demande complète formulée alors qu'une *recherche active* occupe déjà la place n'est pas lancée : le bot nomme ce qui occupe et donne la sortie dans la même phrase (CAP-12).
- **Le bot ne demande jamais le niveau pendant la recherche** : ni pour élargir, ni après avoir montré des candidats, ni pour rattraper un résultat vide.
- Un refus de répondre est accepté : le profil portera un *niveau inconnu*, et le bot dit ce que ça coûte avant que la personne tranche.
- « tennis », « Tennis » et « Tennis » produisent **une seule** clé de sport ; les 11 sports des données d'amorçage produisent 11 clés, pas 12.

## CAP-3 — Enregistrer l'utilisateur dans le vivier *(FR-3)*

- Un visiteur sans compte ne sort jamais comme candidat d'une recherche.
- Après création du compte, une recherche « tennis, mardi, intermédiaire » renvoie le nouveau profil.
- Une nouvelle demande sur le sport déjà porté met à jour ses jours et son niveau.
- Une demande sur un **autre** sport remplace le sport du profil, son niveau et ses jours, **en une seule transaction**. Le bot annonce le remplacement avant de l'appliquer et dit ce qu'il coûte : la personne cesse d'être trouvable sur le sport précédent.
- Un profil de *niveau inconnu* n'est jamais renvoyé par une recherche.
- Le compte est la clé d'identité du profil : deux conversations d'une même personne connectée au même compte ne produisent jamais deux profils.

## CAP-4 — Demander un compte au moment de la mise en relation *(FR-4)*

- Rechercher, obtenir des propositions, retenir un candidat et consulter la jouabilité ne déclenchent aucune demande de compte.
- **Retenir un créneau avec un partenaire** la déclenche. Accepter une alerte différée (CAP-8) la déclenche également.
- Le bot énonce la raison de la demande au moment où il la formule, **et dit que le compte rend l'utilisateur trouvable par les autres**.
- La connexion Google ou Microsoft fournit l'adresse électronique du compte, qui devient le canal des notifications différées. **Cette première autorisation ne demande qu'identité et adresse** : la portée d'écriture agenda fait l'objet d'un second consentement au moment de CAP-11 (AD-18).
- Au retour d'OAuth, le fil se rouvre **au même endroit**, brouillon de saisie intact, sans message de bienvenue supplémentaire, et **sans ouvrir un second fil** (AD-21).
- Le numéro de téléphone est facultatif et n'est jamais exigé pour terminer un parcours.

## CAP-5 — Recherche exacte *(FR-5)*

- « Tennis, mardi, débutant » renvoie Emma Leroy.
- « Tennis, mardi, intermédiaire » ne renvoie aucun candidat.
- Aucun candidat renvoyé n'est d'un autre niveau que celui demandé — ni après élargissement, ni sur proposition, ni sur demande de l'utilisateur.
- Un profil dont le jour demandé est **bloqué** par une rencontre n'est pas renvoyé pour ce jour-là, mais continue de l'être pour ses autres jours (CAP-14).
- Un profil de *niveau inconnu* n'est jamais renvoyé.
- L'utilisateur lui-même n'est jamais renvoyé comme son propre partenaire.
- La comparaison porte sur la **clé de sport normalisée**, jamais sur le libellé affiché (AD-5).

## CAP-6 — Élargir sur le jour *(FR-6)*

- « Tennis, mardi, intermédiaire » renvoie Anna, Iris et Tessa avec leurs jours respectifs.
- Les candidats proposés sont exactement du niveau demandé.
- La proposition indique explicitement que le jour demandé n'était pas disponible.
- **Le bot présente au plus trois candidats**, classés par **délai d'attente croissant** : pour chaque candidat, le nombre de jours à attendre depuis le jour demandé jusqu'à sa prochaine disponibilité, en tournant vers l'avant sur la semaine (depuis mardi : mercredi = 1, jeudi = 2, … lundi = 6). Le plus tôt d'abord.
- À délai égal — le cas le plus fréquent sur les données d'amorçage — l'ordre est celui du vivier, de sorte que deux recherches identiques renvoient toujours le même trio dans le même ordre.
- Au-delà de trois candidats, le bot dit combien il y en a d'autres et propose de les montrer.
- Le jour est le **seul** axe d'élargissement : aucune relaxation du niveau n'existe dans le produit.

## CAP-7 — Annoncer l'absence de résultat sans broder *(FR-8)*

- « Pilates, avancé » ne produit aucun nom de partenaire, quel que soit le jour. « Pilates, intermédiaire » non plus : ce sont les deux seules paires sport × niveau vides des données d'amorçage.
- **La réponse nomme le sport et le jour tentés, et dit ce qui a été élargi** — tous les autres jours — avant de conclure qu'il n'y a personne **à ce niveau**.
- Un sport que le vivier ne connaît pas encore reçoit cette même réponse et non un refus : le bot dit qu'il n'a encore personne dans ce sport.
- La réponse enchaîne sur la proposition d'alerte différée de CAP-8.
- Le bot ne propose jamais une personne absente du vivier, ni quelqu'un d'un autre sport que celui demandé.

## CAP-8 — Alerte différée *(FR-9)*

- L'acceptation d'une alerte exige un compte (CAP-4).
- Une alerte se déclenche sur une **correspondance exacte** — même sport, même niveau, au moins un jour commun. Un profil qui ne correspondrait qu'après élargissement ne la déclenche pas.
- Le déclenchement a lieu à **l'écriture d'un profil**, pas seulement à la création d'un compte : un utilisateur existant qui change de sport déclenche l'alerte de quelqu'un d'autre au même titre qu'une inscription.
- La notification part par courriel à l'adresse du compte, dans l'heure qui suit l'inscription du profil correspondant.
- Une alerte vaut **60 jours**, puis expire ; le bot prévient par courriel lors de l'expiration.
- Un utilisateur peut porter plusieurs alertes simultanées, une par demande — la règle d'une seule *recherche active* ne s'y applique pas.
- L'utilisateur peut annuler une alerte à tout moment, depuis la conversation.

## CAP-9 — Évaluer la jouabilité d'un créneau *(FR-10)*

**Seuils d'alerte :**

| Condition | Seuil |
|---|---|
| Chaleur | température ressentie **supérieure à 28 °C** |
| Vent | rafales **supérieures à 40 km/h** |
| Qualité de l'air | indice **ATMO ≥ 4** sur l'échelle à six degrés |

- Le contrôle intervient **avant** que le créneau soit retenu, jamais après.
- Pour un lieu en extérieur, un créneau dépassant l'un des trois seuils est signalé avant que l'utilisateur le retienne.
- **La jouabilité dépend du lieu, pas du sport.** Seul un équipement **pleinement intérieur** désactive les trois seuils ; un équipement classé *extérieur couvert* y **reste soumis**, les trois seuils ne comportant aucune notion de pluie (FR-10 depuis la v5, AD-14). Sans lieu, aucune évaluation.
- Pour un lieu pleinement intérieur, le bot ne mentionne aucune condition extérieure et ne propose aucune alternative pour ce motif.
- Le bot propose une heure alternative dans la même journée, ou un autre jour, plutôt que de se contenter d'alerter.
- **L'alerte informe et n'interdit pas** : le créneau initial reste retenable si l'utilisateur refuse la contre-proposition.
- **Accepter une heure alternative ne retient pas le créneau** : le geste de *retenir un créneau* reste à faire, et aucun message ne part avant lui.
- En l'absence d'alerte, le bot demande l'heure de la rencontre en une phrase.
- **Les deux horizons sont distincts** (AD-19) : météo à seize jours, qualité de l'air à environ un. Un créneau hors de portée de l'un rend les seuils qu'il a pu établir et **nomme** celui qu'il n'a pas pu — sans valeur inventée. Un créneau à cinq jours rend donc les deux premiers seuils et nomme le troisième comme non établi.

## CAP-10 — Proposer un lieu à Lyon *(FR-11)*

- Les lieux proposés sont à Lyon ou dans son agglomération, et correspondent au sport de la demande.
- Chaque lieu proposé indique s'il est **couvert ou en extérieur** — c'est ce qui détermine si CAP-9 s'applique.
- Le bot peut demander un secteur ou un arrondissement pour affiner, mais ne l'exige jamais : sans réponse, il propose quand même.
- Un secteur donné est enregistré au profil de l'utilisateur inscrit et réutilisé la fois suivante.
- Sans donnée disponible, le bot le dit — il ne propose pas de lieu plausible inventé.

## CAP-11 — Écrire la rencontre dans l'agenda *(FR-12)*

- Les deux fournisseurs, Google et Outlook, sont proposés au choix.
- L'écriture n'a jamais lieu sans confirmation explicite de l'utilisateur, et la portée OAuth d'écriture est demandée **à ce moment**, pour le fournisseur choisi alors (AD-18).
- L'événement porte le sport, le prénom du partenaire, le lieu, le jour, l'heure et le statut de la rencontre.
- L'événement ne contient **aucun numéro de téléphone**.
- L'événement est mis à jour à **chaque** changement de statut, *abandonnée* comprise.
- Le produit n'écrit jamais dans l'agenda de quelqu'un d'autre que l'utilisateur qui lui a donné accès au sien.

## CAP-12 — Statuts et recherche active *(FR-13)*

Le détail — les cinq statuts, la table des transitions et de leurs effets, la règle d'une seule recherche active — vit dans [statuts-rencontre.md](statuts-rencontre.md). Les points saillants à vérifier :

- Une rencontre naît *en attente*, quelle que soit la population dont vient le partenaire.
- Une rencontre n'est jamais annoncée comme confirmée avant que le partenaire ait accepté.
- **Un refus produit le statut *déclinée* et jamais *en attente***.
- Une rencontre *en attente* dont le créneau est passé bascule en *expirée*, par la tâche périodique (AD-15), qui est rejouable sans effet.
- Une rencontre *en attente* ou *confirmée* que l'utilisateur abandonne bascule en *abandonnée*. **C'est le seul chemin vers ce statut.**
- Tout changement de statut notifie l'utilisateur par courriel et met à jour l'événement d'agenda. **Une seule exception : *abandonnée*** — l'agenda est mis à jour, aucun courriel ne part, aucun message ne part au partenaire.
- Une rencontre *déclinée*, *expirée* ou *abandonnée* n'est jamais supprimée en silence : elle reste consultable dans le fil avec son statut.
- Une demande complète formulée pendant qu'une rencontre est *en attente* ou *confirmée* n'est pas lancée ; la réponse nomme le sport, le partenaire et le jour occupés, et propose d'abandonner la rencontre en cours.
- **Deux onglets d'un même utilisateur ne produisent pas deux rencontres** : la vérification de la précondition et la création sont une seule transaction (AD-8).
- Être sollicité par un autre demandeur n'occupe pas la place : la personne sollicitée garde le droit de chercher.

## CAP-13 — Prévenir le partenaire et lui permettre d'accepter *(FR-14)*

- Le partenaire est prévenu par **SMS** s'il a un numéro de téléphone, par **courriel** s'il est utilisateur inscrit et n'en a pas donné. Une personne qui n'a ni l'un ni l'autre n'est jamais sollicitée.
- Le message énonce son propre motif — que la personne figure dans le vivier d'Ex Aequo et que quelqu'un cherche un partenaire — avant de présenter la proposition.
- Le message porte le sport, le jour, l'heure, le lieu et le prénom du demandeur, et **aucune coordonnée** du demandeur.
- Le lien permet d'accepter ou de refuser, et ne fonctionne qu'une fois. Le jeton est opaque, non devinable, distinct de l'identifiant de rencontre.
- Le message porte un moyen de **ne plus jamais être contacté** ; l'exercer retire le profil du vivier définitivement, et ce droit vaut pour les deux populations.
- **Aucun SMS ne part vers un numéro hors de la plage de fiction `+336 39 98 XX XX`, sauf vers un numéro qu'un utilisateur inscrit a lui-même donné.** Un numéro qui ne satisfait ni l'une ni l'autre condition fait échouer l'envoi **bruyamment** plutôt que de partir. Le filtre lit la **provenance enregistrée**, jamais le préfixe (AD-11).
- Le filtre de destinataire est une règle de domaine active en production ; le mode « journaliser sans envoyer » du développement lui est **distinct et ne le remplace pas** (AD-12).
- Un refus fait passer la rencontre en *déclinée* ; l'absence de réponse la laisse *en attente* jusqu'au créneau, puis *expirée*. Jamais annulée d'office, jamais requalifiée en confirmée.
- **La page dit qu'une rencontre a été abandonnée par le demandeur** quand c'est le cas. C'est **le seul endroit** où le partenaire peut l'apprendre. Elle ne le présente **jamais comme un refus du demandeur** et propose la sortie définitive du vivier.
- **Un même partenaire peut être sollicité par plusieurs demandeurs.** Chaque sollicitation a son propre message et son propre lien.
- **Deux acceptations qui se chevauchent sont impossibles :** accepter un créneau en conflit avec une rencontre déjà *confirmée* du même partenaire échoue, la page le dit, et la rencontre concernée passe en *déclinée*.
- Un lien déjà utilisé, expiré, portant une rencontre abandonnée, ou appartenant à un profil désinscrit, affiche la raison plutôt qu'une erreur technique : les **sept états terminaux** sont exhaustifs.

## CAP-14 — Cycle de vie d'un profil au vivier *(FR-16)*

- Une rencontre *en attente* ou *confirmée* bloque, pour les deux profils, **le seul jour de la rencontre**. Chacun continue de sortir des recherches portant sur ses autres jours.
- Une rencontre *déclinée* libère le jour **immédiatement**. Une rencontre *abandonnée* aussi, et **pour les deux profils**.
- Une rencontre *expirée* libère le jour. C'est le seul mécanisme qui rend au vivier les jours immobilisés par une rencontre restée sans réponse.
- Le profil conserve **ses jours demandés et le jour accepté**. Accepter un mercredi qu'on n'avait pas demandé est une information sur sa disponibilité, et elle est gardée.
- Un profil sorti du vivier ne revient dans aucune recherche, quel que soit le statut de ses rencontres passées.
- Une rencontre passée sans incident ne retire rien : le lendemain, le profil est trouvable exactement comme la veille.
- **Il n'existe aucun champ « bloqué »** : la disponibilité d'un jour se dérive par jointure sur les rencontres bloquantes (AD-6).
- **Le blocage est volontairement trop large** : le vivier ne connaît que des jours, donc une rencontre à 19 h retire la personne de toute la journée. C'est le prix du choix de ne pas stocker d'heures, et il se paie en disponibilité perdue, jamais en propositions fausses.
- **Une démonstration demande deux demandeurs et deux jours** : retenir une personne un mercredi, puis la rechercher sur un autre de ses jours — où elle doit encore apparaître.

## CAP-15 — Reprendre une conversation

- Le fil n'est jamais purgé ni réinitialisé de lui-même.
- Un utilisateur inscrit qui revient retrouve ses demandes, ses alertes et ses rencontres.
- Le récapitulatif de reprise est **en prose**, porte **au plus une rencontre** — garanti par la règle d'une seule recherche active — et chaque rencontre nommée y porte sa pastille de statut en ligne dans la phrase.
- Il ouvre le tour du bot, et ce tour **s'insère en bas du fil** comme tous les autres. « En tête » qualifie la place dans le tour, jamais une insertion en haut du document.
- **La reprise ne re-rend aucun bloc.** Le récapitulatif de rencontre posé plus haut dans le fil reste l'unique point de vérité et continue de muter sur place.
- Un visiteur **sans compte** retrouve son fil pendant **30 jours** sur le même navigateur, porté par un cookie signé, après quoi il est effacé.
- **La conversation précède l'identité et lui survit** : à la connexion, la conversation en cours s'attache au compte — ni rejouée, ni dupliquée, ni recommencée (AD-21).

## CAP-16 — Rendre le travail du bot visible

- Chaque port **qui peut échouer d'une façon que la personne doit connaître** émet un événement d'étape à **l'entrée et à la sortie** de l'appel, portant le service et son sort. Cinq ports satisfont ce critère : `meteo`, `air`, `lieux`, `agenda` et `envois` — ce dernier parce que le filtre de destinataire échoue bruyamment (CAP-13). `persistance` n'émet pas : son échec est un **défaut**, pas un fait.
  > *Corrigé le 2026-08-31.* Ce critère disait « chaque **port secondaire** » et l'*intent* de CAP-16 disait « chaque **appel externe** » — deux listes différentes, la persistance et la boîte d'envoi étant des ports secondaires **locaux**. Les deux formulations sont remplacées par le critère de principe, aligné sur AD-3.
- **Le signe de vie part au premier appel d'outil, avant le premier jeton du modèle**, et dans tous les cas en moins de 2 secondes. La réponse complète arrive en moins de 20 secondes ; au-delà, le bot dit ce qu'il fait et pourquoi c'est long.
- **Le modèle ne dispose d'aucun outil lui permettant d'émettre une étape.** Quand le bot dit qu'il regarde la météo, il la regarde.
- Une source qui n'a pas répondu est **annoncée comme telle**, nommément, et l'absence de sa donnée dans la réponse devient cohérente au lieu d'être suspecte.
- Les étapes sont persistées avec le tour : elles sont la trace produit, distincte de la journalisation technique, qui ne s'affiche jamais dans le fil.

## Robustesse et pannes — transversal

- **Météo, terrains et agenda peuvent être indisponibles**, et le parcours reste terminable sans eux : sans météo la rencontre se prend sans contrôle de jouabilité et le bot le dit ; sans données de terrains l'utilisateur indique le lieu lui-même ; sans agenda la rencontre existe et le bot propose de réessayer l'écriture plus tard.
- Tout port retourne un **résultat typé** — succès, ou échec nommant le service et son motif. Aucune exception ne traverse un port ; une exception qui remonte au fil est un défaut. **Aucune valeur par défaut n'est jamais substituée** (AD-13).
- **La panne du LLM est le seul échec sans repli.** Elle est rendue comme un tour du fil qui nomme la panne et **dit ce qui n'est pas perdu**, avec un texte **arrêté et non généré**. Aucune écriture de domaine n'est engagée par un tour interrompu (AD-20).
- Couper le réseau au milieu d'un tour produit un message qui nomme la panne et dit ce qui n'est pas perdu — jamais une réponse vide, jamais un fil cassé.
- **L'échec se rend sans couleur** : le rose-rouge appartient à la seule jouabilité, l'ambre au seul statut *en attente*. L'échec s'écrit en encre primaire, avec un filet réel et le mot écrit.

## Amorçage — transversal

- Le chargement des 86 profils est **idempotent** : relancer l'application ne duplique rien.
- Après le chargement, la base est la source de vérité et le fichier n'est plus lu.
