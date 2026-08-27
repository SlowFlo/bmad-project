---
title: "Research digest — paysage des apps de mise en relation entre sportifs"
source: web research subagent
date: 2026-08-26
status: reference input (not PRD content)
---

# Qui fait déjà ça, et comment

## Le paysage, par nature réelle du produit

### Places de marché de réservation avec du matching greffé dessus

**Playtomic** (ES — padel/pickleball/tennis) : ~1,5 M utilisateurs actifs mensuels, 6 000 clubs dans 63 pays, 346 M€ de volume d'affaires, 29 M€ de revenu net, valorisation 250 M€ (mars 2025). Revenus = 5–15 % de commission sur réservation + SaaS pour les clubs (« Playtomic Manager ») + partenariats de marque (ex. Heineken 0.0). Découverte = parcourir une liste de « matchs ouverts » filtrée par club / horaire / bande de niveau, rejoindre un créneau, payer sa part, chat intégré ; plus un système de niveau façon Elo.

**Anybuddy** (FR/BE/ES/CH) : 600 000 joueurs, ~1 500 clubs, ~15 000 terrains, 15 M€ de volume de transactions en 2025 ; commission sur les réservations à l'heure, sans abonnement. Les « matchs publics » : tu réserves un terrain, tu le déclares public, tu fixes sport / niveau / places ; un algorithme pondère niveau + disponibilité + localisation ; notes communautaires ; chacun paie sa part.

**MATCHi** (pays nordiques) : SaaS de réservation pour salles + « Venue Communities » pour trouver des joueurs.

**Padel Mates** (SE) : réservation + « Game Finder » + suggestions de match par niveau et par centre.

**Ten'Up** (FFT, gratuit, 86 000 notes sur l'App Store) : gestion de licence et de classement + réservation de courts du club + recherche de partenaire + saisie des matchs officiels. Financé par la fédération, pas commercial.

### Opérateurs de parties côté offre

**GoodRec** : achète des créneaux sous-utilisés dans 250+ installations et opère 1 000+ parties par semaine dans 70+ villes (US/CA/EU) ; tu choisis sport + ville et tu viens. Ce n'est pas du matching, c'est de l'inventaire.

### Outillage de groupe / club — pas du matching

**Spond** (comms d'équipe et présences, gratuit, monétise les paiements), **Strava** Clubs/Events (découverte de sorties organisées), **Meetup** (piloté par l'organisateur, sur abonnement), **GoJoe** (bien-être en entreprise B2B).

### Vrais « sport buddy matchers » — tous sous-critiques

**Smatch** (80+ sports, CH/FR/UK) : ~6 000 utilisateurs actifs **au total**, Lausanne étant la plus grosse ville à 2 200. **Sportpartner** : 2,7★ sur 53 notes, messagerie derrière un paywall. **SportLync** (US) : « matching IA » sur niveau/localisation/dispos + fil social, freemium, ~170 000 téléchargements. Puis ConnectPlayers, PlayMate, SportBuddy.io, PoteSport, MeetSport, SportivUp (FR, très minces).

**Bvddy** — le « Tinder du sport », 1,5 M$ levés — **est mort**, faute d'avoir atteint une base active soutenable.

## 1. Le matching par niveau est-il le produit central ?

**Presque jamais.** C'est une fonctionnalité de rétention à l'intérieur d'une place de marché de réservation, parce que **le terrain est l'actif rare monétisable**. Playtomic et Anybuddy gagnent sur la commission de réservation et le SaaS club : le matching existe pour remplir les terrains et augmenter la fréquence de réservation.

Les matchers purs (Smatch, Sportpartner, SportLync, Bvddy) n'ont aucune transaction à taxer, monétisent par abonnement — et sont deux à trois ordres de grandeur plus petits. Ten'Up n'est une exception que parce que la FFT le subventionne.

Le sens de l'histoire le confirme : les produits de réservation ajoutent du matching (Playtomic Open Matches, MATCHi Communities, Anybuddy Matchs publics) ; **aucun produit de matching n'a réussi à ajouter la réservation.**

## 2. Démarrage à froid et densité

Quatre stratégies observées :

- **(a) S'amorcer sur l'offre de réservation** — le graphe club/terrain existe déjà, les matchs s'accrochent à des créneaux déjà réservés, donc la liquidité est *par lieu* plutôt qu'à l'échelle de la ville (Playtomic, Anybuddy, MATCHi).
- **(b) Fabriquer l'offre soi-même** — GoodRec achète des heures creuses et garantit que la partie a lieu, convertissant le matching en inventaire planifié.
- **(c) Hériter d'un graphe institutionnel** — Ten'Up chevauche les licenciés FFT et les effectifs de clubs.
- **(d) Chevaucher un sport chaud dans une géographie dense** — le padel en Espagne, France, Suède, où un seul club peut porter la liquidité.

