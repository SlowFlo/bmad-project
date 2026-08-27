# Notes de reconstruction des maquettes

## Passe v3 — 2026-08-27

Les maquettes sont passées de **trois à quatre**. Elles avaient été laissées en v1
pendant que les spines passaient en v2, puis le PRD est passé en v2 à son tour :
elles étaient à deux générations de retard.

### Ce qui change dans le contenu (renversement du modèle du niveau)

| Écran | Changement |
|---|---|
| `key-declaration-niveau.html` | **Nouveau.** `level-choice` dans ses trois états (repos, survol, focus clavier), le chemin court quand l'un des trois mots exacts était dans la phrase, et le refus écrit avec la fiche au niveau inconnu |
| `key-proposition-partenaires.html` | Le **niveau quitte la carte** et monte dans `candidate-group-label`. La ligne meta passe aux jours et au **délai d'attente** (règle d'ordre de FR-6). L'écart de niveau et l'état « élargissement sur le niveau » sont supprimés — FR-7 est retirée |
| `key-recap-en-attente.html` | **Ligne du jour bloqué** et phrase du **jour gagné** (FR-16). Ajout du cadre « Anna confirme » avec sa région `role="status"`. Le lieu nantais est remplacé par un lieu lyonnais |
| `key-fil-a-froid.html` | Refaite sur le scaffold corrigé ; le vide latéral reste matérialisé par des pointillés hors produit |

### Défauts de la génération précédente, corrigés dans les quatre fichiers

| Défaut | Origine | Correctif |
|---|---|---|
| `--border-decorative` encore présent | jeton **supprimé du système** en v2 | retiré ; tous les filets sont `border-interactive` ou `border-strong` |
| `outline:none` sur la zone de saisie | interdit absolu de la spine | l'anneau est porté par le conteneur via `:focus-within`, jamais supprimé du système |
| `<input>` pour la saisie | la spine exige un `<textarea>` | `<textarea>` avec `<label class="sr-only">` |
| `aria-label` sur des `<div>` nus | ignoré par les technologies d'assistance | `role="group"` réels, ou éléments porteurs de rôle |
| Sort d'une carte inerte en suffixe masqué | invisible pour tout le monde sauf le lecteur d'écran | **mot visible** — *Retenue* / *Non retenue* |
| Lieu nantais (« le Petit-Port ») | le produit ne dessert que **Lyon** | parc de la Tête d'Or, club de Gerland. **Corrigé aussi dans la microcopie contractuelle d'EXPERIENCE.md**, où il figurait deux fois dont une dans le SMS sortant |

### Ce qui est tenu depuis la passe v1 et ne doit pas régresser

Boutons réels avec noms accessibles · anneau de focus en `outline` opaque de 3 px,
décalé de 2 px · **aucune ombre portée** · requêtes média réelles exprimées en `em` ·
`min-height` et jamais `height` · repères ARIA (`<main>`, `role="log"`,
`role="status"`, `<form>`) · étiquettes de locuteur masquées (« Ex Aequo : » / « Vous : ») ·
points d'étape franchie à **pleine opacité**, la pulsation seule distingue l'étape en
cours, et elle est bornée · `prefers-reduced-motion` respecté.

### Décor hors produit

Les cadres de navigateur et de téléphone, ainsi que les traits pointillés du vide
latéral, sont du **décor d'explication**. Leurs couleurs (`#060A12`, `#080E1A`)
n'appartiennent à aucun jeton et ne doivent jamais être reprises dans le produit.

### Autorité

**La spine l'emporte sur la maquette en cas de conflit.** Aucun chiffre de seuil météo
écrit dans une maquette ne fait autorité : seul FR-10 le fait.
