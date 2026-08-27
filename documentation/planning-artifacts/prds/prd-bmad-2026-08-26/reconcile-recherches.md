---
title: "Réconciliation — recherches ↔ PRD"
date: 2026-08-26
status: revue
scope: research-paysage.md + research-niveau.md ↔ prd.md + addendum.md
---

# Réconciliation — recherches ↔ PRD

## Verdict

**research-paysage.md — récolte partielle et sélective.** Le PRD n'a retenu qu'un des deux
diagnostics de la recherche : le vide. La seconde cause de mort documentée — l'intégrité de
la note de niveau et le match déséquilibré qui s'ensuit — n'apparaît nulle part, alors que le
niveau est la promesse centrale d'Ex Aequo (« le jour se négocie, le niveau se défend »).
Plus grave : la recherche énumère en §2 les quatre stratégies d'amorçage qui marchent, le PRD
cite ce §2 comme caution de sa propre réponse, et cette réponse n'est aucune des quatre. La
contrainte la plus actionnable de la recherche — *la liquidité est par lieu* — n'a produit
aucune exigence : FR-5 et FR-6 apparient sport + jour + niveau, sans jamais regarder où
habitent les gens.

**research-niveau.md — l'arbitrage est légitime, sa justification ne l'est pas.** Écarter le
mécanisme `mu`/`sigma` en v1 est défendable et correctement tracé (PRD §9, addendum). Mais la
recherche ne se contente pas de proposer un algorithme : elle **condamne nommément** le choix
que le PRD a fait. §4.1 dit « Ne jamais proposer "débutant/intermédiaire/avancé" comme
saisie » ; §1 dit que ces libellés compriment ~80 % des joueurs dans « intermédiaire ». Le PRD
adopte ces trois valeurs en glossaire contraignant et renvoie à §1 « pour les limites » sans
dire que §1 vise ce choix précis. Et les propositions applicables **sans aucun algorithme** —
le questionnaire de faits vérifiables, les ancres humaines, le signal d'équilibre post-match,
l'affichage d'une fourchette — ont été jetées avec l'algorithme.

---

## Fidélité des citations

