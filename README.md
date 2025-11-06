# 🎴 Card Scanner FR - Base de données Pokémon TCG

Un projet expérimental pour créer une base de données complète des cartes Pokémon en français, avec génération automatique à partir d'images de référence et extraction de métadonnées depuis Cardmarket.

---

## 📋 Table des matières

- [À propos](#à-propos)
- [Structure du projet](#structure-du-projet)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Utilisation](#utilisation)
  - [Téléchargement des images](#téléchargement-des-images)
  - [Génération automatique des cartes](#génération-automatique-des-cartes)
  - [Extraction des métadonnées Cardmarket](#extraction-des-métadonnées-cardmarket)
  - [Fusion des données](#fusion-des-données)
- [Format des données](#format-des-données)
- [Scripts disponibles](#scripts-disponibles)
- [Contribution](#contribution)
- [Licence](#licence)

---

## 🎯 À propos

Ce dépôt permet de travailler sur une base de données des hash de cartes Pokémon TCG en français. Le projet est avant tout expérimental et vise à automatiser la création d'entrées JSON pour chaque carte à partir d'images de référence et de données en ligne.

**Note :** Ce projet est à usage personnel et expérimental. Demandez l'autorisation sur Discord avant d'utiliser les cartes disponibles.

---

## 📁 Structure du projet

```
card-scanner-fr-python/
│
├── json/
│   └── mega-evolution/
│       └── fr/
│           └── cards.json          # Base de données des cartes françaises
│
├── reference_images/
│   └── mega-evolution/
│       └── fr-fr/                  # Images de référence des cartes
│           └── JL2G_FR_*.png
│
├── test_images/                    # Images de test
├── test_reference_images/          # Images de référence pour tests
│
├── generate_cards.py               # Script de génération automatique
├── scrape_cardmarket.py            # Script d'extraction Cardmarket
├── merge_cardmarket_data.py        # Script de fusion des données
├── requirements.txt                # Dépendances Python
├── main.ipynb                      # Notebook Jupyter principal
└── README.md                       # Ce fichier
```

---

## 🔧 Prérequis

- **Python 3.8+**
- **PowerShell** (Windows) ou un terminal bash (Linux/macOS)
- Connexion Internet (pour l'extraction depuis Cardmarket)

---

## 📦 Installation

1. **Cloner le dépôt :**

```powershell
git clone https://github.com/nazimboudeffa/card-scanner-fr.git
cd card-scanner-fr-python
```

2. **Installer les dépendances :**

```powershell
pip install -r requirements.txt
```

---

## 🚀 Utilisation

### 1️⃣ Téléchargement des images

Les images de référence peuvent être téléchargées depuis le site officiel Pokémon :

🔗 **[https://tcg.pokemon.com/fr-fr/galleries/mega-evolution/](https://tcg.pokemon.com/fr-fr/galleries/mega-evolution/)**

Placez toutes les images dans le dossier :
```
reference_images/mega-evolution/fr-fr/
```

Les images doivent suivre le format de nommage : `JL2G_FR_<numéro>.png`

ATTENTION ! Je ne donne pas le dossier vous devez le faire vous même car je ne veux pas de problèmes, merci

---

### 2️⃣ Génération automatique des cartes

Le script `generate_cards.py` crée automatiquement des entrées JSON pour chaque image trouvée dans le dossier de référence.

#### Exécution :

```powershell
python generate_cards.py
```

#### Ce que fait le script :

- 📂 Scanne le dossier `reference_images/mega-evolution/fr-fr/`
- 🔢 Extrait le numéro de carte depuis le nom de fichier (`JL2G_FR_42.png` → numéro 42)
- ✨ Génère une entrée JSON avec des valeurs par défaut
- 💾 Met à jour `json/mega-evolution/fr/cards.json` sans dupliquer les cartes existantes
- 🖼️ Ajoute le chemin de l'image si absent sur les cartes existantes

#### Champs générés :

```json
{
    "set": "Mega Evolution",
    "language": "fr",
    "category": "Pokemon",
    "rarity": "À définir",
    "number": 42,
    "name": "Carte 42",
    "image": "reference_images/mega-evolution/fr-fr/JL2G_FR_42.png"
}
```

#### Sortie exemple :

```
Generated 187 new card entries. Total now: 188
```

---

### 3️⃣ Extraction des métadonnées Cardmarket

Le script `scrape_cardmarket.py` récupère les noms officiels, raretés et autres métadonnées depuis Cardmarket.

#### Exécution :

```powershell
python scrape_cardmarket.py
```

#### Ce que fait le script :

- 🌐 Se connecte à Cardmarket (cardmarket.com)
- 🎴 Extrait les informations de toutes les cartes du set Mega Evolution en français
- 💾 Génère un fichier `cardmarket_cards.json` avec les données complètes

#### Données extraites :

- Nom officiel de la carte
- Numéro dans le set
- Rareté
- Type de carte
- Et plus encore...

---

### 4️⃣ Fusion des données

Le script `merge_cardmarket_data.py` fusionne les données Cardmarket avec vos entrées générées localement.

#### Exécution :

```powershell
python merge_cardmarket_data.py
```

#### Ce que fait le script :

- 📖 Lit `cards.json` et `cardmarket_cards.json`
- 🔄 Remplace les placeholders ("Carte X", "À définir") par les vraies données
- 💾 Met à jour `cards.json` avec les informations complètes
- ✅ Préserve les métadonnées détaillées existantes

---

## 📊 Format des données

### Structure complète d'une carte :

```json
{
    "name": "Mewtwo-EX",
    "illustrator": "5ban Graphics",
    "rarity": "Ultra Rare",
    "category": "Pokemon",
    "set": "Mega Evolution",
    "language": "fr",
    "number": 158,
    "dexId": [150],
    "hp": 180,
    "types": ["Psychic"],
    "suffix": "EX",
    "abilities": [
        {
            "type": "Ability",
            "name": "Psychic Recharge",
            "effect": "..."
        }
    ],
    "attacks": [
        {
            "cost": ["Psychic", "Colorless", "Colorless"],
            "name": "Psystrike",
            "damage": 120,
            "effect": "..."
        }
    ],
    "weaknesses": [{"type": "Psychic", "value": "×2"}],
    "resistances": [{"type": "Fighting", "value": "-20"}],
    "retreat": 2,
    "legalities": {"expanded": true},
    "regulationMark": "D",
    "variants": {
        "normal": false,
        "reverse": true,
        "holo": true,
        "firstEdition": false
    },
    "image": "reference_images/mega-evolution/fr-fr/JL2G_FR_158.png"
}
```

---

## 🛠️ Scripts disponibles

| Script | Description | Sortie |
|--------|-------------|--------|
| `generate_db.py` | Génère des entrées à partir des images | `cards.json` |
| `merge_cardmarket_data.py` | Fusionne les deux sources | `cards.json` (mis à jour) |
| `main.ipynb` | Notebook Jupyter pour tests et analyses | - |

---

## 🔄 Workflow recommandé

1. **Télécharger** les images de référence
2. **Exécuter** `generate_cards.py` pour créer la structure de base
3. **Exécuter** `scrape_cardmarket.py` pour obtenir les métadonnées officielles
4. **Exécuter** `merge_cardmarket_data.py` pour enrichir les données
5. **Personnaliser** manuellement les détails avancés (attaques, talents, etc.)

---

## 💡 Conseils et astuces

### Encodage UTF-8

Si vous voyez des caractères mal affichés dans PowerShell :

```powershell
chcp 65001
```

### Regénération

Vous pouvez relancer `generate_cards.py` après avoir ajouté/supprimé des images. Le script ne crée pas de doublons pour les cartes existantes.

### Recherche et remplacement

Pour remplacer rapidement les placeholders :
- Cherchez `"Carte "` pour trouver les noms à compléter
- Cherchez `"À définir"` pour trouver les raretés manquantes

---

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :

1. 🍴 Forker le projet
2. 🌿 Créer une branche (`git checkout -b feature/amelioration`)
3. 💾 Commiter vos changements (`git commit -m 'Ajout d'une fonctionnalité'`)
4. 📤 Pousser sur la branche (`git push origin feature/amelioration`)
5. 🔀 Ouvrir une Pull Request

---

## 📝 Licence

Ce projet est à usage expérimental et personnel. Contactez l'auteur pour toute utilisation commerciale ou distribution.

---

## 📧 Contact

**Nazim Boudeffa**  
GitHub: [@nazimboudeffa](https://github.com/nazimboudeffa)

---

## 🙏 Remerciements

- Pokémon Company International pour les images officielles
- Cardmarket pour les métadonnées des cartes
- La communauté Pokémon TCG FR

---

**Bon scanning ! 🎴✨**

