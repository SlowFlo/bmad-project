# Revue d'accessibilité — Ex Aequo v3.2

**Référentiel** : WCAG 2.2 niveau AA · ARIA 1.2 · comportement observé des couples NVDA/Firefox, NVDA/Chrome, JAWS/Chrome, VoiceOver/Safari.
**Périmètre** : `DESIGN.md` v3.2, `EXPERIENCE.md` v3.2, les **sept** maquettes de `mockups/`.
**Date** : 2026-08-27. **Posture** : adversariale. Cette revue cherche à réfuter le découplage des régions live, pas à le valider.

> **Limite de méthode, énoncée une fois et tenue partout.** Aucun lecteur d'écran n'a été exécuté pour cette revue. Chaque fois qu'un constat dépend du comportement réel d'un couple navigateur/lecteur d'écran plutôt que du texte de la spécification, il est **marqué `[non testé ici]`**, et la distinction entre ce que la spécification impose et ce que les implémentations font est écrite explicitement. Les ratios de contraste, eux, ont été **recalculés** (formule de luminance relative WCAG 2.x) à partir des hexadécimaux de la frontmatter ; les inventaires de balises, de rôles et d'attributs sont mécaniques et exacts.

> **Ce qui n'est pas re-signalé.** La passe 3 est lue et son verdict repris. Les constats qu'elle a portés et que la v3.2 a **fermés** — A5, l'apparence active du bouton d'envoi, désormais écrite en `DESIGN.md` l. 467 avec sa paire de contraste ; A2 et B3, le récapitulatif sorti de toute portée live, `EXPERIENCE.md` l. 407 — ne réapparaissent pas. Ceux qui restent ouverts ne sont repris que là où la v3.2 **en aggrave la portée** ; ils sont alors signalés comme tels, jamais présentés comme neufs.

---

## 1. Verdict d'ensemble

**Le découplage tient — mais il est justifié par le mauvais argument, et il est livré attelé à une règle qui, telle qu'elle est écrite, retire aux utilisateurs de lecteur d'écran plus qu'elle ne leur donne.** Séparer le rendu visuel de l'annonce est le bon geste, et il l'était déjà avant la v3.2 : la passe 3 avait démontré qu'un fil portant `role="log"` ne peut pas être rendu sûr, parce que `aria-relevant="additions"` neutralise une mutation de texte mais pas la **ligne datée ajoutée** au récapitulatif — et la v3.2 ajoute un quatrième composant mutant (`profile-recap`) qui aggrave ce défaut. C'est **cela** qui impose le découplage, et le document ne l'invoque nulle part : il fait reposer toute la décision sur la règle « rien n'est annoncé pendant que la personne tape » (l. 401), qui est la moins solide des deux raisons disponibles. Le résultat est un raisonnement juste construit sur son appui le plus faible, et une règle de différé conservée par inertie argumentative alors qu'elle n'était pas nécessaire pour obtenir le découplage. Cette règle, telle qu'elle est spécifiée — trois régions concernées, aucun délai maximal, aucun événement DOM nommé — autorise la **suspension illimitée de tout message d'état pour les seuls utilisateurs de lecteur d'écran**, ce qui est le constat critique de cette revue. La recommandation tient en une phrase : **garder le découplage, supprimer la minuterie.**

---

## 2. Les quatre points

### Point 1 — La purge du satellite de tour

`EXPERIENCE.md` l. 406 : « Une fois le tour annoncé, les nœuds précédents sont **retirés** — un retrait est silencieux, `aria-relevant="additions"` l'excluant nommément. »

**En spécification, l'affirmation est exacte.** ARIA 1.2 définit `aria-relevant` comme la liste des types de modification pour lesquels l'agent utilisateur déclenche une notification ; la valeur par défaut est `additions text`, et `removals` en est absent. Poser `aria-relevant="additions"` retire donc `text` **et** laisse `removals` hors du jeu. Un retrait de nœud ne doit pas produire de notification. Le document ne se trompe pas sur ce point, et il a raison d'écrire l'attribut explicitement plutôt que de compter sur une valeur implicite de `role="log"` — la passe 3 l'avait déjà vérifié et validé.

**Mais le document se protège contre le mauvais risque.** Le danger de la purge n'est pas l'annonce fantôme au retrait ; c'est le **silence à la recharge**.

> **P1-a · ÉLEVÉ · 4.1.3.** Purger puis réécrire, c'est **remplacer**. Un satellite qui ne contient jamais plus d'un nœud (l. 406) et qui est vidé avant d'être rempli présente à l'algorithme de diff des régions live exactement la signature d'une mutation de contenu — et `aria-relevant="additions"` **exclut `text`**. Si le retrait et l'insertion tombent dans la même tâche (`textContent = ''` puis `appendChild`, ou un re-rendu de framework qui remplace le sous-arbre), un moteur qui classe le changement en mutation de texte plutôt qu'en addition **n'annonce rien**. Le produit devient muet, tour après tour, et **aucune vérification visuelle ne le révèle** : le fil s'affiche parfaitement. Le document a choisi la valeur d'attribut qui interdit précisément la catégorie de changement que sa propre mécanique produit. `[non testé ici]` — je ne peux pas dire lesquels des quatre couples classent le remplacement en `text` plutôt qu'en `additions`, et l'honnêteté impose de le dire. Mais la contrainte qui neutralise le risque est la même dans les deux lectures, et elle n'est écrite nulle part : **la purge du tour N-1 et l'insertion du tour N doivent être séparées par une tâche** (purger, laisser passer une trame, écrire), ou bien `aria-relevant` doit être abandonné et le défaut `additions text` laissé en place. Une des deux clauses doit entrer dans la spine ; aujourd'hui aucune n'y est.

