# Réconciliation — SportsProfiles.csv ↔ PRD

*Établi le 2026-08-26 par recalcul intégral du fichier (86 lignes de données, 6 colonnes),
sans modification d'aucun fichier existant. Toutes les valeurs ci-dessous sont recomputées,
aucune n'est reprise du PRD.*

## Verdict

**Le PRD dit vrai sur cette donnée : les chiffres vérifiables sont exacts au chiffre près,
les quatre conséquences testables nommées se vérifient, et les 86 numéros sont intégralement
dans la plage de fiction ARCEP.** Ce n'est pas là qu'est le problème. Le problème est que deux
affirmations *structurantes* attachent un chiffre juste au mauvais objet : UJ-2 est présenté
comme « le cas majoritaire à 55 % » alors que sa fréquence réelle sur la grille est de
**5,2 %**, et la règle « le jour se négocie, le niveau se défend » est justifiée par un chiffre
(46, soit 36 %) mesuré sur des combinaisons où FR-7 ne s'exécute jamais — si bien que FR-7 ne
produit un candidat que dans **2 combinaisons sur 231**, toujours la même personne. S'y ajoute
un angle mort que la donnée rend visible et que le PRD ne nomme nulle part : **il n'existe
aucune colonne de localisation**, donc aucun appariement du produit n'est contraint
géographiquement.

---

## Vérification des chiffres

| Affirmation du PRD | Recalculé | Verdict |
|---|---|---|
| 86 profils (§1, §3, §4, §9, addendum) | 86 lignes de données + 1 en-tête | **Confirmé** |
| Colonnes : Prénom, Nom, Numéro de téléphone, Sports pratiqués, Jours disponibles, Niveau | exactement ces 6, dans cet ordre, sans BOM | **Confirmé** |
| 11 sports (§10 SM-2) | 11 : Basket-ball, Course à pied, Danse, Escalade, Football, Natation, Pilates, Rugby, Tennis, Volley-ball, Yoga | **Confirmé** |
| 231 combinaisons sport × jour × niveau (§2.3, §5.2) | 11 × 7 × 3 = 231 ; les 7 jours et les 3 niveaux sont tous présents dans la donnée | **Confirmé** |
| 127 combinaisons vides, soit 55 % (§2.3, §5.2, §10) | 127 / 231 = **54,98 %** | **Confirmé** |
| L'élargissement sur le jour récupère 113 des 127 (89 %) (§5.2, SM-3) | 113 / 127 = **88,98 %** | **Confirmé** |
| L'élargissement sur le niveau adjacent ne récupère que 46 (36 %) (§5.2) | 46 / 127 = **36,22 %** (jour de la demande conservé) | **Confirmé** — mais voir Écart 1 : ces 46 sont inatteignables en pratique |
| « 83 des 86 profils d'amorçage ne déclarent que deux jours » (§5.2) | 83 profils à 2 jours, 3 profils à 3 jours (Lucas Moreau, Hugo Martin, Gabriel Petit) ; moyenne 2,03 | **Confirmé** |
| « 19 % des combinaisons ne renvoient qu'un seul candidat » (§5.2) | 45 / 231 = **19,5 %** — pour la recherche **exacte** (FR-5) | **Chiffre exact, rattachement erroné** : la phrase l'invoque pour éclairer le plafond de FR-6, or après élargissement sur le jour le taux à un seul candidat est de **5 / 127 = 3,9 %**. Voir Écart 7 |
| Numéros dans la plage `+336 39 98 XX XX`, réservée par l'ARCEP à la fiction (§4, §7, addendum) | 86 / 86 conformes à `+3363998NNNN` | **Confirmé** |
| « `+3363998 0001` à `+3363998 0086`, uniques et dans l'ordre du fichier » (addendum) | suffixes 0001→0086, 86 valeurs distinctes, séquence strictement croissante ligne à ligne | **Confirmé** |
| Le vivier ne connaît que des jours, jamais des heures (§3, §5.3, addendum) | aucune colonne d'heure ; « Jours disponibles » ne contient que des noms de jours | **Confirmé** |
| Les profils d'amorçage n'ont ni compte, ni e-mail, ni ville (§3, §4, §5.4) | aucune colonne e-mail, aucune colonne ville | **Confirmé** |
| « Les 86 profils d'amorçage n'en portent qu'un [sport] chacun » (FR-3) | 86 / 86 mono-sport | **Confirmé** |
| « une seule pratiquante de Pilates, débutante » (UJ-2, FR-8) | Sarah Andre, Pilates, Débutant, Mardi;Jeudi — unique | **Confirmé** |
| Les prénoms des parcours sont absents des données d'amorçage (§2.3, §11.1) | « Thomas » et « Nadia » absents des colonnes Prénom **et** Nom | **Confirmé** |
| « 34 profils font un sport d'équipe » (addendum, Pièges de démonstration) | Football 9 + Basket-ball 9 + Rugby 8 + Volley-ball 8 = **34** | **Confirmé** |
| « La moitié du vivier pratique un sport sans appariement en duel (yoga, pilates, danse, natation, course à pied, escalade) » (addendum) | 8 + 1 + 9 + 9 + 8 + 8 = **43 / 86 = 50,0 %** | **Confirmé** arithmétiquement ; la classification, elle, est discutable — voir Écart 6 |
| « un sport d'équipe qui demanderait 10 à 22 personnes » (addendum) | Basket 10, Volley 12, Football 22, **Rugby 30** | **Infirmé sur la borne haute** : la fourchette devrait être 10 à 30 |
| « Le scénario Tennis, mardi […] en Intermédiaire ou Avancé le résultat exact est vide » (addendum) | Tennis/Mardi/Intermédiaire = ∅ ; Tennis/Mardi/Avancé = ∅ | **Confirmé** |
| « Sarah André ne peut jamais trouver personne » (addendum) | vrai sur le fond ; **l'orthographe du fichier est « Sarah Andre », sans accent** | **Confirmé, orthographe divergente** |

