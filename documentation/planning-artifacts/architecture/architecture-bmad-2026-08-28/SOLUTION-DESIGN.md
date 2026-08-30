---
title: "Ex Aequo — conception de solution"
status: final
created: 2026-08-28
updated: 2026-08-28
spine: ./ARCHITECTURE-SPINE.md
---

# Ex Aequo — conception de solution

Ce document porte le **pourquoi**. La spine porte le **quoi**, et elle fait foi : en cas de
désaccord entre les deux, c'est elle qui a raison et ce document qui a vieilli. Chaque
décision est citée par son identifiant — `AD-n` — pour qu'on retrouve la règle exécutable
derrière le raisonnement.

## 0. Ce que l'architecture n'avait pas à décider

Une part inhabituelle du travail était déjà faite. Le PRD v4 et son addendum ne se
contentent pas d'énoncer des capacités : ils comptent des combinaisons, chiffrent des
seuils, nomment les statuts, et signalent les endroits fragiles du modèle. Plusieurs
sections de l'addendum sont, littéralement, des décisions d'architecture déjà prises.

Ces choses ont été **héritées sans être rediscutées** : la base comme source de vérité après
un amorçage idempotent, la distinction entre les deux populations du vivier, le profil
mono-sport, le niveau déclaratif sans aucun calcul, les cinq statuts et l'asymétrie de leurs
notifications, la nécessité d'une clé de sport normalisée, l'exigence de diffusion temps
réel, et le filtre de destinataire comme règle de production. Dix-neuf contraintes de ce
type sont consignées au memlog avant la première décision propre à cette passe.

Ce qui restait ouvert tenait en peu de choses, et l'addendum les désigne lui-même : le
découpage agentique, le contrat de rendu d'un tour, la portée de la normalisation, la forme
de la dérivation du jour bloqué. Plus une dimension qu'aucun document amont n'abordait :
l'enveloppe technique elle-même.

## 1. La décision-mère : où passe la frontière entre le LLM et le code

L'addendum pose la question du découpage agentique — « un agent par capacité, ou un agent
unique avec des outils, ou un mélange » — et la laisse délibérément ouverte. Elle a été
reposée un cran plus bas, parce qu'à cette hauteur elle n'a pas de bonne réponse.

Voici pourquoi. Reprenons ce que le produit demande réellement :

| Règle | Nature réelle |
| --- | --- |
| FR-5 — même sport, niveau exact, un jour commun | une jointure |
| FR-6 — trois candidats, tri par délai d'attente croissant | un `ORDER BY` |
| FR-16 — jour bloqué | une jointure |
| FR-13 — une seule recherche active | une précondition transactionnelle |
| FR-10 — 28 °C, 40 km/h, ATMO ≥ 4 | trois comparaisons |
| FR-14 — filtre de destinataire | une condition |
| Les cinq statuts | une machine à états |

**Aucune n'est un jugement.** Toutes sont déterministes, toutes sont testables, et le PRD
les chiffre au point de compter 231 combinaisons et d'en annoncer 127 vides. Ce que le LLM
apporte que le code n'apporte pas se réduit à trois choses : extraire une demande d'une
phrase libre (FR-2), choisir l'outil à appeler, et écrire dans la voix arrêtée par
`EXPERIENCE.md`.

Cela compte parce que la contrainte la plus structurante du produit — *« le bot n'invente
rien »*, PRD §7 — **n'est pas une consigne de prompt**. C'est une propriété qu'on obtient en
retirant au modèle le droit de produire les faits. Si l'égalité stricte de niveau vit dans
un prompt, elle est probabiliste, et SM-2 devient invérifiable *par construction* : on ne
peut pas prouver l'absence d'invention chez un générateur, on peut seulement l'échantillonner.
Si elle vit dans un `WHERE`, elle est vraie, et un test le montre.

C'est **AD-1**, et tout le reste en découle.

Une fois cette frontière posée, la question du nombre d'agents se dégonfle : il ne reste
qu'une seule chose à propos de laquelle être agentique. Le découpage multi-agents a donc été
écarté, et pas seulement pour la latence — même si elle suffisait, l'addendum notant qu'un
saut inter-agents se paie devant un curseur qui clignote et la NFR fixant le signe de vie à
deux secondes. Il a été écarté parce que quatre des cinq agents envisagés n'auraient eu
**aucune décision de jugement à prendre**. C'est **AD-2** : un seul saut LLM par tour.

