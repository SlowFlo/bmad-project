---
title: "Research digest — représentation et appariement du niveau de joueur"
source: web research subagent
date: 2026-08-26
status: reference input (not PRD content)
---

# Comment les apps et fédérations gèrent le « niveau »

## Base de preuves

**Systèmes fédéraux** — uniquement basés sur les résultats, et lents.

FFT tennis : bilan sur 52 semaines glissantes, points uniquement pour les victoires (0–120 par victoire, pondérés par le classement de l'adversaire au moment du match), les défaites ne coûtent rien directement — modèle d'accumulation pure qui exige du volume de tournois.

FFT padel : même forme (12 mois glissants, 12 meilleurs résultats, P25–P2000) et résout le démarrage à froid par **assimilation** : conversion directe d'un classement tennis (≥15) en rang padel, ou assimilation des joueurs étrangers à un plancher.

**Moteurs de notation modernes** — tous descendants d'Elo, avec trois améliorations communes :

1. **La marge, pas seulement V/D** — UTR utilise le % de jeux gagnés vs attendu ; ITF WTN note chaque *set* séparément.
2. **Confiance explicite** — UTR pondère chaque match par la fiabilité de l'adversaire et dégrade les anciens dans le temps (≤30 matchs sur 12 mois).
3. **Pas d'incrément fixe : il dépend de l'incertitude** — le RD de Glicko et le σ de TrueSkill rendent les mises à jour initiales grandes et les suivantes petites ; Glicko *augmente* le RD pendant l'inactivité.

**Playtomic (échelle 0–7)** — le cas consommateur le plus instructif : questionnaire d'onboarding → niveau de départ ; seuls les matchs *compétitifs* le font bouger ; la mise à jour utilise le résultat, le niveau des adversaires, le niveau du **partenaire**, et ta fiabilité. Faible fiabilité = grandes variations ; forte = petites. Son échappatoire au démarrage à froid est humaine : un club certifié organise une session de calibrage en présentiel, et la fiabilité est fixée à 50 %.

DUPR fait pareil : 1 match → provisoire (astérisque), fiable vers 5–10 matchs, « fiable » = score de fiabilité ≥60 % (nombre de matchs, récence, variété d'adversaires) ; un coach peut attribuer un départ provisoire.

UTR : 1 match → *projeté*, ~5 résultats → fiable ; 0 match → *estimé* par questionnaire.

## 1. Ce qui casse avec un niveau purement auto-déclaré

Biais systématique à la hausse **plus** manipulation délibérée à la baisse.

- Playskan : l'auto-évaluation à l'inscription Playtomic est « notoirement gonflée — la plupart des nouveaux joueurs atterrissent 0,5 à 1,0 au-dessus de leur niveau réel ».
- ProperPadel désigne le questionnaire comme « le plus gros problème pour tout le monde… des notes inexactes dès le départ qui mettent très longtemps à se stabiliser ».
- L'échec inverse, le *sandbagging* : l'auto-notation USTA NTRP a produit « une culture où il est acceptable de sandbagger » — d'anciens joueurs D1 s'auto-notant 4.5, avec des schémas de performance montrant une manipulation délibérée. L'USTA a dû créer une procédure formelle de contestation.
- Fragmentation : « je suis dans un barème différent pour chaque groupe WhatsApp de club ».
- Les libellés grossiers débutant/intermédiaire/avancé compriment ~80 % des joueurs dans « intermédiaire » — exactement la bande qu'il faut découper.

## 2. Le démarrage à froid, tel qu'il est réellement résolu

Quatre patterns réels, à combiner :

- **(a)** Questionnaire structuré → moyenne a priori + incertitude large (Playtomic, UTR).
- **(b)** Événement de calibrage humain (leveling club Playtomic à 50 % de fiabilité ; provisoire attribué par un coach chez DUPR).
- **(c)** Import/assimilation d'une note externe (assimilation FFT tennis→padel ; UTR/DUPR ingèrent des scores auto-déclarés).
- **(d)** Étiqueter le nombre comme provisoire et le laisser bouger vite (UTR « Projected », astérisque DUPR, RD Glicko élevé).

Personne ne fait *confiance* au questionnaire — on lui fait confiance *brièvement et lâchement*.

## 3. Ce qu'il faut au-delà d'un nombre

- **L'incertitude**, et elle doit piloter la taille de la mise à jour, pas seulement décorer l'UI (RD Glicko, σ TrueSkill, fiabilité Playtomic, 1–100 % DUPR).
- **Décroissance par récence** : UTR ne garde que 12 mois ; Glicko gonfle le RD pendant les pauses. On fait décroître la **confiance**, pas la note.
- **Notes par sport** — non négociable. Padel ≠ tennis ≠ pickleball. L'assimilation FFT tennis→padel est une graine à sens unique, pas une équivalence.
- **Gestion du double / du partenaire** : la critique la plus citée de Playtomic est qu'une bonne performance individuelle dans un match perdu coûte quand même des points. Le bruit du partenaire impose plus de matchs ou un modèle d'équipe explicite.
- **Anti-triche** : seuls les matchs compétitifs comptent ; score confirmé par les deux parties ; surveiller les appariements répétés qui « farment » un adversaire faible (exploit documenté chez Playtomic).

## 4. Le minimum viable pour un petit projet (le point important)

Avec quelques dizaines d'utilisateurs, Elo **ne peut pas converger** : l'information par match est faible et — le vrai tueur — le *graphe des matchs est creux et déconnecté*, donc les notes ne sont comparables qu'à l'intérieur d'une composante connexe. Il faut concevoir pour l'information par match, pas pour l'élégance.

**Concrètement : trois champs par utilisateur et par sport — `mu`, `sigma`, `last_played`. C'est tout le système.**

1. **Amorcer par un questionnaire comportemental, pas une auto-étiquette.** Demander des faits vérifiables — années de pratique, compétition en club, classement fédéral actuel ou passé, capacité à servir/retourner/jouer après le mur — et mapper vers `mu`. Ne jamais proposer « débutant/intermédiaire/avancé » comme saisie. `sigma` large au départ (≈±1,0 sur une échelle 0–7).
2. **Mise à jour type Glicko/TrueSkill allégée, pas Elo simple.** Le seul changement qui compte : le pas est proportionnel à `sigma`. Les nouveaux bougent de ~0,3–0,5 par match, les stabilisés de ~0,05. Contracter vers l'a priori du questionnaire au début, pour qu'un résultat aberrant ne propulse personne.
3. **Noter la marge, pas la victoire/défaite.** Évaluer contre les jeux attendus (UTR) ou mettre à jour par set (WTN). C'est un multiplicateur d'information de ~3 à 5× par match — décisif avec 200 matchs au total, pas 200 000.
4. **Planter des ancres.** Une personne de confiance (un coach, ou toi) note à la main 5 à 10 joueurs, avec `sigma` verrouillé bas. Les ancres donnent une échelle au graphe creux et empêchent les grappes isolées de dériver. C'est l'astuce du leveling club de Playtomic, en gratuit.
5. **Ajouter un signal d'équilibre post-match.** Un tap de chaque joueur : « trop facile / équilibré / trop dur ». Avec peu d'utilisateurs, ce signal humain vaut souvent plus que le score, et il optimise directement le vrai objectif (des matchs sympas), pas la probabilité de victoire.
6. **Apparier sur des intervalles qui se recouvrent, pas sur une distance de points.** Proposer les paires dont les intervalles `[mu ± k·sigma]` se recouvrent, et élargir `k` automatiquement quand le vivier est maigre — avec 30 utilisateurs, une bande stricte à ±0,25 ne renvoie rien. Privilégier aussi les paires qui *réduisent* l'incertitude.
7. **Afficher une fourchette, jamais une fausse précision.** « ≈3,0, en cours de calibrage » jusqu'à ~8–10 matchs. Ne jamais exposer de classement public tôt : les classements créent des incitations au sandbagging impossibles à policer à cette échelle.
8. **Faire décroître la confiance, pas le niveau.** Après ~3 mois d'inactivité, `sigma` remonte ; le joueur repasse en mode réajustement rapide plutôt que d'être rétrogradé arbitrairement.

**À écarter explicitement :** la volatilité (3e paramètre de Glicko-2), les sous-scores par geste technique, des notes simple/double séparées, et tout classement public. Livrer 1+2+3+4, ajouter 5 quand les matchs commencent à affluer.

## Sources

- Playtomic — système de niveau : https://playerhelp.playtomic.com/hc/en-gb/articles/43310980754193-How-the-Playtomic-level-system-works
- Playtomic — leveling clubs : https://playerhelp.playtomic.com/hc/en-gb/articles/19832024478097-Playtomic-Leveling-Clubs
- ProperPadel — critique : https://properpadel.uk/2025/09/12/is-playtomics-rating-system-flawed/
- No Strings Padel : https://clubhouse.nostringspadel.com/the-playtomic-app-are-player-ratings-accurate-2/
- Playskan — comparaison de niveaux : https://www.playskan.com/blog/padel-levels-explained-uk
- padel.fyi : https://www.padel.fyi/articles/what-is-my-padel-level/
- UTR — algorithme : https://support.universaltennis.com/en/support/solutions/articles/9000151894-how-is-the-utr-rating-calculated-
- UTR — projected rating : https://support.universaltennis.com/en/support/solutions/articles/9000151963-
- ITF World Tennis Number : https://worldtennisnumber.com/eng/how-wtn-works
- USTA NTRP guidelines : https://www.usta.com/content/dam/usta/pdfs/10013_experience_player_ntrp_guidelines.pdf
- Fiend at Court — sandbagging : https://fiendatcourt.com/sandbagging-sobs/
- DUPR — ratings : https://www.dupr.com/post/understanding-all-pickleball-ratings
- Glicko-2 (Glickman) : https://glicko.net/glicko/glicko2.pdf
- TrueSkill (Microsoft Research) : https://www.microsoft.com/en-us/research/project/trueskill-ranking-system/
- FFT — classement tennis : https://tenup.fft.fr/content/decouvrir-le-classement-tennis-fft
- FFT — barème de points : https://www.tennis-classement.fr/points-et-bareme-classement-fft.html
- FFT — assimilation padel : https://padel-now.co/blog/regles-assimilation-padel-fft-2025-guide-complet