**Bilan : 19 affirmations confirmées, 1 infirmée (« 10 à 22 personnes »), 2 exactes mais mal
rattachées ou mal orthographiées.**

### Distributions recalculées (aucune n'apparaît dans le PRD)

| Sport | Total | Débutant | Intermédiaire | Avancé | Combinaisons vides / 21 |
|---|---|---|---|---|---|
| Football | 9 | 3 | 4 | 2 | 9 |
| Danse | 9 | 3 | 3 | 3 | 9 |
| Basket-ball | 9 | 3 | 3 | 3 | 10 |
| Tennis | 9 | 3 | 3 | 3 | 11 |
| Course à pied | 8 | 3 | 3 | 2 | 11 |
| Escalade | 8 | 3 | 3 | 2 | 11 |
| Rugby | 8 | 2 | 2 | 4 | 11 |
| Volley-ball | 8 | 3 | 3 | 2 | 11 |
| Natation | 9 | 2 | 4 | 3 | 12 |
| Yoga | 8 | 2 | 2 | 4 | 13 |
| **Pilates** | **1** | **1** | **0** | **0** | **19** |

Niveaux : Intermédiaire 30, Débutant 28, Avancé 28 — équilibre à ±2.

Jours : Mardi 28, Jeudi 27, Lundi 26, Mercredi 26, Samedi 24, Vendredi 23, Dimanche 21.
Aucun jour absent ; amplitude 1,33× entre le plus et le moins représenté.

Classes sport × niveau vides : 2 (Pilates/Intermédiaire, Pilates/Avancé). Classes à une seule
personne : 1 (Pilates/Débutant). Classe la plus fournie : 4 personnes (Football/Intermédiaire,
Natation/Intermédiaire, Rugby/Avancé, Yoga/Avancé).

---

## Vérification des conséquences testables nommées

### FR-5 — « Tennis, mardi, débutant » renvoie Emma Leroy → **vérifié**

Filtre `Sports = Tennis` ET `Mardi ∈ Jours` ET `Niveau = Débutant` sur les 86 lignes :
un résultat, **Emma Leroy** (ligne 2, Mardi;Jeudi, Débutant). Aucun autre. La conséquence est
exacte, et le résultat est de surcroît **unique** — ce que le PRD ne dit pas, mais qui en fait
un bon cas de test déterministe.

### FR-5 — « Tennis, mardi, intermédiaire » ne renvoie aucun candidat → **vérifié**

Les trois joueurs de tennis Intermédiaire sont Anna Perrot (Mercredi;Samedi), Iris Payet
(Lundi;Mercredi) et Tessa Armand (Lundi;Samedi). **Aucun n'est disponible le mardi.**
Résultat exact : ∅. Confirmé.