Le paradigme retenu porte ce raisonnement dans son nom. **Hexagonal**, ports et adaptateurs
— et l'invariant qui compte est que **le LLM est un adaptateur primaire, au même titre que
le navigateur**. Il traduit et il rédige. Il n'est pas le centre.

## 2. Le rendu d'un tour : l'attente est un fait, pas une phrase

`EXPERIENCE.md` marque cette décision `[DÉCISION OUVERTE — architecture]` et la renvoie
ici. Trois documents la cernent : l'addendum interdit une orchestration qui prépare une
réponse complète avant de la rendre ; la NFR impose un signe de vie en moins de deux
secondes ; et depuis la v3.2 de la spine UX, le fil visible n'est plus une région live, ce
qui a retiré le dilemme d'accessibilité qui bloquait la question.

Il ne restait donc pas un choix de transport mais un choix de **source**. PRD §7 ne demande
pas d'afficher une attente. Il demande que *les étapes annoncées correspondent aux sources
réellement interrogées*.

Si le modèle écrit « Je regarde la météo », c'est une affirmation — et elle peut être fausse,
l'appel ayant échoué ou n'ayant jamais eu lieu. Si la couche d'appel d'outil émet
l'événement au moment où elle appelle Open-Meteo, c'est une observation. C'est **AD-3** : les
étapes viennent des ports, jamais du modèle.

Cette décision paie deux fois. D'abord elle rend PRD §7 structurellement vrai : une étape ne
peut apparaître que si l'appel a eu lieu, et un échec remonte nommément sans repli
silencieux. Ensuite elle règle la NFR sans effort : **le signe de vie part au premier appel
d'outil, bien avant le premier jeton du modèle** — donc la borne des deux secondes ne dépend
plus de la latence de génération, qui est la variable qu'on ne maîtrise pas.

Le transport qui en découle est **AD-4** : un flux SSE unique par tour, portant quatre types
d'événements — `etape`, `jeton`, `bloc`, `fin`. Le gate a dû préciser qui compose un `bloc` :
l'adaptateur web à partir d'un résultat de domaine, jamais le modèle. Sans cette phrase, deux
constructeurs conformes à tous les autres AD produisaient des fils incompatibles.

## 3. Le modèle : trois choses dérivées, aucune stockée

L'addendum laisse ouverte la forme de la dérivation du jour bloqué — « à la volée ou colonne
dénormalisée ». À 86 profils, un utilisateur et SQLite, la colonne est une optimisation
prématurée qui ajoute un risque d'incohérence pour un gain nul. C'est **AD-6** : ni champ
« bloqué », ni champ « recherche en cours ».

Mais la vraie difficulté n'est pas là. Elle est dans **AD-7**, et l'addendum la nomme :
les deux règles lisent le même état — les statuts *en attente* et *confirmée* — **mais pas
selon le même axe**. Le blocage par jour de FR-16 est symétrique : il s'applique aux deux
profils sans les distinguer. La précondition d'une seule recherche active de FR-13 ne lit que
le côté demandeur. Les confondre inverse le produit : ce serait laisser un inconnu geler
quelqu'un qui n'a rien demandé, et de façon cumulable, FR-14 autorisant plusieurs
sollicitations. Une rencontre porte donc explicitement un côté demandeur et un côté
partenaire, et c'est la seule raison d'être de cette asymétrie dans le schéma.

La troisième dérivation est celle du lien d'acceptation (**AD-10**). Sa validité ne se lit
pas dans son propre état : elle est la **conjonction** du statut de la rencontre et de l'état
du jeton. C'est ce qui fait qu'un lien cesse de fonctionner quand la rencontre est
abandonnée — et la page d'acceptation étant le seul canal par lequel le partenaire peut
l'apprendre, aucun message ne partant, la rendre correctement n'est pas un raffinement.

Enfin, **AD-9** tient l'asymétrie des effets. L'addendum est formel : un déclencheur
générique « statut changé → prévenir » viole le produit dès sa première ligne, parce que
*abandonnée* met à jour l'agenda et n'envoie aucun courriel. Les effets sont donc attachés
aux **arêtes** de la machine à états, jamais aux nœuds.

## 4. Les sports : la seule fragilité que rien ne signale

L'addendum désigne la liste ouverte de FR-2 comme le point de fragilité du modèle, et il a
raison pour une raison précise : **l'échec est silencieux**. Si « tennis » et « Tennis » ne
convergent pas, rien ne se casse, personne ne se plaint, aucune erreur n'est levée. Les
recherches renvoient simplement moins de monde qu'elles ne devraient, indéfiniment.

