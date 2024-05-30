# Discord Message Cleaner

Ce projet fournit des scripts pour nettoyer les messages Discord, y compris les messages privés (DMs) et les messages dans les serveurs. Les scripts sont organisés de manière modulaire pour faciliter leur utilisation et leur gestion.

## Fonctionnalités

- Nettoyer les messages privés (DMs).
- Nettoyer les messages dans tous les serveurs, à l'exception de ceux exclus.
- Nettoyer les messages dans un serveur spécifique.

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

## Utilisation

1. Exécutez le script principal `main.py` pour accéder au menu interactif :

    ```sh
    python main.py
    ```

2. Sélectionnez l'option souhaitée dans le menu :

    - `1` : Nettoyer les messages privés (DMs)
    - `2` : Nettoyer les messages dans tous les serveurs sauf ceux exclus
    - `3` : Nettoyer les messages dans un serveur spécifique (vous serez invité à entrer l'ID du serveur)
    - `4` : Quitter

## Détails des scripts

### `clean_dms.py`

Nettoie les messages dans les DMs ouverts.

### `clean_guild_messages.py`

Nettoie les messages dans tous les serveurs, à l'exception de ceux spécifiés dans `EXCLUDED_GUILD_IDS`.

### `clean_specific_guild.py`

Nettoie les messages dans un serveur spécifique. L'ID du serveur est demandé lors de l'exécution du script.

### `utils.py`

Fournit des fonctions utilitaires pour gérer les couleurs dans le terminal et charger les variables d'environnement.

## Sécurité

- Ne partagez jamais votre token utilisateur et stockez-le de manière sécurisée.
- Respectez les conditions de service de Discord. L'utilisation de tokens utilisateurs pour des opérations automatisées peut enfreindre ces conditions et entraîner la désactivation de votre compte.

## Contribution

Les contributions sont les bienvenues ! Si vous avez des suggestions ou des améliorations, n'hésitez pas à ouvrir une issue ou à soumettre une pull request.

