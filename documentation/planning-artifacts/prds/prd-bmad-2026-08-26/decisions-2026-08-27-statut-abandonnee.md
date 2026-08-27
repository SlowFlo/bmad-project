# Décisions à porter dans le PRD — le statut d'une rencontre abandonnée

- **Date :** 2026-08-27
- **Origine :** passe `bmad-ux` en mode Update sur `ux-designs/ux-bmad-2026-08-26/`,
  resynchronisation des spines sur `prd.md` v3
- **Décideur :** Fbautry
- **Statut :** tranché, **appliqué aux spines UX** en v3.4, **appliqué au PRD** en v4 le
  2026-08-27 — avec une correction, un arbitrage et un ajout :
  - *Correction.* Ce fichier tient la phrase « aucun cinquième état » pour encore juste
    dans le cas du changement de créneau après écriture agenda. Elle ne l'est pas : le
    passage concerné de FR-13 emploie lui-même le verbe *abandonner*, donc il produit
    désormais le cinquième statut. La clause meurt aux **trois** endroits où elle se
    trouvait — deux conséquences testables de FR-13, et l'entrée v3 du §13, qui la comptait
    parmi les trois trous fermés par la v3 — et non au seul signalé ici.
  - *Arbitrage.* Le cinquième statut est **uniforme** : un simple changement de créneau
    produit lui aussi une rencontre *abandonnée*. Exempter ce cas réintroduisait le cas
    particulier que la v3 avait fermé, et laissait à nouveau une rencontre sans statut
    d'arrivée. Le coût est écrit en NOTE FOR PM sous FR-13.
  - *Ajout.* Le point laissé ouvert en fin de fichier — le partenaire d'une rencontre
    *confirmée* n'apprend l'abandon qu'en rouvrant son lien, et rien ne le mesure —
    devient **QO-9**, question numérotée avec sa condition de levée.
- **À lire aussi :** `.memlog.md` du run UX, entrées 120 à 123 ;
  [decisions-2026-08-27-une-seule-recherche.md](decisions-2026-08-27-une-seule-recherche.md),
  dont ce fichier est la suite directe

> **Pourquoi ce fichier existe.** Pour la même raison que le précédent, et c'est la troisième
> fois : une décision de **produit** a dû être fermée pendant une séance de conception
> d'interface. Elle n'y a pas été cherchée — elle est tombée d'une vérification de routine, et
> elle bloquait la règle que le PRD venait d'écrire. **Le PRD ne peut pas rester le seul
> document qui l'ignore.**

---

## Le trou

Le PRD v3 écrit, en conséquence testable de FR-13 :

> Abandonner la rencontre en cours la fait passer par ses **statuts ordinaires**, jamais par
> un cinquième état.

**Aucun des quatre statuts ordinaires ne peut recevoir un abandon.** Les quatre décrivent
tous, sans exception, la **réponse du partenaire** :

| Statut | Ce qui l'a produit | Ce que le bot dit |
|---|---|---|
| En attente | le partenaire a été prévenu, il n'a pas répondu | « prévenu, pas encore de réponse » |
| Confirmée | le partenaire a accepté | « c'est confirmé » |
| Déclinée | **le partenaire a refusé** | « il / elle a décliné » |
| Expirée | **le créneau est passé sans réponse** | « personne n'a répondu à temps » |

L'utilisateur qui renonce n'apparaît dans aucune de ces lignes. Router son abandon vers
*déclinée* ferait dire au bot qu'une personne **a refusé** alors qu'elle n'a rien répondu ;
vers *expirée*, qu'une **échéance est passée** alors que rien ne l'a été. Dans le produit dont
le PRD qualifie lui-même la contrainte « le bot n'invente rien » de **la plus structurante**,
ni l'un ni l'autre n'est disponible. La phrase du PRD n'est donc pas seulement imprécise :
elle est **inexécutable en l'état**.

## Pourquoi c'est bloquant et pas cosmétique

Le trou ne reste pas là où il est. Il remonte la chaîne et **désarme la règle qui l'a créé** :

1. Une rencontre abandonnée n'ayant pas de statut d'arrivée, elle **reste *en attente***.
2. L'état *Jour libéré* (FR-16) n'écoute que *déclinée* et *expirée* : **le jour reste bloqué**,
   indéfiniment.
3. *Une seule recherche active à la fois* mord sur les rencontres *en attente* : **la nouvelle
   recherche reste refusée, pour toujours**.

Autrement dit : la sortie que le bot promet dans sa propre **microcopie contractuelle** —
*« Dites-moi si vous préférez laisser tomber le tennis — je cherche le badminton ensuite »* —
**n'existe pas**. La règle mange sa propre porte de sortie, et la personne se retrouve
enfermée dans une rencontre qu'elle a explicitement abandonnée.

## Ce qui a été décidé

### 1. Un cinquième statut : *abandonnée*

**La rencontre que l'utilisateur abandonne passe en *abandonnée*.** Le jour se libère
aussitôt, la rencontre reste consultable dans le fil avec son statut — comme *déclinée* et
*expirée*, jamais supprimée en silence — et la recherche redevient possible.

