Projet8 Créer une plateforme nutella afin de proposer un aliment plus sain
Installer:
Pour installer et faire fonctionner mon projet vous aurez besoin de certains packages et vous aurez besoin de clonner mon projet de github sur votre machine avec git:

-git clone https://github.com/yannhamdi/projet8
-Installer l'environnement virtuel:
pip3 install virtualenv
-Créer l'environnement virtuel:
virtualenv -p python3 env
-Activer l'environnement virtuel

-Créer la base de données:
python manage.py dbopenfood
-Lancer le serveur
python manage.py runserver