> **P1-b · MOYEN.** `aria-relevant` est l'attribut de région live **le moins uniformément implémenté** de la famille. Faire de lui le mécanisme qui rend la purge sûre, c'est faire reposer la décision structurante de la section sur la pièce la moins fiable. `[non testé ici]` — mais la structure du risque est symétrique et se lit sans test : si un couple **ignore** `aria-relevant`, `removals` redevient pertinent et le fantôme que le document redoutait apparaît ; si un couple l'**applique strictement**, le remplacement est filtré et l'annonce disparaît (P1-a). Le document n'a examiné aucune des deux branches. Il écrit l'attribut comme un fait acquis (« l'excluant nommément ») là où il faudrait écrire une hypothèse et son repli.

> **P1-c · MOYEN.** **`role="log"` purgé à un seul nœud n'a plus de sens propre.** ARIA 1.2 autorise qu'un `log` perde ses entrées anciennes — la purge n'est pas illégale. Mais elle supprime la seule propriété qui distingue `log` de `status` : la liste courante. Un `log` à un nœud, `aria-atomic="false"`, poli, est **comportementalement identique** à `role="status" aria-atomic="true"` — c'est-à-dire identique au satellite d'étapes de la ligne 404, dont le cycle de vie (une phrase à la fois, remplacée) est exactement le même. Le produit spécifie donc **deux satellites au cycle de vie identique avec deux mécanismes différents**, et le plus compliqué des deux est celui qui porte le contenu le plus important. Aligner le satellite de tour sur le satellite d'étapes — `role="status" aria-atomic="true"`, un remplacement, pas d'`aria-relevant` — fait disparaître la question de la purge tout entière, y compris P1-a et P1-b. C'est la correction la plus économique de cette revue.

> **P1-d · MOYEN.** **Le doublon du mode lecture est borné à un tour comme le document le prétend — et posé au pire endroit possible.** Le calcul de volume est juste. Le placement ne l'est pas : dans les six maquettes qui portent un `<main>`, les trois satellites sont insérés **entre `</section>` et le composeur** (`key-recap-en-attente.html` l. 226-228, `key-declaration-niveau.html` l. 148-150, `key-proposition-partenaires.html` l. 179-181, et de même dans les trois autres). En mode lecture, la personne descend le fil, atteint le dernier tour du bot, puis rencontre **immédiatement** sa copie mot pour mot, puis le champ. Le doublon tombe exactement là où le trafic est le plus dense : au point de rattrapage. Et la doctrine du document plaide contre lui : l. 419, « une région live est éphémère ; **le fil est la mémoire** ». Si le fil est la mémoire, le satellite n'a **aucune raison de conserver le dernier tour** — il devrait être **vidé** peu après l'annonce, ce qui supprime le doublon entièrement et ramène le satellite à l'état vide que la ligne 410 exige déjà au premier octet. Le document n'envisage nulle part cette option, alors qu'elle est la conséquence directe de sa propre règle et qu'elle rend le « coût résiduel assumé » de la ligne 406 non pas assumé mais nul. *(Le vidage différé, et non immédiat, est le motif éprouvé : écrire, laisser un délai fixe, vider.)*

> **P1-e · FAIBLE.** `EXPERIENCE.md` l. 424 : « Les trois satellites live vivent **hors des repères**. » Dans six maquettes sur sept, ils sont **à l'intérieur de `<main>`**. La septième, `key-fil-a-froid.html`, n'y est conforme que par accident : ce fichier ne contient **aucun `<main>`** (0 occurrence).

---

### Point 2 — Le point de défaillance unique nouvellement créé

**Oui, il est réel, et le document ne le mentionne pas une seule fois.** Avant la v3.2, un défaut dans les satellites dégradait ; le fil restait live et parlait. Depuis, le fil est inerte pour l'annonce (l. 401) et les trois satellites sont le seul chemin sonore du produit. Deux aggravations que le document ne pèse pas :

> **P2-a · ÉLEVÉ.** **La défaillance est silencieuse au sens technique, pas seulement au sens fonctionnel.** Un satellite mal câblé ne lève aucune exception, ne casse aucune mise en page, n'écrit rien dans la console. La recette visuelle passe à 100 %. Et la v3.2 a interposé une **minuterie** entre l'événement et l'écriture : la panne la plus probable — un écouteur attaché au mauvais événement, une composition IME qui ne se résout jamais, un `setTimeout` annulé par un re-rendu — produit exactement le comportement **spécifié** pour « quelqu'un qui tape sans discontinuer » (l. 418). Le produit ne fournit donc aucun moyen de distinguer le défaut de la fonctionnalité. C'est la propriété la plus dangereuse d'une conception d'accessibilité : elle rend l'échec indiscernable du succès.

> **P2-b · ÉLEVÉ.** **La spine exige que les satellites *existent* au premier octet (l. 410) ; elle n'exige nulle part qu'ils *survivent*.** Dans une application à page unique, un re-rendu qui recrée un nœud satellite détruit la région live — et une région recréée avec son contenu n'est pas annoncée, ce que la ligne 410 énonce elle-même. Jusqu'à la v3.1, la région était le **conteneur du fil** : un élément structurel, qu'aucun rendu ne remonte. Le découplage a déplacé la fonction sur trois `<div>` jetables de trois lignes, et la clause qui les protège n'a pas suivi. La ligne 410 se félicite que la règle « vise désormais trois nœuds vides de trois lignes […] elle en devient plus facile à tenir » : c'est vrai pour la pose initiale, et faux pour la durée de vie, qui est le seul moment où elle compte.

**Existe-t-il une conception qui obtienne le même silence-pendant-la-frappe sans ce risque ? Non — et l'analyse du document sur ce point est correcte.** Avec un fil live, la seule chose qu'on contrôle est l'instant d'insertion du nœud ; différer l'annonce impose de différer l'affichage (l. 401, exact). Basculer `aria-live` de `polite` à `off` pendant la frappe ne marche pas non plus : ce qui est ajouté pendant que la région est `off` n'est **pas** annoncé quand elle revient à `polite`, ce qui viole frontalement la ligne 417 (« rien n'est abandonné en route »). **Le point de défaillance unique est inhérent au motif**, et le motif reste celui qu'emploie toute interface conversationnelle mature.

