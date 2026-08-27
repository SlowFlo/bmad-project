# Réconciliation — `decisions-2026-08-27-statut-abandonnee.md` contre le PRD v4

- **Date :** 2026-08-27
- **Menée :** dans le contexte parent (sous-agents indisponibles sur cette session)
- **Verdict :** **entièrement atterri.** 8 lignes de tableau sur 8, 3 décisions sur 3,
  3 non-changements vérifiés, 2 points ouverts traités. **1 correction de fond**,
  **1 arbitrage**, **1 ajout**, **2 observations pour l'aval**.

---

## Le tableau « Ce que ça change dans le PRD » — 8 lignes sur 8

| # | Où | Demandé | État | Où c'est atterri |
|---|---|---|---|---|
| 1 | FR-13, table | Cinquième ligne *abandonnée* | **atterri** | Ligne de table + paragraphe expliquant pourquoi aucun des quatre ne pouvait la recevoir |
| 2 | FR-13, conséquence | Réécrire la phrase « statuts ordinaires / cinquième état » | **atterri, dépassé** | Réécrite — et **aux deux autres endroits** que le fichier ne signalait pas (voir *Correction*) |
| 3 | FR-13, notification | *Abandonnée* exemptée de courriel, agenda mis à jour | **atterri** | Conséquence testable, avec le motif |
| 4 | FR-13, une seule recherche | La sortie promise devient exécutable | **atterri** | Bullet réécrit, avec ce qui se passerait sans statut d'arrivée |
| 5 | §3 Glossaire, *Rencontre* | Quatre → cinq valeurs | **atterri** | Plus la phrase qui dit lequel des cinq vient du demandeur |
| 6 | FR-16 | *Abandonnée* libère le jour immédiatement | **atterri, précisé** | **Pour les deux profils** — le fichier ne le disait pas, le PRD le dit |
| 7 | FR-14, page d'acceptation | État terminal, jamais présenté comme un refus | **atterri** | Plus : c'est le **seul** endroit où le partenaire peut l'apprendre, et le lien cesse de fonctionner |
| 8 | §13 | À inscrire avec la raison | **atterri** | Entrée v4, plus deux **conventions de tenue** issues du constat de procédure |

## Les trois décisions

1. **Un cinquième statut *abandonnée*** — atterri en entier : le jour se libère aussitôt,
   la rencontre reste consultable dans le fil, la recherche redevient possible. Le nom et
   les deux noms écartés (*annulée*, *retirée*) sont au §13. **Le « aucun jeton visuel
   ajouté » n'est pas porté au PRD, et c'est correct :** le §0 exclut la microcopie et
   l'apparence, qui vivent dans `DESIGN.md`.
2. **Le partenaire n'est prévenu par aucun message** — atterri en deux endroits (FR-13
   pour la règle, FR-14 pour la surface qui la porte), avec l'invariant du contact unique
   écrit en `[NOTE FOR PM]` sous FR-14 plutôt que laissé implicite.
3. **Exception à la règle de notification de FR-13** — atterri, avec la mise à jour de
   l'agenda (FR-12) explicitement maintenue.

## « Ce que ça ne change pas » — les trois vérifiés

- **La règle d'une seule recherche active est intacte.** Vérifié mot pour mot : la
  formulation contractuelle, les six conséquences testables et l'arbitrage FR-14 sont
  inchangés. Le §13 le dit en toutes lettres — *n'assouplit la règle d'aucun pouce*.
- **FR-9 n'est pas touchée.** Le bullet des alertes différées est intact.
- **Aucun jeton aval.** Hors périmètre du PRD, non porté.

## Ce qui reste ouvert

- **Le partenaire d'une rencontre *confirmée* n'apprend l'abandon qu'en rouvrant son
  lien** → devenu **QO-9**, avec sa condition de levée (la première rencontre confirmée
  puis abandonnée à plus d'une semaine de son créneau) et son porteur. Le fichier
  supposait « sans doute le même porteur que QO-8 » ; confirmé.
- **Le septième état de la page d'acceptation n'est rendu dans aucune maquette** — *faux
  au moment où ce rapport le lisait.* Le fichier de décisions a été écrit à 16:49 ;
  `mockups/key-page-acceptation.html` a été mis à jour à **16:52**, et rend l'état 7 en
  entier (titre, corps, sortie du vivier, et les quatre notes de conception). Le point
  était clos trois minutes après avoir été écrit. **Rien à faire en aval.**

---

## Correction de fond

**Le fichier tenait la phrase « aucun cinquième état » pour encore juste dans le cas du
changement de créneau après écriture agenda.** Elle ne l'était pas. Le passage concerné de
FR-13 écrivait :

> Changer le créneau d'une rencontre déjà écrite dans l'agenda (FR-12) l'emprunte aussi :
> **la rencontre est abandonnée**, puis une nouvelle est retenue. Aucun cinquième statut
> n'est nécessaire.

Il emploie lui-même le verbe *abandonner*. Si abandonner produit désormais *abandonnée*,
ce chemin produit le cinquième statut, et la clause s'y contredit. **Elle mourait à trois
endroits, pas un :** les deux conséquences testables de FR-13, et l'entrée v3 du §13, qui la
comptait parmi les trois trous fermés par la v3. Ce qui survit est son intention réelle —
*changer de créneau n'est pas un cas particulier, c'est un abandon suivi d'une nouvelle
rencontre*. C'est la **deuxième réconciliation de suite** où une définition venue de l'aval
doit être corrigée avant d'être écrite.

## Arbitrage

**Le cinquième statut est uniforme.** Un simple décalage d'heure produit lui aussi une
rencontre *abandonnée*. L'alternative — exempter le changement de créneau — réintroduisait
le cas particulier que la v3 avait fermé et laissait à nouveau une rencontre sans statut
d'arrivée. **Vérifié contre l'aval :** `EXPERIENCE.md` v3.4 traite déjà ce cas par
*abandonnée* sans exception. L'arbitrage n'a donc **rien à redescendre**.

## Deux observations pour l'aval

1. **`EXPERIENCE.md` écrit que changer de créneau « n'a plus à inventer un cinquième
   statut »** alors que le mécanisme qu'il décrit emploie précisément le cinquième statut.
   Le comportement est juste, la glose se lit à l'envers. Correction de rédaction, sans
   effet sur le produit.
2. **Cinq états de lien contre sept états de page.** `addendum.md` énumère les états
   terminaux du **jeton d'acceptation** (accepté, refusé, désinscrit, expiré, abandonné) ;
   les spines énumèrent les états terminaux de la **page** (sept, la variante de conflit de
   créneaux comprise). Les deux comptes sont justes à leur granularité — à ne pas lire
   comme une contradiction lors de la passe d'architecture.
