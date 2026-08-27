# Revue d'implémentabilité — Ex Aequo v3

*Point de vue : développeur front-end senior, sans accès aux auteurs, sans accès au PRD.
Entrées : `DESIGN.md` v3, `EXPERIENCE.md` v3, `mockups/*.html`.
Question unique : **puis-je construire ce produit à partir de ces documents seuls ?***

---

## Verdict global

# CONSTRUCTIBLE AVEC RÉSERVES

Le système visuel est constructible presque tel quel : les jetons sont complets, dérivés les uns
des autres, et la table de contraste est un vrai contrat plutôt qu'un certificat. Le plancher
d'accessibilité est le meilleur que j'aie eu à implémenter à partir d'un document de conception —
il nomme ses propres fautes, y compris celles qu'il a lui-même commises. La microcopie est
rédigée, pas décrite.

Ce qui bloque n'est **pas** le rendu d'un état, c'est le **passage** d'un état à l'autre. Les deux
documents décrivent avec une grande précision à quoi ressemble chaque configuration du fil, et
presque jamais ce qui la fait naître ou mourir. Le mot qui porte tout — « **tour résolu** » — est
employé neuf fois comme prédicat de règles opérationnelles et n'est défini nulle part ; deux règles
majeures (« un seul bouton primaire actif à la fois », « le passé est inerte ») sont explicitement
adossées à lui, donc adossées à rien.

Le second front est plus étroit mais plus surprenant : **les trois composants nouveaux de la v3
sont spécifiés au repos et au survol, et pas une fois résolus.** `level-choice` a trois états dans
la maquette (repos, survol, focus) et aucun quatrième ; or le bloc est cliqué, et le produit
interdit par ailleurs de dire l'état d'un contrôle clos autrement que par un mot visible. Ce mot
n'est écrit pour aucun des trois.

Enfin, plusieurs **contrôles cités comme déclencheurs n'existent comme composants nulle part** :
la validation du créneau (citée quatre fois), le consentement d'écriture agenda, les « boutons de
contre-proposition », le bloc d'alerte différée. Le `button-primary` est le composant le plus
contraint des deux documents — et pas une seule de ses instances n'est jamais placée.

Je peux livrer le fil à froid, la déclaration du niveau au repos, la proposition de partenaires,
le récapitulatif et ses quatre statuts, la page d'acceptation, et tout le plancher d'accessibilité.
Je ne peux pas livrer la seconde moitié du parcours 1 (heure, validation, agenda) ni la reprise
sans inventer des composants.

**13 questions bloquantes. 22 questions gênantes.**

---

## Questions BLOQUANTES

### 1. Qu'est-ce qu'un « tour résolu » ?

`EXPERIENCE.md:298` — « Dès qu'un tour est résolu, **tout** ce qu'il contenait de cliquable devient
inerte ». `EXPERIENCE.md:208` — « La règle "une seule instance" tient par l'inertie du passé : dès
qu'un tour est résolu… ». `EXPERIENCE.md:200`, `211`, `244`, `DESIGN.md:433`, `444` reposent sur le
même mot. Aucune de ces occurrences ne dit **quel événement** résout un tour.

Trois lectures produisent trois produits différents :

- *un tour est résolu quand la personne envoie un message quelconque* — mais alors
  `EXPERIENCE.md:244` est faux : « "Montrer les autres" pose une nouvelle salve de cartes à la
  suite ; les précédentes restent actives tant que le tour n'est pas résolu ». Ici la personne a
  parlé (ou cliqué), le bot a répondu, et les cartes précédentes restent **actives**. Donc parler
  ne résout pas.
- *un tour est résolu quand le choix qu'il proposait est fait* — alors un tour dont le choix n'est
  jamais fait reste actif éternellement, et l'ordre de tabulation traîne les vingt tours
  d'historique que la règle existe précisément pour éviter.
- *un tour est résolu quand le bot pose le tour suivant* — contredit également `244`.

Sans ce prédicat je ne peux écrire ni la mise en inertie, ni la garantie du bouton primaire unique,
ni le déplacement de focus de `EXPERIENCE.md:200`. C'est la première ligne de code à écrire et je
n'ai pas sa condition. **C'est la question la plus coûteuse du lot** : elle gouverne le cycle de vie
de tous les composants interactifs.

*Ce qu'il faut écrire : une définition opérationnelle, du type « un tour est résolu quand une
action qu'il proposait est exercée, ou quand le tour suivant propose une action de même nature »,
avec le cas explicite de la salve supplémentaire.*

### 2. À quoi ressemble `level-choice` une fois qu'on a cliqué ?

`DESIGN.md:236-255` définit onze propriétés d'option : fond, fond au survol, filet, filet au
survol, rayon, calage, hauteur minimale, alignement, police du mot, police du fait, écart. Il n'y a
**ni jeton de sélection, ni jeton d'état inerte, ni jeton d'appui**.

Or `EXPERIENCE.md:298` impose que ces trois boutons deviennent inertes avec leur tour, « [portent]
leur sort en toutes lettres **quand il y en a un** ». Y en a-t-il un ? `DESIGN.md:473` interdit
formellement de dire la clôture par le filet (« Un filet plus discret pour dire qu'une carte est
close » est dans la colonne *À éviter*), et `EXPERIENCE.md:367` répète que la distinction
actif / inerte est portée par un mot visible. Pour `partner-card`, les mots sont donnés :
*retenue* / *non retenue* (`DESIGN.md:433`). Pour `level-choice`, rien.

