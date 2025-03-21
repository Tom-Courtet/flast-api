# Flast API

## Description

Flast API est une application Flask permettant de gérer des fichiers JSON via une interface web et une API REST. Les fonctionnalités incluent :

-   Upload de fichiers JSON
-   Liste des fichiers disponibles
-   Consultation du contenu d’un fichier
-   Suppression et renommage des fichiers

L'application est conteneurisée avec Docker et déployée automatiquement via GitHub Actions.

## Installation et Exécution

### 1. Cloner le projet

```sh
 git clone https://github.com/votre-utilisateur/flast-api.git
 cd flast-api
```

### 2. Construire et exécuter le conteneur Docker

```sh
 docker build -t flast-api .
 docker run -d -p 5000:5000 --name flast-api flast-api
```

L’application sera accessible sur `http://localhost:5000/`.

## API Endpoints

| Méthode | Endpoint           | Description                      |
| ------- | ------------------ | -------------------------------- |
| GET     | `/`                | Interface web                    |
| POST    | `/upload`          | Upload un fichier JSON           |
| GET     | `/files`           | Liste des fichiers JSON          |
| GET     | `/file/<filename>` | Retourne le contenu d’un fichier |
| DELETE  | `/file/<filename>` | Supprime un fichier              |
| PUT     | `/file/<filename>` | Renomme un fichier               |

## Déploiement via GitHub Actions

À chaque push sur la branche `main`, l’application est :

1. Construite et poussée sur Docker Hub
2. Déployée automatiquement sur un serveur via SSH

## Contribution

Les contributions sont les bienvenues ! Forkez le projet et proposez vos améliorations via une Pull Request.

## Licence

MIT License
