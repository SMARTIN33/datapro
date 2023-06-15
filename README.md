# Application Web Goldenline


## À propos

Développement d’une solution web permettant de mieux visualiser les données. 
Disponible en ligne grace à pythonanywhere : [Accès à l'application](http://smartin17.eu.pythonanywhere.com/)

## Table des matières

- 🪧 [À propos](#à-propos)
- 📦 [Prérequis](#prérequis)
- 🚀 [Getting started](#getting-started)
- 🛠️ [Utilisation](#utilisation)
- 🏷 [️Tests](#test)
- 📚[️Langages Frameworks](#Langages-et-Frameworks)
- 📝[️Outils recommandés](#Outils-recommandés)

## Prérequis

- Python 3.10 (syntaxe match, ...)
- PostgreSQL 15

## Getting started

1. Cloner le projet :
`git clone git@github.com:SMARTIN33/datapro.git`

2. Installer les dépendances:
`pip install -r requirements.txt`

3. Créer une base de données avec PGadmin 4:
- Clique droit sur Servers > Register > Server > Définir un nom, un port, un hostname, nom utilisateur et un mot de passe
- Clique droit sur Database > Create Database > Définir un nom

4. Modifier le fichier credentials.py :
- USER 
- PASSWORD
- DBNAME
- HOST
- PORT

5. Générer le jeu de données :
`python generate_dataset.py`

6. Modifier dans le fichier settings.py le dictionnaire Database (\GoldenLine\GoldenLine\settings.py) :
- ENGINE
- NAME
- USER
- PASSWORD
- HOST
- PORT

7. Lancer le serveur :
 `python manage.py runserver`  

## Utilisation

`python manage.py runserver [port]` 

## Test

2 tests majeurs sont proposés :
- Vérification du bon fonctionnement du jeu de données
- Vérification du bon fonctionnement de l'export de données

## Langages et Frameworks

- Utilisation de python & Django pour servir les requêtes vers le back et du back.
- Utilisation du Javascipt, html et CSS pour produire une interface intéractive & dynamique pour le client.
- PostgreSQL pour la création et la maintenance d"une base de données persistante.

## Outils recommandés

- PG amdin 4
- VS Code
- Python
- Django
- Chrome