Les matchers purs ne font aucune de ces quatre choses et meurent : « je n'ai pas trouvé un seul partenaire de sport », « peut-être 10 dans une ville », « ces forums étaient vides » (avis Sportpartner). Le site de Smatch annonce lui-même ~2 200 partenaires dans sa **meilleure** ville.

## 3. Interface conversationnelle / chatbot : aucune

**Aucun produit grand public de mise en relation entre joueurs n'utilise une interface chat/LLM comme UI principale.** Tous sont pilotés par liste / carte / profil / filtres. Les revendications « IA » (moteur de matching de SportLync, « assistants IA » de Smatch) sont des algorithmes de classement derrière une UI conventionnelle.

Les seuls agents WhatsApp/chat trouvés sont B2B : l'agent de réservation IA de Visito pour les clubs (qui s'intègre *dans* Playtomic), les bots d'inscription Pabbly, PitchMate d'Infobip (contenu pour supporters).

Les chatbots apparaissent du côté **support**, et les utilisateurs les détestent : « aucun moyen de parler à un vrai humain, toujours renvoyé vers un chatbot » (Playtomic, Trustpilot).

## 4. Principale cause de churn et de plainte

**Deux niveaux.**

Pour les petits matchers, c'est **le vide** — personne à proximité, chats morts, faux profils, aggravé par un paywall avant de pouvoir écrire (Sportpartner, 2,7★).

Pour les apps de réservation à l'échelle, c'est **l'intégrité de la note de niveau et le match déséquilibré qui s'ensuit** : les notes suivent la fréquence plutôt que le niveau, te pénalisent pour les erreurs de ton partenaire, sont opaques, et sont manipulées — « j'ai vu des joueurs affronter intentionnellement des adversaires moins bien notés juste pour gonfler leur note ». Et deux plateformes n'ont jamais la même échelle.

Au second ordre : **la friction financière** — remboursements, doubles débits, paiements non fractionnables (« devoir payer la partie pour les 4 personnes sans pouvoir faire 4 liens de paiement », Anybuddy) — plus **les no-shows**, que Playtomic sanctionne par un blocage punitif : absence sans préavis de 24 h → débité, compte bloqué jusqu'au paiement.

Les plaintes sur Ten'Up sont purement de l'exécution : bugs, déconnexions, recherche de joueur cassée.

## Sources

- Playtomic : https://playtomic.com/ · https://invezz.com/news/2025/03/19/spanish-startup-playtomic-aces-funding-round-reaching-273m-valuation/
- Playtomic — no-shows : https://playerhelp.playtomic.com/hc/en-gb/articles/43240624037393-What-happens-if-a-player-doesn-t-show-up
- Anybuddy : https://www.anybuddyapp.com/fr · https://padelmagazine.fr/anybuddy-lapp-qui-vous-trouve-le-partenaire-de-jeu-ideal/
- MATCHi : https://www.matchi.se/
- Padel Mates : https://play.google.com/store/apps/details?id=com.padelmates
- Ten'Up (FFT) : https://apps.apple.com/FR/app/id1457871907
- GoodRec : https://www.goodrec.com/
- Spond : https://www.spond.com/
- Strava Clubs/Events : https://press.strava.com/articles/strava-adds-race-and-club-event-discovery-elevating-community-led-training-during-peak-running-season
- GoJoe : https://www.gojoe.com/us
- Smatch : https://www.smatchsports.com/en
- Sportpartner : https://apps.apple.com/gb/app/sportpartner/id1572384047
- SportLync : https://sportlync.com/
- Bvddy (défunt) : https://www.crunchbase.com/organization/bvddy · https://techcrunch.com/2016/07/12/bvddy-now-on-android-matches-athletes-of-like-skill-to-play-and-get-fit-together/
- Visito (agent IA B2B pour clubs) : https://www.visitoai.com/en/blog/5-ways-whatsapp-ai-drives-more-court-bookings-for-padel-and-tennis-clubs
- No Strings Padel — intégrité des notes : https://clubhouse.nostringspadel.com/the-playtomic-app-are-player-ratings-accurate-2/
- Playskan — échelles incompatibles : https://www.playskan.com/blog/padel-levels-explained-uk