*Complément :* Tennis/Mardi/Avancé est également vide (Jules Robin Lundi;Samedi, Lina Leclerc
Mercredi;Samedi, Raphaël Delorme Lundi;Samedi). Le mardi est donc mort pour le tennis à deux
niveaux sur trois — ce que le PRD ne relève pas.

### FR-6 — « Tennis, mardi, intermédiaire » renvoie Anna, Iris et Tessa avec leurs jours → **vérifié, avec une réserve de rédaction dans UJ-1**

L'élargissement sur le jour (sport + niveau exact, jour libre) renvoie exactement trois
profils, ni plus ni moins, tous strictement Intermédiaire :

| Ligne | Candidat | Jours réels |
|---|---|---|
| 22 | Anna **Perrot** | Mercredi ; Samedi |
| 52 | Iris **Payet** | Lundi ; Mercredi |
| 82 | Tessa **Armand** | Lundi ; Samedi |

La conséquence testable de FR-6 est donc juste, et le plafond de trois n'a pas à mordre.

**Réserve.** UJ-1 fait dire au bot : *« Anna, Iris et Tessa jouent exactement à votre niveau —
mercredi, samedi ou lundi. »* Lue comme l'**union** des jours disponibles, la phrase est
exacte : {Mercredi, Samedi, Lundi} est bien l'ensemble des jours couverts. Lue
**positionnellement** — Anna→mercredi, Iris→samedi, Tessa→lundi — elle est fausse pour Iris,
qui n'est jamais disponible le samedi. Or FR-6 exige de présenter les candidats « avec leurs
jours **respectifs** » : la formulation de UJ-1 ne satisfait pas sa propre exigence et appelle
une lecture positionnelle erronée. À reformuler par appariement explicite.

### FR-8 — « Pilates, avancé » ne produit aucun nom, quel que soit le jour et après tout élargissement → **vérifié sur les trois branches**

- **Recherche exacte** : Pilates/Avancé sur chacun des 7 jours → ∅ (7 fois sur 7). Le vivier ne
  compte aucun pratiquant de Pilates Avancé, ni Intermédiaire.
- **Élargissement sur le jour** (Pilates + Avancé, jour libre) → ∅.
- **Élargissement sur le niveau adjacent** : l'adjacent d'Avancé est Intermédiaire uniquement.
  Pilates/Intermédiaire → ∅, que le jour soit conservé ou relâché. Débutant n'étant pas adjacent
  d'Avancé, Sarah Andre reste hors d'atteinte.

Le raisonnement du PRD est donc juste dans son détail comme dans sa conclusion. UJ-2 est
également exact quand il dit « le bot ne propose jamais un écart de niveau aussi large ».

**Sarah Andre est en outre le seul profil du fichier qui ne peut jamais être apparié** : elle
est la seule pratiquante de Pilates, et aucun autre profil ne partage son sport à quelque niveau
que ce soit. Elle est simultanément la seule personne capable de déclencher FR-7 (voir Écart 1)
et la seule à qui le produit ne pourra jamais rien proposer si elle devenait demandeuse.

### Numéros de téléphone → **vérifié sur les trois critères**

- **Format** : 86 / 86 satisfont `^\+3363998[0-9]{4}$`. Aucune exception, aucun espace, aucun
  format national résiduel (`06…`), aucun séparateur.
- **Unicité** : 86 valeurs distinctes pour 86 lignes.
- **Aucun numéro d'origine survivant** : la plage occupée est exactement 0001→0086 dans l'ordre
  du fichier, sans trou, ce qui exclut toute valeur héritée. Un balayage de l'ensemble de
  `documentation/` par l'expression `\+33[0-9]{9}` ne retourne **aucune** occurrence hors
  `+3363998*`. Le répertoire n'étant pas suivi par git, la comparaison à une version antérieure
  est impossible ; la vérification porte donc sur l'état courant, qui est propre.

*Réserve de garde-fou, pas un défaut de la donnée :* la séquence est parfaitement prédictible.
FR-14 fait dépendre l'autorisation d'envoi de l'appartenance à la plage ; l'addendum a raison
d'exiger que l'origine du numéro soit portée par le modèle plutôt que déduite du préfixe, car
un numéro de cette plage est trivial à forger.

