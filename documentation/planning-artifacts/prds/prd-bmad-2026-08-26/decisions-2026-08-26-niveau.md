# Décisions à porter dans le PRD — le niveau et l'appariement

- **Date :** 2026-08-26
- **Origine :** séance `bmad-party-mode` (Mary, John, Sally, Winston, Amelia) sur la `[DÉCISION OUVERTE — design]` de FR-15
- **Décideur :** Fbautry
- **Statut :** tranché et **appliqué au PRD le 2026-08-27** (version 2 — voir le §13 du
  PRD pour ce qui a réellement été porté, et pour l'écart assumé sur le moment où la
  question du niveau est posée)
- **À lire aussi :** `.memlog.md` de la séance — `documentation/party-mode/memories/installed/.memlog.md`

> Ce fichier existe pour une raison précise : le 2026-08-26, le PRD a été réécrit après que les spines UX ont été finalisées, sans journal de modifications, et les documents aval ont passé des heures à citer une version disparue. Les décisions ci-dessous **inversent plusieurs exigences du PRD**. Elles doivent être portées en amont explicitement, avec leur raison, et non contredites en silence par l'UX.

---

## Ce qui a été décidé

### 1. Le niveau est déclaratif, demandé, et à trois valeurs

- Le bot **demande** le niveau parmi **Débutant / Intermédiaire / Avancé**.
- La demande se fait **à l'entrée au vivier** — c'est-à-dire à la toute fin du parcours, après le récapitulatif — avec son motif attaché : « pour qu'on puisse vous trouver ».
- **Jamais pendant la recherche.** C'est la seule contrainte de FR-15 qui survit, et elle est à conserver telle quelle.
- Si la personne a déjà employé **l'un des trois mots exacts** dans sa phrase, on le prend et on ne demande rien.
- **Tout autre mot ouvre les trois boutons.** « J'ai un niveau OK » n'est jamais interprété ni stocké : le LLM n'a pas le droit d'improviser sur la donnée qui structure l'appariement.
- La **sur-évaluation est assumée**. Toute forme de calibration (questionnaire comportemental, inférence, correction par les résultats) est **hors périmètre**.
- Refus de répondre accepté : le profil porte un niveau inconnu, et le bot énonce la conséquence — il ne pourra pas le proposer.

### 2. L'appariement se fait au niveau strictement égal, pour tous les sports

- Plus de **niveau adjacent**, plus d'**élargissement sur le niveau**, plus de catégories de sports.
- L'élargissement **sur le jour** est conservé : c'est lui qui fait le travail.
- **Mesuré sur `SportsProfiles.csv`** : 33 combinaisons sport × niveau, **2 vides (6,1 %)**, contre 5,2 % avec l'élargissement de niveau. Le mécanisme supprimé achetait **un point de couverture**. Les deux combinaisons perdues sont *Pilates Intermédiaire* et *Pilates Avancé*.
- Le niveau **disparaît des cartes de partenaires** — il serait identique sur les trois. Il reste stocké, pour rester vérifiable côté produit.

### 3. Les sports d'équipe ne sont pas traités à part

Football, rugby, basket, volley : le produit propose **une** personne, comme pour les autres sports. Aucun travail requis — la promesse existante, « trouver quelqu'un avec qui pratiquer », est déjà à la bonne échelle : c'est un partenaire d'entraînement, pas une équipe. Le glossaire interdit déjà « adversaire », ce qui est cohérent.

### 4. Tous les sports sont acceptés

- Le CSV n'est **qu'un jeu d'amorçage**, pas une liste fermée.
- Un sport inconnu n'est plus refusé : il est **vide**. L'état *Sport hors vivier* fusionne dans *Vivier vide*, et le premier pratiquant d'un sport neuf le fonde.
- Un sport neuf n'a qu'un pratiquant : aucun appariement n'est possible avant le deuxième, ce qui laisse le temps de classer quoi que ce soit paresseusement.

### 5. Cycle de vie d'un profil — n'existait dans aucun document

