# Statuts d'une rencontre — Ex Aequo

Companion de [SPEC.md](SPEC.md), cité par **CAP-12**, **CAP-13** et **CAP-14**. Une rencontre porte un statut et un seul, et c'est le statut — lui seul — qui détermine ce que le bot a le droit de dire.

## Les cinq statuts

| Statut | Ce qui l'a produit | Ce que le bot dit |
|---|---|---|
| **En attente** | le partenaire a été prévenu, il n'a pas répondu | « prévenu, pas encore de réponse » |
| **Confirmée** | le partenaire a accepté | « c'est confirmé » |
| **Déclinée** | le partenaire a refusé | « il / elle a décliné » — jamais « pas encore répondu » |
| **Expirée** | le créneau est passé sans réponse | « personne n'a répondu à temps » |
| **Abandonnée** | l'utilisateur a renoncé à la rencontre | « j'ai laissé tomber » |

Les quatre premiers décrivent tous, sans exception, la **réponse du partenaire**. *Abandonnée* est le seul que produit l'utilisateur lui-même, et c'est la raison de son existence : router un abandon vers *déclinée* ferait dire au bot qu'une personne **a refusé** alors qu'elle n'a rien répondu ; vers *expirée*, qu'une **échéance est passée** alors que rien ne l'a été. Dans un produit dont la contrainte la plus structurante est « le bot n'invente rien », ni l'un ni l'autre n'est disponible.

Le cinquième statut est **uniforme** : un simple décalage d'heure produit lui aussi une rencontre *abandonnée* suivie d'une nouvelle. Changer de créneau n'est pas un cas particulier — c'est le chemin normal, emprunté une fois de plus.

## Les transitions et leurs effets

Les effets sont attachés aux **arêtes**, jamais aux statuts (AD-9). Un déclencheur générique « statut changé → prévenir » viole le produit dès sa première ligne.

| Arête | Franchie par | Courriel au demandeur | Message au partenaire | Événement d'agenda | Jour bloqué |
|---|---|---|---|---|---|
| *(création)* → **en attente** | l'utilisateur, en retenant un créneau | — | **oui**, avec lien d'acceptation | créé après consentement (CAP-11) | **bloqué** pour les deux profils |
| en attente → **confirmée** | le partenaire, par son lien ou depuis sa conversation | **oui** | — | mis à jour | reste bloqué |
| en attente → **déclinée** | le partenaire | **oui** | — | mis à jour | **libéré immédiatement** |
| confirmée → **déclinée** | conflit de créneaux détecté à l'acceptation | **oui** | — | mis à jour | **libéré** |
| en attente → **expirée** | le temps qui passe (tâche périodique, AD-15) | **oui** | — | mis à jour | **libéré** |
| en attente ou confirmée → **abandonnée** | **l'utilisateur seul** | **non** | **non** | mis à jour | **libéré pour les deux profils** |

Trois propriétés de cette table portent une règle et non une commodité.

**L'arête vers *abandonnée* est la seule sans notification.** L'utilisateur vient de demander l'abandon : l'en informer serait lui apprendre ce qu'il vient de faire. Le partenaire, lui, ne reçoit rien parce que **le SMS est le seul contact qu'un profil d'amorçage aura jamais avec Ex Aequo** — rompre cet invariant pour annoncer un abandon le romprait pour la population majoritaire du vivier, au profit de gens qui n'avaient rien fait. La page d'acceptation est **le seul canal** par lequel l'information peut lui parvenir. Ce que ce silence coûte est **QO-9**.

**Seul l'utilisateur franchit l'arête vers *abandonnée*.** Ni une tâche périodique, ni le partenaire — c'est l'inverse exact d'*expirée*.

**Aucune rencontre n'est jamais supprimée en silence.** Une rencontre *déclinée*, *expirée* ou *abandonnée* reste consultable dans le fil avec son statut.

## Une seule recherche active à la fois

Tant qu'une rencontre est *en attente* ou *confirmée*, aucune nouvelle recherche n'est lancée. Le bot **nomme ce qui occupe la place et donne la sortie dans la même phrase** :

> « Une recherche à la fois. Anna n'a pas encore répondu pour mercredi. Dites-moi si vous préférez laisser tomber le tennis — je cherche le badminton ensuite. »

- La règle ne mord que sur les rencontres **nées des demandes de la personne elle-même**. Être sollicité par un autre demandeur n'occupe pas la place : la personne sollicitée garde le droit de chercher, son jour étant déjà bloqué par CAP-14. C'est l'asymétrie d'AD-7 — le blocage par jour est symétrique, la précondition de recherche ne lit que le côté demandeur.
- **Les alertes différées ne sont pas concernées.** Une alerte n'occupe aucun créneau et n'attend la réponse de personne : enchaîner Pilates → vide → alerte → squash → vide → alerte reste possible, et « plusieurs alertes simultanées » reste vrai mot pour mot.
- Abandonner la rencontre en cours la fait passer en *abandonnée*, libère le jour aussitôt et rend la recherche possible. **C'est ce qui rend la sortie exécutable** : sans statut d'arrivée, la rencontre resterait *en attente*, le jour resterait bloqué et la nouvelle recherche resterait refusée — la règle mangerait la porte de sortie que sa propre phrase promet.
- Revenir sur un choix déjà fait — « en fait, Iris » après avoir retenu Anna — emprunte ce chemin. Ce n'est pas un cas concurrent, c'est le chemin normal.

**C'est une précondition à l'entrée d'une demande, pas un statut de plus.** Aucune colonne « recherche en cours » : l'état se dérive de la jointure sur les rencontres bloquantes, filtrée sur le côté demandeur (AD-6). La vérification et la création sont atomiques (AD-8), pour que deux onglets d'un même utilisateur ne produisent pas deux rencontres.

**Ce que la restriction ne mesure pas est QO-8.** C'est le plus restrictif des trois arbitrages possibles, et c'est délibéré : c'est le seul qui se lève sans rien casser le jour où l'usage prouverait qu'il gêne.

## Les sept états de la page d'acceptation

La page rend l'un des sept états terminaux spécifiés par `EXPERIENCE.md` — *invitation ouverte*, *acceptée*, *refusée*, *lien déjà utilisé*, *lien expiré*, *profil désinscrit*, *rencontre abandonnée* — et **jamais une erreur nue**. Le sort affiché se dérive du **statut de la rencontre et de l'état du jeton résolus ensemble** (AD-10) : un lien ne peut pas continuer de fonctionner sur une rencontre abandonnée.

L'état *rencontre abandonnée* n'est **jamais présenté comme un refus du demandeur** : il a renoncé à chercher, il n'a pas jugé la personne. Il propose la sortie définitive du vivier, seule action qui reste utile.

**Conflit de créneaux — la page bloque.** Accepter un créneau qui entre en conflit avec une rencontre déjà *confirmée* du même partenaire **échoue** ; la page le lui dit et la rencontre concernée passe en *déclinée*. Elle ne lui propose pas d'arbitrer : le produit ne connaît que des jours, jamais des durées, et c'est précisément pourquoi il ne peut pas arbitrer. Le blocage par jour de CAP-14 ayant déjà fermé le cas courant, ce conflit résiduel est la **fenêtre de course** entre deux validations quasi simultanées.
