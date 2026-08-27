# Rapport de validation — Ex Aequo / Trouve-moi un partenaire

- **PRD :** `documentation/planning-artifacts/prds/prd-bmad-2026-08-26/prd.md` (`status: draft`)
- **Rubric :** `.claude/skills/bmad-prd/assets/prd-validation-checklist.md`
- **Relecteurs exécutés :** rubric qualité (`review-rubric.md`) · dérive PRD ↔ UX (`review-drift-prd-ux.md`)
- **Non exécuté :** adversarial produit
- **Exécuté le :** 2026-08-26T15:02:01Z
- **Note :** **Poor**

## Comment lire la note

La formule du gate donne *Poor* dès qu'un constat critique existe — il y en a cinq. Elle ne dit
pas que le PRD est mauvais : **aucune dimension n'est *thin* ni *broken***, cinq sont *adequate*
et deux sont *strong*. La note traduit un risque concentré sur quelques points localisés, pas une
faiblesse d'ensemble.

## Verdict global

**Qualité intrinsèque du PRD.** Le document tient largement au-dessus de la barre de ses enjeux :
une thèse assumée, des décisions prises et *justifiées par des chiffres tirés des données réelles*
(§5.2), des non-objectifs qui font un vrai travail (§8, §9), et une séparation exemplaire du
« comment » vers l'addendum. La différenciation revendiquée au §1 n'est pas du théâtre
d'innovation : elle est gagnée par une recherche qui a réellement passé le paysage en revue, et le
PRD nomme le pari comme un pari, y compris dans son interprétation défavorable. Le relecteur a
recalculé l'intégralité des chiffres du PRD contre `SportsProfiles.csv` — **tous exacts**.

