# Critères de réussite — Ex Aequo

Companion de [SPEC.md](SPEC.md), cité par la section *Success signal*. Projet personnel : la mesure est qualitative et volontairement courte. Les identifiants `SM-n` du PRD sont conservés.

## Ce que ces critères mesurent — et ce qu'ils ne mesurent pas

Ils mesurent **la tenue du produit sur les données d'amorçage**, pas son succès auprès de vrais utilisateurs. La distinction n'est pas une coquetterie : le vivier de départ est fictif, il compte 7,8 profils par sport en moyenne, et sa répartition de niveaux est presque uniforme — là où une population réelle s'entasse dans « intermédiaire ». Les taux ci-dessous sont donc calibrés sur une distribution qui n'existe pas dans la nature. **Ils disent que la mécanique fonctionne ; ils ne disent rien de l'utilité.**

## Les deux parcours de référence

Les critères citent UJ-1 et UJ-2, les deux parcours utilisateur du PRD. Ils sont rendus en entier dans `EXPERIENCE.md` § *Key Flows*, où ils portent les noms **Parcours 1** et **Parcours 2** — c'est là qu'il faut aller pour les jouer pas à pas.

- **UJ-1 — trouver quelqu'un à son niveau, mais pas le jour voulu.** Le demandeur ouvre le site sans compte, dit son sport, son jour et son niveau en une phrase ; la recherche exacte ne renvoie rien ; l'élargissement sur le jour propose trois candidats du niveau exact ; il en retient un, la jouabilité décale l'heure, le compte est demandé à ce moment, la rencontre part *en attente* et s'écrit dans l'agenda. **Cas limite :** s'il refuse tous les jours proposés, une alerte différée lui est proposée. C'est le chemin **majoritaire**.
- **UJ-2 — chercher un partenaire là où il n'y a personne à son niveau.** La demandeuse n'emploie aucun des trois mots de niveau : les trois choix lui sont ouverts. Il n'y a personne, et il n'y en aura aucun jour. Le bot nomme le sport et le jour tentés, dit qu'il a regardé tous les autres jours, conclut qu'il n'y a personne **à ce niveau**, et propose l'alerte différée. Elle accepte, crée un compte — et **rejoint le vivier**. Chemin **rare** : 14 combinaisons sur 231, toutes du Pilates. Il doit être irréprochable parce qu'il est le moment où le bot est le plus tenté de broder, pas parce qu'il est fréquent.

## Les critères

- **SM-1** — Le parcours complet de UJ-1 se déroule de bout en bout, en une conversation, sans intervention manuelle. Valide CAP-1 à CAP-6, CAP-9 à CAP-14.
- **SM-2** — Sur un échantillon de demandes couvrant les 11 sports, le bot ne produit jamais un nom, un lieu ou une météo qui ne vienne pas d'une source réelle. Valide CAP-7, CAP-9, CAP-10, et la contrainte « le bot n'invente rien ».
- **SM-3** — **Au moins 85 % des 127 combinaisons sans résultat exact des données d'amorçage produisent au moins un candidat du niveau exact demandé.** Le plafond atteignable est de 89 %. Valide CAP-6.
- **SM-4** — Le parcours de UJ-2 se déroule sans que le bot invente un partenaire, et aboutit à une alerte différée acceptée. Il se vérifie sur les 14 combinaisons réellement vides — les deux paires Pilates, tous jours confondus. Valide CAP-7, CAP-8.
- **SM-5** — **Le pari de la conversation tient** : sur un échantillon de sessions, moins d'une sur cinq voit l'utilisateur réclamer explicitement une liste, une carte, des filtres ou un catalogue de profils. Au-delà, c'est le signe que la forme conversationnelle n'est pas la bonne pour ce problème, et il faut le savoir.

**SM-3 est le seul critère chiffrable par un test**, et il est atteignable en premier : les 231 combinaisons se parcourent en boucle sans une ligne de LLM ni de web, dès que le moteur d'appariement existe.

## Contre-métrique — à ne pas optimiser

- **SM-C2** — Le nombre de tours de conversation avant la première proposition de partenaire. Un bot qui pose beaucoup de questions paraît attentif et devient pénible. **Au-delà de 4 tours**, la forme conversationnelle coûte plus qu'elle ne rapporte. Contrebalance SM-1 et SM-5.

- **SM-C1 est retirée.** Elle mesurait la part des mises en relation obtenues par descente de niveau ; la descente de niveau n'existe plus. **Il ne reste donc aucune contre-métrique sur l'intégrité du niveau** — c'est une perte, pas un nettoyage. Son identifiant n'est pas réattribué.

## Ce que rien ne mesure

Quatre endroits sont laissés sans instrument, et il faut les voir ensemble plutôt qu'un par un :

1. **Le signal d'équilibre après rencontre** est hors périmètre : le produit ne peut pas savoir si un appariement était juste.
2. **SM-C1 a disparu** : plus aucune contre-métrique ne surveille l'intégrité du niveau.
3. **QO-8** — rien ne dit si la restriction d'une seule recherche active gêne, et aucun critère ne peut le dire : les 86 profils d'amorçage ne cherchent jamais.
4. **QO-9** — rien ne dit ce que coûte le silence sur l'abandon : les 86 profils ne rouvrent jamais leur lien.

**Trois garde-fous étaient prévus sur la promesse centrale du produit** — l'établissement du niveau par des faits, le signal d'équilibre après rencontre, et la contre-métrique de descente de niveau. Les trois ont été retirés, chacun pour une raison défendable prise séparément. Ce qui reste est un niveau déclaré, jamais vérifié, jamais corrigé, et dont rien ne mesure la justesse : **le risque est accepté sans aucune contrepartie.** C'est le premier endroit où regarder si les retours d'usage se dégradent — la plainte prendra la forme « je ne trouve pas de partenaire à mon niveau » alors que la cause sera un niveau mal déclaré, pas un vivier trop petit.