Je dois donc décider seul : le bloc entier disparaît-il ? Reste-t-il avec l'option choisie marquée
(par quoi ?) et les deux autres barrées (par quoi ?) ? Aucune des trois issues n'est neutre — la
première viole « tout ce qui est annoncé reste lisible dans le fil » (`EXPERIENCE.md:346`), les
deux autres exigent un mot que personne n'a écrit.

Accessoirement, aucune phrase du bot ne suit le clic. `EXPERIENCE.md:232` fait de la répétition du
mot « la seule occasion qu'a la personne de **corriger** la donnée qui structure tout son
appariement » — mais uniquement sur le chemin où le mot était dans la phrase. Sur le chemin du
bloc, le parcours 2 (`EXPERIENCE.md:468-469`) passe de « elle prend le troisième » directement à
« le bot narre sa recherche ». La garantie de correctibilité existe-t-elle sur ce chemin, ou le
clic en tient-il lieu ?

### 3. Que se passe-t-il si la personne répond au bloc de niveau par un mot que le bot ne sait pas lire ?

`EXPERIENCE.md:232` : « Le bot n'interprète **jamais** une formulation approchante — "bon niveau",
"correct", "ça va" — même évidente : toute autre formulation ouvre le bloc. »
`EXPERIENCE.md:233` : « **Un seul tour**, jamais deux ». Et : « Le bloc n'apparaît jamais pendant
ni après une recherche ».

Le bloc est affiché. La personne, au lieu de cliquer, écrit « je dirais correct ». Les règles
disent simultanément que cette formulation *ouvre le bloc* (déjà ouvert), qu'il ne peut y avoir
qu'un seul tour, et que le bot ne peut pas deviner. Le bloc existant reste-t-il actif ? Le bot
reformule-t-il en prose ? Ne dit-il rien ? La formulation « Niveau non interprétable »
(`EXPERIENCE.md:115`) est écrite pour la **première** occurrence, pas pour la seconde — et sa
réutilisation telle quelle produirait exactement la boucle qu'un chatbot de support fait subir,
c'est-à-dire le repoussoir déclaré du produit.

C'est un état atteignable en deux frappes, sur le composant le plus neuf du produit, et il n'a pas
de sortie écrite.

### 4. Quels sont les deux libellés de `sport-replace` ?

`EXPERIENCE.md:205` : « deux `button-quiet` de rang égal : **passer au nouveau sport, garder
l'ancien** » — une description, pas des libellés. Et immédiatement : « Le coût […] est écrit dans
la prose au-dessus, **jamais dans un libellé de bouton** » : une contrainte sur des mots qui ne
sont pas fournis. `DESIGN.md:439` ne les donne pas davantage. Aucune maquette ne montre ce bloc.

Le document pose lui-même la règle qui rend cette lacune bloquante, `EXPERIENCE.md:110` : « Un état
décrit sans être rédigé est un endroit où le modèle comblera […] Interdire sans fournir le
remplacement ne protège rien. » `level-choice` a obtenu ce traitement — ses trois libellés sont
déclarés contractuels et écrits (`EXPERIENCE.md:116`, `DESIGN.md:438`). Le bloc que les deux spines
qualifient de « geste le plus destructeur du produit » ne l'a pas.

Et le piège est réel : « Passer au badminton » / « Garder le tennis » est acceptable ; « Remplacer »
/ « Annuler » brise le rang égal (l'un nomme la destruction, l'autre nomme un non-événement) ;
« Continuer » / « Retour » réintroduit la langue du formulaire. Je vais choisir, et j'ai une chance
sur trois d'enfreindre une règle du document.

### 5. Quel est le gabarit de `candidate-group-label` ?

Un seul exemplaire est donné, trois fois : « Trois intermédiaires, comme vous »
(`DESIGN.md:440`, `EXPERIENCE.md:206`, `EXPERIENCE.md:445`). C'est une chaîne, pas un gabarit, et
c'est le seul des trois niveaux qui échappe à toutes les difficultés :

- **Genre.** « intermédiaire » est épicène. « Trois avancé**s** » ou « Trois avancé**es** » ? « Trois
  débutant**s** » ou « débutant**es** » ? Le produit ne montre nulle part le genre d'un candidat, et
  `EXPERIENCE.md:325` interdit toute mention de second rang sur les cartes — mais le français
  m'oblige à trancher dans l'intitulé. Les trois exemples de la spine (Anna, Iris, Tessa) sont tous
  féminins et tous « intermédiaires » : le cas difficile est masqué deux fois.
- **Nombre.** La recherche peut rendre une ou deux cartes (`EXPERIENCE.md:398` prévoit ce cas pour
  la mise en page). « Une intermédiaire, comme vous » ? En chiffres ou en lettres ?
- **Seconde salve.** `EXPERIENCE.md:244` : « "Montrer les autres" pose une nouvelle salve de cartes
  à la suite ». Cette salve porte-t-elle son propre intitulé ? Répéter « Trois intermédiaires,
  comme vous » serait faux (il y en a six) et le supprimer laisserait un `role="group"` anonyme, ce
  que `EXPERIENCE.md:206` interdit nommément.