**Ce qui est à risque** tient en trois points, tous localisés et tous réparables : une conséquence
testable est **factuellement fausse** contre le CSV qu'elle invoque (FR-8 / Pilates, vérifié) ; la
jouabilité — une section entière — exige une granularité horaire que le PRD exclut explicitement
deux fois ailleurs ; et la promesse centrale de UJ-1, « Anna est prévenue », n'est portée par
aucune FR, n'a aucun canal, et entre en collision frontale avec le garde-fou le plus structurant du
produit (§7, *Le bot n'invente rien*). Le document est prêt à être découpé en épiques une fois ces
trois points tranchés ; il ne l'est pas avant.

**Dérive vis-à-vis de l'UX.** Le travail UX est substantiellement fidèle. La dérive dominante n'est
pas un dépassement de mandat, c'est une **avance** : l'UX a tranché ce que le PRD laissait ouvert —
le nom du produit, le ton, la surface principale, le canal de notification, l'heure du rendez-vous —
et le PRD, resté en `draft`, n'a rien rattrapé. 11 constats sur 16 vont dans le sens « le PRD
rattrape ». Le PRD porte aujourd'hui plusieurs affirmations fausses pendant que les deux spines qui
en dérivent sont en `final`.

**Ce sur quoi les deux relecteurs convergent**, sans s'être lus : le **canal de notification**
(identifié au memlog, jamais porté au PRD, inventé en hypothèse par l'UX), **l'heure de la journée**
(exclue du périmètre deux fois, exigée par FR-10 et UJ-1, collectée par l'UX), et les **seuils de
jouabilité** (non fixés au PRD, chiffrés en dur dans une maquette). Trois trous du PRD que l'aval a
comblés seul. C'est le cœur du travail de reprise.

## Verdicts par dimension

| Dimension | Verdict |
|---|---|
| Decision-readiness | adequate |
| Substance over theater | adequate |
| Strategic coherence | adequate |
| Done-ness clarity | adequate |
| Scope honesty | **strong** |
| Downstream usability | adequate |
| Shape fit | **strong** |

## Décompte

| Sévérité | Rubric | Dérive | Total |
|---|---|---|---|
| Critical | 3 | 2 | **5** |
| High | 9 | 6 | **15** |
| Medium | 13 | 6 | **19** |
| Low | 5 | 2 | **7** |
| **Total** | **30** | **16** | **46** |

## Ce qui tient — à ne pas rouvrir

- **Les 13 FR ont chacune au moins une conséquence testable réelle**, plusieurs citant des données
  littérales vérifiables (FR-5 → Emma Leroy, FR-6 → Anna/Iris/Tessa, tous deux vérifiés).
- **Tous les chiffres du PRD sont exacts** après recalcul complet du CSV.
- **L'aller-retour de l'index des hypothèses §12 est complet** dans les deux sens.
- **Les identifiants** FR-1→13, UJ-1/2, SM-1→3, SM-C1/C2 sont contigus, uniques, sans doublon, et
  toutes les références croisées résolvent.
- **La différenciation est gagnée par la recherche**, pas décorative.
- **Le glossaire §3 est tenu à la lettre par l'UX**, jusqu'à en faire des interdits de microcopie.
- **Le vivier vide comme état principal** (55 %) a survécu intact jusque dans l'UX.

## Constats par sévérité

### Critical (5)

**[Done-ness] — FR-8 : la conséquence Pilates est fausse contre le CSV qu'elle invoque** (§5.2 FR-8, §2.3 UJ-2)
Vérification faite sur `SportsProfiles.csv` : Sarah André (Pilates, Mardi;Jeudi, Débutant) est dans
le vivier, donc une demande de Pilates renvoie bien un nom dans 9 cas sur 21 (tous les Débutants
quel que soit le jour, plus les Intermédiaires mardi et jeudi via FR-7). Le récit UJ-2 et sa
conséquence testable confondent la protagoniste avec un profil d'amorçage homonyme.
Fix : renommer la protagoniste de UJ-2, et remplacer la conséquence par un cas réellement vide —
un sport absent du vivier, ou « Pilates, Avancé », vide tous les jours et après élargissement.

**[Done-ness] — L'heure est exclue du périmètre mais requise par la jouabilité** (FR-2, FR-10, §2.3 UJ-1, §9)
Le PRD exclut deux fois l'heure de la journée et lui fait jouer un rôle central deux fois. Sans
granularité horaire, FR-10 ne peut ni évaluer un créneau ni « proposer un autre moment ».
Fix : distinguer les deux usages — l'heure n'est **pas** une contrainte d'appariement mais **est**
fixée en fin de conversation, et c'est celle-là que la jouabilité évalue. Une phrase au §5.3 et un
amendement au §9.

**[Decision-readiness] — « Anna est prévenue » n'est adossé à aucune exigence** (§2.3 UJ-1, §7, §11.6)
Le récit affirme que le partenaire est prévenu, la question ouverte 6 demande si un message part
vraiment, et aucune des 13 FR ne couvre la notification du partenaire — pendant que le §7 interdit
d'annoncer ce qui n'a pas eu lieu.
Fix : trancher la question 6 maintenant, puis créer une FR « prévenir le partenaire » (déclencheur,
canal, contenu, et ce que le bot peut dire si rien ne part) — ou réécrire UJ-1 en « Anna sera
contactée si… ».

**[Dérive] — La maquette fixe un seuil de jouabilité que le PRD déclare non fixé** (FR-10 §5.3 ↔ `key-recap-en-attente.html` l. 137, 188)
« Au-dessus de 32 °C », écrit deux fois, sans aucune source dans le PRD, l'addendum ou les
recherches — et le memlog UX affirme le contraire de sa propre maquette. La valeur écrite dans une
maquette est celle qu'un développeur recopiera.
Fix : trancher les trois seuils dans FR-10 et fermer §11.2, puis corriger la maquette. À défaut,
neutraliser la phrase pour qu'aucun nombre non décidé ne circule.

**[Dérive] — La maquette montre Anna, profil d'amorçage, en train de confirmer** (§3, §4, FR-13 ↔ `key-recap-en-attente.html` l. 118 vs 222)
Le glossaire dit « ne répond jamais » ; la maquette l'écrit ligne 118 puis la fait confirmer ligne
222. Le besoin de montrer l'état confirmé est légitime, mais pas illustré par Anna.
Fix : remplacer Anna par une partenaire inscrite dans le troisième cadre, et noter à `State
Patterns` que l'état *confirmée* est « jamais atteignable depuis un profil d'amorçage ».

### High (15)

**[Substance] — Quatre NFR, zéro borne** (§6)
Latence, robustesse, reprise et responsive énoncées sans seuil, sans fenêtre, sans comportement par
service. Aucune n'est vérifiable.
Fix : un chiffre chacune.

**[Strategic] — Aucun critère ne teste le pari central** (§10 vs §1)
La thèse est que la conversation est la bonne forme ; SM-1 à SM-3 mesurent la complétude, la
non-invention et le rattrapage, jamais la forme.
Fix : un SM sur la conversation — nombre de tours avant la première proposition, ou part de
sessions où l'utilisateur réclame une liste, une carte ou un filtre.

**[Strategic] — SM-3 est infalsifiable alors que la donnée fournit le seuil** (§10)
« Dans la grande majorité des cas » : ni échantillon, ni seuil, ni définition d'« utilisable », alors
que le §5.2 a déjà le chiffre (89 %).
Fix : « ≥ 85 % des 127 combinaisons sans résultat exact produisent au moins un candidat du niveau
exact demandé ».

**[Decision-readiness] — Le canal de notification n'existe nulle part** (§6, FR-9, FR-13)
Le memlog acte qu'il faut « un autre canal » ; jamais porté au PRD. FR-9 et FR-13 sont suspendus
dans le vide.
Fix : une NFR ou une conséquence de FR-4 nommant le canal (e-mail du compte) et le délai attendu.

**[Decision-readiness] — Rejoindre le vivier est imposé, pas consenti** (FR-3, §2.3, §7)
UJ-1 le dit franchement (« sans l'avoir demandé ») ; le §7 promet pourtant que le bot dit pourquoi
à chaque demande. Ici il ne demande pas, il inscrit. Information ≠ opt-in.
Fix : trancher explicitement, l'écrire dans FR-3, et taguer si c'est une inférence.

**[Done-ness] — FR-13 : conséquence inexerçable en v1** (§5.5, §9)
« Passe à *confirmée* quand celui-ci accepte » suppose un parcours d'acceptation que le §9 déclare
hors périmètre.
Fix : marquer v2, ou spécifier le minimum côté partenaire (un lien d'acceptation à usage unique).

**[Done-ness] — FR-3 : la déduplication n'a aucun identifiant sur lequel s'appuyer** (§5.1)
« Pas deux profils pour la même personne » alors que FR-4 garantit qu'aucun compte n'existe encore.
Un visiteur anonyme qui revient est indiscernable d'un nouveau.
Fix : nommer la clé d'identité et le moment où elle existe, et rattacher la conséquence à FR-4.

**[Done-ness] — FR-8 n'a aucune conséquence positive** (§5.2)
Ses trois conséquences sont des interdictions. Rien ne dit ce que la réponse **contient**, alors que
c'est le comportement majoritaire du produit à 55 %.
Fix : une conséquence sur le contenu du refus — sport et jour tentés, ce qui a été élargi,
enchaînement sur l'alerte FR-9.

**[Downstream] — Le profil d'un utilisateur inscrit n'est jamais défini** (§3, FR-4, FR-9, FR-11)
Le glossaire donne les champs du profil d'amorçage et laisse l'autre population sans schéma, alors
que trois FR lui ajoutent des attributs. L'aval reconstruira ce modèle de mémoire, différemment
à chaque fois.
Fix : symétriser l'entrée du §3 — champs hérités, ville (FR-11), moyen de contact (FR-4/FR-9), et
ce qui reste vide.

**[Dérive] — Les cartes de la maquette contredisent les données d'amorçage** (§7 + CSV ↔ `key-proposition-partenaires.html`)
Le CSV dit `Iris … Lundi;Mercredi` et `Tessa … Lundi;Samedi` ; la maquette affiche « samedi,
dimanche » et « lundi, jeudi ». C'est l'écran censé prouver que le bot n'invente rien.
Fix : recopier les jours du CSV. Coût nul.

**[Dérive] — Le PRD affirme toujours que le téléphone est l'usage principal** (§6 ↔ `EXPERIENCE.md` §Foundation)
L'UX a pivoté desktop-first et l'a tracé ; l'amont n'a pas suivi. Un architecte qui lit le PRD
d'abord dimensionnera pour le mobile.
Fix : réécrire la NFR *Responsive* — le PC d'abord, le mobile à parité fonctionnelle complète.

**[Dérive] — Le produit a un nom, décidé en UX, absent du PRD** (frontmatter ↔ memlog UX + `DESIGN.md`)
« Ex Aequo » est devenu structurel côté UX et n'existe nulle part côté PRD. Les deux moitiés de la
chaîne ne partagent aucun nom de produit.
Fix : porter « Ex Aequo » dans le `title` du PRD et retirer « titre de travail ».

**[Dérive] — L'heure du rendez-vous : le PRD l'exclut, l'UX la collecte** (FR-2 + §9 vs FR-12 + UJ-1 ↔ Key Flows étape 8)
Même trou que le constat critical côté rubric, vu depuis l'aval : l'UX a comblé avec « l'heure se
décide ici, et c'est la jouabilité qui l'amène ». La réponse est bonne et doit être adoptée.
Fix : voir le constat critical correspondant.

**[Dérive] — Le canal de notification est inventé en UX alors que le PRD savait qu'il manquait** (FR-9, FR-13 ↔ `EXPERIENCE.md` §IA)
L'UX pose l'hypothèse de l'e-mail récupéré à la connexion Google/Microsoft — honnêtement balisée,
mais c'est une capacité produit et une intégration tierce.
Fix : nommer le canal dans FR-9, et ajouter la ligne au tableau des intégrations de `addendum.md`
(aujourd'hui : agenda, météo, terrains — pas d'e-mail sortant).

**[Dérive] — « Trois candidats au maximum » : un plafond sans règle de sélection** (FR-6 ↔ Component Patterns)
Un plafond produit une troncature, et une troncature sans règle d'ordre est une décision produit
laissée au hasard de l'implémentation. Petit sur 86 profils, plus du tout quand le vivier grossit.
Fix : une conséquence testable dans FR-6 — critère d'ordre, et comportement au-delà de trois.

### Medium (19)

**[Decision-readiness] — Le modèle à deux populations en produit trois** (§3, §4, FR-3, FR-4)
L'utilisateur enregistré mais sans compte n'est ni un profil d'amorçage ni un utilisateur inscrit
joignable. Le glossaire affirme le contraire.
Fix : conditionner FR-3 à l'existence d'un moyen de contact, ou ajouter la troisième population au §3.

**[Substance] — FR-10 n'a pas de seuil et le sait** (§5.3)
Tant que les seuils manquent, la conséquence testable centrale de FR-10 est un adjectif.
Fix : poser trois seuils provisoires maintenant — un seuil faux est corrigeable, un seuil absent ne
l'est pas.

**[Substance] — La réponse à la cause de mort n°1 n'est jamais formulée** (§1, §4, §5.1)
Le vivier amorcé et l'inscription-par-conversation sont les deux moitiés d'une même réponse au
problème de densité, jamais rapprochées. La meilleure idée du document est dispersée.
Fix : une phrase au §4 ou au §1 nommant la conversation-inscription comme mécanisme de croissance
du vivier.

**[Strategic] — SM-1 revendique une couverture qu'il n'a pas** (§10)
« Valide FR-1 à FR-13 » : UJ-1 n'exerce ni FR-7, ni FR-8, ni FR-9 hors cas limite, ni la transition
de FR-13.
Fix : restreindre la revendication et ajouter un SM adossé à UJ-2, qui couvre le cas majoritaire.

**[Strategic] — Les deux contre-métriques ne sont pas observables** (§10)
« À ne pas optimiser » sans borne ni mesure : rien ne permettra de dire qu'elles ont été violées.
Fix : une borne à SM-C2 (tours avant la première proposition) et une observable à SM-C1 (part des
mises en relation obtenues via FR-7).

**[Done-ness] — FR-7 est permissif, donc satisfaisable en ne faisant rien** (§5.2)
« Le bot **peut** proposer un niveau adjacent » : une implémentation qui ne descend jamais respecte
l'exigence.
Fix : énoncer l'obligation et sa condition de déclenchement, ou assumer que c'est une autorisation
et le dire.

**[Done-ness] — FR-9 est sans bornes** (§5.2)
Durée de vie d'une alerte, critère de déclenchement, nombre d'alertes simultanées, comportement si
le profil correspondant est un profil d'amorçage : rien n'est fixé.
Fix : au minimum le critère de déclenchement et une durée de validité.

**[Done-ness] — FR-11 est dans le périmètre MVP avec une source de données non tranchée** (§5.4, §9, addendum)
L'addendum note « Terrains : non tranché ». La seule branche garantie atteignable est « le bot dit
qu'il n'a pas de donnée ».
Fix : une question ouverte ou un `[NOTE FOR PM]` au §5.4.

**[Scope] — Un garde-fou contredit une question ouverte** (§7 vs §11.6)
Le §7 affirme comme acquis que « le bot les nomme et les contacte » pendant que la question 6
demande si un SMS part réellement.
Fix : aligner — soit le §7 devient conditionnel, soit la question 6 se ferme.

**[Scope] — L'inscription automatique au vivier n'est pas taguée** (§2.3 UJ-1, FR-3)
Que l'utilisateur accepte d'être rendu trouvable par des inconnus au seul motif qu'il a parlé au bot
est une inférence, mise en avant comme un bénéfice.
Fix : `[ASSUMPTION: l'inscription au vivier est automatique et signalée, non soumise à acceptation]`
+ entrée au §12.

**[Scope] — L'addendum et le PRD divergent sur le niveau** (addendum, §9, §11.5)
L'addendum annonce un niveau qui se corrige avec l'usage et s'affiche en fourchette ; le PRD fait
l'inverse. Un des deux est périmé et l'aval ne saura pas lequel.
Fix : corriger le paragraphe de l'addendum.

**[Downstream] — « Candidat » et « créneau » manquent au glossaire déclaré contraignant** (§0, §3)
7 et 12 occurrences, y compris dans les conséquences testables de FR-5, FR-6, FR-8 et FR-10.
Fix : deux entrées au §3, ou remplacement par les termes déjà définis.

**[Downstream] — Trois étiquettes pour le même fichier** (§0, §2.3, §3, §4, §5.2)
« Données d'amorçage », « jeu d'amorçage » et « les 86 profils » dans cinq sections.
Fix : n'en garder qu'une, celle du glossaire.

**[Dérive] — FR-4 et UJ-1 se contredisent dans le PRD ; l'UX a tranché en silence** (FR-4 vs UJ-1)
FR-4 dit que retenir un partenaire déclenche le compte ; UJ-1 le place après la validation du
créneau. L'UX a tranché dans le bon sens, sans trace.
Fix : « **Valider un créneau avec un partenaire** déclenche la demande de compte ».

**[Dérive] — La question ouverte n° 3 est fermée en UX, mais le PRD la liste toujours** (§11.3, UJ-1/UJ-2)
L'UX a arrêté le vouvoiement ; le PRD dit le ton « pas discuté » et fait parler le bot en tutoiement.
Fix : fermer §11.3 en renvoyant à `EXPERIENCE.md §Voice and Tone`, et réécrire au vouvoiement les
répliques de UJ-1 et UJ-2.

**[Dérive] — La deuxième demande d'une personne déjà inscrite n'existe nulle part** (FR-3 ↔ State Patterns)
Ni le PRD ni l'UX ne disent ce que devient la première demande quand une seconde arrive, ni si un
profil porte plusieurs sports.
Fix : arbitrage, puis une conséquence testable en FR-3 et une ligne d'état UX.

**[Dérive] — Le contenu de l'événement d'agenda exigé par FR-12 n'est spécifié nulle part côté UX** (FR-12)
La seule phrase du dossier UX sur le contenu de l'événement est une interdiction. C'est pourtant la
seule chose du produit qui survit hors du fil.
Fix : une entrée `Component Patterns` énumérant le contenu et la microcopie du titre.

**[Dérive] — L'UX promet une persistance du fil que la NFR du PRD ne couvre pas** (§6)
Le PRD borne la reprise à l'inscrit ; l'UX ne réinitialise jamais le fil, même sans compte. Identité
anonyme persistante, rétention, et une question de vie privée que le §7 n'aborde pas.
Fix : préciser dans la NFR ce qui persiste pour un visiteur sans compte, et combien de temps.

**[Dérive] — Les étapes narrées sont promues en garantie produit** (§6 latence ↔ La grammaire de l'honnêteté)
Un signe de vie décoratif et une trace fidèle des appels d'outils ne sont pas la même exigence : la
seconde contraint l'architecture agentique.
Fix : une phrase au §7 (*Le bot n'invente rien*), plus une note d'orchestration dans `addendum.md`.

### Low (7)

**[Done-ness] — « Niveau adjacent » n'est pas défini** (§3, FR-7)
Le terme porte toute la logique de FR-7, le glossaire s'arrête aux trois valeurs. Fix : une ligne au §3.

**[Scope] — Aucun `[NON-GOAL for MVP]` inline** (tout le document)
Les omissions sont concentrées en §8 et §9 ; aucune n'est signalée là où elle pourrait être
silencieusement supposée (§5.4 : le produit ne réserve rien ; §5.5 : aucune écriture dans l'agenda
du partenaire). Fix : deux callouts inline, ou rien si le regroupement est assumé.

**[Downstream] — Collision de prénom entre une protagoniste et un profil d'amorçage** (§2.3 UJ-2, CSV)
Deux Sarah piégeront toute génération automatique de scénarios de test. Fix : des prénoms de
protagonistes absents du CSV.

**[Downstream] — « Rendez-vous », « rencontre » et « créneau » alternent au §5.5**
Le glossaire ne définit que *rencontre*. Fix : uniformiser.

**[Shape fit] — Écart au format convenu** (tout le document vs memlog)
Cible actée à ~2 pages, document livré à ~10. Le surplus est majoritairement de la substance.
Fix : si compression il doit y avoir, comprimer le §6 et le §7, pas le §4 ni le §5.2.

**[Dérive] — Le droit de passer outre une alerte de jouabilité est décidé en UX** (FR-10 ↔ State Patterns)
« Le bot informe, il n'interdit pas » est une règle produit sur le seul sujet de santé du PRD.
Fix : une conséquence testable en FR-10.

**[Dérive] — L'état « demande incomplète » oublie le jour** (FR-2 ↔ State Patterns)
FR-2 extrait sport, jours et niveau ; l'état UX ne se déclenche que sur sport ou niveau.
Fix : « Sport, jour ou niveau manquant ». Deux mots.

## Notes mécaniques

### Rubric qualité

- **Chiffres vérifiés contre `SportsProfiles.csv`** (recalcul complet) : 86 profils ✓ ; 11 sports ✓ ;
  231 combinaisons ✓ ; 127 vides soit 55 % ✓ ; élargissement du jour récupère 113 des 127 soit
  89 % ✓ ; Emma Leroy unique sur Tennis/Mardi/Débutant ✓ ; Anna, Iris et Tessa sont exactement les
  trois Tennis/Intermédiaire ✓.
- **Précision de reproductibilité (§5.2).** « Relâcher le niveau en conservant le jour n'en récupère
  que 46 (36 %) » n'est vrai qu'en se limitant aux niveaux **adjacents**, conformément à FR-7. Sans
  cette contrainte, le chiffre est 61 (48 %). La phrase ne dit pas « adjacent » : qui referait le
  calcul croirait à une erreur.
- **Nuance sur les 231 combinaisons.** Le décompte est uniforme (11 × 7 × 3) et non pondéré par la
  demande réelle. « 55 % ne renvoient aucun candidat » est un fait sur la grille, pas une prévision
  du taux d'échec vécu. Une incise d'une ligne mettrait le chiffre à l'abri.
- **Aller-retour de l'index §12 : complet.** Deux `[ASSUMPTION]` inline, exactement deux entrées,
  correspondance exacte dans les deux sens.
- **Identifiants.** FR-1→13, UJ-1/2, SM-1→3, SM-C1/C2 : contigus, uniques, sans doublon. Toutes les
  références croisées internes résolvent.
- **Titre.** « Trouve-moi un partenaire » est marqué « titre de travail, à confirmer » au §0 mais ne
  figure pas parmi les questions ouvertes du §11, qui recense des points bien moins ouverts.
- **Sections requises.** Rien ne manque. L'absence de section persona autonome est conforme à
  l'entrée Journey-led et n'est pas comptée comme un manque.

### Dérive du glossaire — terme par terme

Les dix termes du §3 sont tenus côté UX. Trois glissements mineurs, aucun bloquant :

- « la personne » côté UX pour désigner le visiteur, là où le PRD dit « l'utilisateur ». Le choix est
  juste mais il n'existe pas au glossaire.
- §6 « demandes en cours » → UX « **rencontres et alertes** en cours ». Écart de couverture qui se lit
  comme un synonyme.
- « Microsoft » (identité) vs « Outlook » (agenda) cohabitent sans qu'aucun document ne l'écrive.

### Traçabilité côté UX

- `EXPERIENCE.md` ne cite nommément que FR-4, FR-9 et FR-13. Les dix autres FR n'ont aucune trace :
  la vérification de couverture est manuelle et le restera.
- UJ-2 n'est jamais nommé côté UX, alors que le parcours 2 le réalise fidèlement.
- Aucune référence FR/UJ dans `DESIGN.md` ni dans les maquettes. Aucun identifiant fantôme non plus.

### Liens et statuts

- Les quatre `sources:` des frontmatters UX résolvent. Le `.memlog.md` du run PRD est déclaré hérité
  mais absent des `sources:` — c'est pourtant le seul document où vivent plusieurs décisions produit.
- **Asymétrie de statut :** `prd.md` en `draft`, `EXPERIENCE.md` et `DESIGN.md` en `final`. Le
  document amont est moins à jour que ceux qui en dérivent. Aucun lien du PRD ne pointe vers l'UX.
- « Ex Aequo » n'apparaît nulle part côté PRD, « Trouve-moi un partenaire » nulle part côté UX.

### Résidus et menues erreurs

- Résidu intra-UX du pivot desktop : `EXPERIENCE.md` §Responsive & Platform énonce encore « Frappe au
  vol et Échap arment le champ » alors qu'`Interaction Primitives` déclare la règle **retirée**.
- Composant non déclaré : la rangée de trois boutons de réponse de la maquette 3 ne correspond à
  aucune entrée de `Component Patterns`, et ressemble aux puces de réponse rapide que
  `Inspiration & Anti-patterns` rejette comme interface dominante.
- Date fausse dans la maquette 3 : « Mercredi 3 septembre » — le 3 septembre 2026 est un **jeudi**.

## Fichiers de relecture

- `review-rubric.md` — relecture qualité complète, sept dimensions
- `review-drift-prd-ux.md` — relecture complète de la dérive PRD ↔ UX
- *(adversarial produit : non exécuté)*
