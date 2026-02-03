# Projet Data Science : Analyse et Recommandation d'Animés

## Description du projet
Ce projet a pour but d'analyser un jeu de données d'animés afin de proposer un classement basé sur la qualité et la régularité, et pas seulement sur la popularité.

L'objectif est de différencier les œuvres constantes (classées comme "Chefs-d'œuvre") des séries inégales (classées comme "Risquées") en analysant l'écart type entre le meilleur et le pire épisode.

## Méthodologie de notation
Pour classer les animés, un "Score Éditorial" sur 10 a été calculé pour chaque série selon la formule suivante :

Score = (0.4 * Note Globale) + (0.3 * Régularité) + (0.3 * Meilleur Épisode)

Détail des pondérations :
- Note Globale (40%) : La moyenne générale attribuée par le public.
- Régularité (30%) : Calculée en fonction de l'écart entre le meilleur et le pire épisode.
- Meilleur Épisode (30%) : Permet de valoriser les séries ayant des pics de qualité.

## Contenu du dossier
- 01_analyse.ipynb : Le notebook Jupyter contenant le code, les calculs et les graphiques.
- animes.csv : Le jeu de données brut utilisé pour l'analyse.
- resultat_projet.csv : Le fichier de sortie contenant les scores calculés et la segmentation.
- graphique_analyse.png : Visualisation de la relation entre la qualité globale et le risque (écart type).

## Résultats
Le script génère un fichier CSV avec le classement complet. Voici le top 3 obtenu avec cet algorithme :
1. Steins;Gate (Score : 8.98)
2. Frieren (Score : 8.91)
3. Les Carnets de l'apothicaire (Score : 8.89)

## Instructions d'installation et de lancement

1. Prérequis
Assurez-vous d'avoir Python installé avec les bibliothèques suivantes :
pip install pandas seaborn matplotlib

2. Lancement
Ouvrir le fichier "01_analyse.ipynb" dans VS Code ou Jupyter Notebook et exécuter toutes les cellules ("Run All").
Le script générera automatiquement le fichier de résultats et le graphique.

---
Auteur : Aaron Boti
Date : Février 2026