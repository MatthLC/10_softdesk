[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

# **SoftDesk V1.0.0** : The bugtracking API

SoftDesk est un gestionnaire de bug qui vous facilitera la gestion de vos projets ! pour chaque projet, vous pourrez partager avec votre équipe des anomalies afin de les résoudre ensemble !

## Technologies
- Python
- Django REST
- Django JWT / Simple JWT

## Auteurs :

Matthieu LE CAM

## **Initialisation de l'environnement**

### 1. Télécharger la branche Main vers un répertoire local

- Pour Télécharger, cliquez sur le bouton vert "Code" puis "Download ZIP"

- Créer un dossier sur votre ordinateur pour y disposer les fichiers présents sous GitHub

- Ouvrir un terminal (Ex: Windows PowerShell) et se positionner dans le dossier en question avec la commande cd, par exemple:

```
cd d:
cd -- "D:\mon_dossier"
```

### 2. Créer un environnement virtuel et installer les librairies à l'aide du fichier requirements.txt

- Créer l'environnement:


`python -m venv env`

- Activer l'environnement (L'environnement est activé une fois son nom affiché dans le terminal) : 

    - Windows:

    `env/Scripts/Activate.ps1` 

    - Inux et MacOS:  

    `source env/bin/activate`

- Installer les librairies : 

`pip install -r requirements.txt`

## **Lancement du projet**

### 1. Lancer le serveur Django sous l'environnement virtuel, dans le terminal:

Se positionner dans l'application LITReview:

`cd softdesk`

Lancer le serveur :

`py manage.py runserver`

### 2. Accéder à l'API:
L'application vous propose les fonctionnalités suivantes :
- Créer un compte
- S'authentifier
- Créer un projet
- Créer des problèmes à résoudres
- Créer des commentaires au problème associé
    
## Sécurité
Pour profiter de l'application, l'utilisateur doit impérativement:
- Créer un compte
- S'authentifier

On peut distinguer deux types d'utilisateurs :
- auteur
- contributeur

![softdesk](https://user-images.githubusercontent.com/85108007/161517479-1aee1310-93f6-4900-b479-4d585637d41f.png)

## Postman:
Dans la documentation Postman, vous pouvez retrouver les différents Endpoint à disposition de l'utilisateur.
Les permissions des utilisateurs y sont spécifiées suivant le type d'utilisateur.

[Documentation Postman](https://documenter.getpostman.com/view/18469824/UVysybcc)

## Informations complémentaires :

Compte administrateur:
- login : openclassrooms@gmail.com
- password : softdesk00

Autres utilisateurs déjà inscrits (user ID : Login/password):
- Tom Sawyer 2 : tomsawyer@gmail.com / postman00
- Luke Skywalker 3 : lukeskywalker@gmail.com / postman00
- Wonder Woman 4 : wonderwoman@gmail.com / postman00
- Captain Marvel 5 : captainmarvel@gmail.com / postman00