### FR-6, règle d'ordre → **non applicable en l'état : trou de spécification**

La règle est : « au plus trois candidats, classés par proximité au jour demandé, à égalité
l'ordre du vivier ». Trois indéterminations la rendent inexécutable sans décision supplémentaire.

1. **« Proximité » n'a pas de définition sur des jours de semaine sans date.** Deux lectures sont
   également défendables : la *distance cyclique* dans la semaine (Lundi est à 1 de Mardi, comme
   Mercredi), ou la *prochaine occurrence* à partir du jour demandé (Mercredi est à 1 de Mardi,
   Lundi à 6). Les deux donnent des résultats différents.
2. **Un candidat porte 2 ou 3 jours**, jamais un seul. Rien ne dit si la proximité se mesure sur
   son jour le plus proche, sur une moyenne, ou autrement.
3. **La donnée n'a aucun ancrage temporel.** « Mardi » n'est pas une date ; la lecture
   « prochaine occurrence » fait dépendre l'ordre affiché du jour où la conversation a lieu. Deux
   utilisateurs formulant la même demande verraient deux classements différents selon le moment.

**Mesure de l'impact sur la donnée réelle.** Sur les 127 combinaisons vides, 108 produisent plus
d'un candidat après élargissement sur le jour :

| Mesure sur les 108 combinaisons multi-candidats | Résultat |
|---|---|
| Comportent au moins un ex aequo — distance cyclique | 105 / 108 (**97 %**) |
| Comportent au moins un ex aequo — prochaine occurrence | 96 / 108 (**89 %**) |
| Classement différent entre les deux lectures | 37 / 108 (**34 %**) |

Autrement dit : **le critère de proximité est neutralisé par des ex aequo dans neuf cas sur dix,
et c'est le tie-break — « l'ordre du vivier » — qui décide en pratique.** Sur le vivier
d'amorçage, « l'ordre du vivier » est l'ordre du CSV, lui-même un artefact de génération
(rotation régulière des sports, Pilates inséré en ligne 12) : le classement des candidats est
donc gouverné par un ordre arbitraire, systématiquement favorable aux lignes basses.

**Et ce n'est pas cosmétique.** Sur les 12 combinaisons où le plafond de trois mord réellement
(4 candidats disponibles), **7 changent de trio selon la lecture retenue** — un candidat sur
quatre est donc montré ou masqué par une règle que le PRD n'a pas tranchée. Exemples :

- Rugby / Dimanche / Avancé → cyclique : Ethan Arnaud, Noé Jacquet, Sami Paul ; prochaine
  occurrence : Louis Roux, Ethan Arnaud, Noé Jacquet. **Deux noms sur trois diffèrent.**
- Natation / Dimanche / Intermédiaire → Chloé Garcia en tête, ou Inès Chevalier.
- Football / Samedi / Intermédiaire → Nathan Morel affiché, ou Axel Descamps.

**Sur l'exemple phare du PRD, la règle ne fait rien.** Tennis/Mardi/Intermédiaire : en distance
cyclique, Anna, Iris et Tessa sont **toutes trois à distance 1** — égalité parfaite, l'ordre
affiché est purement celui du CSV (lignes 22, 52, 82), qui se trouve être celui du PRD. En
« prochaine occurrence », Anna et Iris sont à 1 et Tessa à 4, ce qui produit le même ordre par
coïncidence. L'illustration de FR-6 ne teste donc pas sa propre règle d'ordre.

**Conclusion : la règle est un trou de spécification.** À trancher explicitement : définition de
la distance, agrégation sur les jours multiples d'un candidat, et ancrage à une date de référence.

---

## Écarts et angles morts

*Du plus grave au plus faible. Chaque constat est chiffré sur la donnée.*

### 1. FR-7 est quasi inatteignable, le chiffre qui le justifie mesure une branche que le produit n'exécute jamais, et SM-C1 en devient inerte

FR-7 ne se déclenche **qu'après échec de l'élargissement sur le jour** (« Un niveau adjacent
n'est proposé qu'après l'échec de l'élargissement sur le jour »). Or l'élargissement sur le jour
échoue dans **14 combinaisons sur 231**, et ces 14 sont **toutes du Pilates**. Dans ces 14 cas :

- si l'élargissement de niveau conserve le jour demandé : **2 combinaisons** produisent un
  candidat — Pilates/Mardi/Intermédiaire et Pilates/Jeudi/Intermédiaire, toutes deux Sarah Andre ;