**La compensation correcte n'est donc pas une région de repli — elle est testable, et elle manque.** Deux clauses écrites suffiraient : (1) *les trois satellites ne sont jamais démontés ni remontés pendant la vie de la page* ; (2) *un tour du bot dont le satellite reste vide au-delà de N ms est un défaut de gravité bloquante*, formulée comme un invariant vérifiable automatiquement. La section *Accessibility Floor* ne contient aujourd'hui **aucun** invariant de ce genre, et c'est la seule section du produit dont l'échec ne se voit pas.

**Verdict : compromis acceptable, mais mal payé.** Le transfert de risque est légitime ; il a été fait sans écrire la contrepartie.

---

### Point 3 — La règle elle-même est-elle nécessaire ?

**Réponse franche : non. Le découplage est nécessaire ; la règle ne l'est pas, et telle qu'elle est écrite elle coûte plus qu'elle ne rapporte. Je la supprimerais.**

> **P3-a · Le découplage survit à la suppression de la règle, et c'est le point que le document ne fait pas.** La ligne 401 fonde toute la décision sur le fait que « les deux règles s'excluaient ». Il existe une seconde raison, indépendante et plus forte, que le document possède mais n'invoque pas : **un fil live est irréparable pour les mutations de composant**. `aria-relevant="additions"` neutralise le changement de texte de la pastille, mais pas la **ligne datée qui s'ajoute** au récapitulatif — c'est le constat A2 de la passe 3, et c'est pour lui que la v3 avait dû poser `aria-live="off"` sur le récapitulatif. La v3.2 ajoute un **quatrième** composant mutant, `profile-recap` (l. 238), dont la mutation *retire* une phrase visible. Retirez demain la règle de la frappe : il faudrait **encore** découpler. Le document a donc raison de découpler et tort de dire pourquoi.

> **P3-b · ÉLEVÉ.** **La règle ne supprime pas l'empilement : elle le concentre, et elle le concentre au pire instant.** La ligne 414 argue qu'une région polie « n'interrompt pas la synthèse, mais elle empile ». C'est exact — et c'est précisément ce qui rend l'empilement inoffensif : une annonce polie attend un creux. La ligne 417 interdit ensuite la fusion et interdit l'abandon : la file doit se vider **dans l'ordre** et **sans rien perdre**. Les annonces ne sont donc pas retirées, elles sont **regroupées**, et elles sortent toutes à la première pause — c'est-à-dire à l'instant exact où la personne vient de finir sa phrase et s'apprête à envoyer. La règle troque un filet d'annonces entrelacé avec l'écho de frappe contre un **mur de parole au moment de l'action**. Ce troc n'est pas pesé dans le document, et il n'est pas favorable.

> **P3-c · Le gain existe, il est réel, il est étroit, et il a des remèdes moins chers.** Deux phénomènes justifient l'intention : l'entrelacement avec l'écho des caractères frappés de NVDA et de JAWS, et l'écrasement des lignes d'étape entre elles dans une région `aria-atomic="true"` (l. 404). Le premier est un **réglage du lecteur d'écran**, hors du contrôle du produit, et modéliser dans une spine produit un paramètre que l'utilisateur possède déjà est une erreur de périmètre. Le second n'a rien à voir avec la frappe : il se corrige par un espacement fixe entre deux écritures dans le satellite d'étapes — dont le produit a besoin de toute façon (P3-d).

> **P3-d · MOYEN · 4.1.3.** **« La file se vide dans l'ordre et jamais par fusion » (l. 417) n'est pas implémentable telle qu'elle est écrite.** JavaScript ne sait pas quand la synthèse a fini de parler. Vider une file de trois phrases dans un `role="status" aria-atomic="true"` en une seule tâche produit exactement la fusion que la règle interdit : la deuxième écriture remplace la première avant qu'elle soit prononcée. La règle exige donc un **espacement chiffré** entre deux sorties — au même titre que les 1 s, les 2 s, les 5 s et les 20 s que cette section chiffre par ailleurs — ou un mécanisme différent. Elle n'a ni l'un ni l'autre. C'est la seule règle chiffrable de la section qui ne l'est pas.