Trois portées étaient possibles. La normalisation seule — casse, accents, espaces — est
trois lignes de code, mais « ping-pong » et « tennis de table » restent séparés **sans
recours** : rien ne permet de les réconcilier après coup sans reprise de données. La
projection par le LLM sur un sport canonique est plus souple, et c'est exactement ce qu'il
ne faut pas ici : non déterministe, elle produit la fragmentation redoutée **en moins
prévisible**, le même mot pouvant se rattacher différemment d'une session à l'autre.

Le choix retenu — **AD-5** — est la clé déterministe plus une table de synonymes qui redirige
à l'écriture. Le coût est assumé et nommé : un libellé absent de la table fonde un sport, ce
que FR-2 exige de toute façon. Ce qui change, c'est que **la réparation reste possible** —
et c'est pour cela que `SPORT` est une entité dans le schéma et non une colonne. Fusionner
deux libellés doit rester une opération, jamais une reprise de données.

## 5. Les envois : ce qui n'arrivera jamais à personne

FR-14 envoie de vrais SMS. Sauf que les 86 numéros d'amorçage sont dans la plage de fiction
réservée par l'ARCEP, **garantie non attribuée à un abonné**. Aucun opérateur ne les
délivrera jamais. Pour la population majoritaire du vivier, l'envoi est structurellement
impossible — et c'est une propriété voulue, le PRD la posant comme garde-fou de vie privée.

Il en découle une conséquence que ni le PRD ni l'addendum ne tirent : **le lien d'acceptation
doit atteindre le constructeur par un autre chemin**, sans quoi FR-14 n'est ni testable ni
démontrable, et les scénarios de démonstration de l'addendum — garder le lien ouvert dans un
second onglet, le recharger après un abandon pour voir le cinquième statut — sont
inexécutables.

D'où **AD-12** : tout message sortant devient une ligne persistée portant son destinataire,
son corps rendu, son lien et son sort, listée par une page locale. Le mode « journaliser sans
envoyer » de l'addendum cesse d'être un interrupteur de développement pour devenir le
transport lui-même.

Le point délicat est que l'addendum exige que le filtre et ce mode **coexistent** et ne se
remplacent pas. La spine les sépare donc en deux couches qui ne se recouvrent pas : le
**filtre** est une règle de domaine, active en production, qui décide si un message a le
*droit* de partir ; la **boîte d'envoi** est un adaptateur, qui décide s'il part
*réellement*. Et **AD-11** tient l'exigence sous-jacente : la provenance de chaque numéro
est portée dans le modèle et jamais déduite du préfixe, pour que la règle survive à un futur
amorçage par d'autres données.

## 6. Les services tiers : ce qui a été vérifié, et ce qu'on a trouvé

Aucun service n'a été retenu de mémoire ; les quatre ont été interrogés ou lus.

**Open-Meteo** couvre les deux premiers seuils de FR-10 — `apparent_temperature` et
`wind_gusts_10m` sont des variables de prévision horaire, jusqu'à seize jours, sans clé
d'API.

**Data ES**, le Recensement des Équipements Sportifs du ministère des Sports, ferme **QO-4** :
la source de terrains que le PRD n'avait pas identifiée existe, s'interroge anonymement en
une requête, et porte les deux champs dont FR-11 et FR-10 dépendent — `equip_nature` et
`aps_name`. Tant que cette question restait ouverte, le PRD notait que FR-11 n'était garanti
que sur sa branche « pas de donnée » ; elle ne l'est plus.

Deux découvertes ont produit des règles.

La première est que `equip_nature` **n'est pas un booléen** : la valeur observée est
« Extérieur couvert ». Or les trois seuils de FR-10 — chaleur ressentie, rafales, qualité de
l'air — ne comportent **aucune notion de pluie**. Un terrain extérieur couvert abrite de ce
que le produit ne vérifie pas, et n'abrite ni de la chaleur, ni du vent, ni de l'air. Le
classer « couvert » désactiverait la jouabilité précisément là où elle reste pertinente.
C'est **AD-14**, et la projection vit dans le domaine, pas dans l'adaptateur.

La seconde est venue du gate. L'API ATMO Auvergne-Rhône-Alpes, que l'addendum désigne comme
faisant foi pour Lyon, retourne l'indice pour **la veille et le jour même**, le jeu de
données régional descendant au lendemain. Son horizon est donc d'environ **un jour**, contre
**seize** pour la météo — un ordre de grandeur d'écart. Le produit prenant des rencontres
quelques jours à l'avance, un constructeur qui aurait supposé un appel « météo » unique
aurait produit soit un trou silencieux, soit une valeur inventée. C'est **AD-19** : deux
ports séparés, aux horizons déclarés distincts, et un créneau hors de portée de l'un emprunte
la branche que FR-10 prévoyait déjà — *« un créneau hors de portée des prévisions est annoncé
comme tel, sans valeur inventée »*.

