![Logo Discord](https://zupimages.net/up/23/26/rumo.png)
[Rejoignez le Discord !](https://discord.gg/rSfTxaW)

[![Utilisateurs en ligne](https://img.shields.io/discord/347412941630341121?style=flat-square&logo=discord&colorB=7289DA)](https://discord.gg/347412941630341121)
---

# Discord Message Cleaner

Ce projet fournit des scripts Python pour nettoyer les messages Discord, y compris les messages privés (DMs) et les messages dans les serveurs. Les scripts sont organisés de manière modulaire et offrent une interface utilisateur simple pour sélectionner l'action souhaitée. Idéal pour maintenir la propreté de vos communications Discord.

## Fonctionnalités

- Nettoyer les messages privés (DMs).
- Nettoyer les messages dans tous les serveurs, à l'exception de ceux exclus.
- Nettoyer les messages dans un serveur spécifique.
- Sauvegarder les messages dans un serveur spécifique sans les supprimer.

## Prérequis

- Python 3.x
- Bibliothèques Python : `requests`, `colorama`, `python-dotenv`

## Installation

1. Clonez ce dépôt sur votre machine locale :

    ```sh
    git clone https://github.com/votre-utilisateur/discord-message-cleaner.git
    cd discord-message-cleaner
    ```

2. Créez un environnement virtuel et activez-le :

    ```sh
    python -m venv venv
    source venv/bin/activate  # Sur Windows, utilisez `venv\Scripts\activate`
    ```

3. Installez les dépendances nécessaires :

    ```sh
    pip install requests colorama python-dotenv
    ```

4. Créez un fichier `.env` à la racine du projet et ajoutez vos informations d'authentification Discord :

    ```env
    DISCORD_TOKEN=VOTRE_TOKEN_UTILISATEUR
    USER_ID=VOTRE_ID_UTILISATEUR
    EXCLUDED_GUILD_IDS=ID_DE_VOTRE_GUILDE_A_EXCLURE,ID_D_UNE_AUTRE_GUILDE
    ```


## Récupérer le DISCORD_TOKEN

1. **Ouvrir Discord dans le navigateur** :
    - Connectez-vous à votre compte Discord.

2. **Ouvrir les outils de développement** :
    - Dans Chrome, appuyez sur `F12` ou faites un clic droit et sélectionnez "Inspecter".

3. **Accéder à l'onglet Réseau (Network)** :
    - Rafraîchissez la page (`Ctrl+R` ou `F5`).

4. **Rechercher la requête vers l'API Discord** :
    - Cherchez une requête vers `discord.com/api/v9/users/@me`.

5. **Copier le token utilisateur** :
    - Dans les en-têtes de la requête, trouvez `Authorization` et copiez le token. dans `DISCORD_TOKEN=` du fichier .env
    - Renseignez `USER_ID` par votre propre ID utilisateur, que vous pouvez obtenir en activant le mode développeur dans Discord et en cliquant droit sur votre profil pour copier l'ID.

## Utilisation

1. Exécutez le script principal `main.py` pour accéder au menu interactif :

    ```sh
    python main.py
    ```

2. Sélectionnez l'option souhaitée dans le menu :

    - `1` : Nettoyer les messages privés (DMs)
    - `2` : Nettoyer les messages dans tous les serveurs sauf ceux exclus
    - `3` : Nettoyer les messages dans un serveur spécifique (vous serez invité à entrer l'ID du serveur)
    - `4` : Sauvegarder les messages dans un serveur spécifique (vous serez invité à entrer l'ID du serveur)
    - `0` : Quitter

## Détails des scripts

### `clean_dms.py`

Nettoie les messages dans les DMs ouverts.

### `clean_guild_messages.py`

Nettoie les messages dans tous les serveurs, à l'exception de ceux spécifiés dans `EXCLUDED_GUILD_IDS`.

### `clean_specific_guild.py`

Nettoie les messages dans un serveur spécifique. L'ID du serveur est demandé lors de l'exécution du script.

### `backup_guild_messages.py`

Sauvegarde les messages dans un serveur spécifique sans les supprimer. L'ID du serveur est demandé lors de l'exécution du script.

### `utils.py`

Fournit des fonctions utilitaires pour gérer les couleurs dans le terminal et charger les variables d'environnement.

## Limitations

- **Messages privés (DMs)** : Vous devez avoir le MP ouvert pour que les messages soient trouvés et supprimés.
- **Enregistrements par d'autres bots** : Si d'autres bots comme Nightbot enregistrent les messages, ces enregistrements ne seront pas supprimés par ces scripts. Les scripts ne suppriment que les messages directement sur Discord.

## Sécurité

- Ne partagez jamais votre token utilisateur et stockez-le de manière sécurisée.
- Respectez les conditions de service de Discord. L'utilisation de tokens utilisateurs pour des opérations automatisées peut enfreindre ces conditions et entraîner la désactivation de votre compte.

## Contribution

Les contributions sont les bienvenues ! Si vous avez des suggestions ou des améliorations, n'hésitez pas à ouvrir une issue ou à soumettre une pull request.

