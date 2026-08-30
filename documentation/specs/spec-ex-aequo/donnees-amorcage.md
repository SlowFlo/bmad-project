# Données d'amorçage — Ex Aequo

Companion de [SPEC.md](SPEC.md). Le fichier, ses propriétés contractuelles, les chiffres sur lesquels reposent les règles du produit, et les pièges à connaître avant de montrer le produit.

**Fichier source :** [`SportsProfiles.csv`](../../planning-artifacts/prds/prd-bmad-2026-08-26/SportsProfiles.csv) — 86 profils, chargés en base au premier lancement.

## Ce que le fichier est

86 personnes qui n'ont jamais entendu parler du produit. Elles ont un prénom, un nom, un numéro de téléphone, un sport, des jours disponibles et un niveau — et rien d'autre : pas de compte, pas d'adresse électronique, pas de ville. Elles peuplent le vivier pour qu'il ne soit pas vide au démarrage.

**C'est du décor, pas de la densité.** Le diagnostic vient de la recherche — un matcher vide meurt — mais **pas ce remède** : charger des profils fictifs ne figure dans aucune des quatre stratégies d'amorçage réellement observées. Le pari du produit est que la friction nulle de la conversation-inscription convertisse des chercheurs en profils assez vite pour que le décor cède la place. Ce pari n'est validé par aucune source.

**Les 86 personnes sont fictives, et leurs numéros aussi.** Tous appartiennent à la plage `+336 39 98 XX XX`, réservée par l'ARCEP aux œuvres de fiction et garantie non attribuée à un abonné ([décision ARCEP, art. 2.5.12](https://www.legifrance.gouv.fr/jorf/article_jo/JORFARTI000037263033)). Les 86 profils portent `+3363998 0001` à `+3363998 0086`, uniques et dans l'ordre du fichier.

**C'est une propriété dont le produit dépend** : CAP-13 envoie de vrais SMS, et les données d'amorçage doivent être incapables d'en faire parvenir un à quelqu'un. Le filtre de destinataire lit cependant la **provenance enregistrée dans le modèle**, jamais le préfixe, pour que la règle survive à un futur amorçage par d'autres données.

> **Asymétrie de consentement, neutralisée mais pas résolue.** Un utilisateur inscrit choisit de donner son numéro ; un profil d'amorçage a déjà le sien dans les données et recevrait un SMS sans l'avoir demandé. Le fait que ces numéros soient fictifs supprime le dommage, pas le principe. **À rouvrir impérativement avant tout amorçage par des données réelles.**

## Les chiffres sur lesquels reposent les règles

La grille compte **231 combinaisons** : 11 sports × 7 jours × 3 niveaux, comptées uniformément.

| Fait | Valeur | Ce qu'il justifie |
|---|---|---|
| Combinaisons sans candidat exact | **127**, soit 55 % | Le comportement principal n'est pas le refus, c'est l'élargissement et son explication |
| Récupérées en relâchant le jour, niveau conservé | **113**, soit 89 % | Le plafond de SM-3, dont le plancher est fixé à 85 % |
| Résidu réellement vide | **14**, soit 6,1 % | Toutes du Pilates. Le refus total est un cas rare |
| Ce qu'un élargissement au niveau voisin aurait récupéré | 46, faisant tomber le résidu à 3,0 % | Les **3,1 points** refusés en connaissance de cause : ils correspondent tous à *Pilates Intermédiaire* |
| Profils d'amorçage ne déclarant que deux jours | **83 sur 86** | Le jour est le facteur limitant, donc le bon axe d'élargissement |
| Paires sport × niveau peuplées | **31 sur 33** | Les deux vides sont *Pilates Intermédiaire* et *Pilates Avancé* |
| Médiane de profils par paire sport × niveau | **3** | Le plafond de trois candidats ne mord presque jamais aujourd'hui — raison d'écrire sa règle d'ordre maintenant, pendant qu'elle ne coûte rien |
| Paires comptant plus de trois profils | **4** | *idem* |
| Combinaisons ne renvoyant qu'un candidat | 19 % | *idem* |

> **Les 231 combinaisons ne sont pas pondérées par la demande réelle.** « 55 % ne renvoient aucun candidat » est un fait sur la grille, pas une prévision du taux d'échec que vivront les utilisateurs — lequel dépendra des sports réellement demandés.

## Conséquences pour le modèle de données

- Le schéma doit accueillir **plus de colonnes que le CSV n'en a**. Les profils d'amorçage arrivent avec des champs vides — ni adresse, ni secteur — là où les profils créés par conversation sont plus complets. **Nullabilité plutôt que valeurs par défaut trompeuses.**
- Il faut **distinguer un profil d'amorçage d'un utilisateur inscrit**, car le produit les traite différemment. Chaque profil porte sa population ; chaque numéro porte sa provenance (AD-11).
- Le champ « jours disponibles » est une liste de **jours de la semaine**, pas des dates ni des heures. L'heure appartient à la rencontre, jamais au profil.
- Le CSV est **mono-sport**, et le modèle l'est aussi — non plus par propriété de la donnée, mais par décision (CAP-3).
- Le chargement est **idempotent**, sur une clé naturelle stable : relancer l'application ne duplique pas les 86 profils. Après lui, la base est la source de vérité et le fichier n'est plus lu.

## Pièges de démonstration

Matière opérationnelle, pas une exigence : ce qu'il faut savoir avant de montrer le produit en direct.

- **Sarah André ne peut jamais trouver personne.** Seule pratiquante de Pilates des données d'amorçage : la prendre comme *demandeuse* ne produira jamais de candidat, quel que soit l'élargissement. Excellent cas pour montrer CAP-7, très mauvais pour le parcours nominal.
- **Le scénario « Tennis, mardi » est étroit.** Il ne renvoie qu'Emma Leroy, et seulement si le demandeur est Débutant. En Intermédiaire ou Avancé, le résultat exact est vide — soit exactement le scénario de UJ-1, où l'élargissement prend le relais. À choisir sciemment selon ce qu'on veut démontrer.
- **Le Pilates est le seul sport entièrement mort, et il l'est deux fois.** *Pilates Intermédiaire* et *Pilates Avancé* sont les deux seules paires sans aucun candidat des 33, soit 14 combinaisons sur 231.
- **Démontrer le cycle de vie demande deux demandeurs et deux jours.** Le blocage porte sur le jour de la rencontre seulement : retenir une personne un mercredi, puis la rechercher sur un autre de ses jours — où elle doit encore apparaître.
- **Démontrer l'abandon demande de préparer deux surfaces, pas une.** Le cinquième statut se voit dans le fil du demandeur *et* sur la page d'acceptation du partenaire, et **aucun message ne relie les deux** : garder le lien d'acceptation ouvert dans un second onglet et le recharger après l'abandon. Une démonstration qui ne montre que le fil laisse croire que le partenaire n'apprend jamais rien.
- **La moitié du vivier pratique un sport sans appariement en duel** — yoga, pilates, danse, natation, course à pied, escalade — et 34 profils font un sport d'équipe qui demanderait 10 à 30 personnes. C'est la décision « partenaire de pratique » plutôt qu'« adversaire » qui rend ces profils exploitables ; une démonstration qui ignorerait cette nuance donnerait l'impression d'un vivier absurde.
