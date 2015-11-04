# Improllow-up

Ce projet sert d'exemple au [livre Git - maitriser la gestion de vos versions](http://www.editions-eni.fr/livres/git-maitrisez-la-gestion-de-vos-versions-concepts-utilisation-et-cas-pratiques/.d1ea8f871b0b4c12b2f863e5020d8a14.html)

## Présentation
Ce logiciel permet de **suivre les tâches des membres d'une équipe**. Ses tâches sont groupées par projets eux-mêmes groupés par client.
Ce projet permet de **savoir facilement les projets sur lesquels a travaillé un collaborateur** sur une période donnée. Un export CSV des tâches est également présent.

## Technologie
Ce projet utilise le framework Django (Python) pour la partie serveur. Par défaut les données sont stockées dans une base de données SQLite. Il est possible d'utiliser un autre système de bases de données en personnalisant la configuration du projet Django.

## Utilisation

### Installation de Python
Il est possible d'installer Python 3.4+ a partir du site officiel : 
https://www.python.org/downloads

Il est aussi possible de l'installer via le gestionnaire de paquets APT :

```
apt-get install python3.4
```

> Toutes les commandes effectuées sous Windows ne seront pas suffixées de la version 3.4 ou 3. Ainsi **python3** devient **python** sous windows et **pip3.4** devient **pip**. Si plusieurs versions de Python cohabitent, il est préférable d'utiliser les chemins absolus des exécutables (ou de créer des alias).

Il faut ensuite essayer la commande suivante sous MAC OS et sous Debian

```
pip3.4
```

Si la comande est inconnue il faut installer explicitement pip : 

```
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py
```

### Récupération du dépôt

Pour cloner ce dépôt il faut utiliser la commande :

```
git clone https://github.com/SamuelDauzon/Improllow-up.git
```

### Installation des dépendances

Il faut se placer dans le dépôt :

```
cd Improllow-up
```

Puis utiliser la commande :

```
pip3.4 install -r requirements.txt
```

### Initialisation des dépôts intégrés
Dans le dépôt il faut exécuter les commandes suivantes :

```
git submodule init
git submodule update
```

La dernière commande peut être longue à l'exécution car elle télécharge tout le contenu des dépôts intégrés.

### Génération des bibliothèques
Pour installer NodeJS et npm il faut aller sur la page de téléchargement du site officiel (https://nodejs.org/en/download/). Cette page permet de télécharger des installeurs pour Windows et Mac OS.
Pour Debian il est possible de compiler les sources ou d'utiliser apt-get :

```
sudo apt-get install nodejs
sudo apt-get install npm
```

#### Jquery

Pour Debien il est nécessaire d'installer le paquet suivant : 

```
apt-get install nodejs-legacy
```

Les commandes suivantes permettent de générer jQuery pour les 3 OS principaux.

```
cd improllowup/static/lib/js/jquery
npm run build
```

#### AngularJS
Pour générer AngularJS :

```
cd ../angularjs/
npm install -g grunt-cli
npm install -g bower
npm install
bower install
grunt package
```

### Fichier de configuration
Contenu possible du fichier improllowup/settings/local.py :

```
from .base import *

SECRET_KEY = '_dklma3)=/?kdjDE885$+0f88(ys1!7^+@b'
DEBUG = True
```

### Création de la base
Pour créer la base il faut se placer à la base du projet (et du dépôt) :

```
python3 manage.py migrate --settings=improllowup.settings.local
```

### Création d'un compte root
Pour créer le premier compte qui permettra d'ajouter d'autres comptes et d'ajouter des types de tâches dans l'interface d'administration : 

```
python3 manage.py createsuperuser --username=root --email=git@dauzon.com --settings=improllowup.settings.local
```

### Lancement du serveur
Pour lancer le serveur :

```
python3 manage.py runserver --settings=improllowup.settings.local
```

Pour accéder au site : http://127.0.0.1:8000
Pour accéder au système d'administration : http://127.0.0.1:8000/admin

Les identifiants utilisés pour se connecter sont les identifiants du compte root.


