# Voix et microcopie — Ex Aequo

> Audit de la voix, du registre et de la microcopie. Périmètre : `EXPERIENCE.md`, `DESIGN.md`,
> `mockups/*.html`, confrontés au `prd.md` et à `research-paysage.md`.
> Aucun fichier existant n'a été modifié. Les reformulations proposées sont des propositions rédigées, pas des correctifs appliqués.

## Verdict d'ensemble

La voix d'Ex Aequo est juste partout où elle est **écrite** : pas un emoji, pas un point d'exclamation, pas une excuse, pas une félicitation, pas un « Bonjour » — le repoussoir du chatbot de support est tenu à distance avec une rigueur rare, et le vouvoiement ne glisse jamais au tutoiement. Le problème n'est pas ce qui est écrit, c'est **ce qui ne l'est pas** : environ vingt-cinq chaînes existent en tout pour un produit dont le fil *est* l'application entière, et les trous tombent exactement là où la promesse se joue — les neuf états d'échec, le vivier vide qui couvre 55 % des recherches, les deux statuts de rencontre que le PRD exige et que la spine a oubliés, et le message d'alerte différée, seul texte du produit lu hors du produit. Deuxième constat, plus grave encore : là où l'honnêteté est écrite, elle l'est parfois en langue administrative (« Lieu non déterminé ») ou avec un adverbe qui ment (« pas **encore** confirmé »), et la spine affirme que « la personne le sait » à propos des profils d'amorçage alors qu'aucune phrase du produit ne le lui dit jamais.

**28 constats — 8 élevés, 14 moyens, 6 faibles.**

---

## 1. Tenue du vouvoiement

**Aucun glissement au tutoiement, nulle part.** Recherche exhaustive sur `EXPERIENCE.md`, `DESIGN.md` et les trois maquettes : zéro occurrence de « tu / ton / ta / tes / toi » en position de microcopie. Le seul tutoiement du corpus amont est dans `research-paysage.md`, qui décrit des concurrents et n'est pas de la copie produit. C'est un point fort à consigner.

