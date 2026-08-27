# Réconciliation — `decisions-2026-08-27-une-seule-recherche.md` contre le PRD v3

- **Entrée réconciliée :** [decisions-2026-08-27-une-seule-recherche.md](decisions-2026-08-27-une-seule-recherche.md) (94 lignes)
- **Cibles :** [prd.md](prd.md) v3, [addendum.md](addendum.md)
- **Date :** 2026-08-27
- **Méthode :** réconciliation menée **dans le contexte parent**, les sous-agents n'étant
  pas disponibles sur cette session. Chaque affirmation du fichier d'entrée a été cherchée
  dans le PRD v3 et son emplacement noté.

## Le tableau « Ce que ça change dans le PRD » — 4 lignes sur 4 atterries

| Ligne du fichier | Où c'est atterri | Écart |
|---|---|---|
| **FR-13** — la conséquence testable sur le statut | §5.5 FR-13, bloc *Une seule recherche active à la fois* : 6 conséquences testables au lieu d'une, la formulation contractuelle en citation, une `[NOTE FOR PM]` | **enrichi** — la règle proposée était une phrase ; elle se décline en 6 cas parce que le fichier lui-même en fermait trois |
| **FR-10 / §5.3** — nommer le geste | §3 (définition), §5.3 (antériorité + « deux décisions distinctes »), FR-10 (« accepter une heure alternative ne retient pas le créneau »), FR-14 et §9 alignés sur le terme | **déplacé** — la définition va au §3 et non au §5.3 : le reproche d'origine était qu'une expression était employée sans être définie, or le §3 est le lieu des définitions |
| **§3 Glossaire** — entrée *recherche active* | §3, entre *Rencontre* et *Jouabilité* | **corrigé** — voir ci-dessous |
| **§11** — question fermée sans numéro `QO-n` | §11, liste *Questions fermées depuis la première rédaction* | conforme |

## La correction portée à la définition

Le fichier proposait : *« une demande complète dont la rencontre n'est pas encore déclinée
ou expirée »*. Cette formulation est **ancrée sur la demande alors que la règle mord sur la
rencontre**, et l'état dominant du produit est la demande qui ne produit aucune rencontre —
55 % des recherches exactes échouent, 6,1 % des combinaisons sont vides. Une telle demande
n'est ni *déclinée* ni *expirée* : la lettre de la définition la rendait **active à vie**,
et tuait FR-9 au passage, une alerte différée étant exactement une demande complète sans
rencontre.

Réancrée sur les deux statuts bloquants — *en attente*, *confirmée* — ceux-là mêmes que
FR-13 et FR-16 découpent déjà. **FR-9 survit alors par construction**, et non par le
paragraphe d'avertissement que le fichier lui consacrait.

## Les deux indéterminations du fichier, arbitrées

| Indétermination | Arbitrage | Où |
|---|---|---|
| Le fichier dit « une rencontre en attente ou confirmée » sans dire **de quel côté**. FR-14 autorise plusieurs sollicitations : la lecture littérale laissait un inconnu geler quelqu'un qui n'a rien demandé, de façon cumulable | **Seules comptent les rencontres nées de ses propres demandes.** Le jour de la personne sollicitée est déjà bloqué par FR-16, ce qui suffit | §3, FR-13, §13 |
| « Aucune mesure ne dit si la restriction gêne » — laissé ouvert, sans porteur | **QO-8**, identifiant stable, avec sa condition de levée. Pas de contre-métrique : le §10 mesure la tenue sur les données d'amorçage, or les 86 profils ne cherchent jamais | §11, §12, FR-13 |

## Les affirmations de détail — vérifiées une à une

- **Formulation contractuelle** — reprise **verbatim**, vérifié par comparaison normalisée.
- **Les trois trous fermés** — récapitulatif d'au plus une rencontre → §6 ; revenir sur un
  choix déjà fait → conséquence FR-13 ; changer le créneau après écriture agenda → conséquence
  FR-13, avec « aucun cinquième statut n'est nécessaire » écrit en toutes lettres.
- **« Le plus restrictif des trois arbitrages possibles »** et les deux écartés → `[NOTE FOR PM]` de FR-13.
- **« FR-9 reste intact »** → écrit des deux côtés, au §3 et en conséquence testable de FR-13,
  comme le fichier le demandait explicitement (« une lecture rapide fait exactement l'erreur inverse »).
- **QO-2 non affectée** → constaté, et dit au §13.
- **« Le seul bouton primaire du produit »** → le PRD nomme le **geste** et son contrat ; le
  libellé *« Retenir ce créneau »* est cité comme celui de l'interface, non figé dans le PRD (§0).

## Gaps — ce que le fichier ne portait pas et qui a dû être écrit

1. **La conséquence architecturale.** La règle exige de distinguer le **côté demandeur** du
   côté partenaire d'une rencontre, là où le blocage par jour de FR-16 est **symétrique** :
   même état lu, axe différent. S'y ajoute une exigence d'atomicité (deux onglets du même
   utilisateur). Versé dans [addendum.md](addendum.md), *Persistance*.
2. **Le bénéfice invisible en amont.** L'argument « au plus une rencontre à récapituler »
   s'appuyait sur un point de rupture que le PRD n'énonçait nulle part — la NFR *Reprise de
   conversation* ne parlait pas de récapitulatif. Clause ajoutée au §6, sans quoi la raison
   de l'arbitrage restait illisible pour qui lit le PRD seul.
3. **Un désaccord de vocabulaire avec l'aval.** `EXPERIENCE.md` v3.2 parle d'une seule
   **« demande active »**. *Demande* est déjà un terme du §3 et désigne autre chose — un
   sport, des jours, un niveau — dont on peut formuler autant qu'on veut sans jamais occuper
   la place. Le terme qui fait foi est **recherche active** ; l'écart est tracé au §13 comme
   conséquence aval, et **reste à corriger dans les spines UX**.

## Verdict

Le fichier d'entrée est **entièrement atterri**, avec une correction de fond, deux
arbitrages qu'il laissait ouverts, et trois manques comblés. Aucune de ses affirmations n'a
été écartée.
