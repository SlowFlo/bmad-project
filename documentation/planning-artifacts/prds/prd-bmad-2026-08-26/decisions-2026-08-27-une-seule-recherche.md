# Décisions à porter dans le PRD — la concurrence des demandes

- **Date :** 2026-08-27
- **Origine :** passe `bmad-ux` v3.2 sur `ux-designs/ux-bmad-2026-08-26/`, fermeture des
  questions bloquantes du rapport d'implémentabilité
- **Décideur :** Fbautry
- **Statut :** tranché, **appliqué aux spines UX**, **appliqué au PRD** en v3 le
  2026-08-27 — avec une correction : la définition de *recherche active* proposée plus
  bas était ancrée sur la **demande**, ce qui rendait active à vie toute demande sans
  candidat et tuait FR-9 ; elle est réancrée sur les deux statuts bloquants de la
  **rencontre**. Deux points que ce fichier laissait indéterminés ont été arbitrés :
  la règle ne compte que les rencontres nées de ses propres demandes, et l'absence de
  mesure devient QO-8. Voir `prd.md` §13, *v3*.
- **À lire aussi :** `.memlog.md` du run UX, entrées 101 et 106

> **Pourquoi ce fichier existe.** Une `[DÉCISION OUVERTE — produit]` a été fermée pendant
> une séance de conception d'interface. C'est légitime — un développeur ne peut pas sortir
> seul d'une question ouverte, et celle-ci en bloquait trois autres — mais **une décision
> de produit ne doit pas rester enfermée dans un document aval**. C'est exactement le
> mécanisme qui a coûté deux resynchronisations complètes à ce projet : le PRD ignore ce
> que l'UX a tranché, quelqu'un réécrit le PRD, et l'écart se découvre à la relecture.

---

## Ce qui a été décidé

### 1. Une seule recherche active à la fois

**Lancer une recherche de badminton pendant qu'une rencontre de tennis est *en attente* ou
*confirmée* est refusé**, et le bot dit pourquoi : il nomme ce qui occupe la place et donne
la sortie dans la même phrase. La personne peut abandonner la rencontre en cours — elle
passe alors par ses états ordinaires — ou attendre.

Formulation contractuelle arrêtée côté UX :

> « Une recherche à la fois. Anna n'a pas encore répondu pour mercredi. Dites-moi si vous
> préférez laisser tomber le tennis — je cherche le badminton ensuite. »

**Le motif n'est pas de brider, c'est de fermer trois trous d'un coup.** Le PRD et les
spines laissaient chacun un cas non spécifié, et les trois se refermaient par le même
arbitrage :

| Ce qui n'était pas spécifié | Ce que la règle en fait |
|---|---|
| Combien de rencontres la reprise doit-elle récapituler ? | **Une au plus.** Le point de rupture connu — « au-delà de deux ou trois rencontres, un récapitulatif en prose devient illisible » — cesse d'être atteignable |
| Que se passe-t-il si la personne revient sur un choix déjà fait (« en fait, Iris » après avoir retenu Anna) ? | Ce n'est plus un cas concurrent mais le **chemin normal** : la rencontre en cours passe par ses états ordinaires, la recherche reprend |
| Que devient une rencontre dont on change le créneau **après** écriture dans l'agenda ? | Plus besoin d'un cinquième statut : la rencontre est d'abord abandonnée, donc elle passe par **l'une des quatre valeurs de FR-13**, et rien n'atterrit dans un état qui n'existe pas |

**C'est le plus restrictif des trois arbitrages possibles, et c'est délibéré** : c'est le
seul qui se lève sans rien casser le jour où l'usage prouverait qu'il gêne. Les deux autres
étaient : autoriser plusieurs demandes et accepter plusieurs récapitulatifs dans le fil ; ou
autoriser sans limite mais renoncer au récapitulatif de reprise en prose au-delà de deux.

### 2. « La validation du créneau » devient un geste nommé

Le PRD emploie l'expression **sans jamais la définir**. FR-10 s'y adosse pourtant
directement — « le contrôle intervient **avant** la validation du créneau, pas après » — et
toute la §5.3 en dépend. Tant qu'aucun geste ne la portait, cette antériorité n'était pas
vérifiable.

Côté UX, c'est désormais **le seul bouton primaire du produit** : *« Retenir ce créneau »*,
le seul geste qui engage **quelqu'un d'autre** — à partir de là, un message part vers le
partenaire. Deux conséquences testables en découlent :

- **Choisir une heure et décider d'y aller sont deux décisions distinctes.** La
  contre-proposition de l'encadré de jouabilité fixe l'heure ; **elle ne retient rien**.
- **Rien n'est retenu tant que ce geste n'a pas eu lieu.** Le produit ne déduit jamais un
  engagement d'une réponse à une question de jouabilité ou d'horaire.

---

## Ce que ça change dans le PRD

| Où | Nature | Proposition |
|---|---|---|
| **FR-13** | Ajout | Une conséquence testable : *« Tant qu'une rencontre est en attente ou confirmée, aucune nouvelle recherche n'est lancée ; le bot le dit et propose d'abandonner la rencontre en cours. »* C'est le bon foyer : la règle se déclenche sur un **statut de rencontre** |
| **FR-10 / §5.3** | Précision | Nommer le geste que « la validation du créneau » désigne, et poser que la contre-proposition de jouabilité ne vaut **pas** validation |
| **§3 Glossaire** | Ajout | Entrée *recherche active* — une demande complète dont la rencontre n'est pas encore *déclinée* ou *expirée* |
| **§11** | Question fermée | *« Peut-on mener plusieurs recherches de front ? »* → **non**, une seule à la fois. À verser aux « questions fermées depuis la première rédaction », **sans consommer de numéro `QO-n`** : la question n'a jamais été posée sous ce format |

---

## Ce que ça ne change **pas** — et qu'il ne faut pas lire de travers

**FR-9 reste intact.** « Un utilisateur peut porter **plusieurs alertes simultanées**, une
par demande » n'est pas contredit. Une alerte n'occupe aucun créneau et n'attend la réponse
de personne : rien n'empêche d'enchaîner Pilates → vide → alerte → squash → vide → alerte.
La règle ne vise **que** les recherches qui ont abouti à une rencontre.

La distinction est écrite en toutes lettres des deux côtés, parce qu'une lecture rapide fait
exactement l'erreur inverse.

---

## Ce qui reste ouvert

- **Aucune mesure ne dit si la restriction gêne.** L'usage décrit par le PRD — un trou dans
  un agenda, quelques jours à l'avance — ne produit pas de file d'attente, mais c'est une
  hypothèse, pas une observation. Si elle est fausse, c'est le premier arbitrage à lever.
- **QO-2 n'est pas affectée.** La négociation entre deux inscrits reste hors périmètre v1.