Ce n'est pas un détail de rédaction : `DESIGN.md:440` dit que « c'est par lui que la promesse du
produit reste énoncée après que la carte a cessé de la répéter ». La phrase qui porte la promesse
du produit n'a pas de forme générale.

### 6. Que désigne « délai d'attente », et dans quel sens trie-t-on ? [CONTRADICTION interne]

`EXPERIENCE.md:244`, en une seule phrase : « L'ordre est celui du **délai d'attente croissant** —
qui attend depuis le plus longtemps passe en premier ».

Les deux moitiés s'annulent. Si « délai d'attente » est le temps **à venir** avant de pouvoir jouer,
alors « croissant » place le plus proche en premier et la glose est inversée. Si c'est
l'ancienneté **passée** du candidat dans le vivier, alors « croissant » place le plus récemment
inscrit en premier et la glose est également inversée. Aucune lecture ne sauve la phrase.

`EXPERIENCE.md:445` désambiguïse dans un sens (« mercredi, samedi, lundi, dans cet ordre parce que
c'est celui du délai d'attente croissant **depuis mardi** ») et la maquette suit (« dans 1 jour »,
« dans 4 jours », « dans 6 jours », `key-proposition-partenaires.html:155-163`). Mais ces deux
sources sont *illustratives* et la règle normative est celle de la ligne 244, qui renvoie à FR-6
que je n'ai pas.

Les deux lectures ne changent pas seulement l'ordre : elles changent le **texte visible de la
carte**, seule information qui distingue les trois candidats depuis que le niveau en est parti
(`DESIGN.md:433`). « dans 1 jour » et « inscrite depuis 40 jours » ne sont pas la même carte, et
le tri n'est pas le même.

### 7. Où sont les contrôles qui engagent — et où est le seul `button-primary` du produit ?