- s'il relâche aussi le jour : **7 combinaisons** — Pilates/Intermédiaire sur les 7 jours,
  toujours Sarah Andre.

**FR-7 produit donc un candidat dans 2 combinaisons sur 231 (0,9 %), au mieux 7 (3,0 %), et
toujours la même personne.** Sur le vivier d'amorçage, la « descente de niveau » est une exigence
morte.

Le chiffre qui fonde la règle est symétriquement trompeur. Le PRD écrit : « relâcher le niveau
vers un niveau adjacent en conservant le jour n'en récupère que 46 (36 %) ». **Ces 46
combinaisons sont toutes incluses dans les 113 que l'élargissement sur le jour récupère
d'abord** — vérifié : les seules combinaisons où le jour échoue sont les 14 du Pilates, et
l'élargissement de niveau y récupère 2 combinaisons, pas 46. Le « 36 % » est donc une comparaison
*contrefactuelle* entre deux stratégies alternatives, présentée comme si elle décrivait la
stratégie séquentielle réellement spécifiée. Le chiffre est exact ; l'usage qu'en fait le
raisonnement ne l'est pas.

**Conséquence directe sur les critères de réussite : SM-C1 est inatteignable.** La contre-métrique
surveille « la part des mises en relation obtenues par descente de niveau » et fixe un seuil
d'alarme à 20 %. Sur le vivier d'amorçage, le plafond structurel de cette part est de l'ordre
de 1 %. **La contre-métrique ne peut pas se déclencher, donc elle ne contrebalance rien.** Elle
ne redeviendra significative que sur un vivier enrichi — ce que ni le §10 ni le §5.2 ne disent.

*À faire :* soit reformuler le §5.2 pour dire que le 46 / 36 % est une comparaison de stratégies
et non une propriété du parcours retenu, soit assumer que FR-7 est une exigence prospective ; et
dans les deux cas indiquer que SM-C1 ne devient mesurable qu'au-delà du vivier d'amorçage.

### 2. UJ-2 n'est pas « le cas majoritaire à 55 % » — sa fréquence réelle est de 5,2 %, et elle tient tout entière à un seul profil sur 86

Le PRD affirme deux fois que le parcours « il n'y a personne » est majoritaire : en §2.3 (« Ce
parcours n'est pas un cas limite : […] 55 % ne renvoient aucun candidat ») et en SM-4 (« Le
parcours de UJ-2 — le cas majoritaire à 55 % »).

Recalcul. Les 55 % (127 / 231) mesurent l'absence de résultat **exact**, avant tout
élargissement — c'est-à-dire précisément le domaine de FR-6 et de **UJ-1**, où le bot trouve
quelqu'un mais pas le bon jour. Le cas de UJ-2 — rien du tout, après recherche exacte,
élargissement sur le jour **et** élargissement sur le niveau — se produit dans :

- **12 combinaisons sur 231 = 5,2 %** si l'élargissement de niveau conserve le jour ;
- **7 combinaisons sur 231 = 3,0 %** s'il relâche aussi le jour.

**Écart d'un facteur dix.** Et le constat le plus lourd : **les 12 combinaisons mortes sont
toutes du Pilates**, donc toutes imputables à l'unique ligne 12 du fichier. Retirez Sarah Andre
du vivier et **le parcours UJ-2 ne se produit jamais sur les données d'amorçage** : FR-8 et FR-9
ne seraient exercés par aucune demande.

Le PRD élève ce comportement au rang de « comportement principal du produit, pas un traitement
d'erreur ». Sur cette donnée, c'est l'inverse : c'est un comportement que **1,2 % du vivier**
rend observable. La justification est bonne pour FR-6 / UJ-1 ; elle a été recopiée sous UJ-2 où
elle ne s'applique pas.

*À faire :* corriger SM-4 et le dernier paragraphe de UJ-2. Le bon argument existe pourtant —
UJ-2 se justifie non par sa fréquence sur la grille, mais par le fait qu'un vivier réel en
amorçage comportera toujours des sports à un seul pratiquant. Le dire ainsi serait vrai et tout
aussi fort.

### 3. Aucune colonne de localisation : le produit apparie sans aucune contrainte géographique, et le PRD ne le nomme jamais

