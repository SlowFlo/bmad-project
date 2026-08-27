---
title: "Revue de dérive amont — PRD v2 → spines UX v3"
type: review
status: final
created: 2026-08-27
scope:
  amont:
    - ../../prds/prd-bmad-2026-08-26/prd.md (v2, 2026-08-27)
    - ../../prds/prd-bmad-2026-08-26/addendum.md
    - ../../prds/prd-bmad-2026-08-26/SportsProfiles.csv
    - ../../prds/prd-bmad-2026-08-26/research-niveau.md
    - ../../prds/prd-bmad-2026-08-26/research-paysage.md
  aval:
    - DESIGN.md (v3, 2026-08-27)
    - EXPERIENCE.md (v3, 2026-08-27)
    - mockups/*.html (7 fichiers)
---

# Revue de dérive amont — PRD v2 → spines UX v3

## 0. Verdict

**La resynchronisation v3 est réelle et globalement réussie.** Le renversement du modèle du
niveau (FR-15 retirée, FR-7 retirée, FR-16 ajoutée, FR-3 mono-sport, FR-2 liste ouverte) est
absorbé dans les deux spines, les chiffres périmés de la v2 sont corrigés, la géographie est
propre, et le contre-pied assumé de `research-niveau` §4.1 est énoncé sans maquillage — c'est
le meilleur passage des deux documents.

**Mais la dérive n'est pas entièrement résorbée.** Elle s'est déplacée : elle ne porte plus sur
le modèle du niveau, elle porte sur **FR-14 et le côté partenaire**, que la v3 n'a pas rouvert
alors qu'elle en avait l'occasion. Une contradiction est frontale et non tracée (le conflit de
créneaux), une autre est structurelle (le canal e-mail du partenaire inscrit n'existe nulle
part), et un jeu de données fabriqué s'est glissé dans le parcours canonique — trois jours
disponibles sur quatre sont faux dans la maquette de référence de UJ-1, dont un jour qui
n'existe dans aucun profil du fichier d'amorçage.

| Catégorie | Compte |
|---|---|
| Exigences vivantes du PRD | **14** (FR-1→6, FR-8→14, FR-16) |
| Avec un foyer dans les spines | **14 / 14** |
| Orphelines au niveau de l'exigence | **0** |
| Conséquences testables orphelines | **7** |
| Contradictions **silencieuses** | **9** |
| Divergences **tracées** (encadrés) | **9**, dont **1 dont l'encadré ne dit pas vrai** |
| Chiffres de la liste de contrôle vérifiés | **13 présents / 14** (« 33 paires » absent), **13 exacts en valeur**, **1 attribué au mauvais parcours** |
| Chiffres hors liste faux ou périmés | **2** (34 °C ; « mercredi 3 septembre ») |
| Noms propres vérifiés | **7**, **2 fautifs** (Iris, Anna) |
| Géographie | **conforme** — aucun lieu non lyonnais |

---

## 1. Exigences vivantes du PRD et leur foyer

### 1.1 État civil des identifiants

| Identifiant | État PRD | Traitement dans les spines |
|---|---|---|
| **FR-7** | **Supprimée** (prd.md:991-993) | Correctement traitée comme retirée : EXPERIENCE.md:8, 200, 243, 372, 427, 463 ; DESIGN.md:8, 369. Aucune spine ne la cite comme vivante. ✅ |
| **FR-15** | **Pierre tombale** (prd.md:318-329) | Correctement traitée : EXPERIENCE.md:74, 99, 231, 233, 443 la citent comme retirée et disent ce qui lui est arrivé. ✅ |
| **FR-16** | **Nouvelle** (prd.md:628-660, 1020-1023) | Absorbée : EXPERIENCE.md:201, 236-238, 313, 452 ; DESIGN.md:299, 435. ✅ |
| **SM-C1** | **Retirée** | Citée comme retirée en EXPERIENCE.md:427. ✅ |
| **SM-C2** | Abaissée 5 → 4 tours | EXPERIENCE.md:233 « SM-C2 est abaissée à quatre tours ». ✅ |
| **QO-3** | Fermée | Non citée par les spines — sans conséquence. |

### 1.2 Table de couverture

| Exigence | Foyer dans les spines | Verdict |
|---|---|---|
| **FR-1** Dialoguer sans authentification | IA `Le fil, à froid` EXPERIENCE.md:50 ; état `Fil à froid, inconnu` EXPERIENCE.md:229 ; parcours 1 étape 1 EXPERIENCE.md:441 | ✅ **Foyer** — jamais cité par son identifiant (voir §2, D-3) |
| **FR-2** Extraire la demande, niveau non interprété | `level-choice` DESIGN.md:236-255, 438 ; états `Demande incomplète` / `Niveau pris dans la phrase` / `Déclaration du niveau` / `Refus du niveau` EXPERIENCE.md:231-234 ; libellés contractuels EXPERIENCE.md:114-118 ; `Sport hors vivier` EXPERIENCE.md:239 ; `Hors zone` EXPERIENCE.md:240 | ✅ **Foyer riche** — le mieux traité de la v3 |
| **FR-3** Enregistrer l'utilisateur, mono-sport | `sport-replace` DESIGN.md:256-264, 439 ; EXPERIENCE.md:205, 235 ; `Entrée au vivier` EXPERIENCE.md:142 ; parcours 3 variante EXPERIENCE.md:488 | ✅ **Foyer** |
| **FR-4** Demander un compte au bon moment | `auth-block` DESIGN.md:153-158, 436 ; EXPERIENCE.md:55, 202 ; parcours 1 étape 9 | ✅ **Foyer** — sauf le numéro facultatif (§3, O-4) |
| **FR-5** Recherche exacte | `Correspondance exacte` EXPERIENCE.md:242 ; égalité stricte rappelée EXPERIENCE.md:206, 243, 461 | ✅ **Foyer** — jamais mis en scène nommément (§4, N-3) |
| **FR-6** Élargir sur le jour | `partner-card` DESIGN.md:433 ; `candidate-group-label` DESIGN.md:440 ; EXPERIENCE.md:200, 206, 243, 244 ; parcours 1 étape 5 | ⚠️ **Foyer, mais règle d'ordre inversée** (§2, C-3) |
| **FR-8** Annoncer l'absence sans broder | `Vivier vide` EXPERIENCE.md:245 ; `Sport hors vivier` EXPERIENCE.md:239 ; microcopie EXPERIENCE.md:119-120 ; parcours 2 étape 4 | ✅ **Foyer** — jamais cité par son identifiant |
| **FR-9** Alerte différée | EXPERIENCE.md:59, 141, 184-189, 246, 247 ; parcours 2 étape 5 | ✅ **Foyer** |
| **FR-10** Jouabilité | `playability-callout` DESIGN.md:173-181, 441 ; EXPERIENCE.md:211, 248, 249, 251 ; parcours 1 étape 8 | ✅ **Foyer** — les seuils sont correctement délégués à FR-10 |
| **FR-11** Proposer un lieu à Lyon | `Proposition de lieu` EXPERIENCE.md:210 ; `Aucun lieu disponible` EXPERIENCE.md:250 ; microcopie EXPERIENCE.md:127 | ⚠️ **Foyer** — jamais cité par son identifiant ; repli PRD non implémenté (§2, C-6) |
| **FR-12** Écrire dans l'agenda | `agenda-choice` DESIGN.md:159-164, 437 ; EXPERIENCE.md:57, 203, 268 ; parcours 1 étape 10 | ⚠️ **Foyer côté geste**, aucun côté contenu de l'événement (§3, O-1, O-6) |
| **FR-13** Quatre statuts | `status-badge-*` DESIGN.md:434 ; EXPERIENCE.md:212, 253-256 ; texte sortant n° 3 | ⚠️ **Foyer** — deux conséquences testables orphelines (§3, O-1, O-3) |
| **FR-14** Prévenir le partenaire, lien d'acceptation | Page d'acceptation DESIGN.md:449 ; EXPERIENCE.md:36, 60, 213, 271-284 ; SMS EXPERIENCE.md:173-175 ; parcours 4 | 🔴 **Foyer, mais contredit sur deux points** (§2, C-1, C-2) |
| **FR-16** Cycle de vie au vivier | `meeting-recap` DESIGN.md:435 ; EXPERIENCE.md:201, 236-238, 313 ; parcours 1 étape 12, parcours 3 étape 2 | ✅ **Foyer** — l'ajout le plus propre de la v3 |

**Exigences non fonctionnelles (§6)** — latence 2 s / 20 s : EXPERIENCE.md:259, 415 ✅ ·
robustesse des services externes : EXPERIENCE.md:129, 252, 457 ⚠️ (une clause non tenue, §2 C-6) ·
reprise de conversation 30 jours : EXPERIENCE.md:269, 299, 383 ✅ ·
surface responsive 360 px : EXPERIENCE.md:26, 393 ✅.

**Garde-fous (§7)** — « le bot n'invente rien » : `La grammaire de l'honnêteté`
EXPERIENCE.md:304-315 ✅ (excellent) · « l'intégrité du niveau » : EXPERIENCE.md:425-431 ✅
(voir §5) · « l'enfermement dans la conversation » : EXPERIENCE.md:126, 258 ✅ ·
« vie privée » : EXPERIENCE.md:99, 202, 329 ✅.

---

## 2. Contradictions

### 2.1 Contradictions SILENCIEUSES (défauts)

---

#### 🔴 C-1 — CRITIQUE — Le conflit de créneaux : la spine fait exactement l'inverse de FR-14

**PRD**, prd.md:622-624 :

> **Deux acceptations qui se chevauchent sont impossibles :** accepter un créneau qui
> entre en conflit avec une rencontre déjà *confirmée* du même partenaire **échoue**, la page
> le lui dit, et la rencontre concernée passe en *déclinée*.

**Spine**, EXPERIENCE.md:284 :

> **Conflit de créneaux.** Si la personne a déjà accepté une rencontre qui chevauche celle-ci,
> la page le dit avant les boutons et **laisse le choix — elle ne bloque pas** : c'est elle qui
> sait si les deux tiennent.

Et la maquette `mockups/key-page-acceptation.html:243` **argumente** la décision inverse :
« La page dit, et ne bloque pas. Le conflit est énoncé avant les boutons, et les deux réponses
restent ouvertes. »

Le PRD dit **échoue** ; la spine dit **ne bloque pas**. Ce n'est pas un flou, c'est le
contraire terme à terme, sur la seule règle de FR-14 qui protège l'intégrité des données.
La maquette va plus loin : elle affiche les deux boutons actifs et rend le double engagement
atteignable en un clic.

**Aucun encadré ne signale l'écart.** La v3 a écrit trois encadrés de correction sur d'autres
sujets ; celui-ci n'existe pas. Le raisonnement de la maquette (« le produit ne connaît que
des jours, jamais des durées ») est peut-être meilleur que la règle du PRD — mais c'est un
arbitrage produit, et il doit remonter au PRD, pas se prendre en silence dans une spine
qui se déclare subordonnée.

**Constat aggravant :** FR-16 rend cette collision rare (un jour se bloque dès l'état *en
attente*), et le PRD le dit lui-même (prd.md:656-660) : la règle de FR-14 « ne protège plus
que la fenêtre de course entre deux validations quasi simultanées ». La maquette met en scène
précisément ce cas (18 h et 19 h le même mercredi) et le laisse passer.

**À faire :** soit la spine s'aligne sur FR-14 (l'acceptation échoue et la rencontre passe en
*déclinée*), soit le PRD amende FR-14 et le journalise au §13. Pas de troisième issue.

---

#### 🔴 C-2 — ÉLEVÉ — Le partenaire est toujours traité comme un profil d'amorçage : le canal e-mail de FR-14 n'existe nulle part

**PRD**, prd.md:601-602 (FR-14) :

> Le partenaire est prévenu par **SMS** s'il a un numéro de téléphone, **par e-mail s'il est
> utilisateur inscrit et n'en a pas donné**.

**Spines** — le partenaire est un profil d'amorçage joint par SMS, sans exception, six fois :

- EXPERIENCE.md:36 — « la personne qu'on vient de retenir **reçoit un SMS**, suit un lien »
- EXPERIENCE.md:60 — « Atteinte depuis : **un SMS** reçu par la personne retenue »
- EXPERIENCE.md:173 — « **envoyé par SMS**. C'est le **seul contact qu'un profil d'amorçage
  aura jamais avec le produit** »
- EXPERIENCE.md:213 — « Hors du fil, **atteinte par le lien d'un SMS** »
- EXPERIENCE.md:319 — « n'entre en contact avec le produit qu'une fois, **par le SMS** »
- EXPERIENCE.md:492 — « **Anna figure dans les données d'amorçage** »

Le texte sortant n° 2 (EXPERIENCE.md:175) est rédigé pour cette seule population et devient
**faux** pour l'autre : « votre nom figure dans les données de départ d'Ex Aequo » n'a aucun
sens envoyé à quelqu'un qui a créé un compte la semaine dernière.

C'est une régression de raisonnement, et la spine s'était pourtant corrigée sur ce point :
son propre encadré EXPERIENCE.md:321 dénonce une v1 qui décrivait ces profils comme
« incapables de répondre », et EXPERIENCE.md:325 pose que « la carte de partenaire est
identique pour les deux populations ». **Si un utilisateur inscrit peut être proposé comme
partenaire — et il le peut, FR-3 le fait entrer au vivier pour cela — alors il peut être
celui qu'on retient, et il n'y a pas de SMS pour lui.** La v3 tient la symétrie côté
proposition et la perd côté notification.

**À faire :** un cinquième texte sortant (sollicitation par e-mail d'un partenaire inscrit),
et une reformulation des six passages ci-dessus en « SMS ou e-mail selon la population ».

---

#### 🔴 C-3 — ÉLEVÉ — La règle d'ordre de FR-6 est glosée à l'envers

**PRD**, prd.md:431-434 (FR-6) :

> classés par **délai d'attente croissant** : pour chaque candidat, **le nombre de jours à
> attendre depuis le jour demandé jusqu'à sa prochaine disponibilité** […] **Le plus tôt
> d'abord.**

**Spine**, EXPERIENCE.md:244 :

> L'ordre est celui du **délai d'attente croissant** — **qui attend depuis le plus longtemps
> passe en premier** — et l'ordre du vivier départage les ex æquo.

L'étiquette est juste, la glose est fausse deux fois :

1. Elle transforme un **délai à venir** (jours d'ici à la prochaine disponibilité du candidat)
   en une **ancienneté** (depuis quand le candidat attend), qui n'est nulle part dans le modèle
   de données — aucun profil ne porte de date.
2. « Le plus longtemps passe en premier » décrit un tri **décroissant**, l'inverse de la
   phrase qui le précède dans la même cellule.

La maquette `mockups/key-proposition-partenaires.html:181` énonce la règle correctement
(« le plus tôt d'abord, l'ordre du vivier départageant les ex æquo ») — c'est donc la spine,
contractuellement supérieure à la maquette, qui porte l'erreur.

**À faire :** remplacer la glose par « celui qui redevient disponible le plus tôt passe en
premier ».

---

#### 🔴 C-4 — ÉLEVÉ — Le niveau est encore sur la carte de partenaire, dans le plancher d'accessibilité

Toute la v3 repose sur le retrait du niveau de la carte : DESIGN.md:8, 369, 433 ;
EXPERIENCE.md:8, 200, 206, 325, 372, 445. La règle est écrite six fois.

**Elle est enfreinte une septième**, dans une règle contractuelle d'accessibilité —
EXPERIENCE.md:354 :

> si la carte affiche « Anna » et « **Intermédiaire** · mercredi, samedi », le nom accessible
> commence par ces mots-là […] (« **Anna, intermédiaire**, disponible mercredi et samedi »)

C'est un résidu de la v2 dans la seule section qui décrit **ce que le lecteur d'écran entend**.
Un développeur qui implémente WCAG 2.5.3 depuis cette ligne recrée exactement l'affichage que
la v3 a supprimé, et le rend au surplus non conforme : le nom accessible contiendrait un mot
que le texte visible ne porte pas.

Le PRD est du même côté que la v3 — prd.md:721-723 : « **Il ne l'affiche pas non plus sur les
cartes de partenaires** : à niveau strictement égal il y serait identique partout, et se
lirait comme une garantie qu'il n'est pas. »

**À faire :** corriger l'exemple en « Anna » / « mercredi, samedi · dans 1 jour ».

---

#### ⚠️ C-5 — MOYEN — L'intitulé de groupe réinstalle le niveau que §7 voulait invisible, sans encadré

Le PRD interdit le niveau **sur la carte** et donne sa raison — prd.md:721-723 : il « se lirait
comme une garantie qu'il n'est pas ».

La spine le déplace d'un cran au-dessus et le rend **plus** promissoire :
DESIGN.md:440 et EXPERIENCE.md:206, libellé arrêté « **Trois intermédiaires, comme vous** ».
EXPERIENCE.md:206 assume explicitement le contre-argument : « absent c'est la promesse du
produit rendue invisible ».

La **lettre** de §7 est respectée (ce n'est pas la carte). Le **motif** de §7 est contredit :
« comme vous » est la formulation exacte d'une garantie sur une valeur que le PRD décrit
comme « déclarée, jamais vérifiée, jamais corrigée, et dont rien ne mesure la justesse »
(prd.md:735). Le produit vient de retirer les trois garde-fous du niveau ; c'est précisément
le moment où l'interface ne devrait pas gagner en aplomb sur ce point.

C'est le seul arbitrage de la v3 qui pèse dans le sens opposé à sa propre honnêteté, et
**aucun encadré ne l'expose**, alors que la spine en écrit sur des sujets bien moins lourds.

**À faire :** soit un encadré de divergence assumé, soit un libellé qui décrit sans promettre
(« Trois personnes du niveau que vous avez déclaré »).

---

#### ⚠️ C-6 — MOYEN — Sans données de terrains, le PRD fait saisir le lieu par l'utilisateur ; la spine continue sans lieu

**PRD**, prd.md:672-674 (§6, robustesse) :

> **sans données de terrains l'utilisateur indique le lieu lui-même**

**Spine** — trois endroits, tous « on continue sans » :

- EXPERIENCE.md:127 — « Je continue sans lieu : vous pouvez retenir le créneau et **convenir
  de l'endroit avec Anna**. »
- EXPERIENCE.md:250 — « Le créneau reste retenable **sans lieu**. »
- EXPERIENCE.md:457 — « Le lieu apparaît en `{components.unknown-value}` »

Nulle part la personne ne peut **donner** le lieu. La conséquence est chaînée : sans lieu, pas
d'attribut couvert/extérieur, donc **pas de jouabilité** (FR-10) — et la branche que le PRD
considère comme la seule garantie de FR-11 (`[NOTE FOR PM]` prd.md:545-548, QO-4) devient
la seule branche du produit. La NFR existait exactement pour empêcher ça.

**À faire :** ajouter au parcours le beat « dites-moi où, je le note » et son état.

---

#### ⚠️ C-7 — MOYEN — « Voici les cinq personnes » contre le plafond de trois de FR-6

**PRD**, prd.md:431 : « **Le bot présente au plus trois candidats** » — puis prd.md:438-439 :
au-delà, il « dit combien il y en a d'autres et propose de les montrer ».

**Spine**, microcopie contractuelle EXPERIENCE.md:126 :

> « Je n'ai pas de carte à vous montrer. **Voici les cinq personnes qui correspondent**, avec
> leurs jours. »

et EXPERIENCE.md:258 : « il donne ce qu'il peut sous une forme plus dense — **davantage de
candidats en une fois** ».

DESIGN.md:391 et EXPERIENCE.md:200 posent pourtant « trois au maximum » comme disposition
canonique. Le garde-fou §7 (l'enfermement dans la conversation) est réel et bien traité par
ailleurs, mais la microcopie arrêtée franchit le plafond sans dire de quelle forme (cartes ?
prose ?) ni sous quelle autorisation.

**À faire :** rattacher explicitement cette réponse à la branche « montrer les autres » de
FR-6, ou changer le chiffre.

---

#### ⚠️ C-8 — MOYEN — Le SMS de FR-14 est contredit par la règle commune des textes sortants

**Spine**, règle commune EXPERIENCE.md:160 : « **jamais le prénom du partenaire** ni son
numéro ». EXPERIENCE.md:59 : les courriels portent « **aucune donnée du partenaire** ».

**Spine**, texte sortant n° 3, EXPERIENCE.md:179 : « **Objet : Anna a répondu** ».

Le prénom du partenaire est dans l'objet du courriel, en violation de la règle écrite dix-neuf
lignes plus haut. Le PRD, lui, autorise le prénom du partenaire (FR-12, prd.md:563 : l'événement
d'agenda le porte) : c'est donc la **spine qui s'est imposé une règle plus stricte que sa
source, puis l'a enfreinte**. Un développeur qui lit les deux ne sait pas laquelle tient.

**À faire :** restreindre la règle commune à « jamais le numéro, jamais les coordonnées », ce
qui est ce que le PRD demande réellement (prd.md:606, prd.md:754-756).

---

#### ⚠️ C-9 — FAIBLE — « aucun terrain de tennis **ouvert** » suppose une connaissance des disponibilités

**PRD**, prd.md:542-543 (hors périmètre FR-11) : le produit « ne réserve rien, **ne connaît pas
les disponibilités** ».

**Spine**, EXPERIENCE.md:127 : « Je ne trouve aucun terrain de tennis **ouvert** dans votre
secteur. »

Un mot, mais il promet une donnée que le produit n'a pas — dans le document dont la thèse
centrale est que le bot n'affirme rien qu'il n'ait vérifié.

**À faire :** « aucun terrain de tennis dans votre secteur ».

---

#### ⚠️ C-10 — FAIBLE — Contradiction interne sur le coût en tours du bloc de niveau

EXPERIENCE.md:233, même cellule : « sans interroger personne et **sans coûter un tour** »
puis, deux phrases plus loin, « **Un seul tour**, jamais deux ». Le bloc coûte un tour ou n'en
coûte pas ; SM-C2 est comptée en tours, donc la phrase compte.

---

### 2.2 Divergences TRACÉES (légitimes — vérification de l'encadré)

| # | Où | Ce que l'encadré assume | L'encadré dit-il vrai ? |
|---|---|---|---|
| **D-1** | EXPERIENCE.md:425-429 | Le produit contredit sciemment `research-niveau` §4.1 ; la spine applique la décision du PRD « et ne la maquille pas en conformité » | ✅ **Vrai, et exemplaire.** Citation fidèle (voir §5). L'encadré va jusqu'à écrire ce que le design **ne** récupère **pas** et que « plus aucun instrument ne la mesure » — ce qui reprend fidèlement prd.md:731-739 |
| **D-2** | EXPERIENCE.md:28 | « Le PRD §6 énonce désormais la même chose » sur le PC-first, l'encadré de divergence v2 est supprimé | ✅ **Vrai** — prd.md:680-683, citation mot pour mot |
| **D-3** | EXPERIENCE.md:38 | Le principe « tout vit dans le fil » excluait FR-14 du produit ; corrigé côté partenaire | ✅ **Vrai** — prd.md:819-820 place FR-14 dans le périmètre |
| **D-4** | EXPERIENCE.md:74 | La `[DÉCISION OUVERTE — design]` de la v2 sur l'établissement du niveau est refermée par le retrait de FR-15 | ✅ **Vrai** — prd.md:985-990 |
| **D-5** | EXPERIENCE.md:321 | Correction de la prémisse « profils d'amorçage incapables de répondre » | ✅ **Vrai** — prd.md:237-241. ⚠️ Mais la correction est incomplète : voir C-2 |
| **D-6** | EXPERIENCE.md:465 | Le prénom « Sarah » de la v2 était celui de la seule pratiquante de Pilates ; le PRD avait choisi « Nadia » | ✅ **Vrai** — `SportsProfiles.csv:13` (Sarah Andre, Pilates, Débutant), prd.md:144, prd.md:904-906 |
| **D-7** | EXPERIENCE.md:477 | La v2 faisait dire au bot qu'il enregistrait Nadia sans compte — phrase fausse | ✅ **Vrai** — FR-3, prd.md:331-338 |
| **D-8** | EXPERIENCE.md:72, 301 | Deux `[DÉCISION OUVERTE]` non tranchées, dont le changement de créneau après écriture agenda (« le statut d'arrivée n'existe dans aucune des quatre valeurs de FR-13 ») | ✅ **Vrai** — prd.md:575-580 n'a effectivement pas de statut pour ça |
| **D-9** | DESIGN.md:397, 454 ; EXPERIENCE.md:68, 223, 288 (× 5) | « **Les quatre maquettes** sont à jour de la v3 » | 🔴 **FAUX — voir ci-dessous** |

#### 🔴 D-9 — MOYEN — L'encadré des maquettes, répété cinq fois, ne dit plus vrai

Le dossier `mockups/` contient **sept** fichiers, pas quatre :

```
key-declaration-niveau.html      27/08 09:01   ← référencée
key-fil-a-froid.html             27/08 09:01   ← référencée
key-proposition-partenaires.html 27/08 09:01   ← référencée
key-recap-en-attente.html        27/08 09:01   ← référencée
key-page-acceptation.html        27/08 11:06   ← JAMAIS référencée
key-remplacement-sport.html      27/08 11:07   ← JAMAIS référencée
key-vivier-vide.html             27/08 11:09   ← JAMAIS référencée
```

Les trois non référencées sont postérieures aux spines (09:02) et couvrent **FR-14, FR-3 et
FR-8** — c'est-à-dire les trois exigences les plus fragiles de cette revue. `key-page-acceptation.html`
est même l'artefact qui matérialise la contradiction C-1.

L'encadré affirme aussi que les défauts de la génération précédente sont corrigés, dont
`outline: none`. Il subsiste, littéralement : `key-recap-en-attente.html:99` et
`key-proposition-partenaires.html:112` portent `textarea:focus{outline:none}`. La règle est
techniquement rattrapée par le `form:focus-within` de la ligne précédente — que
EXPERIENCE.md:361 autorise — mais la même ligne 361 écrit « **Aucune règle `outline: none`
n'existe dans ce produit, sur aucun élément, sous aucun prétexte de style** ». La maquette
contredit la lettre de la spine, et l'encadré affirme le contraire.

**Vérifié en revanche et exact :** le lieu nantais a bien disparu (aucune occurrence de
« Nantes » dans les sept maquettes), et `border-decorative` n'apparaît plus que dans les
commentaires qui annoncent sa suppression.

**À faire :** passer l'encadré à « les sept maquettes », référencer les trois nouvelles, et
supprimer la règle `textarea:focus{outline:none}` ou amender EXPERIENCE.md:361.

---

## 3. Conséquences testables orphelines

Les 14 exigences vivantes ont toutes un foyer, mais sept conséquences testables du PRD n'en
ont aucun.

| # | Conséquence testable | Source PRD | Gravité |
|---|---|---|---|
| **O-1** | « Tout changement de statut […] **met à jour l'événement d'agenda** (FR-12) » | prd.md:590-591 | **ÉLEVÉ** — l'état `Rencontre confirmée` (EXPERIENCE.md:254) décrit la pastille, la date et l'annonce, jamais l'agenda. Or l'agenda est le livrable du parcours 1 : sa ligne « en attente » y reste éternellement |
| **O-2** | « Le partenaire est prévenu […] **par e-mail s'il est utilisateur inscrit** » | prd.md:601-602 | **ÉLEVÉ** — voir C-2 |
| **O-3** | « Une rencontre passe à *confirmée* ou *déclinée* quand le partenaire […] **s'il est utilisateur inscrit, répond depuis sa conversation** » | prd.md:587-588 | **MOYEN** — aucun beat. Le PRD est lui-même en tension ici (§9 met le parcours conversationnel côté partenaire hors périmètre, prd.md:827-829) : à faire trancher en amont |
| **O-4** | « Le **numéro de téléphone est facultatif** et n'est jamais exigé pour terminer un parcours » | prd.md:368 ; §3 prd.md:184-187 | **MOYEN** — les spines interdisent d'**afficher** un numéro (EXPERIENCE.md:329) mais n'offrent jamais de l'**donner**. Sans lui, un utilisateur inscrit est injoignable par SMS, ce qui referme la boucle de C-2 |
| **O-5** | « **L'événement porte** le sport, le prénom du partenaire, le lieu, le jour, l'heure **et le statut** » | prd.md:563-564 | **MOYEN** — seule la clause négative (« aucun numéro ») est reprise, EXPERIENCE.md:329 |
| **O-6** | « sans données de terrains **l'utilisateur indique le lieu lui-même** » | prd.md:673-674 | **MOYEN** — voir C-6 |
| **O-7** | « La notification part par e-mail […] **dans l'heure qui suit** l'inscription du profil correspondant » | prd.md:471-472 | **FAIBLE** — délai serveur, sans surface ; le texte n° 1 (EXPERIENCE.md:164-171) est correct par ailleurs |

---

## 4. Vérification des chiffres

### 4.1 Liste de contrôle

| Chiffre | Occurrences dans les spines | Source PRD | Verdict |
|---|---|---|---|
| **6,1 %** | EXPERIENCE.md:8, 97, 245, 461, 463 | prd.md:162, 1008 | ✅ **Exact** — 14 / 231 = 6,06 % |
| **3,0 %** | EXPERIENCE.md:245, 463 | prd.md:385, 1008 | ✅ **Exact** |
| **3,1 points** | EXPERIENCE.md:245, 463 | prd.md:383 | ⚠️ **Valeur exacte, attribution fautive** — voir N-1 |
| **55 %** | EXPERIENCE.md:97 | prd.md:160, 401 | ✅ **Exact** — 127 / 231 = 54,98 % |
| **127 sur 231** | EXPERIENCE.md:97, 243 | prd.md:377-378, 872 | ✅ **Exact** |
| **113 rattrapées** | EXPERIENCE.md:97, 243 | prd.md:378 | ✅ **Exact** |
| **89 %** | EXPERIENCE.md:97 | prd.md:378, 874 | ✅ **Exact** — 113 / 127 = 88,98 % |
| **14 sur 231** | EXPERIENCE.md:97 (implicite), 245, 461 | prd.md:162, 876 | ✅ **Exact** |
| **86 profils** | EXPERIENCE.md:319 | prd.md:172, 221 ; `SportsProfiles.csv` (87 lignes − en-tête) | ✅ **Exact** |
| **33 paires** | **absent des deux spines** | prd.md:394 | ➖ **Non repris** — sans conséquence, mais le plafond de trois candidats perd sa justification chiffrée |
| **231 combinaisons** | EXPERIENCE.md:97, 243, 245, 461 | prd.md:159-160, 400 | ✅ **Exact** — 11 sports × 7 jours × 3 niveaux ; les 11 sports sont vérifiés au CSV |
| **60 jours** | EXPERIENCE.md:59, 141, 184, 188, 246, 247, 471 | prd.md:473-475 | ✅ **Exact**, y compris l'expiration notifiée |
| **4 tours (SM-C2)** | EXPERIENCE.md:233 | prd.md:890-896, 1017 | ✅ **Exact** |
| **0,5–1,0 point** | DESIGN.md:438 ; EXPERIENCE.md:425 | `research-niveau.md:34` (§1) | ⚠️ **Valeur exacte, source mal désignée** — voir §5 |

**Bilan : 13 chiffres présents sur 14, 13 exacts en valeur, 1 mal attribué, 1 non repris.**

### 4.2 Chiffres hors liste — deux erreurs

#### 🔴 N-1 — ÉLEVÉ — Les 3,1 points sont attribués au mauvais parcours

**PRD**, prd.md:383-386 :

> Ces **3,1 points** […] correspondent **tous** à *Pilates **Intermédiaire***, c'est-à-dire au
> droit de proposer la seule pratiquante de Pilates du fichier — débutante — à quelqu'un qui
> ne l'est pas.

**Spine**, EXPERIENCE.md:463, encadré du parcours 2 :

> Le PRD assume ces 3,1 points […] **C'est le prix de la promesse, et il se paie exactement
> ici.**

Or **Nadia est *Avancée*** (EXPERIENCE.md:461, prd.md:148). Son cas n'est **pas** dans les
3,1 points : sous FR-7, l'élargissement au niveau voisin d'une demande *Avancé* atteignait
*Intermédiaire*, où le Pilates est vide aussi — Nadia était déjà refusée dans les 3,0 % de la
v2. Les 7 combinaisons ajoutées (7 → 14) sont **toutes** *Pilates Intermédiaire*, un profil
de demandeur que le parcours 2 ne met pas en scène.

Ce qui est vrai : le parcours 2 **décrit** désormais deux fois plus de cas (14 au lieu de 7),
et la spine l'écrit correctement dans la phrase précédente. Ce qui est faux : « le prix se
paie exactement ici ». Il se paie dans un parcours voisin que **aucune spine ne met en scène** —
un demandeur *Pilates Intermédiaire*, qui est précisément le cas nouveau de la v2.

**À faire :** corriger l'encadré, et envisager de nommer le cas *Pilates Intermédiaire* dans
l'état `Vivier vide`, puisque c'est lui le nouveau.

#### ⚠️ N-2 — FAIBLE — 34 °C contre les 31 °C de UJ-1

EXPERIENCE.md:86 (colonne « À faire », donc microcopie exemplaire) et
`mockups/key-recap-en-attente.html:131` écrivent **34 °C** là où UJ-1 écrit **31 °C ressentis**
(prd.md:123). Les deux dépassent le seuil de 28 °C de FR-10, donc le comportement est correct
et les spines couvrent le point (« les chiffres de ce parcours sont illustratifs »,
EXPERIENCE.md:448). Mais le parcours canonique du PRD a une valeur, et il n'y a aucune raison
d'en inventer une autre : un scénario de test écrit depuis la spine ne correspondra pas à UJ-1.

#### ⚠️ N-3 — FAIBLE — « mercredi 3 septembre » n'est pas un mercredi

Le 3 septembre **2026 est un jeudi** ; le mercredi est le 2. La date apparaît quatre fois dans
des textes contractuels — EXPERIENCE.md:136, 175, 181, 339 — et dans trois maquettes. C'est le
créneau de la rencontre d'Anna, celui qui est écrit dans l'agenda, dans le SMS et dans la
région de statut. Un jeu d'essai construit sur ces textes se contredit dès la première
assertion de jour.

---

## 5. Noms propres et données d'amorçage

Référence : `SportsProfiles.csv`.

| Personne | Donnée d'amorçage | Emploi dans les spines | Verdict |
|---|---|---|---|
| **Thomas** | **Absent du CSV** (voulu, prd.md:103, 904-906) | EXPERIENCE.md:437-457, 479-488 ; `[ASSUMPTION]` reprise | ✅ Correct, et l'hypothèse du PRD est reprise |
| **Nadia** | **Absente du CSV** (voulu) | EXPERIENCE.md:459-477 ; encadré 465 | ✅ Correct, collision avec Sarah bien traitée |
| **Sarah Andre** | l. 13 — **Pilates, Mardi;Jeudi, Débutant** | EXPERIENCE.md:463, 465 ; `mockups/key-vivier-vide.html:180` | ✅ Correct : sport, niveau, unicité |
| **Emma Leroy** | l. 3 — **Tennis, Mardi;Jeudi, Débutant** | **Absente des deux spines** | ⚠️ **MOYEN** — voir ci-dessous |
| **Anna** (Perrot) | l. 23 — Tennis, **Mercredi;Samedi**, Intermédiaire | EXPERIENCE.md:354 « mercredi, samedi » ✅ ; EXPERIENCE.md:445 « mercredi » ✅ ; `mockups/key-proposition-partenaires.html:155` « **Mercredi, vendredi** » 🔴 | 🔴 **Faux dans la maquette** |
| **Iris** (Payet) | l. 53 — Tennis, **Lundi;Mercredi**, Intermédiaire | EXPERIENCE.md:445 « **samedi** » 🔴 ; `mockups:159` « **Samedi · dans 4 jours** » 🔴 | 🔴 **Faux dans les deux** |
| **Tessa** (Armand) | l. 83 — Tennis, **Lundi;Samedi**, Intermédiaire | EXPERIENCE.md:445 « lundi » ⚠️ ; `mockups:163` « **Lundi · dans 6 jours** » 🔴 | ⚠️ **Incomplet / délai faux** |

### 🔴 N-4 — ÉLEVÉ — Le trio de UJ-1 porte des jours fabriqués, et le calcul de FR-6 en découle faux

**Ce que dit le PRD** (prd.md:118-120) : « Anna, Iris et Tessa jouent exactement à votre niveau
— **mercredi, samedi ou lundi** ». C'est l'**union non ordonnée** des jours des trois profils :
{Mercredi, Samedi} ∪ {Lundi, Mercredi} ∪ {Lundi, Samedi} = {Mercredi, Samedi, Lundi}. Le PRD
est exact.

**Ce qu'en fait la spine** (EXPERIENCE.md:445) : elle transforme le « ou » en **appariement
positionnel** et en fait la justification de l'ordre —

> Anna, Iris, Tessa — **mercredi, samedi, lundi**, dans cet ordre parce que c'est celui du
> **délai d'attente croissant** depuis mardi.

**Le vrai calcul, depuis mardi** (mercredi = 1 … lundi = 6) :

| Candidate | Jours réels | Délais | Délai retenu |
|---|---|---|---|
| Anna Perrot | Mercredi, Samedi | 1, 4 | **1** |
| Iris Payet | Lundi, Mercredi | 6, 1 | **1** |
| Tessa Armand | Lundi, Samedi | 6, 4 | **4** |

L'ordre **Anna, Iris, Tessa est juste** — mais pour une autre raison que celle écrite : Anna et
Iris sont **ex æquo à 1 jour**, et c'est **l'ordre du vivier** (l. 23 avant l. 53) qui les
départage, pas un délai croissant 1 / 4 / 6. La spine documente donc la règle de FR-6 sur un
exemple qui ne l'exerce pas, et masque le seul cas où le départage secondaire mord.

**La maquette est pire** : elle affiche `Anna — Mercredi, vendredi`. **Aucun profil du fichier
d'amorçage n'a de vendredi pour Anna** ; c'est une donnée inventée, affichée sur une carte,
dans le produit dont la contrainte la plus structurante est que le bot n'invente rien. Elle
affiche aussi `Iris — Samedi` (faux : lundi, mercredi) et `Tessa — Lundi · dans 6 jours`
(délai faux : son samedi donne 4).

**Conséquence :** tout scénario de test écrit depuis le parcours 1 ou depuis la maquette
échouera sur les jours, et la seule démonstration de FR-6 du corpus produit un ordre correct
par accident.

**À faire :** `Anna — mercredi, samedi · dans 1 jour` / `Iris — lundi, mercredi · dans 1 jour`
/ `Tessa — lundi, samedi · dans 4 jours`, et reformuler la justification d'ordre pour nommer
le départage par l'ordre du vivier.

### ⚠️ N-5 — MOYEN — Emma Leroy, le seul cas de correspondance exacte du corpus, n'est nulle part

Le PRD donne un unique scénario nominal de FR-5 (prd.md:412) : « **"Tennis, mardi, débutant"
renvoie Emma Leroy** », et l'addendum le désigne comme piège de démonstration
(`addendum.md:213-216`). Les spines n'en font rien : l'état `Correspondance exacte`
(EXPERIENCE.md:242) tient en deux lignes, sans nom, sans maquette, sans parcours. Les quatre
parcours mettent en scène l'élargissement (1), le vide (2), la reprise (3) et le partenaire (4)
— **le chemin le plus simple du produit n'est jamais montré**.

Ce n'est pas une contradiction, c'est un angle mort : c'est aussi le seul chemin où
`candidate-group-label` porterait « Une débutante, comme vous » au singulier, forme qu'aucun
libellé n'a prévue.

---

## 6. Géographie — conforme

Vérification exhaustive sur les deux spines et les sept maquettes.

| Lieu cité | Où | Verdict |
|---|---|---|
| Lyon / son agglomération | DESIGN.md:397, 454 ; EXPERIENCE.md:68, 124, 210, 223, 240, 288, 447 | ✅ |
| Parc de la Tête d'Or | EXPERIENCE.md:136, 175 ; `key-recap-en-attente.html`, `key-page-acceptation.html` | ✅ Lyon 6ᵉ |
| Gerland | `key-recap-en-attente.html:134` | ✅ Lyon 7ᵉ |
| **Bordeaux** | EXPERIENCE.md:124 | ✅ **Légitime** — c'est le contre-exemple de l'état `Hors zone` : « Je ne couvre que Lyon et son agglomération. Je ne peux pas chercher à Bordeaux. » |
| Nantes | **aucune occurrence** | ✅ Le défaut v2 est bien corrigé |

Le traitement est même plus fort que le PRD ne l'exige : EXPERIENCE.md:210 pose
« **Aucune ville n'est demandée** », et EXPERIENCE.md:240 fait de `Hors zone` le **seul** état
qui court-circuite la recherche — conforme à prd.md:296-297 et à la décision fermée
prd.md:935-936.

---

## 7. Fidélité des citations de recherche

### 7.1 `research-niveau.md`

| Citation de la spine | Source réelle | Verdict |
|---|---|---|
| EXPERIENCE.md:425 — « amorcer par un questionnaire **comportemental**, pas une auto-étiquette ; demander des faits vérifiables ; **ne jamais proposer débutant / intermédiaire / avancé comme saisie** » | `research-niveau.md:65` (§4, point 1) : « Amorcer par un questionnaire comportemental, pas une auto-étiquette. Demander des faits vérifiables […] Ne jamais proposer "débutant/intermédiaire/avancé" comme saisie. » | ✅ **Fidèle, mot pour mot** |
| EXPERIENCE.md:425 — « **Elle** [§4.1] **mesure** ce que coûte l'infraction : des niveaux gonflés de 0,5 à 1,0 point, qui mettent très longtemps à se corriger » | La mesure est en **§1** (`research-niveau.md:34-35`), pas en §4.1. « se **stabiliser** » dans la source, « se **corriger** » dans la spine | ⚠️ **FAIBLE** — valeur exacte, **section mal désignée**, verbe altéré. Le PRD, lui, cite correctement §1 (prd.md:717-719) |
| EXPERIENCE.md:427 — « La recherche demandait un questionnaire **dont la personne ne voit pas le barème** » | §4.1 prescrit des faits vérifiables « mappés vers `mu` ». L'opacité du barème est une **inférence raisonnable**, jamais écrite | ⚠️ **FAIBLE** — présenté comme une demande de la recherche, c'est une lecture. Défendable, mais « la recherche demandait » est trop fort |
| DESIGN.md:438 / EXPERIENCE.md:204 — l'empilement vertical, parce que « le centre est exactement là où tombe **la sur-évaluation** » | Deux constats distincts sont fusionnés : la sur-évaluation de 0,5–1,0 (`:34`) **et** la compression de ~80 % des joueurs dans « intermédiaire » (`:38`). C'est le second qui justifie l'argument du centre | ⚠️ **FAIBLE** — raccourci de raisonnement. L'argument tient, la référence est imprécise |
| EXPERIENCE.md:431 — « l'incertitude affichée (UTR "Projected", astérisque DUPR) » | `research-niveau.md:47` (§2 d) | ✅ **Fidèle** |
| EXPERIENCE.md:423 — « une note visible crée des incitations à la manipulation incontrôlables à cette échelle » | `research-niveau.md:71` (§4.7) via prd.md:792-794 | ✅ **Fidèle** |
| EXPERIENCE.md:427 — « plus aucun instrument ne la mesure, SM-C1 ayant été retirée avec FR-7 » | prd.md:727-729, 885-889 | ✅ **Fidèle** |

### 7.2 Le §4.1 contredit sciemment — la spine le reflète-t-elle honnêtement ?

**Oui, et c'est le meilleur passage de la v3.** EXPERIENCE.md:425-429 fait quatre choses que
la consigne demande et qu'une spine dérivée aurait pu esquiver :

1. Elle **nomme la contradiction** : « c'est le seul endroit où ce produit contredit sciemment
   ses propres sources ».
2. Elle **cite l'interdit littéralement**, y compris les trois mots que le produit propose.
3. Elle **refuse le maquillage** : « Cette spine applique la décision du PRD ; elle ne la
   maquille pas en conformité » — et elle sépare explicitement ce que l'anatomie du bloc
   récupère (les faits en *description*) de ce qu'elle ne récupère pas (« Ce n'est **pas** la
   parade prescrite. […] La sur-évaluation est réduite, pas empêchée »).
4. Elle **historise son propre revirement** (EXPERIENCE.md:429) : v1 → v2 → v3, en disant que
   la v3 renverse la v2 « non parce que la v2 avait tort sur la recherche, mais parce que le
   PRD a changé d'avis en sachant ce qu'il faisait ».

Le contre-pied est cohérent avec prd.md:708-715 et prd.md:985-990. **Aucune trace de
conformité prétendue, aucun euphémisme.** Le seul défaut est la référence de section
(§4.1 vs §1) relevée ci-dessus, qui ne change rien au fond.

### 7.3 `research-paysage.md`

| Citation de la spine | Source réelle | Verdict |
|---|---|---|
| DESIGN.md:286 / EXPERIENCE.md:421 — « aucun moyen de parler à un vrai humain, toujours renvoyé vers un chatbot » | `research-paysage.md:63` (§3), avis Trustpilot Playtomic | ✅ **Fidèle** |
| EXPERIENCE.md:419 — « aucun produit grand public de mise en relation entre joueurs n'utilise le chat comme interface principale » | `research-paysage.md:59` (§3) | ✅ **Fidèle** |
| EXPERIENCE.md:420 / DESIGN.md:286 — le catalogue (Playtomic, Anybuddy, MATCHi) | `research-paysage.md:12-22`, §1 | ✅ **Fidèle** |
| EXPERIENCE.md:424 — « le paywall avant la messagerie (Sportpartner, **2,7 ★**) » | `research-paysage.md:34, 69` | ✅ **Fidèle**, note exacte |
| EXPERIENCE.md:423 — « la plainte n° 1 des plateformes à l'échelle porte justement sur l'intégrité de la note » | `research-paysage.md:71` (§4) | ✅ **Fidèle** |
| EXPERIENCE.md:258 — le garde-fou §7 « mesuré par SM-5 » | prd.md:742-750, 878-881 | ✅ **Fidèle** |

**Non repris, et c'est un manque discret :** `research-paysage.md:73` désigne **le no-show**
comme mode d'échec terminal du parcours nominal, et prd.md:836-839 le met explicitement hors
périmètre en le nommant. Les spines n'en disent rien — ni dans les anti-patterns, ni dans les
décisions ouvertes. Le PRD assume ; la spine ne relaie pas. **FAIBLE**, mais c'est le seul
constat de la recherche que le corpus aval perd en route.

---

## 8. Synthèse par gravité

### CRITIQUE (1)

- **C-1** — Le conflit de créneaux : EXPERIENCE.md:284 et `key-page-acceptation.html:233-243`
  laissent le partenaire accepter deux rencontres qui se chevauchent, là où FR-14
  (prd.md:622-624) exige que l'acceptation **échoue** et que la rencontre passe en *déclinée*.
  Aucun encadré. Décision produit prise en silence dans un document subordonné.

### ÉLEVÉ (5)

- **C-2 / O-2** — Le partenaire est traité partout comme un profil d'amorçage joint par SMS ;
  le canal e-mail de FR-14 (prd.md:601-602) n'existe dans aucune spine, et le texte sortant
  n° 2 devient faux pour un partenaire inscrit.
- **C-3** — La règle d'ordre de FR-6 est glosée à l'envers (EXPERIENCE.md:244), contre
  prd.md:431-434 et contre la maquette qui, elle, l'énonce juste.
- **C-4** — Le niveau subsiste sur la carte de partenaire dans le plancher d'accessibilité
  (EXPERIENCE.md:354), résidu v2 dans la règle qui décrit ce qu'entend un lecteur d'écran.
- **N-1** — Les 3,1 points sont attribués au parcours de Nadia (*Avancée*) alors qu'ils sont
  **tous** en *Pilates Intermédiaire* (prd.md:383-386) : chiffre exact, parcours faux.
- **N-4** — Les jours d'Anna, Iris et Tessa sont fabriqués dans EXPERIENCE.md:445 et
  `key-proposition-partenaires.html:152-164` — dont un « vendredi » qui n'existe dans aucun
  profil du CSV, affiché sur une carte du produit qui n'invente rien.
- **O-1** — La mise à jour de l'événement d'agenda au changement de statut (prd.md:590-591)
  n'a aucun foyer : le livrable du parcours 1 reste « en attente » pour toujours.

### MOYEN (8)

- **C-5** — `candidate-group-label` « Trois intermédiaires, comme vous » réinstalle, sans
  encadré, la lecture de garantie que §7 (prd.md:721-723) cherchait à empêcher.
- **C-6 / O-6** — Sans données de terrains, le PRD fait saisir le lieu par l'utilisateur
  (prd.md:673-674) ; les spines continuent sans lieu, ce qui referme aussi FR-10.
- **C-7** — « Voici les cinq personnes » (EXPERIENCE.md:126) contre le plafond de trois de FR-6.
- **C-8** — La règle « jamais le prénom du partenaire » (EXPERIENCE.md:160) est enfreinte par
  le texte sortant n° 3 (« Objet : Anna a répondu », EXPERIENCE.md:179) — règle plus stricte
  que le PRD, puis violée.
- **D-9** — « Les quatre maquettes » est faux (sept existent, trois jamais référencées, dont
  celle qui matérialise C-1) ; `outline: none` subsiste malgré l'encadré qui l'affirme corrigé.
- **N-5** — Emma Leroy et le seul scénario de correspondance exacte du PRD (prd.md:412) ne sont
  mis en scène nulle part.
- **O-3** — La réponse d'un partenaire inscrit « depuis sa conversation » (prd.md:587-588) n'a
  pas de beat — tension à trancher en amont, le §9 du PRD la met par ailleurs hors périmètre.
- **O-4 / O-5** — Le numéro facultatif d'un utilisateur inscrit (prd.md:368) et le contenu de
  l'événement d'agenda (prd.md:563-564) n'ont pas de foyer.

### FAIBLE (6)

- **C-9** — « aucun terrain de tennis **ouvert** » suppose une connaissance des disponibilités
  que FR-11 exclut.
- **C-10** — « sans coûter un tour » / « un seul tour » dans la même cellule (EXPERIENCE.md:233).
- **N-2** — 34 °C contre les 31 °C de UJ-1.
- **N-3** — « mercredi 3 septembre » : le 3 septembre 2026 est un jeudi (4 occurrences +
  3 maquettes).
- **§7.1** — La mesure 0,5–1,0 point est attribuée à `research-niveau` §4.1 alors qu'elle est
  en §1 ; « se corriger » pour « se stabiliser » ; « la recherche demandait un questionnaire
  dont la personne ne voit pas le barème » est une inférence présentée comme une citation.
- **§7.3** — Le no-show, mode d'échec terminal documenté (`research-paysage.md:73`, repris par
  prd.md:836-839), n'est relayé nulle part dans les spines.

---

## 9. Ce qui est bien fait, et qu'il faut préserver

Une revue de dérive qui ne dit que ce qui casse donne une image fausse de l'écart réel.

- **Le §13 du PRD a servi.** Les cinq changements de fond de la v2 sont chacun traçables dans
  les spines, avec leur raison. Les deux changelogs (DESIGN.md:8, EXPERIENCE.md:8) ne se
  contentent pas d'annoncer la resynchronisation : ils énumèrent les composants créés et ceux
  qui perdent une propriété.
- **Les chiffres périmés sont réellement purgés.** Aucune occurrence de **5,2 %** ne subsiste
  dans le corps des deux spines — seulement dans les entrées de changelog v2, où c'est de
  l'historique et non une affirmation. C'était la dérive n° 1 de la passe précédente.
- **La correction de la phrase « personne ne fait de Pilates »** (EXPERIENCE.md:119, 245, 470 ;
  `key-vivier-vide.html:180`) est exemplaire : la spine identifie que la formulation devenait
  factuellement fausse sous l'égalité stricte, le dit, barre l'ancienne, et explique pourquoi
  la v1 s'en tirait.
- **`La grammaire de l'honnêteté`, point 4** (EXPERIENCE.md:313) est un ajout que le PRD ne
  demandait pas et qui sert FR-16 mieux que FR-16 ne se sert lui-même : « le produit écrit les
  conséquences qu'il s'inflige, au moment où il se les inflige ».
- **Le contre-pied de `research-niveau` §4.1** est traité comme la consigne l'exige : nommé,
  cité, non maquillé, et historisé sur trois versions.
- **La géographie est propre** sur les neuf documents, maquettes comprises.

---

## 10. Actions, par ordre

| # | Action | Où | Gravité |
|---|---|---|---|
| 1 | Trancher le conflit de créneaux : aligner la spine sur FR-14, **ou** amender FR-14 et journaliser au §13 | EXPERIENCE.md:284 ; `key-page-acceptation.html:220-245` | CRITIQUE |
| 2 | Écrire le canal e-mail du partenaire inscrit (5ᵉ texte sortant) et corriger les six passages « SMS » | EXPERIENCE.md:36, 60, 173, 175, 213, 319, 492 | ÉLEVÉ |
| 3 | Corriger les jours d'Anna, Iris et Tessa depuis le CSV, et reformuler la justification d'ordre | EXPERIENCE.md:445 ; `key-proposition-partenaires.html:152-164, 195-210, 230-237` | ÉLEVÉ |
| 4 | Retourner la glose de la règle d'ordre de FR-6 | EXPERIENCE.md:244 | ÉLEVÉ |
| 5 | Retirer « Intermédiaire » de l'exemple de nom accessible | EXPERIENCE.md:354 | ÉLEVÉ |
| 6 | Corriger l'attribution des 3,1 points (*Pilates Intermédiaire*, pas le parcours de Nadia) | EXPERIENCE.md:463 | ÉLEVÉ |
| 7 | Donner un foyer à la mise à jour de l'événement d'agenda au changement de statut | EXPERIENCE.md:254, 201 | ÉLEVÉ |
| 8 | Encadrer ou reformuler `candidate-group-label` au regard de §7 | DESIGN.md:440 ; EXPERIENCE.md:206 | MOYEN |
| 9 | Ajouter le beat « dites-moi le lieu » (NFR robustesse) | EXPERIENCE.md:127, 250 | MOYEN |
| 10 | Passer l'encadré à « sept maquettes », référencer les trois nouvelles, régler `outline: none` | DESIGN.md:397, 454 ; EXPERIENCE.md:68, 223, 288 | MOYEN |
| 11 | Rattacher « voici les cinq » à la branche « montrer les autres » de FR-6 | EXPERIENCE.md:126, 258 | MOYEN |
| 12 | Restreindre la règle « jamais le prénom du partenaire » à « jamais les coordonnées » | EXPERIENCE.md:59, 160, 179 | MOYEN |
| 13 | Mettre en scène Emma Leroy dans `Correspondance exacte` | EXPERIENCE.md:242 | MOYEN |
| 14 | Corriger 34 °C → 31 °C, « mercredi 3 septembre » → « mercredi 2 septembre », « terrain ouvert » → « terrain » | EXPERIENCE.md:86, 127, 136, 175, 181, 339 + maquettes | FAIBLE |
| 15 | Rectifier la référence `research-niveau` §4.1 → §1 pour la mesure 0,5–1,0 | DESIGN.md:438 ; EXPERIENCE.md:425 | FAIBLE |
