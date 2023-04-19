# EPIC EVENTS - PROJET 12 - OPENCLASSROOMS

Epic Events est une entreprise (fictive) de conseil et de gestion dans l'événementiel qui répond aux besoins des start-up voulant organiser des « fêtes épiques ».
L'objectif de ce projet était de développer une CRM sécurisé, interne à l'entreprise.

Les utilisateurs Epic Events peuvent : 
- Créer de nouveaux clients
- Créer et signer des contrats avec les clients
- Créer des événements


## Documentation de l'API (Liste des points de terminaison)

Pour la liste des points de terminaison de l'API Epic Events veuillez vous référer à cette documentation : [Documentation Postman](https://linktodocumentation)


## Prérequis

[![](https://img.shields.io/badge/Python-3.11.0-green)](https://www.python.org/)
[![](https://img.shields.io/badge/Django-4.2-brightgreen)](https://www.djangoproject.com/) 
[![](https://img.shields.io/badge/DRF-3.14.0-red)](https://www.django-rest-framework.org/)
[![](https://img.shields.io/badge/Pip-23.0.1-orange)](https://pypi.org/project/pip/)


## Installation (sous Windows)

- Cloner le repository sur votre ordinateur
```shell
    git clone https://github.com/iuliancojocari/epicevents.git
```

- Créer un environnement virtuel Python
```shell
    cd <nom_du_dossier_projet>
    python -m venv venv
```

- Activer l'environnement virtuel Python
```shell
    ./venv/Scripts/activate
```

- Installer les dépéndances
```shell
    pip install -r requirements.txt
```

- Créer une base de données dans Pgadmin

- Configuration de la base de données au niveau du projet Django
    1. Aller dans le fichier `settings.py`
    2. Trouver la variable appelée `DATABASES`
    3. Modifier les valeurs : 
        + `"ENGINE": "django.db.backends.postgresql_psycopg2"`
        + `"NAME": "nom_base_de_donnee"`
        + `"USER": "username"`
        + `"PASSWORD": "mot_de_passe"`
        + `"HOST": "hostname ou adresse ip du serveur de base de donénes"`
        + `"PORT": "port"`

- Réaliser les migrations Django
```shell
    python manage.py makemigrations
    python manage.py migrate
```

## Utilisation de l'application 

- Pour lancer le serveur
```shell
    python manage.py runserver
```

- Créer un superutilisateur pour pouvoir accèder au site d'aministration
```shell
    python manage.py createsuperuser
```

Voici le lien pour accèder au site d'administration : `http://127.0.0.1:8000/admin`