Le fichier ne porte ni ville, ni code postal, ni région, ni rayon. Le PRD le constate comme une
**absence de donnée** (« Les données d'amorçage ne contenant aucune localisation, la ville est
demandée dans la conversation », §5.4) mais jamais comme une **contrainte manquante sur
l'appariement**.

Or la chaîne complète en dépend. FR-11 demande la ville de **l'utilisateur** et propose des
terrains **dans cette ville**. FR-14 envoie ensuite au partenaire un SMS portant « le sport, le
jour, l'heure, **le lieu** et le prénom du demandeur ». Le partenaire d'amorçage, lui, n'a jamais
déclaré où il vit — et le produit n'a aucun moyen de le savoir. **Un utilisateur lyonnais peut
recevoir Anna Perrot comme candidate et lui proposer par SMS un court de tennis à Lyon alors que
rien n'indique qu'elle y habite.**

Ce n'est pas un détail d'implémentation : c'est la seule contrainte du monde physique que le
produit organise et qu'il ne modélise pas. Le §5.2 énonce une hiérarchie explicite — « le jour se
négocie, le niveau se défend » — dans laquelle **la distance n'apparaît pas**, alors qu'en
pratique elle domine les deux autres : personne ne traverse la France pour un match de tennis
avec quelqu'un de son niveau.

SM-1 (« le parcours complet de UJ-1 se déroule de bout en bout ») peut être déclaré atteint alors
même que le rendez-vous produit est géographiquement absurde, parce qu'aucun critère ne regarde
ce point.

*À faire :* soit poser explicitement une hypothèse `[ASSUMPTION]` selon laquelle le vivier
d'amorçage est réputé colocalisé avec l'utilisateur — hypothèse fausse mais assumée, acceptable
pour un vivier fictif — soit inscrire la localisation en question ouverte au même rang que la
source des terrains. Le silence actuel est le pire des trois.

### 4. FR-7 est ambigu sur le devenir du jour, et l'ambiguïté change le résultat sur la donnée

FR-7 dit « le bot **propose** un niveau adjacent » sans dire si la contrainte de jour est
maintenue. Les deux lectures cohabitent dans le document : le chiffre du §5.2 (46) est calculé
**jour conservé**, tandis que UJ-2 fait dire au bot qu'il a regardé « les autres jours **puis** le
niveau en dessous », ce qui suggère un élargissement cumulatif.

Sur la donnée, le choix n'est pas neutre : il fait passer de **2 à 7** le nombre de combinaisons
où FR-7 produit un candidat — les cinq combinaisons Pilates/Intermédiaire des jours autres que
mardi et jeudi. Sur un vivier enrichi, l'écart sera bien plus large. À trancher dans le texte de
FR-7, pas dans une note.

### 5. La règle d'ordre de FR-6 est indécidable sur des jours sans date, et le tie-break gouverne neuf cas sur dix

Développé plus haut, section « Vérification des conséquences testables ». Résumé : 97 % des
combinaisons multi-candidats comportent un ex aequo en distance cyclique, 34 % changent de
classement selon la lecture retenue, et **7 des 12 combinaisons où le plafond de trois mord
changent de trio affiché**. Le tie-break « ordre du vivier » n'est lui-même pas défini une fois
que des utilisateurs inscrits rejoignent le vivier — ordre d'inscription ? identifiant ? — la
spécification manque donc à deux niveaux.

S'y ajoute le trou sous-jacent : **le vivier ne porte que des jours de semaine, et rien ne dit
comment un jour devient une date.** FR-10 (météo) et FR-12 (agenda) exigent pourtant une date
précise. UJ-1 la produit narrativement (« un trou le mardi suivant ») sans qu'aucune exigence
n'en fixe la règle.

### 6. Quatre profils sur dix pratiquent un sport que le produit dit ne pas servir — et selon la taxonomie de l'addendum, un seul sport sur onze est un vrai sport de duel