`button-primary` est spécifié avec un soin remarquable (`DESIGN.md:192-206`, `444` : fond, survol,
appui, désactivé, filets d'état, plancher de cible) et gouverné par une règle globale
(`EXPERIENCE.md:208`, `300`). **Aucune instance n'est jamais placée.** Tous les blocs nommés le
refusent explicitement : `level-choice` (`DESIGN.md:438`), `sport-replace` (`DESIGN.md:439`),
`acceptance-page` (`DESIGN.md:449`) ; `auth-block` et `agenda-choice` utilisent deux `button-quiet`.

Il manque en réalité trois contrôles entiers :

- **La validation du créneau.** Citée quatre fois comme déclencheur (`EXPERIENCE.md:57`, `203`,
  `211`, `248` : « avant la validation du créneau », « après validation du créneau »). Aucun
  composant, aucun libellé, aucun jeton. Est-ce un bouton ? Une phrase tapée ? Le parcours 1
  (`EXPERIENCE.md:448`) écrit « Thomas la prend » sans dire par quel geste.
- **Le consentement d'écriture agenda.** `EXPERIENCE.md:203` : « un second geste explicite, jamais
  implicite au choix du fournisseur ». Quel geste ? `agenda-choice` ne décrit que le choix du
  fournisseur, et son jeton (`DESIGN.md:159-164`) ne prévoit qu'un conteneur à deux options.
- **Les « boutons de contre-proposition ».** `EXPERIENCE.md:298` les énumère parmi les contrôles qui
  deviennent inertes. Mais `DESIGN.md:441` rend la contre-proposition « en `meta` / `ink-secondary`
  sous le constat », et la maquette la rend en `<p class="alt">`
  (`key-recap-en-attente.html:132`) : ce n'est pas un bouton. Une règle d'inertie s'applique à un
  contrôle que le composant n'a pas.

Je ne peux pas construire les étapes 8 à 10 du parcours 1.

### 8. Qu'est-ce que le « bloc d'alerte différée » ?

`EXPERIENCE.md:246` : « Un bloc dans le fil récapitule l'alerte **avec un bouton d'annulation** —
c'est donc un composant distinct du récapitulatif de rencontre, qui est non interactif. »

Le document affirme l'existence d'un composant, le distingue explicitement d'un autre, et ne le
définit nulle part : aucune entrée dans le frontmatter `components` de `DESIGN.md`, aucune ligne
dans *DESIGN.md.Components*, aucune ligne dans *Component Patterns*, aucune maquette, aucun libellé
pour son bouton d'annulation, aucun rôle ARIA, aucun état pour l'alerte expirée
(`EXPERIENCE.md:247` : « l'alerte reste visible dans le fil **avec son statut** » — quel statut ?
les quatre valeurs de FR-13 sont celles d'une *rencontre*).

C'est aussi le seul composant interactif **persistant** du produit, ce qui le met en collision
frontale avec `EXPERIENCE.md:298` : tout contrôle devient inerte avec son tour, mais un bouton
d'annulation devenu inerte au tour suivant n'annule plus rien. Et `EXPERIENCE.md:246` précise que
« plusieurs alertes peuvent coexister ; la reprise les liste toutes ».

L'alerte différée est par ailleurs la seule valeur produite par le parcours 2 tout entier —
`EXPERIENCE.md:162` : « Si l'alerte est la seule valeur produite par une conversation sans
résultat, ce courriel *est* la livraison. »

### 9. Quel composant porte « Niveau : je ne sais pas encore » avant toute recherche ?

`EXPERIENCE.md:234` et `118` : « **Le récapitulatif** porte *« Niveau : je ne sais pas encore »* […]
suivi de la phrase qui dit ce que ce trou empêche ». Mais le seul récapitulatif défini est le
`meeting-recap`, et il n'existe **qu'après écriture dans l'agenda** (`EXPERIENCE.md:58`, `201` ;
`DESIGN.md:435`). Le refus du niveau se produit avant même la recherche : à cet instant il n'y a
aucune rencontre, donc aucun récapitulatif.

La maquette a rencontré le même mur et a inventé un composant pour s'en sortir :
`key-declaration-niveau.html:194-198` pose un `<div class="recap" role="group" aria-label="Votre
fiche">` contenant « Pilates — mardi », la valeur inconnue et la phrase de coût. Ce bloc — un
récapitulatif **de profil**, distinct du récapitulatif de rencontre — n'existe dans aucune des deux
spines : pas de nom, pas de jeton, pas de déclencheur, pas de règle de persistance, pas de sort
quand le niveau finit par être donné.

Or il porte la seule formulation que `EXPERIENCE.md:154` qualifie de « seul inconnu du produit dont
le coût s'écrit », et `EXPERIENCE.md:315` en fait l'unique exception nommée à une règle générale de
conception. L'exception nommée n'a pas de support.

### 10. La reprise : « en tête de fil » de quoi, exactement ?

Quatre passages disent que le bot récapitule « **en tête de fil** » (`EXPERIENCE.md:52`, `64`,
`230`, `484`). Trois problèmes s'empilent :

- **Position.** Le fil est un `role="log" aria-relevant="additions"` (`EXPERIENCE.md:338`) et défile
  vers le bas ; la personne arrive en bas. Insérer en tête d'un `log` est le contraire de ce que le
  rôle décrit, et le contenu ne serait ni vu ni annoncé. « En tête de fil » veut-il dire « au sommet
  du DOM » ou « en premier dans le nouveau tour » ?
- **Forme.** `EXPERIENCE.md:64` : « un récapitulatif **en prose** ». `EXPERIENCE.md:230` : « avec
  leurs **pastilles** ». Une pastille est un composant, pas de la prose. Prose contenant des
  pastilles ? Blocs `meeting-recap` re-rendus ?
- **Duplication.** Le `meeting-recap` « persiste dans le fil et se met à jour **sur place** »
  (`EXPERIENCE.md:201`). À la reprise il est donc déjà présent, plus haut. Le récapitulatif de
  reprise en produit-il un second, pour la même rencontre ? Si oui, lequel des deux mute quand Anna
  répond, et lequel porte la ligne du jour bloqué que le parcours 3 dit « toujours en place »
  (`EXPERIENCE.md:484`) ? Deux récapitulatifs divergents pour une même rencontre casseraient la
  seule promesse que ce composant porte : être « le point de vérité du parcours ».

### 11. Comment tenir « rien n'est annoncé pendant que la personne tape » quand le fil *est* la région live ?

`EXPERIENCE.md:338` : le fil entier est `role="log"`.
`EXPERIENCE.md:345` : « **Rien n'est annoncé pendant que la personne tape** […] Les annonces
attendent une pause de saisie. »

Si le fil est la région live, la seule chose que je contrôle est **le moment où j'insère le nœud**.
Trois issues, toutes lourdes, aucune choisie :

- retarder l'insertion **visuelle** aussi — le message du bot n'apparaît pas à l'écran tant que la
  personne tape, ce qui contredit la promesse de vivacité (`EXPERIENCE.md:415` : signe de vie en
  moins de 2 s) et le fait que la zone de saisie « reste active pendant que le bot travaille » ;
- insérer visuellement en désarmant `aria-live` puis le réarmer — fragile, non décrit, et contraire
  à `EXPERIENCE.md:341` (« les régions live existent avant d'avoir quoi que ce soit à annoncer ») ;
- ne rien faire, la région polie empilant d'elle-même — mais alors la règle est décorative, ce que
  le document nie explicitement en la posant comme plancher contractuel.

Et la **durée** de la pause n'est pas chiffrée, alors que le même document chiffre 5 s pour la
pulsation, 2 s pour le signe de vie et 20 s pour l'attente longue, en justifiant chaque fois le
chiffre. Ici il ajoute même une limite explicite (« la pause doit être détectée sur la frappe,
jamais sur la position du focus ») sans donner le seuil. Trop court : j'interromps ; trop long : la
réponse attendue n'est jamais annoncée — précisément le défaut que cette limite existe pour éviter.

### 12. Que dit la pastille « nouveau message » quand l'événement n'est pas un message ? [CONTRADICTION entre les deux spines]

`DESIGN.md:443` : « Apparaît quand **un message arrive** alors que la personne a remonté le fil. »
`EXPERIENCE.md:207` : « Apparaît quand **le fil change** […] un message qui arrive, **et aussi une
rencontre qui change de statut** — la confirmation ne produit par règle aucun message, elle serait
donc autrement le seul événement attendu et invisible. »

Deux déclencheurs différents pour le même composant. Le préambule des deux fichiers règle les
conflits **avec les maquettes** (« Cette spine l'emporte sur toute maquette, tout wireframe et tout
import », `DESIGN.md:280`, `EXPERIENCE.md:22`) et ne dit **rien** du conflit entre les deux spines.
C'est un silence, pas une règle : rien ne désigne le document qui l'emporte, et les deux se
déclarent « contrat jumeau » l'un de l'autre.

Pire, la version large casse un libellé qui est lui contractuel : `EXPERIENCE.md:207` impose
« **1 nouveau message — revenir en bas** ». Sur une confirmation d'Anna, aucun message n'est arrivé
— `EXPERIENCE.md:254` l'interdit formellement (« Pas de nouveau message triomphal »). Le produit
dont la thèse entière est qu'il ne dit rien de faux afficherait « 1 nouveau message » alors qu'il
n'y en a aucun. Il faut soit un second libellé, soit un compteur capable de compter autre chose que
des messages.

### 13. Deux demandes en cours, retour sur une décision, changement de créneau

`EXPERIENCE.md:301` est une `[DÉCISION OUVERTE — produit]` **honnêtement posée** — le document
nomme trois issues défendables et refuse d'arbitrer à la va-vite, en constatant que la version
antérieure « acceptait au lieu de trancher, ce qui laisse un développeur inventer ».

Le signalement est exemplaire ; il n'en reste pas moins que je suis le développeur en question, et
que la puce bloque trois choses distinctes :

- **plusieurs demandes** → je ne peux pas coder la reprise (question 10) sans savoir combien de
  récapitulatifs peuvent coexister ;
- **revenir sur une décision** (« en fait, Iris » après avoir retenu Anna) → c'est le cas d'usage
  direct de la primitive centrale « on ne revient jamais en arrière : **on le redit au bot** »
  (`EXPERIENCE.md:298`). La primitive est énoncée partout et son seul cas concret est déclaré non
  arbitré ;
- **changer de créneau après écriture agenda** → « le statut d'arrivée n'existe dans aucune des
  quatre valeurs de FR-13 », donc le `meeting-recap` n'a aucun état pour le rendre.

C'est la bonne façon de laisser une question ouverte. Cela reste une question dont je ne peux pas
sortir seul.

---

## Questions gênantes

*Je peux choisir un défaut raisonnable pour chacune. Elles coûtent du temps et de la reprise, pas
un arrêt.*

**a. Gouttière entre cartes et largeur d'une carte — et la maquette de référence contredit la
disposition canonique.** `DESIGN.md:391` et `EXPERIENCE.md:398` : « Cartes sur une ligne, trois au
maximum ; une ou deux cartes gardent **la largeur d'une carte** et ne s'étirent pas. » La largeur
d'une carte n'est définie nulle part, et l'écart entre cartes non plus (`partner-card.gap` =
`spacing.2` est l'écart **interne** entre le prénom et la ligne meta). Or l'unique référence
visuelle du composant héros, `key-proposition-partenaires.html:85`, écrit `.cards{display:grid;
gap:12px}` : les trois cartes y sont **empilées** au format PC, c'est-à-dire dans la disposition que
les deux spines réservent au mobile. La règle « la spine l'emporte » couvre bien ce conflit — mais
elle a pour conséquence qu'il n'existe **aucune image de la disposition canonique** du composant
central du produit, et que les proportions réelles (trois cartes de ~14 rem, texte meta qui passe à
deux lignes) n'ont jamais été vues. *Défaut retenu : 12 px de gouttière, largeur =
(45rem − 2×12px)/3.*

**b. Durée du fondu et amplitude de la translation.** `DESIGN.md:413` : « fondu bref accompagné
d'une translation verticale de **quelques pixels** ». C'est la seule animation du produit et elle
n'est pas chiffrée, alors que la pulsation l'est (5 s) avec sa justification WCAG. *Défaut :
150 ms, 4 px.*

**c. Rythme de la pulsation.** La borne est chiffrée (5 s, `EXPERIENCE.md:375`) mais pas la période.
*Défaut : celui de la maquette, `1.4s ease-in-out 3` (`key-proposition-partenaires.html:77`) —
4,2 s, sous la borne.*

**d. État pressé de `level-choice` et de `sport-replace`.** `DESIGN.md:433` établit que l'appui
tactile sur une carte doit porter **un filet** parce que la marche de fond seule ne fait que 1,48:1,
et qualifie l'absence de ce filet de défaut (« sans ce filet, ce serait un défaut, et c'en était
un », `DESIGN.md:344`). Les deux blocs neufs n'ont ni `optionBackgroundPressed` ni filet d'appui,
alors que `EXPERIENCE.md:400` généralise la règle. *Défaut : recopier le traitement de
`partner-card`.*

**e. Le jeton `borderSelected` de `partner-card` est orphelin.** `DESIGN.md:433` définit un état
**Sélectionnée** (filet `accent` 2 px). Aucun état d'`EXPERIENCE.md` n'y mène : la carte passe
directement d'active à inerte au clic (`EXPERIENCE.md:200`, parcours 1 étape 6). Y a-t-il une étape
de confirmation entre les deux, ou ce jeton est-il un résidu de la v2 ? *Défaut : état transitoire
de quelques centaines de ms avant l'inertie.*

**f. Le filet de `sport-replace` : au-dessus ou en dessous du rappel ?** [contradiction jeton/prose]
Le jeton se nomme `lossBorderTop` (`DESIGN.md:264`), donc le filet est **au-dessus** de la zone de
perte. La prose de `DESIGN.md:439` dit qu'il **sépare le rappel des deux boutons**, donc en dessous.
*Défaut : la prose, plus explicite.* Accessoirement, `EXPERIENCE.md:205` demande que le rappel soit
« rendu dans la grammaire du récapitulatif » (titre en `card-name`, détails en `meta` /
`ink-secondary`) tandis que le jeton impose `lossFont: meta` / `lossColor: ink-primary` pour tout le
bloc : les deux ne décrivent pas le même rendu. *Défaut : le jeton, qui est explicite sur le
pourquoi (« c'est ce qu'on s'apprête à détruire, il n'a pas à être plus discret »).*

**g. Disposition des deux boutons de `sport-replace`.** `level-choice` reçoit `direction: column` et
deux paragraphes justifiant l'empilement ; `auth-block` est décrit « côte à côte »
(`DESIGN.md:436`). `sport-replace` ne dit ni l'un ni l'autre, ni ce qu'il advient sous 49 rem.
*Défaut : côte à côte, empilés sous le point de rupture.*

**h. La formulation de la date de changement de statut n'est pas arrêtée.** `DESIGN.md:435` et
`EXPERIENCE.md:201` exigent « la date du dernier changement de statut », présentée comme la trace
visible sans laquelle « une information annoncée qui ne laisse aucune trace n'existe pas ». Le texte
n'est dans aucune des deux tables de formulations, et la maquette en propose deux formes
différentes — « Statut posé le 27 août » et « Confirmée le 28 août »
(`key-recap-en-attente.html:146`, `188`). *Défaut : celles de la maquette, une par statut.*

**i. L'accroche est-elle le `<h1>` ?** `EXPERIENCE.md:352` exige « un `<h1>` **visuellement masqué
permanent** » ; `DESIGN.md:366` dit que l'accroche `display` « disparaît au premier message ». La
maquette en fait un `<h1>` **visible** (`key-fil-a-froid.html`, corps). Un seul `<h1>` par page :
celui qui reste doit donc survivre en `sr-only` après le premier message. Le texte de l'accroche
(« Trouvez quelqu'un à votre niveau. »), sa sous-ligne et la phrase d'exemple sous le champ ne sont
dans aucune table de formulations, alors que `EXPERIENCE.md:229` prescrit structurellement
l'exemple. *Défaut : un `<h1>` unique, visible à froid, masqué ensuite ; textes de la maquette.*

**j. Format d'affichage du délai d'attente.** « dans 1 jour » n'existe que dans la maquette. Voir
aussi la question bloquante 6, dont ce format dépend.

**k. Ordre des questions quand plusieurs éléments manquent.** `EXPERIENCE.md:231` : « le bot demande
**un seul** élément manquant à la fois » parmi sport, jours, niveau. Le niveau est de fait dernier
(le bloc n'apparaît que « quand la demande se complète »), mais l'ordre entre sport et jours n'est
pas donné. *Défaut : sport, puis jours, puis niveau.*

**l. Durée de la « pause de saisie ».** Voir question bloquante 11 — la valeur elle-même reste
gênante une fois le mécanisme tranché. *Défaut : 800 ms.*

**m. Empilement au-dessus de la zone de saisie.** La `service-notice` est « ancrée sous le fil,
au-dessus de la saisie » (`EXPERIENCE.md:214`) et la pastille « nouveau message » est « ancrée
au-dessus de la zone de saisie » (`DESIGN.md:443`). Les deux occupent le même point d'ancrage et
entrent toutes deux dans le calcul de la zone que la saisie ne doit pas recouvrir
(`EXPERIENCE.md:362`). Leur ordre relatif n'est pas dit. *Défaut : notice au-dessus de la pastille.*

**n. `outline: none` sur la zone de saisie : la règle absolue et l'option `:focus-within` sont
conjointement intenables — et les quatre maquettes contiennent le défaut que cinq encadrés déclarent
corrigé.** [erreur factuelle des documents] `EXPERIENCE.md:361` : « **Aucune règle `outline: none`
n'existe dans ce produit, sur aucun élément, sous aucun prétexte de style** », puis, deux lignes plus
loin : « Si l'anneau doit être porté par le conteneur plutôt que par le champ, c'est par
`:focus-within` ». Or dans cette configuration le `<textarea>` focalisé affiche **en plus** l'anneau
par défaut de l'agent utilisateur, que seule une règle `outline: none` neutralise. Les deux règles
ne sont tenables ensemble qu'en portant l'anneau sur le champ lui-même. Les quatre maquettes ont
choisi l'autre voie et écrivent littéralement `textarea:focus{outline:none}`
(`key-declaration-niveau.html:90`, `key-proposition-partenaires.html:112`,
`key-recap-en-attente.html:99`, `key-fil-a-froid.html`) — alors que l'encadré répété cinq fois dans
les deux spines (`DESIGN.md:397`, `454` ; `EXPERIENCE.md:68`, `223`, `288`) affirme que
« `outline: none` sur la zone de saisie » fait partie des défauts **corrigés**. Des six défauts que
cet encadré déclare corrigés, c'est le seul qui ne l'est pas — les cinq autres le sont bien
(`border-decorative` absent, `<textarea>` partout, rôles réels sous les `aria-label`, sort de la
carte inerte en mot visible, lieux lyonnais). *Défaut : anneau porté par le champ.*

**o. Capitales forcées dans l'encadré de jouabilité.** [conflit maquette/spine] `DESIGN.md:373` :
« Pas de capitales forcées ». `key-recap-en-attente.html:71` : `.playability .head{…text-transform:
uppercase}`, sur un texte de produit et non sur du décor de maquette. Couvert par la règle de
préséance, mais non signalé par l'encadré des correctifs. *Défaut : casse normale.*

**p. Nommage du groupe de candidats.** `EXPERIENCE.md:206` : la ligne « nomme aussi le groupe […]
via un `role="group"` réel ». Les maquettes posent un `aria-label` qui **duplique** le texte visible
(`key-proposition-partenaires.html:150-151`), ce qui le fait entendre deux fois. *Défaut :
`aria-labelledby` pointant sur le `<p>` visible.*

**q. Le bouton d'envoi.** Son nom accessible est contractuel (« Envoyer », `EXPERIENCE.md:355`),
mais son contenu visuel ne l'est pas ; la maquette met un caractère « ↑ ». Le produit interdit
l'icône seule ailleurs (`DESIGN.md:434`). *Défaut : celui de la maquette, avec `aria-label`.*

**r. Combien de salves de cartes ?** `EXPERIENCE.md:244` autorise « Montrer les autres » sans borne
supérieure, alors que tout le reste du produit est borné (trois cartes, deux lieux, quatre lignes de
saisie, deux ou trois rencontres). *Défaut : pas de borne, l'ordre de tri s'épuise de lui-même.*

**s. Remplacement de sport pour un visiteur sans compte.** Le déclencheur est « un **utilisateur
inscrit** demande un autre sport » (`EXPERIENCE.md:205`, `235`). Un visiteur sans compte qui change
de sport en cours de conversation n'a pas de profil à détruire — le bloc ne s'applique donc pas, mais
rien ne le dit. *Défaut : on enchaîne sans bloc.*

**t. Phrase après application du remplacement.** `EXPERIENCE.md:313` classe « un sport en remplace un
autre » parmi les trois mutations qui « ne peuvent se produire en silence ». L'annonce est écrite
**avant** (`EXPERIENCE.md:121`) ; rien n'est écrit **après**. Les deux autres mutations (jour bloqué,
jour gagné) ont chacune leur phrase arrêtée. *Défaut : une phrase de constat sobre.*

**u. « Une seule fois par conversation » — quelle est la borne ?** La phrase sur l'incertitude du
vivier est dite « **une seule fois par conversation** » (`EXPERIENCE.md:137`, `327`). Or le fil ne se
réinitialise jamais pour un inscrit (`EXPERIENCE.md:299`) : « par conversation » vaut donc « une
seule fois à vie », y compris pour une rencontre posée six mois plus tard, auprès de quelqu'un qui
aura oublié. *Défaut : une fois par rencontre en attente posée.*

**v. « L'accroche apparaît une seule fois dans la vie du produit ».** `DESIGN.md:366`. Faux dans les
termes du document lui-même : le fil d'un visiteur sans compte est effacé à 30 jours et il retrouve
« un fil à froid ordinaire » (`EXPERIENCE.md:269`), donc l'accroche. Sans conséquence sur le code.

---

## Ce qui est remarquablement bien spécifié

Il faut le dire aussi nettement que le reste : **je n'ai jamais eu à implémenter un document de
conception qui se corrige lui-même en public.** Une bonne moitié des difficultés que je m'attendais
à rencontrer avaient déjà été rencontrées, nommées et résolues par les auteurs.

**La table de contraste est un contrat, pas un certificat.** `DESIGN.md:336-353`. Elle liste seize
paires conformes **puis dix compositions qui échouent**, chacune avec la raison précise pour
laquelle l'échec est admis — un filet, un mot, un alignement. Elle nomme sa marge la plus fine
(`ink-secondary` sur `surface-raised-pressed`, **4,513:1**, treize millièmes au-dessus du seuil) et
gèle les deux jetons concernés. Elle nomme une dépendance non évidente : `focus-ring` sur `accent`
ne fait que 1,14:1, et l'anneau du bouton primaire n'est conforme **que** grâce à
`outlineOffset: 2px`. Aucun de ces trois faits n'aurait survécu à une reprise sans être écrit ; les
trois le sont, avec le chiffre. C'est la section la plus utile des deux documents.

**La gestion du focus est complète, ce qui est rarissime.** Le focus est déplacé sur le message du
tour (qui porte `tabindex="-1"`) **avant** que le rôle soit retiré à la carte (`EXPERIENCE.md:200`,
`364`) ; le retour d'OAuth prime explicitement sur la focalisation automatique du champ
(`EXPERIENCE.md:365`) ; le chemin `Maj+Tab` est **énoncé par le produit lui-même**, à froid et dans
l'annonce du tour, parce que le même document interdit ailleurs les chemins clavier sans équivalent
visible (`EXPERIENCE.md:363`). Chacun de ces trois points est un bug que j'aurais livré.

**La microcopie est rédigée et non décrite.** Une table de plus de vingt états
(`EXPERIENCE.md:112-142`), un lexique de l'inconnu à cinq entrées avec les formes bannies en regard
(`144-154`), quatre textes sortants intégralement écrits (`156-189`). La justification est donnée et
elle est juste : « Un état décrit sans être rédigé est un endroit où le modèle comblera » (`110`).
Là où cette règle est appliquée — et elle l'est presque partout — je n'ai rien à inventer. Les
quatre lacunes que je signale plus haut (questions 2, 4, 5, gênante h) sont notables **parce que**
le reste est tenu.

**Le double rendu des étapes, avec la faute nommée.** `EXPERIENCE.md:199`, `343` : liste visible
persistante **plus** nœud satellite `role="status" aria-atomic="true"` à une phrase — et
l'explication de pourquoi poser `role="status"` sur la liste elle-même est une faute double
(écrasement du rôle `list`, ré-annonce de toute la pile à chaque ajout). C'est un piège dans lequel
tombe la plupart des implémentations.

**`aria-relevant` corrigé, avec l'erreur antérieure exposée.** `EXPERIENCE.md:338` explique que
`role="log"` ne porte pas implicitement `aria-relevant="additions"` en ARIA 1.2, que la version
précédente de la spine l'affirmait à tort, et quelle double annonce en résultait pour la pastille
qui mute. C'est exact, et c'est le genre de détail qui ne se découvre normalement qu'au test avec
un lecteur d'écran.

**Le chiffrage est fait là où il est normatif, et seulement là.** 5 secondes pour la pulsation, avec
WCAG 2.2.2 en justification et la remarque que « quelques secondes » pouvait vouloir dire dix
(`EXPERIENCE.md:375`) ; 2 s / 20 s de latence (`415`) ; 24 px contre 48 px avec l'exemption 2.5.8
correctement appliquée au seul « Pourquoi ? » (`366`, et l'aveu que la version antérieure inventait
une distinction que la norme ne fait pas) ; 360 px de plancher ; 60 jours d'alerte ; 30 jours de
rétention. Le point de rupture est **dérivé** et non posé : 49 rem = `thread-max-width` +
2 × `gutter-desktop`, en `rem`, requête média en `em`, avec l'explication de pourquoi « 720 px »
était faux (`DESIGN.md:389`, `EXPERIENCE.md:391`). Un développeur ne peut pas se tromper là-dessus.

**Les délégations sont propres.** Les seuils météo sont renvoyés à FR-10 — et le renvoi est répété
dans chacune des quatre maquettes et dans les trois encadrés des spines, avec la mention explicite
qu'aucun chiffre de maquette ni d'exemple de parcours ne fait autorité. Le canal courriel, la
rétention à 30 jours et le contrat de rendu d'un tour (flux contre mutation) sont correctement
renvoyés à l'amont ou à l'architecture — ce dernier avec **les deux implémentations décrites**
(`aria-busy="true"` sur un `<article>` inséré vide, `EXPERIENCE.md:342`), de sorte que le choix
architectural ne rouvre pas la question d'accessibilité. C'est la bonne manière de ne pas trancher :
ces documents ne se font jamais reprocher de ne pas spécifier ce qui n'est pas de l'UX.

**Les listes de bannis sont opérationnelles.** Composants bannis (`EXPERIENCE.md:219`), interactions
bannies (`302`), interdits de vocabulaire et de forme (`104-106`), tableau *Do's and Don'ts*
(`DESIGN.md:458-479`). Elles m'évitent une revue.

**Les trois composants neufs sont bien assemblés au repos.** Aucun jeton nouveau n'a été introduit —
`level-choice`, `sport-replace` et `candidate-group-label` sont entièrement dérivés de l'existant, et
la table de contraste a été **étendue de trois paires précisément pour eux** (`DESIGN.md:315`), avec
un argument juste : `level-choice` est le premier composant dont le texte secondaire porte du sens
à l'intérieur d'une cible qui se survole. Les trois libellés de niveau sont contractuels, écrits,
génériques par construction (formulés sur l'ancienneté et la fréquence, jamais sur le geste — « je
tiens un échange » ne veut rien dire au Pilates), l'empilement vertical est justifié par la mesure
de sur-évaluation, et l'absence de quatrième bouton est argumentée plutôt que subie.

**L'auto-critique documentée est un actif d'implémentation.** `border-decorative` supprimé avec le
raisonnement complet (`DESIGN.md:409`), `ink-muted` avant lui, la « frappe au vol » retirée avec la
violation WCAG 2.1.4 **et** l'inversion de son propre garde-fou (`EXPERIENCE.md:295`), l'auto-
étiquette adoptée contre la recherche amont en le disant et en chiffrant ce que l'infraction coûte
(`425-429`). Ces passages m'épargnent de reproposer chacune de ces idées, et ils me disent quelles
objections ont déjà été pesées.

---

### Résumé chiffré

| | Nombre |
|---|---|
| Questions bloquantes | **13** |
| Questions gênantes | **22** |
| Contradictions entre les deux spines | 1 (pastille « nouveau message ») — **non couverte** par la règle de préséance, qui ne vise que les maquettes |
| Contradictions internes à une spine | 3 (délai d'attente ; `lossBorderTop` ; `outline:none` / `:focus-within`) |
| Conflits maquettes / spines | 3 (cartes empilées au PC ; `outline:none` ; capitales forcées) — couverts par la règle de préséance, mais l'un est déclaré corrigé alors qu'il ne l'est pas |
| Composants cités et jamais définis | 4 (validation du créneau, consentement d'écriture agenda, bloc d'alerte différée, récapitulatif de profil) |
| Composant défini et jamais placé | 1 (`button-primary`) |