**Aucun impersonnel maladroit non plus dans la prose.** Le bot parle toujours à la première personne (« Je cherche… », « Je vous propose plutôt 19 h », « Je n'arrive pas à… ») et s'adresse toujours à la deuxième du pluriel (« à votre niveau », « votre agenda Google », « Dites-moi ce que vous cherchez »). C'est tenu dans 100 % de la prose écrite.

**Mais la règle de marque porte sur les libellés, et elle n'est réalisée nulle part.** `DESIGN.md:224` — « Le vouvoiement est tenu partout, **y compris dans les libellés d'interface** » — et `DESIGN.md:364` — « Vouvoiement jusque dans les libellés de boutons ». Inventaire complet des libellés existants :

| Libellé | Où | Forme |
|---|---|---|
| « Envoyer » | maquettes, `aria-label` du bouton d'envoi | infinitif |
| « Retenir 19 h » | `key-recap-en-attente.html:32,83` | infinitif |
| « Garder 17 h » | `key-recap-en-attente.html:33,84` | infinitif |
| « Un autre jour » | `key-recap-en-attente.html:34` | groupe nominal |
| « Pourquoi ? » | `EXPERIENCE.md:96`, `DESIGN.md` Components | interrogatif nu |
| « nouveau message » | pastille | groupe nominal |
| « En attente » / « Confirmée » | pastilles de statut | participe / locution |
| « en cours » | marqueur `prefers-reduced-motion` | locution |
| « Retenue » / « Non retenue » | noms accessibles des cartes inertes | participe passé |

**Zéro libellé vouvoyé sur neuf.** La règle de marque la plus explicitement énoncée du produit — celle que le brief cite en premier — n'a aucune instance. Voir **É7**.

**Infinitif administratif :** « Retenir 19 h », « Garder 17 h », « Envoyer ». Il n'est pas fautif en soi, mais il devient une incohérence dès lors que les cartes de partenaires, à trois centimètres de là, portent la voix de la personne (« Anna », « Iris ») et que la spine exige que **tout ce qui se clique soit dicible** (`EXPERIENCE.md:147`). Personne ne dit « Retenir 19 h » à voix haute. Voir **É7** et **M3**.

---

## 2. Contamination par le chatbot de support

**Bilan : nulle part dans la copie effective.** Aucune occurrence de « Bonjour », « Oups », « Super », « Parfait », « Désolé », « Je comprends que… », « N'hésitez pas », d'emoji ou de point d'exclamation dans une phrase du bot. Les seules occurrences de ces formes dans les artefacts sont **dans la colonne « À éviter »** de `EXPERIENCE.md:66-75` et dans le paragraphe de repoussoir de `DESIGN.md:220` — c'est-à-dire à leur place. Le produit n'est pas contaminé.

Trois points de vigilance subsistent néanmoins :

- **L'accroche est le seul énoncé qui frôle la ligne.** « Dites-moi ce que vous cherchez. » (`key-fil-a-froid.html:20`) est structurellement le même acte de parole que « Comment puis-je vous aider ? » : une offre ouverte, émise par la machine, avant que la personne ait parlé. Elle est **sauvée par sa sous-ligne** — « Je trouve quelqu'un à votre niveau, ou je vous dis qu'il n'y a personne » — qui borne la compétence et annonce le refus, ce qu'aucun widget d'assistance ne fait jamais. Le couple tient ; il ne tiendrait plus si la sous-ligne disparaissait. À traiter comme **indissociable** dans la spine, ce qu'elle ne dit pas.
- **L'interdit d'emoji est écrit trop étroitement.** `EXPERIENCE.md:83` bannit « tout emoji **d'accueil** ». La lettre de la règle laisse passer un emoji de météo, de statut ou de sport, et surtout un emoji dans les messages sortants (e-mail, SMS), où la pente est la plus forte. Voir **M14**.
- **Le vrai risque de contamination est ailleurs : dans les trous.** Vingt-cinq chaînes sont écrites ; une trentaine de moments en attendent une. L'interface étant un LLM « dont la pente naturelle est de faire plaisir » (PRD, cité en `EXPERIENCE.md:160`), chaque état sans phrase arrêtée est un endroit où le modèle produira spontanément « Oups, une erreur est survenue ! » ou « Je comprends que ce soit frustrant ». **L'interdiction sans la formulation de remplacement ne protège rien.** C'est le fil rouge des constats **É3**, **É4** et **É5**.

---

## 3. La grammaire de l'honnêteté à l'épreuve

La spine énonce (`EXPERIENCE.md:164`) que l'inconnu s'écrit en italique **et en mots**, et que « tant qu'il existe une manière propre et lisible d'afficher *je ne sais pas*, l'implémentation n'a pas de raison de combler ». Les mots proposés ne tiennent pas toujours cette promesse.

**Non — « Lieu non déterminé » ne dit pas la même chose que « je ne sais pas encore où ».** « Lieu non déterminé » (`key-recap-en-attente.html:96`, et cité comme exemple canonique en `DESIGN.md:237`) est un participe passé négatif à la voix passive : c'est la langue d'un champ vide dans une base de données, pas celle d'un interlocuteur qui admet une ignorance. Personne n'a rien avoué ; le lieu s'est simplement *trouvé* non déterminé. La spine a résolu le problème **typographique** de l'inconnu (l'italique, la pleine lisibilité) et a laissé le problème **lexical** entier. Même diagnostic pour « Prévisions indisponibles », cité dans le même paragraphe de `DESIGN.md` — alors que la table Voice and Tone, vingt pages plus loin, écrit correctement le **même** état : « Je n'ai pas les prévisions aussi loin. Je peux revérifier en début de semaine. » Deux documents, deux registres, une seule valeur. Voir **É6**.

**Non, le produit n'enrobe pas quand il n'y a personne — quand il l'écrit.** « Personne à votre niveau au tennis le mardi. » est exemplaire : constat, pas d'excuse, pas de coussin, la mauvaise nouvelle d'abord. Mais c'est la **seule** phrase de refus écrite dans tout le corpus, et elle couvre un refus partiel. Le refus total — le vivier vide, 55 % des recherches, le climax du parcours 2 — n'a **pas une seule phrase rédigée**, ni dans la spine, ni dans une maquette. Voir **É3**.

### Profils d'amorçage : oui, la microcopie ment par omission

C'est le point le plus grave de l'audit, et il se joue en deux temps.

**Premier temps — l'adverbe.** La phrase canonique est « Anna est prévenue. Elle n'a pas **encore** confirmé. » (`EXPERIENCE.md:71` et `key-recap-en-attente.html:49,99`). « Pas encore » est un présupposé d'aspect : il pose la confirmation comme un événement à venir dont seule la date manque. Pour un profil d'amorçage — 86 profils sur 86 qui ne répondront jamais — c'est faux, et le produit le sait au moment où il l'écrit. La spine se contredit d'ailleurs elle-même : `EXPERIENCE.md:178` prescrit « Il écrit qu'elle est prévenue et **n'a pas confirmé** » — sans « encore ». Le PRD (FR-13) écrit « prévenu, pas encore de réponse ». Trois documents, trois formulations, et c'est la moins honnête qui est passée dans les maquettes. Voir **É1**.

**Second temps — l'omission.** `EXPERIENCE.md:130` affirme : « Un partenaire issu d'un profil d'amorçage reste en attente indéfiniment, **et la personne le sait**. » Aucune phrase du produit ne le lui dit. La carte est identique par décision (`EXPERIENCE.md:176`, à raison), le statut est identique par nature, le mot « en attente » est identique — **rien** ne distingue Anna-qui-ne-répondra-jamais d'Anna-qui-répondra-demain. La personne ne « sait » que si on le lui a écrit, et on ne le lui a écrit nulle part. La spine décrit ici un état de connaissance qu'elle n'a produit par aucun moyen. C'est la définition exacte du mensonge par omission, et il porte sur la contrainte que le PRD qualifie de « la plus structurante ». Voir **É2**.

La sortie n'est pas de badger les profils d'amorçage — cela romprait la règle « aucune mention de second rang ». Elle est de dire **la propriété générale du vivier**, une fois, au moment où le statut *en attente* apparaît. Reformulation en **É2**.

### Deux autres omissions

- **L'alerte différée expire au bout de 60 jours** (PRD FR-9) et rien dans la microcopie ne le dit. La spine écrit seulement « Aucune promesse de délai » (`EXPERIENCE.md:124`), ce qui règle la question du *délai de réponse* mais laisse croire que l'alerte est éternelle. Voir **M11**.
- **Le profil d'amorçage a un droit de retrait écrit** (« un moyen de ne plus jamais être contacté », PRD FR-14) ; l'utilisateur inscrit, qui est versé au vivier par une simple phrase déclarative (« Vous figurez maintenant dans le vivier »), n'en a aucun de rédigé. L'injoignable est mieux traité que l'inscrit. Voir **M12**.

---

## 4. Cohérence de registre

Le produit oscille, et les oscillations sont localisables.

- **Laconique puis bavard, à un message d'intervalle.** `key-recap-en-attente.html:40` : « C'est dans votre agenda Google. » — cinq mots, parfait. Dix lignes plus bas (`:50`) : « Vous figurez maintenant dans le vivier — l'ensemble des profils parmi lesquels je cherche. La prochaine personne qui cherchera un partenaire de tennis niveau intermédiaire le mardi vous trouvera. » — trente-quatre mots, deux idées, une incise définitionnelle, une relative longue. Les deux ne semblent pas écrits par la même voix. Voir **M6**.
- **La règle « une idée par message » (`EXPERIENCE.md:75`) est enfreinte dans chaque message long des maquettes** : `key-proposition-partenaires.html:29` (deux idées), `key-recap-en-attente.html:50` (deux idées), `:77` (trois idées). La règle est énoncée dans la spine et démentie par les trois artefacts censés la démontrer. Voir **M7**.
- **Technique contre familier.** « J'élargis sur le jour, à niveau égal… » (`key-proposition-partenaires.html:26`) emploie le vocabulaire interne de la spine — l'« élargissement » est un nom d'algorithme, pas un mot que la personne a en tête. Même chose pour « Je n'arrive pas à joindre les **données de terrains** » (`key-recap-en-attente.html:77`) : la personne n'a pas de données, elle a des terrains. Voir **M2** et **M10**.
- **Deux voix sur un seul champ de saisie.** L'étiquette masquée dit « Écrivez à Ex Aequo » (le bot à la troisième personne, registre système) ; le texte indicatif dit « Écrivez-moi » (le bot à la première personne, registre conversation). Un lecteur d'écran entend l'un, un œil lit l'autre. Voir **M5**.
- **Trois textes indicatifs différents pour le même champ**, sans qu'aucune spine n'en arbitre un : rien du tout (`key-fil-a-froid.html:28`), « Écrivez-moi » (`:50`, et les deux autres maquettes), « …ou dites-moi simplement un prénom » (`key-proposition-partenaires.html:51`). Le troisième est contextuel et excellent ; les deux autres sont des défauts non décidés. `DESIGN.md:340` ne dit que sa couleur. Voir **M4**.
- **Télégraphique contre phrase complète, dans les textes non visuels.** La région de statut écrit une phrase autonome — « Anna a confirmé. Mercredi 3 septembre, 19 h. » — pendant que l'`aria-label` du même récapitulatif écrit une liste de virgules : « Rencontre avec Anna, tennis, mercredi 3 septembre 19 h, lieu non déterminé, en attente ». Deux registres à deux lignes d'écart, pour le même lecteur. Voir **M8**.
- **Un mot, deux sens, dans le même parcours.** « Retenir 19 h » (bloquer un créneau) et « Anna, retenue » (choisie parmi trois) sont séparés par deux tours de parole. Voir **M3**.

---

## 5. Les messages d'échec

| État | Formulation proposée ? | Dit ce qui s'est passé ? | Dit quoi faire ? | Verdict |
|---|---|---|---|---|
| **Hors-ligne** | Non — seulement « une ligne d'état persistante dit que l'envoi attend le réseau » (`EXPERIENCE.md:136`) | — | — | **Manquant.** Comportement spécifié, mots absents |
| **Échec d'envoi** | Non — « marqué non envoyé, avec une action de réémission » (`:137`) | — | — | **Manquant.** Et « réémission » ne doit surtout pas atteindre le libellé |
| **Bot indisponible** | Non — « le bot dit qu'il ne peut pas répondre maintenant » (`:138`) | — | — | **Manquant.** La consigne décrit la phrase au lieu de l'écrire |
| **OAuth annulé** | Non — « rappelle en une phrase ce que la connexion débloquait » (`:139`) | — | — | **Manquant.** Bon réflexe (« sans reproche »), aucun mot |
| **OAuth refusé** | Non — « nomme l'échec sans jargon, propose l'autre fournisseur » (`:140`) | — | — | **Manquant.** Trois exigences, zéro rédaction |
| **Permission d'agenda refusée** | Non — « le bot le dit et propose de réessayer plus tard » (`:141`) | — | — | **Manquant.** C'est pourtant l'échec le plus anxiogène : la personne peut croire la rencontre perdue |
| **Ville inconnue** | Non — « demandée en prose avec le motif attaché » (`:126`) | — | — | **Manquant.** Le motif est exigé et jamais écrit |
| **Aucun lieu disponible** | Non — « le bot l'annonce et poursuit » (`:127`) | — | — | **Manquant.** Distinct de la panne de service, et confondu avec elle dans les maquettes |
| **Sport hors vivier** | Non (`:118`) | — | — | **Manquant** (état hors liste, relevé au passage) |
| **Vivier vide** | Non (`:123`, parcours 2) | — | — | **Manquant, et c'est 55 % des recherches** |
| **Service externe indisponible** | **Oui** — « Je n'arrive pas à joindre les données de terrains en ce moment. Je continue sans le lieu, vous pourrez me le redemander plus tard. » | Oui | Oui | **Le seul acquis.** Dit ce qui s'est passé, ce qui n'est pas perdu, ce qu'on peut faire. Réserve de vocabulaire : « données de terrains » (**M10**) |
| **Prévision hors portée** | **Oui** — « Je n'ai pas les prévisions aussi loin. Je peux revérifier en début de semaine. » | Oui | Oui | **Bon.** Modèle à généraliser |
| **Hors périmètre** | **Oui** — « Je ne sais faire que ça : trouver quelqu'un avec qui pratiquer. » | Oui | Implicite | **Bon** |
| **Rencontre déclinée** (PRD FR-13) | **Absent de la spine** — le statut n'existe pas | — | — | **Trou de spécification.** Voir **É8** |
| **Rencontre expirée** (PRD FR-13) | **Absent de la spine** | — | — | **Trou de spécification.** Voir **É8** |

**Bilan : trois formulations écrites sur quinze états d'échec ou d'absence.** Aucune des formulations existantes ne culpabilise, ne blâme la personne ni ne s'excuse — la discipline est bonne là où elle s'exerce. Mais douze états sur quinze laissent dans l'ignorance **par défaut**, ce qui est exactement le reproche que le produit adresse à ses repoussoirs. Reformulations complètes en **É4**.

---

## 6. Le message d'alerte différée

**Il n'est écrit nulle part.** `EXPERIENCE.md:48` en donne le cahier des charges — « Le message sortant porte le strict nécessaire — un partenaire correspond, pour quel sport — et **aucune donnée du partenaire** ; tout le reste se lit en revenant dans le fil » — et s'arrête là. `EXPERIENCE.md:50` assume que la surface n'est traversée par aucun parcours. Le résultat est qu'**aucune phrase n'existe** pour le seul texte du produit lu hors du produit.

C'est un manque de premier ordre pour trois raisons :

1. C'est le texte qui décide du retour. Si l'alerte différée est l'unique valeur produite par 55 % des conversations, ce courriel *est* la livraison.
2. C'est le seul texte affranchi du contexte du fil. Dans le fil, la voix est portée par tout ce qui précède ; dans une boîte de réception, entre deux infolettres, elle n'est portée que par elle-même — et c'est précisément là que la pente vers « Bonne nouvelle ! 🎾 » est la plus raide.
3. **Trois autres textes sortants sont dans le même cas et ne sont même pas nommés par l'expérience :** le message de sollicitation du partenaire (PRD FR-14 — le seul contact qu'un profil d'amorçage aura *jamais* avec le produit, donc le texte dont dépend toute la conversion du vivier), les e-mails de changement de statut (FR-13), et l'e-mail d'expiration d'alerte à 60 jours (FR-9). Le PRD en fixe les contraintes ; aucune spine UX n'en fixe les mots.

Rédactions proposées en **É5**.

---

## 7. Maquettes vs spines

| Point | Spine | Maquette | Verdict |
|---|---|---|---|
| Statut en attente | `EXPERIENCE.md:178` — « prévenue et **n'a pas confirmé** » | `key-recap-en-attente.html:49,99` — « n'a pas **encore** confirmé » | **Contradiction, élevée** (**É1**) |
| Valeur inconnue | `EXPERIENCE.md:164` — l'inconnu s'écrit « en mots » | `:96` — « Lieu non déterminé », participe passé passif | **Contradiction de registre, élevée** (**É6**) |
| Nom accessible d'une carte inerte | `EXPERIENCE.md:94` — « **préfixé** de son sort (« Anna, retenue ») » | `key-proposition-partenaires.html:68-70` — « Retenue » **suffixé**, après le méta | **Contradiction** (**M9**) |
| Nom accessible d'une carte active | `EXPERIENCE.md:201` — « commençant par le texte visible », exemple en prose | `key-proposition-partenaires.html:31-42` — le premier texte du bouton est l'étiquette de démonstration (« repos », « focus clavier », « survol au pointeur »), suivie de « Intermédiaire · mercredi, samedi » | **Contradiction** (**M9**) |
| Texte indicatif du champ | `DESIGN.md:340` — couleur seulement | Trois valeurs différentes | **Non arbitré** (**M4**) |
| Casse de la pastille | `EXPERIENCE.md:103,166` — *en attente*, minuscules | « En attente » / « Confirmée », capitale initiale | **Divergence faible** (**F2**) |
| Contre-proposition de jouabilité | `EXPERIENCE.md:102` — « porte toujours une contre-proposition » | Cadre nominal : trois boutons ; variante en panne : deux, « Un autre jour » disparaît sans raison | **Divergence faible** (**F5**) |
| Chiffres météo | Voice and Tone : « 34 °C en fin d'après-midi » ; PRD §UJ-1 : 19 h à **24 °C** | « 34 °C prévus à 17 h », 19 h à **26 °C** | **Divergence faible** (**F3**) |
| Phrase de proposition | `EXPERIENCE.md:69` s'arrête à « …à votre niveau. » | Ajoute « Voici leurs jours. » | **Divergence faible** (**F4**) |

---

## Constats par sévérité

### Élevés

- **É1 — « Pas encore confirmé » est un présupposé faux, et la spine le sait.** (`EXPERIENCE.md:71` · `mockups/key-recap-en-attente.html:49` et `:99`). L'adverbe « encore » pose la confirmation comme différée, alors que 86 partenaires sur 86 du vivier d'amorçage ne confirmeront jamais. `EXPERIENCE.md:178` prescrit déjà la bonne forme, sans « encore » ; c'est la mauvaise qui a été retenue dans les maquettes. *Correctif :* « **Anna est prévenue. Elle n'a pas confirmé.** » — retirer l'adverbe, et l'inscrire dans les interdits absolus de `Voice and Tone` au même titre que « réservé » : *ne jamais qualifier une absence de réponse d'un adverbe qui en promet une*.

- **É2 — « Et la personne le sait » : elle ne le sait pas, personne ne le lui a dit.** (`EXPERIENCE.md:130` et `:177`). Le produit sait qu'un partenaire peut être injoignable ; la carte, le statut et la phrase sont identiques dans les deux cas ; aucune microcopie ne porte l'information. C'est le mensonge par omission au cœur exact de la promesse. *Correctif :* une phrase, écrite **une seule fois**, à la pose du récapitulatif, qui énonce la propriété du vivier sans désigner Anna — ce qui préserve la règle « aucune mention de second rang » :
  > « Anna est prévenue. Elle n'a pas confirmé.
  > Une partie des personnes que je propose ne sont pas encore inscrites ici : elles peuvent ne jamais répondre. Votre créneau tient quand même, et le lieu aussi. »

  Et, à la reprise (parcours 3), pour ne pas laisser la personne en attente indéfinie sans issue :
  > « Anna n'a toujours pas répondu, et je ne peux pas vous dire si elle le fera. Je peux chercher quelqu'un d'autre pour ce créneau, si vous voulez. »

- **É3 — Le vivier vide n'a pas une phrase, et c'est 55 % du produit.** (`EXPERIENCE.md:123` · parcours 2, `:290-300`). L'état est décrit trois fois (« constat net, aucun nom inventé, aucune suggestion latérale ») et rédigé zéro fois, alors que le chemin heureux — 45 % — dispose de trois maquettes et d'une dizaine de phrases. *Correctif :*
  > « Personne ne fait de Pilates dans le vivier. Pas à un autre niveau, pas un autre jour : personne.
  > Je peux enregistrer votre demande et vous prévenir si quelqu'un s'inscrit. Il me faudra une adresse pour vous joindre.
  > Vous êtes la seule personne du vivier à faire du Pilates — le vivier, c'est l'ensemble des profils parmi lesquels je cherche. La deuxième, si elle vient, vous trouvera. »

- **É4 — Neuf états d'échec sur onze n'ont aucune formulation.** (`EXPERIENCE.md:118, 123, 126, 127, 136-141`). La spine décrit ce que le bot « dit » au lieu de l'écrire ; à l'implémentation, un LLM comblera, et il comblera avec la voix du chatbot de support. *Correctif — jeu complet :*

  | État | Formulation proposée |
  |---|---|
  | Hors-ligne | « Vous êtes hors ligne. Je garde votre message et je l'envoie dès que le réseau revient. » |
  | Échec d'envoi | Marque : *« Non envoyé »* · Action : « Renvoyer » · Ligne : « Ce message n'est pas parti. Il est toujours là, je n'efface rien. » |
  | Bot indisponible | « Je ne peux pas répondre en ce moment. La conversation reste là, vos rencontres aussi. Réessayez dans quelques minutes. » |
  | OAuth annulé | « Vous n'êtes pas connecté. Sans compte, je ne peux pas prévenir Anna : je n'aurais aucun moyen de vous joindre quand elle répondra. Le reste est intact. » *(puis se taire — ne pas redemander)* |
  | OAuth refusé | « Google n'a pas accepté la connexion, et je ne sais pas pourquoi de mon côté. Vous pouvez essayer avec Microsoft. Sans compte, vous pouvez continuer à chercher, à comparer les jours et à voir la météo — je ne peux simplement pas prévenir Anna. » |
  | Permission d'agenda refusée | « Vous n'avez pas donné l'accès en écriture : je n'écris rien dans votre agenda. La rencontre tient — Anna, mercredi 3 septembre, 19 h, au Petit-Port. Notez-la de votre côté. Vous pourrez me redemander de l'écrire plus tard. » |
  | Ville inconnue | « Dans quelle ville jouez-vous ? J'en ai besoin pour proposer un terrain et pour regarder la météo au bon endroit. Je ne vous le demanderai qu'une fois. » |
  | Aucun lieu disponible | « Je ne trouve aucun terrain de tennis à Nantes. Je continue sans lieu : vous pouvez retenir le créneau et convenir de l'endroit avec Anna. » · Récapitulatif : *« Lieu : je ne sais pas encore »* |
  | Sport hors vivier | « Le squash ne fait pas partie des onze sports que je connais. Je ne vais pas chercher pour rien. » |

  Deux règles transversales à inscrire dans `Voice and Tone` : **tout message d'échec dit ce qui n'est pas perdu** (c'est ce que fait déjà, bien, la panne de terrains) ; **aucun message d'échec ne s'ouvre sur une excuse** (l'interdit existe pour l'absence de résultat, pas encore pour la panne).

- **É5 — Le message d'alerte différée n'est pas écrit, ni aucun des trois autres textes sortants.** (`EXPERIENCE.md:48`, PRD FR-9, FR-13, FR-14). *Correctif — alerte différée :*
  > **Objet :** Quelqu'un joue au tennis à votre niveau
  >
  > Vous m'aviez demandé de vous prévenir si quelqu'un s'inscrivait au tennis à votre niveau. C'est arrivé.
  > Je n'en dis pas plus ici. Le reste est dans notre conversation.
  >
  > [ Reprendre la conversation ]
  >
  > Pour ne plus recevoir d'alerte sur cette demande : [se désinscrire].

  *Correctif — sollicitation d'un partenaire (FR-14), le seul texte qu'un profil d'amorçage verra jamais :*
  > « Vous ne me connaissez pas : votre nom figure dans les données de départ d'Ex Aequo, un service qui met en relation des joueurs de même niveau. Quelqu'un y cherche un partenaire de tennis, mercredi 3 septembre à 19 h, au Petit-Port, à Nantes. Vous pouvez accepter ou refuser ici : [lien]. Pour ne plus jamais recevoir de message : [lien]. »

  *Correctif — expiration d'alerte (FR-9) :* « Votre alerte au tennis niveau intermédiaire arrive au bout de ses soixante jours. Personne ne s'est inscrit. Je peux la reconduire : [reprendre la conversation]. »

  *Règles à graver pour tout texte sortant :* pas de salutation, pas d'emoji, pas de point d'exclamation, pas de prénom du partenaire, pas de jour ni de lieu dans l'alerte différée, une seule action, et un moyen d'arrêter.

- **É6 — L'inconnu est écrit en langue administrative, dans le document qui interdit précisément cela.** (`DESIGN.md:237` · `mockups/key-recap-en-attente.html:96`). « Lieu non déterminé » et « Prévisions indisponibles » sont des participes passés passifs : aucun locuteur, aucun aveu, aucune première personne. La spine a résolu la typographie de l'inconnu et abandonné son lexique. *Correctif — règle : **l'inconnu se conjugue.** Toute valeur inconnue s'écrit avec un verbe à la première personne, jamais en participe passé négatif :*

  | Ce que le produit ignore | À bannir | À écrire (en `{components.unknown-value}`) |
  |---|---|---|
  | Le lieu | « Lieu non déterminé » | *« Lieu : je ne sais pas encore »* |
  | La météo hors portée | « Prévisions indisponibles » | *« Je n'ai pas les prévisions aussi loin »* |
  | La ville | « Ville non renseignée » | *« Vous ne m'avez pas dit où »* |
  | L'heure | « Heure non définie » | *« L'heure reste à choisir »* |

  Corollaire pour les textes non visuels : l'`aria-label` du récapitulatif doit porter la même formulation, pas sa traduction administrative.

- **É7 — « Vouvoiement jusque dans les libellés de boutons » : règle énoncée deux fois, réalisée zéro fois.** (`DESIGN.md:224` et `:364` · tous les libellés listés en §1). Neuf libellés, neuf infinitifs ou groupes nominaux. Pire : les cartes de partenaires portent déjà la voix de la personne (« Anna »), et la spine exige que tout cliquable soit dicible (`EXPERIENCE.md:147`) — la règle a donc un modèle disponible qu'elle n'applique pas. *Correctif — séparer deux familles et l'écrire dans la spine :*
  - **Les boutons qui sont une réplique de la personne** portent la voix de la personne, parce qu'on doit pouvoir les taper mot pour mot : « **Va pour 19 h** » · « **Je garde 17 h** » · « **Un autre jour** » · « **Pourquoi ?** » · « **Anna** ». (Test de validité d'un libellé de choix : *puis-je le dire au bot à la place de cliquer ?* Si non, il est mal écrit.)
  - **Les commandes de l'appareil** — envoyer, renvoyer, revenir en bas — restent à l'infinitif : « Envoyer », « Renvoyer ». Elles ne s'adressent pas au bot, elles actionnent l'interface.
  - Et reformuler la règle de `DESIGN.md` en conséquence : *« Aucun libellé ne tutoie et aucun libellé n'anime ; tout libellé de choix est une phrase que la personne pourrait dire. »*

- **É8 — Deux statuts dans la spine, quatre dans le PRD : *déclinée* et *expirée* n'ont pas de mots.** (`EXPERIENCE.md:103` — « Deux valeurs seulement » — contre PRD FR-13, quatre statuts). Le PRD interdit explicitement de présenter un refus comme une absence de réponse ; la spine, faute de statut *déclinée*, n'a pas d'autre choix que de le faire. La grammaire de l'honnêteté est cassée là où elle coûte le plus. *Correctif :* deux pastilles de plus, avec leur mot écrit, dans une teinte neutre (le rose-rouge appartient à la jouabilité, l'ambre à *en attente*), et deux phrases :
  > *Déclinée* — « Anna a décliné. Mercredi 19 h est libre : je peux chercher quelqu'un d'autre. »
  > *Expirée* — « Mercredi est passé et Anna n'a pas répondu. Je laisse la rencontre dans le fil, pour mémoire. »

  Interdit à ajouter : *ne jamais écrire « pas encore de réponse » sur une rencontre déclinée.*

### Moyens

- **M1 — « Exactement à votre niveau » surpromet sur une donnée déclarative.** (`EXPERIENCE.md:69` · `key-proposition-partenaires.html:29,66` · récapitulatif « Intermédiaire, à votre niveau »). Le niveau est auto-déclaré (spine : « le niveau reste déclaratif en v1 »), et `research-niveau.md` documente une inflation de 0,5 à 1,0 point. « Exactement » est le seul adverbe du produit qui affirme une précision que la donnée n'a pas — dans un produit dont le nom même est une promesse d'égalité. *Correctif :* « En revanche Anna, Iris et Tessa **se déclarent au même niveau que vous**. Voici leurs jours. » Et au récapitulatif : « Intermédiaire, **le niveau qu'elle annonce** ».

- **M2 — « J'élargis sur le jour » est un nom d'algorithme.** (`key-proposition-partenaires.html:26`). L'« élargissement » est le vocabulaire de la spine, pas celui de la personne. *Correctif :* « Personne ce mardi-là. Je regarde les autres jours, sans changer de niveau… »

- **M3 — « Retenue » désigne deux choses dans le même parcours.** (`EXPERIENCE.md:94` — « Anna, retenue » — contre `key-recap-en-attente.html:32` — « Retenir 19 h »). Choisir une personne et bloquer un créneau ne sont pas le même acte. *Correctif :* réserver « retenir » au créneau, et pour les cartes : *« Anna, choisie »* / *« Iris, non choisie »*.

- **M4 — Trois textes indicatifs de champ, aucun arbitré.** (aucun, « Écrivez-moi », « …ou dites-moi simplement un prénom »). *Correctif :* poser la règle dans `EXPERIENCE.md.Component Patterns` — **le texte indicatif est contextuel quand le tour précédent propose un choix, et vide sinon.** Soit : rien à froid (l'accroche fait le travail), « …ou dites-moi simplement un prénom » après des cartes, « …ou dites-moi une autre heure » après la jouabilité. Un texte indicatif générique n'apprend rien et ressemble à un widget.

- **M5 — Deux voix sur le même champ de saisie.** Étiquette masquée « Écrivez à Ex Aequo » (le bot vu de l'extérieur) contre texte indicatif « Écrivez-moi » (le bot qui parle). *Correctif :* aligner l'étiquette sur la voix de la conversation — « **Votre message à Ex Aequo** » — qui nomme la destination sans faire parler le système à la troisième personne.

- **M6 — Rupture de longueur entre deux messages voisins.** (`key-recap-en-attente.html:40` puis `:50`). *Correctif :* scinder le message long en deux tours d'une idée chacun : « Vous êtes maintenant dans le vivier — l'ensemble des profils parmi lesquels je cherche. » puis « Si quelqu'un cherche un partenaire de tennis à votre niveau, il vous trouvera. »

- **M7 — La règle « une idée par message » est démentie par les trois maquettes.** (`EXPERIENCE.md:75` contre `key-proposition-partenaires.html:29`, `key-recap-en-attente.html:50,77`). *Correctif :* appliquer la scission partout, ou assouplir la règle en « **une idée par message ; une phrase de conséquence est admise si elle tient en une ligne** » — mais choisir, car la spine et ses démonstrations ne peuvent pas se contredire.

- **M8 — Les textes non visuels ont deux registres.** Région de statut en phrase complète, `aria-label` du récapitulatif en liste de virgules. *Correctif :* écrire l'`aria-label` comme une phrase : « Rencontre avec Anna, tennis. Mercredi 3 septembre, 19 h, au Tennis Club de la Beaujoire. En attente. »

- **M9 — Le nom accessible des cartes contredit la spine sur deux points.** (`EXPERIENCE.md:94` et `:201` contre `key-proposition-partenaires.html:31-42,68-70`). Le sort est suffixé au lieu d'être préfixé ; les étiquettes de démonstration (« repos », « focus clavier », « survol au pointeur ») sont **dans** le bouton et ouvrent donc son nom accessible ; et le séparateur « · » de « Intermédiaire · mercredi, samedi » ne se prononce pas. *Correctif :* sortir les étiquettes de démonstration du `<button>`, et donner un nom accessible rédigé — « Anna, intermédiaire, disponible mercredi et samedi », puis « Anna, choisie » une fois le tour résolu.

- **M10 — « Les données de terrains » est du vocabulaire interne.** (`key-recap-en-attente.html:77`). La personne n'a pas de données. *Correctif :* « Je n'arrive pas à consulter les terrains de Nantes en ce moment. Je continue sans le lieu ; vous pourrez me le redemander plus tard. »

- **M11 — L'alerte expire à 60 jours et la microcopie ne le dit pas.** (`EXPERIENCE.md:124` contre PRD FR-9). « Aucune promesse de délai » règle la question de la réponse, pas celle de la durée de vie. *Correctif :* à la pose de l'alerte — « C'est enregistré. Je la garde soixante jours ; si personne ne s'inscrit d'ici là, je vous le dirai et vous pourrez la reconduire. » Cela ne promet aucun délai de réponse et ferme l'omission.

- **M12 — L'inscrit entre au vivier par une phrase déclarative et n'a aucun moyen écrit d'en sortir.** (`key-recap-en-attente.html:50` contre PRD FR-14, qui garantit ce droit aux profils d'amorçage). *Correctif :* ajouter la sortie à la même phrase — « Vous êtes maintenant dans le vivier. Dites-le-moi si vous voulez en sortir, je vous retire tout de suite. »

- **M13 — Le climax du parcours 2 affirme une certitude que le produit n'a pas.** (`EXPERIENCE.md:298` — « le prochain pratiquant de Pilates, lui, la trouvera »). Le produit sait qu'il n'y en a aucun. *Correctif :* « La deuxième personne, **si elle vient**, vous trouvera. » Le conditionnel coûte trois mots et sauve la seule phrase optimiste du parcours d'échec.

- **M14 — L'interdit d'emoji est écrit trop étroitement.** (`EXPERIENCE.md:83` — « tout emoji **d'accueil** » · `DESIGN.md:364` — « Emoji d'accueil »). *Correctif :* « **Aucun emoji, nulle part** — ni accueil, ni statut, ni météo, ni sport, ni dans les messages sortants. » Même traitement pour le point d'exclamation, dont l'interdit ne couvre aujourd'hui que « une phrase du bot » et laisse donc passer un objet de courriel.

### Faibles

- **F1 — « Je cherche au tennis » n'est pas idiomatique.** (`key-proposition-partenaires.html:25` · `EXPERIENCE.md:275`). On cherche *un partenaire de tennis*, on ne cherche pas *au tennis*. *Correctif :* « Je cherche un partenaire de tennis, mardi, niveau intermédiaire… »

- **F2 — Casse des pastilles.** Les spines écrivent *en attente* et *confirmée* en minuscules, les maquettes « En attente » et « Confirmée ». *Correctif :* trancher dans `DESIGN.md.Typography` (`label`) ; la capitale initiale est le bon choix pour une pastille isolée, mais elle doit être écrite quelque part.

- **F3 — Chiffres météo divergents.** PRD §UJ-1 : 19 h à 24 °C. Maquette : 26 °C. *Correctif :* aligner sur une valeur unique dans les trois documents — ce sont des données d'illustration, mais elles seront copiées telles quelles à l'implémentation.

- **F4 — « Voici leurs jours. »** apparaît dans la maquette et pas dans la citation de la spine (`EXPERIENCE.md:69`). *Correctif :* compléter la citation de `Voice and Tone`, la phrase est bonne.

- **F5 — « Un autre jour » disparaît dans la variante en panne** (`key-recap-en-attente.html:82-85`) alors que la spine exige toujours une contre-proposition. *Correctif :* rétablir le troisième bouton, ou dire pourquoi il tombe.

- **F6 — Les points de suspension des lignes d'étape** (« Je cherche… », « Je vérifie la météo de mercredi… ») empruntent l'indicateur de frappe des widgets de discussion, dans un produit qui interdit par ailleurs l'arrivée caractère par caractère (`EXPERIENCE.md:92`). *Correctif :* forme accomplie une fois l'étape franchie — « J'ai regardé la météo de mercredi. » — et suspension réservée à l'étape en cours. Cela renforce en prime la « trace vérifiable » de `La grammaire de l'honnêteté`.