Recompté : Football 9 + Basket-ball 9 + Rugby 8 + Volley-ball 8 = **34 profils, soit 39,5 % du
vivier**, pratiquent un sport collectif que le §2.2 exclut explicitement (« Les sports d'équipe
pris comme tels […] Un footballeur peut y trouver un partenaire d'entraînement, pas un match »).
Danse 9 + Yoga 8 + Pilates 1 = **18 profils, 20,9 %**, pratiquent une activité de cours collectif
où la notion de « partenaire » est faible.

L'addendum aborde désormais ce point dans « Pièges de démonstration », ce qui est un progrès
réel — mais sa propre classification range natation, course à pied et escalade parmi les sports
« sans appariement en duel ». Additionnée à ses 34 profils de sport collectif, cette lecture
laisse **le tennis seul — 9 profils, 10,5 %** — comme sport d'appariement en duel véritable. Le
vivier d'amorçage soutient donc mal la promesse du §1 (« trouver quelqu'un avec qui pratiquer son
sport, à son niveau »), et SM-2 (« un échantillon de demandes couvrant les 11 sports ») valide la
non-invention sur des sports dont six sur onze ne produisent pas d'usage naturel. Le PRD tient la
position par la définition élargie de « Partenaire » au §3, mais ne chiffre jamais l'ampleur de
ce que cette définition doit absorber.

### 7. Le plafond de trois candidats de FR-6 ne mord presque jamais, et la phrase qui l'admet cite le mauvais chiffre

Recalcul de la taille des lots après élargissement sur le jour, sur les 127 combinaisons vides :
0 candidat → 14 ; 1 → 5 ; 2 → 40 ; 3 → 56 ; 4 → 12. **Le plafond ne mord que dans 12
combinaisons (9,4 %), et toujours d'exactement une personne**, la classe sport × niveau la plus
fournie du fichier comptant 4 membres. La branche « au-delà de trois candidats, le bot dit qu'il
y en a d'autres et propose de les montrer » est donc exercée par 12 combinaisons sur 231, avec un
seul candidat caché à chaque fois.

