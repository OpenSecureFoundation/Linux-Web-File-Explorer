# Conception et mise en œuvre d’un gestionnaire de fichiers multi-utilisateurs: cas de Pop!_OS

# Objectifs:

1. Concevoir un explorateur de fichiers avec la  gestion de droits d’accès.
   
2. Mettre en œuvre les concepts clé sur les fichiers et les répertoires.

# Fonctionnalités attendues
Créer une application web permettant de faire du CRUD sur les fichiers et répertoires (création, lecture, écriture, suppression).

# NB: README à mettre à jour progressivement par l'équipe.
## Technologies utilisées
- Python 3
- Django
- Système d’exploitation : Linux (Pop!_OS)

## Prérequis
- Python 3.x
- pip
- virtualenv (optionnel)

## Installation

1. Cloner le dépôt :
- git clone https://github.com/OpenSecureFoundation/Linux-Web-File-Explorer.git
- cd Linux-Web-File-Explorer

2. Créer et activer l’environnement virtuel :
- python -m venv env
- source env/bin/activate  # Linux

4. Installer les dépendances :
- pip install -r requirement.txt

5. Appliquer les migrations :
   entre dans le repertoire : "cd fileManager" avant de taper la commande  
- python manage.py migrate

6. Lancer le serveur :
- python manage.py runserver

7. Accéder à l’application :
- Ouvrir le navigateur à l’adresse :http://127.0.0.1:8000/
    
# Étapes en cours... 
    ##Conception des interfaces Html Css