L'API ATMO est aussi la seule dépendance qui demande une démarche : gratuite, mais sur
inscription.

## 7. La stack, et pourquoi elle est si petite

Le projet est un apprentissage exécuté en local. Cela retire d'un coup l'hébergement, les
secrets managés, l'observabilité de production, les environnements multiples et
l'orchestration de conteneurs. Ce qui reste tient dans un processus.

Le produit a par ailleurs une forme qui décide plus que les préférences. **Le fil est un
journal append-only** : le passé devient inerte et ne change plus, seuls deux blocs mutent
sur place (**AD-17**). Il n'y a ni tableau de bord, ni navigation, ni routes. C'est la forme
d'un rendu serveur poussé en SSE. Et `EXPERIENCE.md` interdisant toute bibliothèque de
composants — « le point de départ est une page blanche » — le HTML et le CSS s'écrivent à la
main de toute façon, ce qui retire l'argument principal en faveur d'un framework client.

D'où **Python 3.13 + FastAPI**, avec SQLAlchemy pour un travail dominé par les jointures, et
**SQLite** — dont le modèle à écrivain unique rend d'ailleurs quasi gratuite l'atomicité
qu'exigent **AD-8** et FR-13, là où Postgres demanderait un verrouillage explicite. Les
versions sont épinglées et ont été vérifiées le jour de la rédaction.

## 8. Ce que cette passe renvoie en amont

Trois choses méritent de redescendre vers le PRD plutôt que de rester ici.

- **QO-4 est fermable.** La source existe et porte l'attribut dont FR-10 dépend. La présence
  de FR-11 dans le périmètre MVP cesse d'être un pari.
- **La projection `equip_nature` → jouabilité applicable est un arbitrage produit déguisé en
  détail d'intégration.** L'architecture l'a tranché (AD-14) sur la lettre de FR-10 — trois
  seuils, pas de pluie — mais c'est le PRD qui devrait le porter.
- **L'horizon de la qualité de l'air limite FR-10 dans les faits.** Le PRD prévoit la branche
  « hors de portée des prévisions » ; il ne dit pas qu'elle sera le cas courant pour l'air dès
  que la rencontre est à plus d'un jour. C'est une propriété du produit, pas une panne.

Un quatrième point relève de l'arbitrage que l'addendum laissait ouvert entre produit et
architecture : **QO-6, la fraîcheur d'une fiche**. Il a été tranché ici, en suivant l'argument
de l'addendum — la poser maintenant coûte une colonne, la poser après coup coûte une reprise
de données. La colonne existe et n'est **jamais lue** en v1. Le seuil et son usage restent
entièrement du produit.

## 9. Ce que l'architecture ne fait pas

Elle n'anticipe rien de la calibration du niveau : ni `mu`, ni `sigma`, ni historique de
résultats. Le PRD assume la sur-évaluation sans contrepartie, et un schéma qui préparerait la
correction laisserait croire qu'elle est prévue.

Elle ne modélise pas le parcours conversationnel côté partenaire (QO-2), ni la réservation,
ni le multi-sport. Elle ne prévoit aucun repli au LLM — il n'y en a pas — mais **AD-20**
impose que la panne se dise, avec un texte arrêté, et qu'aucune écriture de domaine ne soit
engagée par un tour interrompu.

## Note sur la revue

Le gate de revue prévoit des lentilles dispatchées en sous-agents indépendants. Les consignes
de cette session les interdisant, les deux lentilles configurées et le marcheur de rubrique
ont été appliqués **en séquence dans le contexte de l'auteur**. La passe déterministe
(`lint_spine.py`) est sans appel et retourne zéro finding, mais **l'indépendance de contexte
que le gate recherche n'a pas été obtenue** : un relecteur neuf trouve les divergences que
l'auteur contourne sans les voir. Six trous ont malgré tout été trouvés et fermés — AD-19,
AD-20 et AD-21 ajoutés, AD-4, AD-5 et AD-17 resserrés, et deux cardinalités de l'ERD
corrigées qui contredisaient FR-1 et le §4 du PRD. C'est une limite réelle de cette passe, et
une revue indépendante reste souhaitable avant de construire.
