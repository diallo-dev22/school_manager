# School Manager

Application Django pour consulter la liste des étudiants d'une école.

## Prérequis
- Windows 10 ou 11
- Python 3 et Git installés

## Installation
- Cloner le dépôt : git clone https://github.com/diallo-dev22/school_manager.git
- Entrer dans le dossier : cd school_manager
- Créer le venv : python -m venv venv

## Activation du venv
venv\Scripts\activate

## Installation de Django
pip install -r requirements.txt

## Lancement du serveur
- cd school_project
- python manage.py runserver
- Ouvrir http://127.0.0.1:8000/

## URLs disponibles
- / : page d'accueil
- /students/ : liste des étudiants
- /students/<id>/ : détail d'un étudiant