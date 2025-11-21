# Band Names Generator (Projet Docker Compose)


## But
Un petit site web qui génère 10 noms de groupes de musique aléatoires suivant le template `The {adjective} {noun}`. Les adjectifs et noms sont stockés en base de données MySQL et initialisés automatiquement au démarrage du conteneur.


## Prérequis
- Docker & Docker Compose (v2.x recommandé)
- (optionnel) accès réseau sur les ports 8085 (web) et 8086 (adminer)


## Installation / lancement (environnement développement)
1. Copier le fichier d'environnement :


```bash
cp .env.dist .env