**La contre-proposition, défendue au fond.** Supprimer la règle donne : les annonces sont écrites dans les satellites **dès qu'elles sont produites**. Ce qu'on perd : la protection contre l'entrelacement, un confort réel mais que personne n'a mesuré, et qui reste corrigeable par un réglage que l'utilisateur possède. Ce qu'on gagne : la disparition de la suspension illimitée des messages d'état (P4-c, le seul constat critique de cette revue), la disparition d'une minuterie dont la panne est indiscernable du fonctionnement nominal (P2-a), la disparition d'une règle d'ordonnancement non implémentable (P3-d), et la disparition de l'intégralité de l'effet adverse sur les saisies lentes, dictées et assistées (P4-a, P4-b). Le solde est franchement positif. **Le découplage se garde, la minuterie se coupe** — et l'option que le document a listée puis écartée est celle qu'il aurait fallu retenir, à ceci près qu'elle n'impliquait pas de garder le fil live, contrairement à ce que le document suppose.

---

### Point 4 — Le seuil d'1 s, et l'absence de délai maximal

> **P4-a · ÉLEVÉ · 4.1.3.** **« La pause se détecte sur la frappe » (l. 416) ne nomme aucun événement, et les deux lectures naturelles ont des modes de défaillance opposés.** Ni `EXPERIENCE.md` ni `DESIGN.md` ne contiennent le mot *dictée*, *vocal*, *composition* ou *IME* (vérifié par recherche exhaustive sur les deux fichiers).
>
> - **Lecture `keydown`.** La **saisie vocale** (Dragon, Voice Access, la reconnaissance vocale de Windows et de macOS) insère du texte par `beforeinput`/`input` et ne produit **pas** de `keydown` par caractère. La règle ne s'armerait jamais pour l'utilisateur qui dicte — c'est-à-dire que la personne qui a le plus besoin que le canal audio reste propre reçoit les annonces en plein milieu de son énoncé, où la synthèse peut être reprise par le micro. Symétriquement, si l'application compte **n'importe quel** `keydown`, alors `Tab`, les flèches, `Maj`, `Ctrl+A` et `Page suiv.` comptent comme de la frappe : quelqu'un qui ne compose rien peut être maintenu indéfiniment dans l'état différé. `[non testé ici]` — je ne peux pas affirmer quelles touches de navigation en mode lecture atteignent réellement la page selon le couple ; NVDA et JAWS en consomment la plupart en mode navigation, VoiceOver moins. Mais un plancher contractuel ne doit pas dépendre de cette incertitude.
> - **Lecture `input` sur le champ.** Un paragraphe dicté arrive en un événement, la minuterie part immédiatement : c'est le comportement correct.
>
> La spine doit donc écrire **« tout événement qui modifie la valeur du champ »**, et écrire ce qui se passe entre `compositionstart` et `compositionend`. Elle n'écrit ni l'un ni l'autre. Corollaire : le faux positif que le document évite (l. 416, la détection par le focus, dont le raisonnement est juste et non trivial) est remplacé par un faux positif qu'il ne nomme pas — la touche qui ne compose rien.

> **P4-b · MOYEN.** **La seconde est calibrée sur un rythme de frappe qu'aucune des populations du plancher d'accessibilité n'a.** « Une seconde passe la fin d'un mot sans atteindre le temps qu'on met à chercher le suivant » (l. 415) décrit un dactylographe. Pour un utilisateur à licorne, à contacteur avec balayage, à commande oculaire ou à clavier virtuel, l'intervalle entre deux caractères est de 2 à 10 secondes : la règle **relâche la file entre chaque caractère**, c'est-à-dire qu'elle ne fait rien. Ce n'est pas nuisible en soi — elle échoue en position ouverte — mais c'est la preuve que le chiffre ne dérive d'aucune propriété des utilisateurs concernés. Le document le range au même rang que les 5 s de la pulsation, qui dérivent, elles, du texte de WCAG 2.2.2. Les deux chiffres n'ont pas le même statut épistémique, et le document les présente comme s'ils l'avaient.

> **P4-c · CRITIQUE · 4.1.3.** **« Aucune annonce n'attend plus longtemps que la première pause. Pas de second seuil, pas de délai maximal » (l. 418), combiné à « La règle vaut pour les trois » (l. 414), autorise la suspension illimitée de *tout* message d'état — et elle ne frappe que les utilisateurs de lecteur d'écran.** Pendant que la personne tape sans discontinuer, sont retenus : l'échec d'envoi (« Ce message n'est pas parti », l. 253), le hors-ligne et l'indisponibilité du bot (`service-notice`, l. 252), et la confirmation du partenaire (l. 408) — c'est-à-dire l'échec, la panne, et le seul événement que la personne attendait. L'utilisateur voyant voit chacun d'eux apparaître à l'instant où il arrive ; l'utilisateur de lecteur d'écran ne reçoit rien, sans borne. La formule qui porte toute la décision — « quelqu'un qui tape sans discontinuer est quelqu'un qui n'écoute pas » — est **fausse pour exactement la population concernée** : pour une personne voyante, taper et percevoir sont deux canaux parallèles, elle voit ce qui arrive pendant qu'elle écrit ; pour une personne aveugle, la synthèse est le canal unique, et le suspendre pendant la frappe suspend la perception entière. **La règle retire à l'utilisateur aveugle la conscience que l'utilisateur voyant conserve gratuitement.** C'est le contraire de ce qu'une section nommée *plancher d'accessibilité* est censée produire, et le renversement est logé dans une formule, pas dans une mesure.
>
> *Correction minimale si la règle survit : la région de statut est exemptée sans condition, et aucune panne ni aucun échec n'est jamais différé. La ligne 414 dit aujourd'hui exactement l'inverse, en toutes lettres.*

