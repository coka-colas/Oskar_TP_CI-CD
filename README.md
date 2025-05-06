#################################################################################
#										#
#				   REAL LIFE RPG				#
#										#
#################################################################################

To overcome the hardships in life, become stronger. One step at a time.



#####################################
	GUIDE DE LANCEMENT
#####################################

1. Utiliser la commande :
	docker build -t realliferpg

2. Utiliser la commande :
	docker run -p 5000:5000 realliferpg

3. Se rendre à l'adresse 127.0.0.1:5000

4. Profit ! $$$




##############################
Description de l'application :
##############################

Commencez votre voyage en tant que personnage principal de votre propre vie !
	Ajoutez vous des points ou enlevez-en, selon les activités que vous menez.
	- Vous mangez une pomme ? +5 points de vie
	- Vous fumez une cigarette ? -10 points de vie
	- Vous avez monté les escaliers au lieu de prendre l'ascenseur ? + 10 points d'énergie
	- Vous avez pris votre voiture pour faire 200 mètres ? -600 points d'énergie et une couronne en caca vous sera offerte dans un prochain patch
Rappelez-vous, vous pouvez tricher, mais on ne triche pas contre le réel. Cette application vous permet uniquement de savoir où vous vous situez dans vos habitudes et encourager ce qui est bon pour vous.




#################################
Fonctionnement global du projet :
#################################

Initialisation d'une base de donnée
Utilisation de "squelettes" html dans lesquels seront envoyé des données
Stockées dans une base SQLite
Consultation possible pour constater l'évolution/la régression




#######################
Logique du Dockerfile :
#######################

1. Copie des fichiers nécessaires pour l'appli & install des dépendances
2. Exposition du port
3. Lancer l'appli via CLI




###########################
Logique du docker-compose :
###########################

1. Ouverture du port pour le service web
2. Localisation du volume créé
3. Description de l'environnement
4. Description de la base de données utilisée.