- Un profil **reste au vivier** après sa rencontre.
- Il est **bloqué par jour**, jamais en entier : un créneau tennis le mercredi ne le retire pas des recherches du samedi.
- Sa fiche porte **les jours demandés et le jour accepté** — accepter un mercredi est une information sur sa disponibilité, et la jeter serait un gâchis.
- Sur-blocage assumé : le vivier ne connaît que des jours, jamais des heures ; un créneau à 19 h bloque toute la journée.
- **Déclinée libère immédiatement.** **Expirée** est le seul mécanisme qui rend au vivier les profils bloqués par une rencontre fantôme — c'est le ramasse-miettes, pas une politesse.

---

## Modifications à apporter au PRD

| # | Où | Quoi |
|---|---|---|
| 1 | **FR-15** | **Retirer l'exigence**, avec sa raison écrite : la précision du niveau est hors périmètre, donc le mécanisme d'inférence n'a plus d'objet. Conserver la seule phrase qui survit — *le bot ne demande jamais le niveau pendant la recherche* — en la rattachant à FR-2 ou au garde-fou de §7. |
| 2 | **FR-8** | Amputer la moitié « niveau ». L'élargissement ne porte plus que sur le jour. La conséquence testable citée (Pilates, non-adjacence Débutant/Avancé) devient simplement « aucun candidat à ce niveau ». |
| 3 | **§3 glossaire** | Supprimer l'entrée **`niveau adjacent`**. Mettre à jour l'entrée **`niveau`** : valeur déclarée parmi trois, demandée une fois à l'entrée au vivier, jamais vérifiée. |
| 4 | **FR-2** | Les sports ne sont plus une liste fermée. Une demande portant sur un sport inconnu reçoit une réponse de vivier vide, pas un refus. |
| 5 | **FR-6** | Vérifier l'ordre des candidats : le délai d'attente croissant reste valable, mais la médiane est de **3 candidats par combinaison** sur les données d'amorçage — le plafond de trois ne mord presque jamais. |
| 6 | **§3 glossaire, `vivier`** | Résoudre la contradiction déjà relevée — « il grossit ; il ne diminue pas » contre FR-14 qui permet d'en sortir définitivement. Ajouter le cycle de vie d'un profil : entrée, visibilité, blocage par jour, déblocage, sortie. |
| 7 | **Frontmatter** | Ajouter un **journal des modifications** ou une ligne de version. C'est la cause racine de la désynchronisation du 2026-08-26 et le correctif le moins cher du lot. |
| 8 | **§11 questions ouvertes** | Donner des identifiants stables (`QO-1…QO-n`) et conserver les entrées fermées à leur numéro : la renumérotation a cassé les citations aval deux fois en une journée. |

## Questions ouvertes, à verser à l'architecture

- **Fraîcheur d'une fiche.** Un vivier qui ne diminue jamais fabrique ses propres profils injoignables : quelqu'un qui a joué une fois en septembre est encore proposé en mars. Winston soutient que c'est une colonne (dernière activité + comparaison), John que c'est du périmètre. Non tranché.
- **Normalisation des noms de sport.** Avec une liste ouverte, « tennis » et « Tennis » fragmentent le vivier et ne se rencontrent jamais.
- **Boucle de retour.** Le niveau est écrit une fois et jamais corrigé — il n'existe aucun résultat de match en MVP. Le choix d'un **jour** par la personne est un signal propre et gratuit ; le choix d'une **personne** est confondu avec la disponibilité et ne l'est pas.

---

## Conséquences aval, une fois le PRD à jour

Les deux spines UX (`../../ux-designs/ux-bmad-2026-08-26/`) sont en **v2** et devront passer en v3 : l'état *Établissement du niveau* et sa `[DÉCISION OUVERTE]`, l'état *Élargissement sur le niveau*, l'écart de niveau écrit sur la carte, l'état *Sport hors vivier*, le niveau dans `partner-card`, et l'ajout du cycle de vie d'un profil. **Faire le PRD d'abord.**