---

## 3. Autres constats

### ÉLEVÉ

> **X1 · ÉLEVÉ · 4.1.3 — la mutation de `profile-recap` n'est annoncée par rien, et aucune des trois régions n'y a droit.**
> `EXPERIENCE.md` l. 238 : le récapitulatif de profil « **persiste et mute sur place** : si le niveau finit par être donné, la valeur inconnue est remplacée **et la phrase de coût disparaît avec elle** ». C'est un remplacement de valeur **et un retrait de texte visible** — la seule mutation du produit qui *retire* une phrase. Les trois satellites sont spécifiés de façon exhaustive : texte d'un tour du bot (l. 403), lignes d'étape (l. 404), et « les changements de statut **d'une rencontre** » (l. 405, l. 408). Un profil n'est pas une rencontre, et le document interdit lui-même de lui prêter un statut (l. 238 ; `DESIGN.md` l. 460 : « Aucune pastille de statut : un profil n'a pas de statut »). L'énumération rassurante de la ligne 407 — « la pastille […], la ligne datée […], la ligne du jour bloqué : ces **trois** mouvements » — a été écrite avant ce quatrième mouvement et n'a pas été mise à jour. Maquette : `key-declaration-niveau.html` l. 214-218. Le composant le plus neuf de la v3.2 porte la seule mutation muette du produit, et la grammaire de l'honnêteté « interdit de **taire**, pas seulement d'inventer ».

> **X2 · ÉLEVÉ · 4.1.3 — activer la contre-proposition change l'heure retenue, en silence.**
> `EXPERIENCE.md` l. 292 : « Elle fixe l'heure ; **elle ne retient rien** » ; l. 249 et l. 148 en font un `button-quiet` réel depuis la v3.2 (`key-recap-en-attente.html` l. 155, « Jouer à 19 h »). Aucun des deux documents ne dit ce qui est annoncé quand elle est activée, ni quelle trace visible l'heure changée laisse. Ce n'est ni un tour du bot, ni une ligne d'étape, ni un changement de statut d'une rencontre : comme pour X1, **aucun satellite n'y a droit**. C'est le seul contrôle du produit dont la fonction est de modifier une valeur que la personne s'apprête à engager, et il le fait sans dire qu'il l'a fait. *En devenant un vrai bouton, la contre-proposition a gagné un rôle et perdu son annonce : en prose, l'information « je vous propose plutôt 19 h » était au moins dans le texte du tour.*

> **X3 · ÉLEVÉ · 2.4.6, 4.1.2 — « Retenir ce créneau » n'a pas d'objet, et son objet est mutable.**
> `key-recap-en-attente.html` l. 158. Le nom accessible est le libellé seul ; rien n'associe programmatiquement le bouton à une date, une heure ou un lieu. Dans la maquette il suit une phrase qui parle du court **couvert** de Gerland alors que la contre-proposition au-dessus concerne le parc de la Tête d'Or : l'ambiguïté existe même visuellement. Pour qui liste les boutons de la page — le geste le plus courant en lecture d'écran — le contrôle le plus engageant du produit répond « retenir *lequel* ? » par rien. Et après X2, l'heure qu'il engage a changé sans annonce et sans réétiquetage. Le document tient les cartes de partenaires à « **le nom accessible contient le texte visible, mot pour mot** » (l. 427) et son unique `button-primary` à rien. Le libellé contractuel (l. 147) est défendu longuement contre « Confirmer » et « Réserver » — sur le verbe, jamais sur le complément.

> **X4 · ÉLEVÉ · 2.4.3, 2.4.11 — la pastille « nouveau message » détruit le focus qu'elle détient.**
> `EXPERIENCE.md` l. 245 : « Ramène en bas. **Ne disparaît jamais sur minuterie** : elle s'efface uniquement quand le fil est revenu en bas. » Son unique action garantit donc sa propre suppression. La règle de sauvetage du focus (l. 437) est explicitement bornée à « un élément focalisé **perd son rôle** — une carte qui devient inerte, un bouton dont le tour se résout » : la pastille ne perd pas son rôle, elle est **retirée du DOM**, et le retrait n'est couvert nulle part. Une personne au clavier ou au lecteur d'écran qui l'active perd le focus au profit de `<body>`, ce qui en mode navigation ramène la position de lecture au début du document — c'est-à-dire l'exact contraire de ce que la pastille existe pour faire. Aggravation : la pastille n'apparaît dans **aucune des sept maquettes**, alors que la v3.2 en a modifié le libellé (`DESIGN.md` l. 468). Le composant dont la v3.2 a changé le contrat n'a aucune référence visuelle.