Le nom suit le vocabulaire **déjà posé des deux côtés** : le PRD écrit « abandonner la
rencontre en cours », la microcopie dit « laisser tomber ». Écartés : *annulée* (trop proche
de *déclinée* à la lecture rapide, alors que les deux désignent des côtés opposés — l'un vient
du demandeur, l'autre du partenaire) et *retirée* (absent du vocabulaire des deux documents).

**Aucun jeton visuel n'est ajouté** : la pastille *abandonnée* rejoint *déclinée* et *expirée*
sur `status-badge-neutral`, sans teinte. L'ambre et le rose-rouge ont chacun un seul métier, et
la doctrine du produit veut que ce soit le mot qui porte.

### 2. Le partenaire n'est prévenu par aucun message

**Aucun texte sortant nouveau.** C'est un **septième état terminal** de la page d'acceptation
qui l'annonce à qui suit son lien.

Le motif est un invariant que les spines s'imposent déjà et que le PRD porte en creux : **« le
SMS est le seul contact qu'un profil d'amorçage aura jamais avec le produit »**. Prévenir d'un
abandon le romprait — pour la population **majoritaire** du vivier, et au profit de gens qui
n'avaient rien fait. Écartés : prévenir toujours, et prévenir seulement si la rencontre était
*confirmée*.

### 3. Une exception à la règle de notification de FR-13

FR-13 pose que **tout** changement de statut déclenche une notification à l'utilisateur par
e-mail. *Abandonnée* en est **exempté** : la personne vient elle-même de le demander, et l'en
informer serait lui apprendre ce qu'elle vient de faire. La mise à jour de l'événement
d'agenda (FR-12), elle, reste due.

---

## Ce que ça change dans le PRD

| Où | Nature | Proposition |
|---|---|---|
| **FR-13**, table des statuts | Ajout | Cinquième ligne : *abandonnée* — « l'utilisateur a renoncé à la rencontre » — « j'ai laissé tomber » |
| **FR-13**, conséquence testable | **Correction** | *« Abandonner la rencontre en cours la fait passer par ses statuts ordinaires, jamais par un cinquième état »* devient faux et doit être réécrit. La phrase visait à l'origine le **changement de créneau après écriture agenda**, où elle reste juste ; elle a été sur-généralisée à l'abandon, où elle est inexécutable |
| **FR-13**, notification | Exception | *Abandonnée* ne produit pas de courriel de changement de statut. L'événement d'agenda est mis à jour |
| **FR-13**, une seule recherche | Précision | La sortie promise par la microcopie est désormais exécutable : abandonner produit *abandonnée*, le jour se libère (FR-16), la recherche reprend |
| **§3 Glossaire**, *Rencontre* | Correction | « un statut et un seul : en attente, confirmée, déclinée ou expirée » → **cinq valeurs** |
| **FR-16** | Précision | *Abandonnée* libère le jour, immédiatement, au même titre que *déclinée* |
| **FR-14**, page d'acceptation | Ajout | Un état terminal de plus : la rencontre a été abandonnée par le demandeur. **Jamais présentée comme un refus du demandeur** — il a renoncé à chercher, il n'a pas jugé la personne |
| **§13** | Journal | À inscrire, avec la raison |

## Ce que ça ne change **pas**

- **La règle « une seule recherche active » est intacte** — elle est au contraire *rendue
  applicable*. Le cinquième statut ne l'assouplit pas d'un pouce.
- **FR-9 n'est pas touchée.** Les alertes différées n'ont jamais eu de statut de rencontre.
- **Aucun jeton de couleur, de typographie, d'espacement ni d'arrondi** n'est ajouté en aval.

---

## Un constat de procédure, qui vaut plus que la décision elle-même

Le PRD v3 écrit, en conséquence aval : *« Le reste de la décision est déjà appliqué en aval,
les deux spines étant en v3.3 : la conséquence aval annoncée en v2 est **soldée**. »* Il ne
déclarait donc **qu'un désaccord de vocabulaire**.

**Deux arbitrages manquaient en réalité**, et pour la même raison : ils ont été rendus **au
niveau du PRD, après la clôture des spines**. Ce sont les « deux indéterminations du fichier,
arbitrées » de [reconcile-decisions-recherche.md](reconcile-decisions-recherche.md) — le PRD
comptait comme soldée la décision **d'origine**, sans voir qu'il avait lui-même **ajouté** de
la matière que rien n'avait redescendue.

Le plus coûteux des deux était **« seules comptent les rencontres nées de ses propres
demandes »**. Sans lui, la spine se lisait littéralement : *toute* rencontre en attente ou
confirmée occupe la place, **y compris celles où l'on est sollicité**. Un inconnu gelait alors
la capacité de chercher de quelqu'un qui n'avait rien demandé — et **de façon cumulable**,
FR-14 autorisant plusieurs sollicitations. C'est exactement le mode de défaillance contre
lequel le PRD avait arbitré ; il n'était simplement jamais descendu. Il est écrit dans les
spines v3.4.

**La leçon est étroite et réutilisable :** quand une réconciliation amont **enrichit** une
décision venue de l'aval, l'enrichissement est une **nouvelle** conséquence aval. Le journal
du PRD gagnerait à distinguer *ce qui a été porté depuis l'aval* de *ce qui a été ajouté en le
portant* — seul le second a besoin de redescendre.

## Ce qui reste ouvert

- **Le partenaire d'une rencontre *confirmée* n'apprend l'abandon que s'il rouvre son lien.**
  C'est le coût assumé de l'invariant du contact unique. Il est faible tant que les rencontres
  se prennent à quelques jours ; il ne l'est plus si l'usage réel les prend à plusieurs
  semaines. **Aucune mesure ne le dit** — même angle mort que QO-8, et sans doute le même
  porteur.
- **Le septième état de la page d'acceptation n'est rendu dans aucune maquette.** Il est né
  après le dernier rendu ; la spine le note explicitement.