Le §5.2 a raison sur le fond (« le plafond n'y mord donc presque jamais »), mais l'étaye avec
« 19 % des combinaisons ne renvoient qu'un seul candidat » — soit 45 / 231, une statistique de la
recherche **exacte** (FR-5), où le plafond de FR-6 ne s'applique pas. Le chiffre pertinent pour
FR-6 est **5 / 127 = 3,9 %** de combinaisons à un seul candidat, ou, plus directement,
**12 / 127 = 9,4 %** de combinaisons où le plafond agit. Argument juste, preuve mal choisie.

### 8. SM-3 n'est pas une mesure mais un test binaire

SM-3 exige « au moins 85 % des 127 combinaisons sans résultat exact produisent au moins un
candidat du niveau exact demandé », et le §5.2 en donne le plafond : 89 %. Or **113 / 127 est un
invariant de la donnée** : une implémentation correcte de FR-6 rend exactement 88,98 %, une
implémentation défaillante rend moins. Il n'existe aucun mécanisme produisant une valeur
intermédiaire entre 85 % et 89 % autre qu'un bug partiel. La marge autorisée vaut 5 combinaisons
sur 127. SM-3 ne mesure donc pas une performance, il vérifie une exactitude — ce qui est utile,
mais devrait être écrit comme tel : « FR-6 récupère les 113 combinaisons attendues, sans
exception ».

### 9. Constats de donnée que le PRD ne relève pas (impact faible, mais exploitables)

- **Le mardi est le jour le mieux couvert (28 profils) et le dimanche le moins (21)** — mais aucun
  jour n'est absent et l'amplitude n'est que de 1,33×. La donnée ne comporte donc **aucun jour
  mort** : le facteur limitant n'est pas la répartition des jours, c'est leur rareté par personne
  (2,03 jours déclarés en moyenne, soit 29 % de la semaine). Le PRD a désormais la bonne cause
  (« 83 des 86 ne déclarent que deux jours ») ; il pourrait ajouter que la couverture hebdomadaire
  est en revanche homogène, ce qui garantit qu'aucune demande ne meurt à cause du jour choisi.
- **La colonne « Sports pratiqués » est au pluriel et admet le séparateur `;`, mais 86 profils sur
  86 sont mono-sport.** Le chemin multi-sport du chargement d'amorçage n'est donc exercé par
  aucune ligne du fichier : l'addendum a raison d'exiger un modèle multi-sport, mais aucune donnée
  ne le testera au chargement.
- **La colonne « Nom » est chargée et n'est exploitée par aucune exigence.** FR-12 écrit « le
  prénom du partenaire », FR-14 « le prénom du demandeur », UJ-1 nomme « Anna, Iris et Tessa ».
  Le §7 (Vie privée) protège les numéros mais ne dit rien des noms de famille de 86 personnes qui
  n'ont rien demandé, alors qu'ils sont stockés sans usage. À arbitrer : les charger ou non.
- **« Lucas » est à la fois un prénom et un nom à l'intérieur du même sport** : Lucas Moreau
  (Football, Intermédiaire, ligne 1) et Théo Lucas (Football, Avancé, ligne 41). La convention
  « prénom seul » de FR-12 et FR-14 y est ambiguë. « Paul » et « Robin » présentent la même
  collision mais sur des sports différents, donc sans conséquence. Aucun prénom n'est dupliqué et
  aucun nom non plus : c'est le seul cas.
- **L'ordre du fichier est un artefact de génération** : rotation régulière des dix sports
  principaux, Pilates inséré en ligne 12, cycle des niveaux régulier. Comme cet ordre sert de
  tie-break à FR-6 (Écart 5), les candidats de rang bas dans la rotation sont systématiquement
  favorisés — un biais reproductible, pas un aléa.
- **Le format des libellés impose un travail d'extraction à FR-2** : « Basket-ball » et
  « Volley-ball » avec trait d'union, « Course à pied » en trois mots accentués, et des prénoms à
  diacritiques rares (Maëlys, Thaïs, Anaëlle, Timéo). FR-2 doit rapprocher « foot », « basket »,
  « volley », « course » de ces libellés exacts ; aucune exigence ne le dit, et « Un sport absent
  du vivier reçoit une réponse explicite » suppose résolue une normalisation qui ne l'est nulle
  part.
- **Trois profils déclarent trois jours** (Lucas Moreau, Hugo Martin, Gabriel Petit) ; deux
  profils seulement déclarent un week-end complet (Arthur Lopez et Paul Maillard, Samedi;Dimanche,
  tous deux en Escalade) ; trois profils seulement portent deux jours consécutifs. La donnée est
  donc construite pour disperser les disponibilités — ce qui explique mécaniquement les 55 % de
  vide, et confirme que ce taux est une propriété du générateur, pas une observation du monde.

---

## Notes

- **Périmètre.** Aucun fichier existant n'a été modifié. Ce document est le seul fichier créé.
- **Méthode.** Toutes les valeurs proviennent d'un recalcul direct sur `SportsProfiles.csv`
  (lecture CSV, UTF-8 sans BOM, séparateur `,`, listes internes séparées par `;`). Les définitions
  retenues pour reproduire les chiffres du PRD sont : *recherche exacte* = même sport ET jour
  demandé présent dans les jours disponibles ET niveau identique ; *élargissement sur le jour* =
  même sport ET niveau identique, jour libre ; *élargissement sur le niveau* = même sport ET jour
  demandé conservé ET niveau adjacent (Débutant↔Intermédiaire, Intermédiaire↔Avancé, jamais
  Débutant↔Avancé). Ces trois définitions reproduisent exactement les 127 / 113 / 46 du PRD, ce
  qui confirme qu'elles sont bien celles employées par ses auteurs.
- **Les deux lectures de l'élargissement de niveau** (jour conservé / jour relâché) sont
  distinguées partout où elles donnent des résultats différents, parce que le PRD ne tranche pas.
- **Le PRD et l'addendum ont été modifiés pendant l'analyse** : ajout du paragraphe sur les 83
  profils à deux jours et sur le plafond de FR-6 en §5.2 ; ajout de la section « Pièges de
  démonstration » dans l'addendum. Les chiffres ci-dessus portent sur l'état final des deux
  documents et intègrent ces ajouts.
- **Vérification des numéros.** Le répertoire `documentation/` n'est pas suivi par git ; il
  n'existe donc aucune version antérieure du CSV à laquelle comparer. La conclusion « aucun numéro
  d'origine n'a survécu » s'appuie sur deux constats indépendants : la séquence 0001→0086 est
  complète et sans trou, et aucune chaîne `+33XXXXXXXXX` hors plage de fiction n'apparaît nulle
  part dans `documentation/`.
- **Ce qui n'a pas été vérifié.** Le contenu de `research-niveau.md` et `research-paysage.md`
  n'entre pas dans le périmètre de cette réconciliation, qui porte uniquement sur la cohérence
  entre le CSV et les affirmations qu'en tirent `prd.md` et `addendum.md`.