> **X5 · ÉLEVÉ · 3.3.1, 4.1.3 — le silence au deuxième échec n'est pas perceptible. La réponse à la question posée est : non.**
> `EXPERIENCE.md` l. 277 et l. 128 : « **Au deuxième échec, il se tait** : le bloc reste, rien n'est ajouté. » Rien n'est écrit dans aucun satellite, rien ne change à l'écran, et le focus est revenu dans le champ après l'envoi (l. 436). Ce que la personne entend est : rien. Or **cinq situations distinctes produisent exactement ce rien** — le bot refuse délibérément de se répéter ; le message n'est pas parti ; le bot travaille encore ; un satellite est cassé ; et, depuis la v3.2, la minuterie retient la file. La personne voyante les sépare instantanément, parce qu'elle **voit** son message se poser, le bloc rester debout, et aucun texte nouveau apparaître : le silence lui est un non-événement lisible dans la mise en page. Pour qui ne voit pas la mise en page, un silence n'est pas un signal, c'est une absence de signal, et une absence ne se distingue pas d'une autre absence. Le document interdit lui-même l'asymétrie inverse — « un repli d'accessibilité **plus riche** que le chemin nominal est un défaut, pas une faveur » (l. 446) — sans voir qu'il vient de créer l'asymétrie dans le sens ordinaire. S'ajoute que le **changement de comportement entre la première tentative** (le bot parle, l. 128) **et la seconde** (il se tait) est lui-même une information — « j'arrête de vous répondre » — transmise uniquement par une absence.
>
> *Une lecture stricte de 3.3.1 (niveau A) — une erreur de saisie détectée doit être décrite en texte — rend ce constat critique. Je m'arrête à `élevé` parce que la phrase du premier échec et le nom accessible du bloc restent dans le fil, ce qu'un évaluateur peut accepter comme identification persistante de l'erreur. La frontière est mince et mérite d'être connue plutôt qu'arbitrée en silence.*
>
> *La correction ne demande pas de rompre la règle anti-boucle, qui est bonne : rendre la persistance perceptible sans nouvelle prose — déplacer le focus sur le `role="group"` « Votre niveau » toujours ouvert. La question se réénonce sans que le bot dise un mot de plus.*

### MOYEN

> **X6 · MOYEN · 4.1.3 — une quatrième région live, dans le fil, avec son contenu déjà dedans.**
> `key-recap-en-attente.html` l. 221 : `<p class="sr-only" role="status">Anna a confirmé…</p>`, à l'intérieur du `.turn`, à l'intérieur de la `<section>` — **trois lignes au-dessus** du satellite de statut dédié et vide de la ligne 228. Contre `EXPERIENCE.md` l. 402 (« **Trois** régions live, toutes hors du flux visuel ») et l. 410 (« présentes et **vides** dès le premier octet »). Le constat A3 de la passe 3 n'a pas été fermé ; la v3.2 l'aggrave, parce que la région correcte existe désormais, vide, dans le même document, et que la maquette écrit à côté d'elle plutôt que dedans. **L'unique démonstration du mécanisme de statut dans sept maquettes le montre à l'envers.**

> **X7 · MOYEN — `button-primary` n'a aucun état inerte, dans aucun des deux documents.**
> `partner-card` possède `borderInert` (`DESIGN.md` l. 126) et un mot obligatoire — *retenue* / *non retenue* (`EXPERIENCE.md` l. 427, `DESIGN.md` l. 457). L'unique `button-primary` devient inerte avec son tour (l. 354, l. 246) sans jeton et sans mot : la clause « porte son sort en toutes lettres **quand il y en a un** » (l. 354) est l'échappatoire, et elle est employée sur le seul contrôle dont l'issue engage quelqu'un d'autre. Une personne qui revient sur ce point du fil trouve du texte là où était un bouton, et rien qui dise qu'il a été pris. La frontmatter `button-primary` (`DESIGN.md` l. 204-218) spécifie repos, survol, appui et désactivé — quatre états — et pas l'inerte, qui est le seul état durable des cinq. Maquette : `.commit` (`key-recap-en-attente.html` l. 87-92) n'a ni `:disabled` ni rendu inerte.

> **X8 · MOYEN — `button-quiet` n'a toujours ni état pressé ni état inerte, et la v3.2 lui a ajouté un sixième employeur.**
> `DESIGN.md` l. 219-228. Le composant porte `level-choice`, `sport-replace`, `agenda-choice`, `auth-block`, les deux réponses de la page d'acceptation, et depuis la v3.2 la contre-proposition de jouabilité — c'est-à-dire **tous les choix de rang égal du produit**. Il n'a pas de retour tactile et pas de rendu de clôture, alors que `DESIGN.md` l. 457 fait du retour à l'appui un impératif pour la carte et que l'inertie du passé (`EXPERIENCE.md` l. 354) s'applique nommément à lui. Constat B5 de la passe 3, non fermé, et la v3.2 en étend la portée sans le traiter. `DESIGN.md` l. 362 pré-écrit d'ailleurs la correction (« Si cet état est ajouté un jour, il prend `border-strong`, comme la carte ») : le garde-fou existe, il n'a simplement pas été appliqué.

> **X9 · MOYEN · 1.3.1, 2.4.1 — les repères des maquettes contredisent la règle que la v3.2 vient d'écrire.**
> Les satellites sont dans `<main>` dans six fichiers sur sept, contre l. 424 (« hors des repères »). Et `key-fil-a-froid.html` — **l'écran d'entrée du produit** — ne contient **aucun `<main>`** (0 occurrence ; la colonne vit dans un `<div class="void">`, l. 106-118), contre l. 424 (« un seul `main` par page »). Les autres fichiers en portent 2, 3 ou 8 par document : artefact de maquette multi-états, mais qui laisse le lecteur sans référence correcte pour la règle.

