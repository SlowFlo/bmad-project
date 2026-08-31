# Epic 2 Context: Recherche

<!-- Compilé depuis les artefacts de planification. Éditez librement. Régénérez avec compile-epic-context si les documents de planification changent. -->

## Goal

Cette épique livre le moteur d'appariement complet — sans une ligne de LLM ni d'appel web — et rien
d'autre : elle écrit `domaine/recherche` seul, par-dessus le socle du vivier déjà livré. À son terme,
le produit sait rendre des candidats exactement du niveau demandé, élargir sur le jour quand la
recherche exacte est vide, ordonner et plafonner ce qu'il rend, et prouver par un test que le seul
critère chiffrable du produit (SM-3) est tenu. C'est le premier moment où l'égalité stricte de niveau
— la promesse émotionnelle qui fonde le produit, éviter le match déséquilibré dans les deux sens —
cesse d'être une intention et devient une propriété vérifiée du code.

## Stories

- Story 2.1 : Chercher des candidats du niveau exact
- Story 2.2 : Élargir sur le jour, et sur lui seul
- Story 2.3 : Ordonner et plafonner les candidats
- Story 2.4 : Mesurer SM-3 sur les 231 combinaisons
- Story 2.5 : Aucun élargissement de niveau, à aucune étape

## Requirements & Constraints

- **Égalité stricte de niveau, sans exception et à aucune étape.** Aucun candidat rendu n'est d'un
  autre niveau que celui demandé — ni après élargissement, ni sur proposition, ni si l'utilisateur le
  réclame. Le coût est chiffré et refusé sciemment : élargir au niveau voisin ferait tomber le résidu
  vide de 6,1 % à 3,0 %. L'interdit doit être structurel — aucune fonction à appeler, aucun paramètre
  de tolérance ou d'adjacence à passer — et non une convention de relecture.
- **Le jour est le seul axe d'élargissement du produit.** Il n'est relâché que si la recherche exacte
  n'a rien rendu ; sport et niveau restent identiques. Le résultat de l'élargissement porte, comme
  donnée, le fait que le jour demandé n'était pas disponible.
- **Exclusions permanentes du résultat :** un profil de *niveau inconnu* (une absence, jamais une
  quatrième valeur), un profil sorti du vivier, le demandeur lui-même, et un profil dont le jour
  considéré est bloqué par une rencontre — bloqué pour ce jour seul, il reste rendu sur ses autres
  jours.
- **Déterminisme et plafond :** au plus trois candidats, triés par délai d'attente croissant, l'ordre
  du vivier (identifiant croissant) départageant les ex æquo — cas le plus fréquent sur les données
  d'amorçage, dont la médiane est de trois profils par paire sport × niveau. Deux exécutions
  identiques rendent le même trio dans le même ordre. Le résultat porte aussi le nombre de candidats
  restants au-delà de trois.
- **Le délai d'attente se compte vers l'avant** depuis le jour demandé jusqu'à la prochaine
  disponibilité du candidat, en tournant sur la semaine. Ce n'est pas une ancienneté : rien dans le
  modèle ne dit depuis quand quelqu'un attend.
- **Chiffres contractuels de la grille d'amorçage** (11 sports × 7 jours × 3 niveaux = 231) : 127
  combinaisons sans candidat exact, dont l'élargissement doit récupérer au moins 85 % sans dépasser le
  plafond atteignable de 89 % — le dépasser signalerait une fuite de niveau. Le résidu réellement vide
  compte 14 combinaisons, toutes du Pilates, sur les deux seules paires sport × niveau vides. Repères
  de mise au point : « Tennis, mardi, débutant » rend Emma Leroy ; la même demande en intermédiaire
  rend vide en exact, puis Anna, Iris et Tessa après élargissement.
- **Ces règles d'ordre et de plafond ne sont mesurées par aucun critère de réussite** : une recherche
  qui rendrait tous les candidats, non triés, passerait SM-3. Elles se vérifient donc par leurs
  propres tests, et l'interdit d'élargissement de niveau par un test négatif dédié.
- Un sport que le vivier ne connaît pas donne un résultat vide, jamais un refus — la conséquence
  conversationnelle appartient à une autre épique.

## Technical Decisions

- **Le domaine seul.** Ce lot ne touche que `domaine/recherche`. Aucun LLM n'intervient : le modèle
  n'est qu'un adaptateur primaire et ne produit ni nom, ni sélection, ni ordre. La prose qui présente
  les candidats appartient à l'épique du fil ; ce lot rend des données structurées.
- **L'appariement porte sur la clé de sport normalisée, jamais sur le libellé affiché.** Trois graphies
  d'un même sport rendent le même ensemble. La table de synonymes redirige à l'écriture uniquement :
  la recherche ne la consulte jamais.
- **La disponibilité est dérivée, jamais stockée** — pas de champ « bloqué ». Mais la dérivation du
  jour bloqué (jointure sur les rencontres *en attente* ou *confirmée*) appartient à une épique
  ultérieure : la recherche est donc écrite pour **accepter en paramètre un ensemble de jours
  indisponibles**, afin d'être branchée plus tard sans être réécrite.
- Le vocabulaire du glossaire est employé littéralement jusque dans les noms de types, de champs et de
  fonctions — *candidat*, *élargissement*, *jour disponible*, *vivier*, *niveau*. Jamais `match`,
  `slot` ou un synonyme.
- Un report d'implémentation ouvert par l'épique précédente doit être clos ici : l'absence d'index sur
  la clé étrangère de sport, « chercher les profils d'un sport » étant l'accès central du lot. Poser
  l'index ou justifier son absence par une mesure sur les 86 profils, et mettre à jour le registre des
  reports dans les deux cas.
- Enveloppe inchangée : un seul processus local, base SQLite fichier, aucune infrastructure.

## UX & Interaction Patterns

Ce lot ne rend aucune interface, mais son résultat doit porter tout ce dont le fil aura besoin, sinon
la couche de présentation devra inventer ou recalculer : le niveau commun du groupe (dit une fois pour
la salve, jamais répété par candidat), les jours disponibles et le délai d'attente de chaque candidat,
l'indication que le jour demandé n'était pas disponible, et le nombre de candidats supplémentaires —
le produit propose de les montrer par salves successives, jamais par un carrousel. Un candidat sans
aucun jour disponible n'est jamais proposé. Le niveau n'est jamais redemandé pendant la recherche :
aucune signature de ce lot ne doit ouvrir cette possibilité.

## Cross-Story Dependencies

- L'épique du socle du vivier est livrée et fournit le schéma, les deux populations, la clé de sport
  normalisée et les 86 profils d'amorçage ; tout ce lot s'appuie dessus.
- 2.1 fonde la recherche exacte ; 2.2 ne s'exécute que sur son résultat vide ; 2.3 s'applique aux
  candidats produits par l'une ou l'autre ; 2.4 parcourt la grille complète et suppose 2.1 à 2.3 en
  place ; 2.5 réutilise ce parcours pour vérifier la distribution des niveaux rendus.
- L'épique du cycle de vie des rencontres branchera la dérivation du jour bloqué sur le paramètre de
  jours indisponibles prévu ici ; le blocage y sera symétrique entre les deux profils.
- L'épique du fil consommera ces résultats pour la prose, les cartes et les étapes ; l'épique des
  alertes différées réutilise la notion de correspondance **exacte** — un profil qui ne correspondrait
  qu'après élargissement ne déclenche aucune alerte.
- Ce lot est le jalon qui rend SM-3 mesurable ; l'ordre imposé est socle → recherche → fil avant tout
  le reste.