| Citation du PRD | Ce que dit la source | Verdict |
|---|---|---|
| **§1, l.44** — « la recherche n'a trouvé **aucun** produit grand public de mise en relation entre joueurs utilisant une interface conversationnelle » (paysage §3) | §3 : « Aucun produit grand public de mise en relation entre joueurs n'utilise une interface chat/LLM comme UI principale. » | **Fidèle, mais tronquée.** Le PRD coupe avant les deux phrases suivantes du même §3 : les seuls agents chat existants sont **B2B**, et côté grand public les chatbots apparaissent en **support**, où « les utilisateurs les détestent » (verbatim Trustpilot Playtomic). Le PRD lit ce §3 comme un espace vide ; la source y voit aussi un terrain où le chat a déjà déçu. |
| **§1, l.50** — « La recherche a identifié le vide comme la cause de mort n°1 de ce type de produit » (sans lien) | §4 : « **Deux niveaux.** Pour les petits matchers, c'est le vide […] Pour les apps de réservation à l'échelle, c'est l'intégrité de la note de niveau et le match déséquilibré qui s'ensuit. » | **Fidèle sous condition, mais le « deux niveaux » disparaît.** « Cause de mort n°1 » vaut pour les matchers sous-critiques, ce qu'Ex Aequo est — la lecture est donc défendable. Ce qui ne l'est pas, c'est que la deuxième cause soit escamotée par la formulation « n°1 » : elle laisse croire à un classement là où la source décrit deux régimes successifs. Ex Aequo doit traverser le premier pour rencontrer le second. |
| **§4, l.182** — les 86 profils « peuplent le vivier pour qu'il ne soit pas vide au démarrage, ce que la recherche a identifié comme la cause de mort n°1 » (paysage §2) | §2 énumère **quatre** stratégies d'amorçage réellement observées : (a) s'amorcer sur l'offre de réservation, (b) fabriquer l'offre soi-même, (c) hériter d'un graphe institutionnel, (d) chevaucher un sport chaud en géographie dense. Puis : « Les matchers purs ne font aucune de ces quatre choses **et meurent**. » | **Infidèle par extension.** Le diagnostic est exact ; le remède est prêté à la source. Amorcer avec 86 profils **fictifs, qui ne jouent jamais**, n'est aucune des quatre stratégies — c'est du décor, pas de la densité. Le PRD invoque §2 comme s'il validait sa réponse alors que §2 range précisément Ex Aequo dans la catégorie qui meurt. La thèse réelle du PRD (l'inscription sans friction fait grossir le vivier) est peut-être bonne, mais elle est du PRD, pas de la recherche, et doit être présentée comme telle. |
| **§8, l.558** — « Pas de classement public. La recherche montre qu'un classement visible crée des incitations à la manipulation impossibles à contrôler à cette échelle » (niveau §4.7) | §4.7 : « **Afficher une fourchette, jamais une fausse précision.** "≈3,0, en cours de calibrage" jusqu'à ~8–10 matchs. Ne jamais exposer de classement public **tôt** : les classements créent des incitations au sandbagging impossibles à policer à cette échelle. » | **Fidèle sur la moitié citée.** Deux écarts mineurs, un manque majeur. Écarts : la source dit « tôt » (temporel), le PRD en fait un non-objectif permanent — durcissement défendable ; et la source dit *sandbagging*, le PRD dit « manipulation » — généralisation acceptable. Manque : la **première** phrase de §4.7, la fourchette contre la fausse précision, n'est récoltée nulle part alors qu'elle s'applique directement (voir plus bas). |
| **§9, l.589** — « Le niveau évolutif […] le mécanisme de correction par les résultats est documenté dans §4 **pour plus tard** » | §4 s'intitule « Le minimum viable pour un petit projet (**le point important**) » et conclut : « **Livrer 1+2+3+4**, ajouter 5 quand les matchs commencent à affluer. » | **Fidèle en pointeur, minorante en statut.** §4 n'est pas un raffinement optionnel : la recherche le présente comme le plancher, et démontre au passage pourquoi Elo ne convient pas ici (graphe de matchs creux et déconnecté). Le ranger en « pour plus tard » est un arbitrage légitime, mais le PRD ne signale pas qu'il écarte ce que la source appelait le minimum. |
| **§11.3, l.634** — « Le niveau reste déclaratif, **avec les limites documentées dans §1**. Acceptable en v1 ; à rouvrir si les matchs déséquilibrés deviennent la plainte principale. » | §1 « Ce qui casse avec un niveau purement auto-déclaré » : biais à la hausse de **0,5 à 1,0 point** ; sandbagging (« une culture où il est acceptable de sandbagger », l'USTA a dû créer une procédure de contestation) ; fragmentation des barèmes ; et **« Les libellés grossiers débutant/intermédiaire/avancé compriment ~80 % des joueurs dans "intermédiaire" — exactement la bande qu'il faut découper. »** §4.1 renchérit : « **Ne jamais proposer "débutant/intermédiaire/avancé" comme saisie.** » | **Infidèle par omission — le constat le plus grave du document.** Le renvoi est formellement exact et fonctionne comme un paravent : il traite §1 comme un catalogue de limites génériques de l'auto-déclaration, alors que §1 et §4.1 visent **nommément les trois libellés que le PRD a retenus**. Un lecteur du PRD seul ne peut pas savoir que la recherche a explicitement interdit sa solution. La formule « à rouvrir si les matchs déséquilibrés deviennent la plainte principale » aggrave le cas : la recherche dit que ce sera le cas, pas que ça pourrait l'être. |
| *(complément)* **addendum, « Notation du niveau »** — « Le détail algorithmique […] est documenté dans research-niveau.md, section 4. Ce mécanisme n'est pas retenu en v1. » | Conforme. | **Fidèle.** C'est la meilleure trace d'arbitrage des deux documents : la décision est nommée, datée, et la matière écartée est conservée. Le reproche ne porte pas sur l'arbitrage mais sur son périmètre — il jette aussi les éléments non algorithmiques (§4.1 questionnaire, §4.4 ancres, §4.5 signal post-match, §4.7 fourchette). |

**Bilan : 6 citations de contenu vérifiées** (5 dans le PRD + 1 dans l'addendum), **2 infidèles**
(§4 / paysage §2, par extension ; §11.3 / niveau §1, par omission), **2 fidèles mais affaiblies**
(§9, §8), **2 fidèles** (§1 l.44, tronquée mais exacte ; addendum).

---

## Non récolté — research-paysage.md

### 1. La deuxième cause de mort : l'intégrité du niveau *(perte majeure — absence non défendable)*

**Ce que dit la recherche (§4).** Le churn a deux régimes. Passé le vide, ce qui tue est
« l'intégrité de la note de niveau et le match déséquilibré qui s'ensuit » : les notes suivent
la fréquence plutôt que le niveau, pénalisent pour les erreurs du partenaire, sont opaques, et
sont manipulées. Verbatim : « j'ai vu des joueurs affronter intentionnellement des adversaires
moins bien notés juste pour gonfler leur note. »

**Où ça manque.** Partout. §7 « Contraintes et garde-fous » ne connaît qu'un risque, l'invention
par le LLM. Il n'y a **aucun risque assumé sur le niveau** dans le PRD. Or la promesse produit
est le niveau — §5.2 « le niveau se défend », SM-C1 plafonne les mises en relation par descente
à 20 %, §2.1 érige « l'humiliation douce du match trop déséquilibré » en besoin émotionnel
central.

**Défendable ?** Non. C'est le seul endroit où le PRD nie un constat de sa propre recherche
tout en construisant sa promesse dessus. Il ne s'agit pas de changer la décision (le niveau
déclaratif à trois valeurs peut rester) mais d'écrire en §7 que la catégorie meurt de ça en
second temps, et que le produit accepte ce risque sans instrument.

### 2. La liquidité est *par lieu* — et le matching d'Ex Aequo est géographiquement aveugle *(perte majeure — absence non défendable)*

**Ce que dit la recherche (§2a, §2d).** Chez Playtomic, Anybuddy, MATCHi, « la liquidité est
*par lieu* plutôt qu'à l'échelle de la ville » — les matchs s'accrochent à des créneaux déjà
réservés dans un club donné. La stratégie (d) est de « chevaucher un sport chaud dans une
géographie dense », où « un seul club peut porter la liquidité ».

**Où ça manque.** FR-5 et FR-6 apparient sur sport + jour + niveau. **La ville n'est jamais un
critère de recherche** : elle n'est demandée qu'en FR-11, *après* que le partenaire a été
retenu, et uniquement pour proposer un terrain. Les profils d'amorçage n'ont pas de ville du
tout (§4, addendum « Persistance »). Le bot peut donc proposer Anna en tenant scrupuleusement
son niveau, puis découvrir qu'elle est à 600 km — et la seule chose que le produit sait faire
alors est de proposer un terrain dans la ville de Thomas.

**Défendable ?** Non, et c'est la perte la moins chère à réparer. Elle n'exigeait pas de
changer les données (elles n'ont pas de ville) mais d'écrire l'aveu : le PRD n'a pas de
critère géographique, donc SM-3 (85 % de récupération) mesure une performance sur un vivier
sans espace. Le chiffre est vrai et sans rapport avec l'utilité des candidats renvoyés.

### 3. L'ordre de grandeur des matchers purs qui meurent *(perte notable — absence non défendable)*

**Ce que dit la recherche.** Smatch : ~6 000 utilisateurs actifs **au total**, sa meilleure
ville à 2 200. Sportpartner : 2,7★ sur 53 notes. **Bvddy, le « Tinder du sport », 1,5 M$ levés,
est mort.** Et les verbatims du vide : « je n'ai pas trouvé un seul partenaire de sport »,
« peut-être 10 dans une ville », « ces forums étaient vides ».

**Où ça manque.** Le PRD parle du vide comme d'un concept (§1, §4) et n'écrit jamais un seul
de ces chiffres. Résultat : rien ne calibre le lecteur sur ce que « ne pas être vide » exige.
2 200 personnes réelles dans la meilleure ville de Smatch ne suffisent pas ; Ex Aequo démarre
avec 86 personnes fictives réparties sur 11 sports et 7 jours — **soit une moyenne de 7,8
profils par sport**, ce qui explique mécaniquement les 55 % de combinaisons vides que le PRD
constate sans en nommer la cause.

**Défendable ?** Non. Un projet d'apprentissage n'a pas besoin d'atteindre la masse critique,
mais son PRD gagne à dire qu'il ne l'atteindra pas — sans quoi SM-3 et SM-4 se lisent comme
des mesures de succès produit alors qu'elles mesurent la tenue d'un scénario.

### 4. Les no-shows *(perte réelle — absence non défendable comme silence)*

**Ce que dit la recherche (§4, second ordre).** Le no-show est une plainte documentée ;
Playtomic le sanctionne durement — absence sans préavis de 24 h → débité, compte bloqué
jusqu'au paiement.

**Où ça manque.** Le produit s'arrête à l'écriture dans l'agenda. Le PRD couvre l'acceptation
(FR-13, FR-14) et rien après : ni annulation, ni relance, ni no-show. §9 renvoie la négociation
entre inscrits en v2, mais le no-show n'est pas de la négociation — c'est le mode d'échec
terminal du parcours nominal.

**Défendable ?** L'absence de *fonctionnalité* est défendable en MVP. L'absence de *mention*
ne l'est pas : sans terrain réservé et sans argent en jeu, Ex Aequo est **plus** exposé au
no-show que Playtomic, pas moins. Rien ne coûte à la personne qui ne vient pas.

### 5. Le sens de l'histoire est à sens unique *(perte modérée — absence partiellement défendable)*

**Ce que dit la recherche (§1).** « Le terrain est l'actif rare monétisable. » Les produits de
réservation ajoutent du matching (Playtomic Open Matches, MATCHi Communities, Anybuddy Matchs
publics) ; **« aucun produit de matching n'a réussi à ajouter la réservation. »**

**Où ça manque.** §8 pose « Ce n'est pas une plateforme de réservation » comme un choix de
périmètre neutre, et §5.4 met la réservation hors périmètre. Nulle part le PRD ne dit que la
recherche établit que ce chemin ne se remonte pas — donc que le non-objectif d'aujourd'hui est
probablement définitif.

**Défendable ?** Oui pour un projet personnel sans ambition commerciale. Mais la conséquence
produit, elle, n'est pas économique : sans le terrain, il n'y a **aucune raison de revenir**
entre deux envies de jouer. Le PRD n'a pas de mécanique de rétention et ne le sait pas.

### 6. GoodRec — le contre-exemple qui inverse le problème *(perte modérée — absence défendable)*

**Ce que dit la recherche.** GoodRec achète des créneaux sous-utilisés dans 250+ installations
et opère **1 000+ parties par semaine dans 70+ villes**. « Ce n'est pas du matching, c'est de
l'inventaire » : on convertit le problème d'appariement en offre planifiée, et on **garantit
que la partie a lieu**.

**Où ça manque.** Le PRD n'envisage jamais l'inversion — proposer des créneaux existants
plutôt que d'apparier deux personnes. C'est pourtant le seul modèle du paysage qui résout le
vide sans densité.

**Défendable ?** Oui : Ex Aequo n'a ni terrain ni capital, et l'inversion tuerait la thèse
conversationnelle. Mais c'est le contre-exemple le plus fort à la forme même du produit, et il
méritait une ligne en §8 pour montrer qu'il a été vu et écarté.

### 7. Le paywall avant d'écrire *(anodin — décision déjà prise, crédit non pris)*

**Ce que dit la recherche (§4).** Le vide chez Sportpartner est « aggravé par un paywall avant
de pouvoir écrire » — 2,7★.

**Où ça manque.** FR-1 (dialoguer sans authentification) et FR-4 (compte demandé au dernier
moment) font exactement l'inverse, et c'est une bonne décision. Elle n'est simplement jamais
reliée au constat qui la justifie.

**Défendable ?** Oui, c'est une perte de traçabilité, pas de contenu.

### 8. Ten'Up meurt de l'exécution, pas de la densité *(anodin — couvert de fait)*

**Ce que dit la recherche.** Ten'Up est subventionné par la FFT, hérite d'un graphe
institutionnel — et ses plaintes sont « purement de l'exécution : bugs, déconnexions,
**recherche de joueur cassée** ».

**Où ça manque.** Le PRD a des NFR de latence et de robustesse externe qui couvrent le sujet
en pratique. Le point non récolté est moral : même en résolvant la densité, on peut mourir de
l'exécution du seul écran qui compte.

**Défendable ?** Oui.

---

## Non récolté — research-niveau.md

### 1. Les trois libellés retenus sont ceux que la recherche interdit *(perte majeure — absence non défendable)*

**Ce que dit la recherche.** §1 : « Les libellés grossiers débutant/intermédiaire/avancé
compriment **~80 % des joueurs dans "intermédiaire"** — exactement la bande qu'il faut
découper. » §4.1 : « **Ne jamais proposer "débutant/intermédiaire/avancé" comme saisie.** »

**Où ça manque.** §3 du PRD fait de ces trois valeurs un glossaire **contraignant** (« les
exigences fonctionnelles l'emploient littéralement, sans synonyme ») ; FR-2 les extrait du
langage naturel ; FR-7 construit dessus la notion de niveau adjacent. Le PRD ne mentionne
jamais l'interdiction, ni la compression à 80 %.

**Conséquence chiffrable, non vue par le PRD.** Les 86 profils d'amorçage sont répartis
**30 Intermédiaire / 28 Débutant / 28 Avancé** — une distribution quasi uniforme, donc
irréaliste au regard de ce que la recherche documente. Toute l'arithmétique du §5.2 en dépend :
les 231 combinaisons, les 55 % de vide, les 113 recherches récupérées sur 127 (89 %), et donc
le seuil SM-3 à 85 %. Sur une population réelle où ~80 % se déclarent Intermédiaire, ces
chiffres se disloquent — l'élargissement sur le jour deviendrait trivial pour les
intermédiaires et quasi impossible pour les débutants et les avancés. **Le PRD calibre sa
métrique de succès principale sur une distribution que sa propre recherche déclare fausse.**
Le `[NOTE FOR PM]` du §5.2 avertit bien que les 231 combinaisons ne sont pas pondérées par la
demande réelle, mais il ne voit que la pondération par sport, jamais celle par niveau.

**Défendable ?** L'usage de trois valeurs en v1 est défendable — c'est ce qu'on peut extraire
d'une phrase. Le **silence** ne l'est pas.

### 2. Le signal d'équilibre post-match *(perte majeure — absence non défendable)*

**Ce que dit la recherche (§4.5).** « Un tap de chaque joueur : **trop facile / équilibré /
trop dur**. Avec peu d'utilisateurs, ce signal humain vaut souvent plus que le score, et il
optimise directement le vrai objectif (**des matchs sympas**), pas la probabilité de victoire. »

**Où ça manque.** Le PRD n'a **aucune boucle de retour après la rencontre**. Le parcours
s'achève à l'agenda et au SMS. §10 mesure la tenue du scénario (SM-1), la non-invention (SM-2),
la couverture de l'élargissement (SM-3), le refus honnête (SM-4), le pari conversationnel
(SM-5), et plafonne la descente de niveau (SM-C1) — **rien ne mesure si le match était bon**.

**Défendable ?** Non, et c'est la perte la plus paradoxale du document. Trois boutons, aucun
algorithme, aucune infrastructure de notation : c'est le seul instrument qui aurait dit si la
promesse centrale du produit est tenue, et c'est l'élément de §4 le plus facile à livrer sans
livrer §4. Il a été jeté avec `mu`/`sigma` parce que l'addendum a traité §4 en bloc
« algorithmique ». SM-C1 mesure aujourd'hui un proxy (la part de mises en relation par descente
de niveau) là où le signal direct était disponible.

### 3. Le biais de l'auto-déclaration a un sens et une amplitude connus *(perte majeure au PRD — partiellement récoltée en UX)*

**Ce que dit la recherche (§1).** L'auto-évaluation Playtomic est « notoirement gonflée — la
plupart des nouveaux joueurs atterrissent **0,5 à 1,0 au-dessus** de leur niveau réel ».
ProperPadel : « le plus gros problème pour tout le monde… des notes inexactes dès le départ
qui mettent **très longtemps** à se stabiliser ». Et l'échec inverse, le sandbagging : d'anciens
joueurs D1 s'auto-notant 4.5, au point que l'USTA a dû créer une procédure formelle de
contestation.

**Où ça manque.** §11.3 dit « le niveau reste déclaratif, avec les limites documentées dans
§1 » — sans énoncer ni le sens, ni l'amplitude, ni le fait que le biais est **bidirectionnel**.
Or ces deux biais n'ont pas le même effet ici : le gonflement produit un match trop dur pour le
gonfleur, le sandbagging produit un match trop facile pour le sandbagger et humiliant pour
l'autre. §2.1 du PRD nomme précisément ces deux souffrances (« se faire écraser, ou passer une
heure à faire du renvoi de balle par politesse ») **sans jamais les relier à leur cause
documentée**.

**Nuance à porter au crédit du projet.** `EXPERIENCE.md` (UX, l.262) a récolté ce que le PRD a
laissé : « Rejeté — le questionnaire d'auto-évaluation à l'inscription (Playtomic). La recherche
montre qu'il produit des niveaux gonflés de 0,5 à 1,0 point… ». La matière n'est donc pas perdue
pour le projet — elle est **mal placée** : une décision produit motivée par la recherche est
prise en aval, dans un document de conception, et le PRD qui devait la porter l'ignore.

**Défendable ?** Non au niveau du PRD. Il fallait deux lignes en §7 : le niveau déclaré est
biaisé vers le haut, parfois délibérément vers le bas, et le produit n'a aucun moyen de le
corriger en v1.

### 4. « Intermédiaire » n'est défini nulle part — la fragmentation des barèmes *(perte majeure — absence non défendable)*

**Ce que dit la recherche (§1).** Verbatim : « **je suis dans un barème différent pour chaque
groupe WhatsApp de club.** » Et §4.1 donne la parade sans algorithme : « Amorcer par un
questionnaire **comportemental**, pas une auto-étiquette. Demander des **faits vérifiables** —
années de pratique, compétition en club, classement fédéral actuel ou passé, capacité à
servir/retourner/jouer après le mur. »

**Où ça manque.** Le glossaire §3 définit Niveau par « Débutant, Intermédiaire ou Avancé.
Déclaré par la personne, propre à un sport. » — une définition circulaire. **Nulle part le PRD
ne dit ce que ces mots veulent dire, ni au bot, ni à l'utilisateur, ni par sport.** Deux
personnes qui écrivent « je suis intermédiaire » ne désignent pas la même chose, et le produit
les apparie en garantissant qu'il a tenu le niveau.

**Défendable ?** Non, et c'est la perte la meilleur marché du document. Récolter *la forme de
la question* de §4.1 — un ancrage de deux lignes par sport, ou une relance du bot sur un fait
vérifiable quand la personne s'auto-étiquette — ne demandait **aucun** des mécanismes écartés.
La décision de rester déclaratif à trois valeurs aurait survécu intacte, avec trois valeurs
qui veulent dire quelque chose.

### 5. « Afficher une fourchette, jamais une fausse précision » *(perte notable — absence non défendable)*

**Ce que dit la recherche (§4.7, première moitié).** « Afficher une fourchette, jamais une
fausse précision. "≈3,0, en cours de calibrage" jusqu'à ~8–10 matchs. »

**Où ça manque.** Le PRD n'a récolté de §4.7 que la seconde moitié (pas de classement public,
§8). Or un niveau auto-déclaré, présenté sans marque d'incertitude, **est** la fausse précision
visée. `EXPERIENCE.md` (l.263) garde la porte ouverte (« En réserve pour plus tard —
l'incertitude affichée […] `{components.unknown-value}` fournit déjà la grammaire »), mais le
PRD ne demande rien : il n'existe aucune exigence sur la **façon dont le niveau d'un candidat
est énoncé**. « Anna, niveau intermédiaire » se lit comme un fait établi ; « Anna se déclare
intermédiaire » aurait coûté un mot et dit la vérité.

**Défendable ?** Non. C'est une exigence de langage, pas d'algorithme, et le PRD est par
ailleurs très exigeant sur le langage du bot (§7 « Le bot n'invente rien »). Le niveau est le
seul endroit où le produit affirme plus qu'il ne sait.

### 6. Faire décroître la confiance, pas le niveau — la péremption des profils *(perte notable — absence non défendable)*

**Ce que dit la recherche (§3, §4.8).** « Décroissance par récence : UTR ne garde que 12 mois ;
Glicko gonfle le RD pendant les pauses. On fait décroître la **confiance**, pas la note. »
Et : « Après ~3 mois d'inactivité, `sigma` remonte. »

**Où ça manque.** Le PRD n'a **aucune notion de fraîcheur de profil**. Les 86 profils d'amorçage
sont disponibles « le mardi » pour l'éternité, sans que personne ait jamais confirmé quoi que
ce soit. Un profil qui ne répond jamais aux SMS reste candidat indéfiniment et continue de
consommer les trois places de FR-6.

**Asymétrie révélatrice :** le PRD sait faire expirer une **alerte** (FR-9, 60 jours, avec
notification d'expiration) mais pas une **disponibilité**. La demande périme, l'offre non.

**Défendable ?** Non. La version sans algorithme est triviale — au bout de N mois sans signe de
vie, le profil est déclassé dans le tri ou son niveau est présenté comme ancien. Le PRD n'a même
pas la question ouverte.

### 7. Les ancres humaines *(perte modérée — absence partiellement défendable)*

**Ce que dit la recherche (§4.4).** « Planter des ancres. Une personne de confiance (un coach,
ou **toi**) note à la main 5 à 10 joueurs, avec `sigma` verrouillé bas. Les ancres donnent une
échelle au graphe creux […] C'est l'astuce du leveling club de Playtomic, **en gratuit**. »
§2(b) confirme le pattern : événement de calibrage humain, fiabilité fixée à 50 %.

**Où ça manque.** Les niveaux des 86 profils d'amorçage sont posés sans aucune justification —
ni dans le CSV, ni dans le PRD, ni dans l'addendum. La recherche indiquait au constructeur, en
s'adressant à lui directement, comment leur donner une échelle.

**Défendable ?** Partiellement : sur un vivier fictif, ancrer des profils fictifs ne produit pas
d'information. Mais le jour où de vrais utilisateurs s'inscrivent à côté des 86, ils sont
comparés à une échelle arbitraire. C'est un risque à nommer, pas une fonctionnalité à livrer.

### 8. L'import d'un classement fédéral existant *(perte modeste — absence défendable)*

**Ce que dit la recherche (§2c, §3).** L'assimilation FFT tennis→padel, l'ingestion de scores
auto-déclarés par UTR/DUPR — avec la mise en garde : « une graine **à sens unique**, pas une
équivalence ».

**Où ça manque.** FR-2 n'extrait que trois valeurs. Une personne qui écrit « je suis classé
30/2 » — information autrement plus dure que « intermédiaire », et courante dans le public
français visé — voit cette information écrasée vers « Intermédiaire ».

**Défendable ?** Oui en v1 : sans mécanisme de niveau continu, il n'y a nulle part où ranger un
classement FFT. Mais le PRD pouvait au moins ne pas le jeter — le conserver en texte libre au
profil coûte un champ.

### 9. Apparier sur des intervalles qui se recouvrent, et élargir automatiquement *(perte modérée — absence largement défendable)*

**Ce que dit la recherche (§4.6).** « Proposer les paires dont les intervalles `[mu ± k·sigma]`
se recouvrent, et **élargir `k` automatiquement quand le vivier est maigre** — avec 30
utilisateurs, une bande stricte à ±0,25 ne renvoie rien. »

**Où ça manque.** Le PRD a bien un élargissement, mais en escalier fixe et discret (jour, puis
niveau adjacent, puis rien). Il n'est pas fonction de la maigreur du vivier.

**Défendable ?** Oui, largement : avec trois valeurs discrètes il n'y a pas d'intervalle à
recouvrir, et l'escalier jour→niveau est un choix produit assumé et chiffré (89 % vs 36 %). Le
principe sous-jacent — l'élargissement doit être proportionnel à la maigreur — est toutefois
déjà à l'œuvre sans être nommé : le PRD élargit *parce que* le vivier est maigre.

### 10. Pourquoi Elo ne marche pas ici *(perte modérée — absence défendable)*

**Ce que dit la recherche (§4).** « Avec quelques dizaines d'utilisateurs, Elo **ne peut pas
converger** : l'information par match est faible et — le vrai tueur — **le graphe des matchs
est creux et déconnecté**, donc les notes ne sont comparables qu'à l'intérieur d'une composante
connexe. »

**Où ça manque.** C'est le raisonnement qui **justifie** la décision du PRD de ne pas faire de
niveau évolutif. Ni le PRD ni l'addendum ne le reprennent : l'addendum dit seulement « ce
mécanisme n'est pas retenu en v1 ».

**Défendable ?** Oui — le lien vers §4 suffit. Mais une phrase aurait transformé un renoncement
en décision motivée : ce n'est pas « trop compliqué pour la v1 », c'est « mathématiquement
inopérant à cette échelle ».

### 11. Notes par sport *(récolté, sans citation)*

§3 de la recherche : « Notes par sport — **non négociable**. » Le PRD le fait (glossaire §3 :
« propre à un sport » ; FR-3 : une demande sur un nouveau sport l'ajoute avec son niveau).
Récolté correctement, sans référence. Rien à signaler.

### 12. Anti-triche, gestion du double, matchs compétitifs uniquement *(non récolté, absence défendable)*

§3 de la recherche : seuls les matchs compétitifs comptent, score confirmé par les deux parties,
surveillance des appariements répétés qui « farment » un adversaire faible ; et la critique la
plus citée de Playtomic — une bonne performance individuelle dans un match perdu coûte quand
même des points. Sans résultats enregistrés, sans score et sans double, tout cela est sans
objet en v1. **Absence pleinement défendable.**

---

## Matière qualitative perdue

C'est ici que la structure en exigences fonctionnelles a coûté le plus cher. Chacun des éléments
ci-dessous est une observation sur le **ressenti, le ton ou le vocabulaire des gens** — de la
matière qui ne se met pas en FR, et qui a donc disparu par construction plutôt que par décision.

**1. « trop facile / équilibré / trop dur ».** Ce sont les mots exacts avec lesquels les gens
parlent d'un match — trois adjectifs de ressenti, pas trois niveaux de compétence. La recherche
les propose comme signal (§4.5) ; ils valent aussi comme **vocabulaire**. Le PRD parle
Débutant/Intermédiaire/Avancé, un langage d'inscription à un cours ; les joueurs parlent en
termes de ce que le match leur a fait. Le produit demande à quelqu'un de se classer alors que ce
qu'il sait vraiment dire, c'est comment c'était la dernière fois.

**2. « des matchs sympas », pas « la probabilité de victoire » (§4.5).** C'est la formulation la
plus juste du but d'Ex Aequo qui existe dans l'un des deux corpus, et elle n'est nulle part dans
le PRD. §10 mesure la tenue du parcours, la non-invention, la couverture de l'élargissement, le
nombre de tours — **aucun critère de réussite ne parle de la qualité de la rencontre.** Le PRD a
optimisé le fait qu'un rendez-vous soit pris, ce qui n'est pas le même objet.

**3. « Personne ne fait *confiance* au questionnaire — on lui fait confiance *brièvement et
lâchement*. » (§2, niveau).** La phrase la plus importante de la recherche sur le niveau, et
elle est purement qualitative : elle porte sur **la posture** à adopter face à une déclaration,
pas sur un mécanisme. Le PRD fait exactement l'inverse — il fait confiance à la déclaration
**durablement et fermement** : le niveau est un attribut stable du profil, le glossaire l'énonce
sans réserve, et FR-6 en fait une promesse (« Les candidats proposés sont **exactement** du
niveau demandé »). Aucun FR ne pouvait porter « brièvement et lâchement » ; c'est précisément
pour ça qu'il fallait l'écrire ailleurs — en §7, en garde-fou.

**4. « je suis dans un barème différent pour chaque groupe WhatsApp de club » (§1, niveau).** Le
PRD ouvre sur le groupe WhatsApp (§1) — mais comme lieu où l'on relance sans réponse. La
recherche en fait aussi le lieu où **le niveau se fragmente**. Le même décor, deux problèmes ;
le PRD n'en a vu qu'un, celui qu'il savait résoudre.

**5. Les verbatims du vide : « je n'ai pas trouvé un seul partenaire de sport », « peut-être 10
dans une ville », « ces forums étaient vides » (§2, paysage).** UJ-2 est bâti sur ce moment et
le traite très bien sur le fond (« ce parcours n'est pas un cas limite »), mais avec le
vocabulaire du produit, jamais avec celui de la déception. Ces trois phrases sont la **matière
de microcopie** du seul état que 55 % des demandes vont rencontrer. Elles disent la texture de
la chose : pas une erreur, une lassitude.

**6. « aucun moyen de parler à un vrai humain, toujours renvoyé vers un chatbot » (§3,
paysage).** Le seul verbatim du corpus qui porte sur **l'interface même** qu'Ex Aequo a choisie,
et il est hostile. Le PRD cite ce §3 pour dire que la place est libre, et laisse tomber la
phrase qui dit pourquoi elle pourrait l'être. La perte est double : c'est un risque non assumé,
et c'est une **exigence manquée** — ce que les gens détestent n'est pas le chat, c'est
l'enfermement dans le chat. SM-5 mesure d'ailleurs un symptôme voisin (« l'utilisateur réclame
une liste ») sans nommer la maladie, et §8 pose « Le bot n'est pas un assistant généraliste »,
ce qui **referme** la porte de sortie au lieu d'en ouvrir une.

**7. « j'ai vu des joueurs affronter intentionnellement des adversaires moins bien notés juste
pour gonfler leur note » (§4, paysage).** Un ressenti d'injustice, pas une faille technique. Ce
que ça dit du produit : le jour où le niveau compte, quelqu'un trichera, et **les autres le
verront**. Aucun document du projet ne porte cette matière.

**8. Le régime punitif de Playtomic sur les no-shows (§4, paysage).** « Absence sans préavis de
24 h → débité, compte bloqué jusqu'au paiement. » C'est un exemple de **ton produit** — le
degré de sévérité qu'une plateforme s'autorise envers ses utilisateurs — et il est cité parmi
les motifs de plainte. Ex Aequo, dont tout le ton est l'honnêteté sans reproche (« le bot
informe, il n'interdit pas », FR-10), avait là un repoussoir explicite à nommer.

**9. « l'humiliation douce du match trop déséquilibré » (§2.1 du PRD).** L'exception qui
confirme la règle : c'est la meilleure phrase qualitative des quatre documents, et elle **ne
vient pas des recherches** — elle est du PRD. Elle aurait pourtant pu s'ancrer directement dans
§1 de research-niveau (gonflement → se faire écraser ; sandbagging → le renvoi de balle poli).
Le PRD a produit sa propre matière qualitative pendant que celle des recherches restait sur
l'étagère.

---

## Notes

**Ce que le PRD fait bien, et qu'il faut dire.** L'arbitrage sur le niveau est *tracé* : §9 le
sort du périmètre, §11.3 en fait une question ouverte, l'addendum conserve la matière écartée
en nommant la décision. C'est mieux que la moyenne — le reproche porte sur ce que cet arbitrage
a emporté par ricochet, pas sur son existence. De même, le `[NOTE FOR PM]` du §5.2 (les 231
combinaisons ne sont pas pondérées par la demande réelle) montre un PRD qui sait douter de ses
propres chiffres ; il lui manquait d'appliquer ce doute au niveau autant qu'au sport.

**Le motif de perte est structurel, pas accidentel.** Les pertes se répartissent en trois
familles, et aucune n'est un oubli isolé :

1. **La récolte par bloc.** L'addendum a traité research-niveau §4 comme une unité
   « algorithmique » et l'a écartée en entier. Or §4 contient au moins quatre éléments
   **non algorithmiques** et livrables tels quels : le questionnaire de faits vérifiables (4.1),
   les ancres humaines (4.4), le signal d'équilibre post-match (4.5), la fourchette contre la
   fausse précision (4.7). Écarter `mu`/`sigma` n'obligeait à écarter aucun des quatre.

2. **La citation qui couvre au lieu d'exposer.** Deux des six citations fonctionnent comme des
   paravents : §4 invoque paysage §2 pour légitimer une réponse que §2 ne valide pas ; §11.3
   renvoie à niveau §1 « pour les limites » alors que §1 condamne nommément la solution retenue.
   Dans les deux cas la référence est formellement correcte, et sa fonction rhétorique est
   d'éviter d'écrire le constat gênant dans le corps du texte. **Un lecteur du PRD seul ne peut
   pas reconstituer le désaccord.**

3. **La matière qualitative n'a pas de case.** Le PRD est organisé en FR, NFR, non-objectifs,
   critères de réussite, questions ouvertes — cinq contenants dont aucun n'accueille « voici
   comment les gens parlent de ça » ou « voici ce qui les dégoûte ». §7 (Contraintes et
   garde-fous) était le seul candidat, et il ne contient qu'un risque, celui de l'invention par
   le LLM. Résultat : **9 éléments de matière qualitative** identifiés ci-dessus, dont deux ont
   survécu en se réfugiant dans `EXPERIENCE.md` (le biais de gonflement, l'incertitude
   affichée) — c'est-à-dire dans un document *aval*, où une décision produit motivée par la
   recherche n'a rien à faire toute seule.

**Le trou fonctionnel à traiter en priorité.** Indépendamment de toute question de style :
**le matching d'Ex Aequo ne regarde jamais où sont les gens.** FR-5 et FR-6 apparient sur sport
+ jour + niveau ; la ville n'entre dans la conversation qu'en FR-11, après le choix du
partenaire, et les 86 profils d'amorçage n'en ont aucune. La recherche établit pourtant que la
liquidité de cette catégorie est *par lieu* (paysage §2a). Ce n'est pas une perte de nuance,
c'est une exigence manquante — et elle relativise SM-3, qui mesure une couverture de 85 % sur
un vivier sans espace.

**Deux corrections bon marché à fort rendement**, si une seule passe de reprise est possible :

- Ajouter en **§7** un garde-fou « Le niveau déclaré est faux dans une direction connue » —
  trois lignes citant niveau §1 (gonflement de 0,5 à 1,0 ; sandbagging ; compression à 80 % dans
  Intermédiaire), et assumant que la v1 n'a aucun moyen de corriger. Cela ferme à la fois la
  citation infidèle de §11.3, la deuxième cause de mort de paysage §4, et la matière qualitative
  n°3.
- Ajouter **une exigence de langage** sur l'énoncé du niveau : le bot dit qu'un candidat *se
  déclare* d'un niveau, il n'affirme pas qu'il *l'est*. Un mot par phrase, et le produit cesse
  d'être plus sûr de lui que sa donnée — ce qui est exactement la règle que §7 applique déjà à
  la météo, aux terrains et aux confirmations.

**Ce qui reste hors du champ de cette revue.** Je n'ai pas évalué la justesse des recherches
elles-mêmes, ni vérifié leurs sources externes. Les documents UX (`EXPERIENCE.md`,
`DESIGN.md`) n'ont été consultés que pour établir si une matière absente du PRD avait survécu
ailleurs dans le projet — deux fois, la réponse est oui, et c'est signalé au fil du texte.