> **X10 · MOYEN · 1.3.1, 2.4.1, 2.4.6 — zéro `<article>` et zéro `<h2>` dans les sept maquettes, et la v3.2 en augmente l'enjeu.**
> Inventaire mécanique : `<article>` = 0, `<h2>` = 0, `tabindex` = 1 occurrence sur sept fichiers (et elle est dans un texte d'explication, `key-proposition-partenaires.html` l. 239, pas dans le produit). Contre l. 411 (« un seul `<article>` nommé par son contenu réel »), l. 425 (« un `<h2>` masqué par tour de parole ») et l. 437 (le repli du focus par `tabindex="-1"`). Constat A7 de la passe 3, non fermé. **Ce qui est neuf, c'est le poids :** la ligne 411 fait désormais de l'`<article>` l'unité dont le contenu est copié dans le satellite de tour — l'ossature n'est plus une commodité de navigation, elle est l'unité de découpe de l'annonce ; et la purge (l. 406) fait du fil visible la **seule** transcription durable, de sorte que la navigation par titres, que la ligne 425 appelle « le premier réflexe en mode lecture », est le seul moyen de la relire et ne renvoie rien.

### FAIBLE

> **X11 · FAIBLE · hygiène 1.4.3 — une composition réelle absente d'une table déclarée contractuelle.**
> `ink-secondary` / `status-danger-quiet` = **6,197:1** (recalculé). Conforme, et absente de la table (`DESIGN.md` l. 328-348) alors que `playability-callout` déclare `colorMeta: '{colors.ink-secondary}'` (l. 189) et que la maquette l'emploie (`key-recap-en-attente.html` l. 78, la ligne « Je vous propose plutôt 19 h »). La note de la ligne 370 affirme que les quatre lignes ajoutées couvrent « trois compositions qu'aucune ligne ne couvrait » : la prose secondaire de l'encadré en est une quatrième, et elle est antérieure à la v3.2. Le défaut n'est pas le contraste, il est qu'une table présentée comme un contrat reste incomplète après avoir été amendée pour cette raison même.
>
> *Contrôle de sincérité — les quatre lignes ajoutées en v3.2 ont été recalculées : `border-interactive`/`status-danger-quiet` **4,062**, `border-strong`/`status-danger-quiet` **5,982**, `surface-raised-hover`/`status-danger-quiet` **1,214**, `focus-ring`/`accent` **1,136**. Toutes exactes.*

> **X12 · FAIBLE — le bouton d'envoi se contredit dans le même paragraphe.**
> `DESIGN.md` l. 467 spécifie un état *désactivé* « tant que le champ est vide : `disabled` natif », puis écrit quatre phrases plus loin « il ne devient jamais inerte, aucun tour ne le résout, et **il est actif en permanence** » ; `EXPERIENCE.md` l. 246 et l. 356 répètent « actif en permanence ». Le sens visé est « jamais inerte » au sens de l'inertie du tour, mais un document qui fait de la distinction `disabled` / `aria-disabled` une clause contractuelle (l. 428) ne peut pas laisser le mot *actif* signifier deux choses à trois endroits. Accessoirement : les **douze** boutons d'envoi des sept maquettes sont `disabled` ; l'apparence active, écrite pour la première fois en v3.2, n'est démontrée nulle part.

> **X13 · FAIBLE — `text-transform:uppercase` sur l'en-tête de l'encadré de jouabilité.**
> `key-recap-en-attente.html` l. 75-76, contre `DESIGN.md` l. 394 (« Pas de capitales forcées »). Constat B1 de la passe 3, non fermé, et il porte sur le composant que la v3.2 a modifié.

> **X14 · FAIBLE · 4.1.2 — `aria-label` dupliquant un intitulé visible interne.**
> `key-recap-en-attente.html` l. 151 (`aria-label="Conditions de jeu — chaleur"`) et l. 152 (`<p class="head">Conditions de jeu — chaleur</p>`). `DESIGN.md` l. 466 écrit que le mot en tête « **nomme aussi le groupe** » : `aria-labelledby` est l'implémentation littérale de cette phrase, et supprime le risque de divergence entre les deux chaînes. Constat C-4 de la passe 3, non fermé.

> **X15 · FAIBLE — le nom accessible de `profile-recap` introduit un mot que le produit n'emploie pas.**
> `key-declaration-niveau.html` l. 214 : `aria-label="Votre fiche"`. Aucun des deux documents n'écrit jamais « fiche » ; le composant s'appelle *récapitulatif de profil*, et son frère est nommé d'après son sujet (« Rencontre avec Anna »). Nommer « Votre fiche » le seul bloc dont la raison d'être est de ne **pas** être un formulaire est le vocabulaire exact que la ligne 238 refuse (« le poser à chaque conversation en ferait le formulaire que le produit refuse d'être »).

> **X16 · FAIBLE — le déclencheur de la pastille est une position de défilement, notion mal définie en mode lecture.**
> `EXPERIENCE.md` l. 346 et l. 245 : la pastille apparaît « alors que la personne a remonté ». En mode navigation, la fenêtre suit le curseur virtuel : quelqu'un qui relit le milieu du fil a « remonté » sans avoir défilé. Aucun des deux documents ne dit si la pastille apparaît pour lui — et si elle apparaît, c'est un `<button>` inséré hors de toute région live, donc muet. Le coût est nul aujourd'hui (les satellites portent l'événement), mais une règle contractuelle sans comportement défini pour le mode de lecture qu'elle rencontrera le plus souvent est une lacune.

> **X17 · FAIBLE — le `<h1>` n'est pas permanent d'une maquette à l'autre.**
> `EXPERIENCE.md` l. 425 exige « un `<h1>` visuellement masqué **permanent** », précisément parce que l'accroche disparaît au premier message. `key-fil-a-froid.html` l. 109 et l. 136 font de l'accroche le `<h1>` (« Trouvez quelqu'un à votre niveau. ») ; les six autres fichiers portent un `<h1>` masqué « Conversation avec Ex Aequo ». Le titre de niveau 1 change donc d'identité au premier message — l'instabilité exacte que la règle existe pour empêcher.

---

## 4. Ce qui est bien fait

Bref, et vrai.

- **L'auto-diagnostic de la ligne 401 est juste et rare.** Avec un fil live, « rien pendant la frappe » et « affichage immédiat » s'excluent réellement, pour la raison exacte qui est donnée : on ne contrôle que l'instant d'insertion. La plupart des documents ne s'en aperçoivent jamais. C'est le raisonnement qui est faible (point 3), pas l'observation.
- **Le satellite d'étapes (l. 404, l. 412) est la meilleure pièce de la section**, et l'interdit qui l'accompagne — poser `role="status"` sur la `<ul>` écrase le rôle `list`, prive les `<li>` de leur dénombrement et fait ré-annoncer la pile entière — est rigoureusement exact et presque jamais écrit.
- **La bidirectionnalité de la ligne 419** — « une phrase de confirmation rendue uniquement en `sr-only` viole cette règle autant qu'une mutation muette » — est une règle que presque personne n'écrit, et `key-recap-en-attente.html` l. 214/218 la respecte : la confirmation a une trace visible **et** une annonce.
- **Le constat A5 de la passe 3 est fermé proprement** : l'apparence active du bouton d'envoi est écrite avec sa paire de contraste (`DESIGN.md` l. 467), et la distinction avec `button-primary` est argumentée sur le cycle de vie plutôt que sur l'apparence, ce qui est le bon critère.
- **Le raisonnement de la ligne 416 contre la détection par le focus est correct et non évident** — le champ étant refocalisé après chaque envoi, la file ne se libérerait jamais. Le remède introduit son propre faux positif (P4-a), mais le diagnostic est bon.
- **Le système de couleur reste exact.** Les quatre compositions ajoutées en v3.2 et la dépendance contractuelle du décalage de focus (`focus-ring`/`accent` = 1,136:1) ont été recalculées ici et sont toutes conformes aux valeurs déclarées. Une table qui liste ce qu'elle échoue, et qui va jusqu'à documenter une composition que le système **ne produit pas** comme garde-fou (`DESIGN.md` l. 362), reste le bon instinct.

---

## 5. Résumé chiffré

| Gravité | Nombre |
|---|---|
| **CRITIQUE** | **1** |
| **ÉLEVÉ** | **10** |
| **MOYEN** | **10** |
| **FAIBLE** | **8** |
| **Total** | **29** |

**Critique** : P4-c.
**Élevé** : P1-a, P2-a, P2-b, P3-b, P4-a, X1, X2, X3, X4, X5.
**Moyen** : P1-b, P1-c, P1-d, P3-d, P4-b, X6, X7, X8, X9, X10.
**Faible** : P1-e, X11, X12, X13, X14, X15, X16, X17.

**Critères WCAG 2.2 en échec avéré ou fortement exposé**

| Critère | Constats |
|---|---|
| **4.1.3** Messages d'état (AA) | **P4-c**, P1-a, P3-d, X1, X2, X6 |
| **2.4.3** Ordre du focus (A) | X4 |
| **2.4.6** En-têtes et étiquettes (AA) | X3, X10 |
| **2.4.11** Focus non masqué (AA) | X4 |
| **3.3.1** Identification des erreurs (A) | X5 *(frontière argumentée)* |
| **1.3.1** Information et relations (A) | X9, X10 |
| **2.4.1** Contourner des blocs (A) | X9, X10 |
| **4.1.2** Nom, rôle et valeur (A) | X3, X14 |

**Ordre de traitement recommandé**

1. **P4-c** — exempter la région de statut du différé, et n'y différer jamais une panne ni un échec. Une clause, et le seul constat critique tombe.
2. **P3-b + P3-d + P4-a + P4-b** — supprimer la minuterie. Les quatre constats tombent ensemble, et P2-a s'allège. C'est la recommandation de fond de cette revue.
3. **P1-c** — aligner le satellite de tour sur le satellite d'étapes (`role="status" aria-atomic="true"`, un remplacement). P1-a, P1-b et P1-d tombent avec la purge.
4. **X1 + X2** — étendre le droit de la région de statut aux mutations qui ne sont pas des rencontres, ou créer la quatrième région qui les porte. Deux mutations muettes, toutes deux introduites en v3.2.
5. **P2-b** — écrire que les satellites ne sont jamais démontés, et l'invariant vérifiable qui manque à toute la section.
6. **X3, X4, X5** — le complément du libellé engageant, le sauvetage du focus de la pastille, la perceptibilité du silence délibéré.
7. Le reste par gravité décroissante. X10 et X9 sont du travail de maquette ; X12, X13, X14 et X17 sont des corrections de texte.
