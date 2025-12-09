

Ce journal résume les étapes techniques réalisées lors du développement, du test et du déploiement du modèle IA à l’aide de Docker.

# Étape 1 – Préparation et exploration des données

Chargement du dataset de qualité de l’air.

Nettoyage des valeurs manquantes.

Encodage des variables catégorielles (OrdinalEncoder).

Séparation X / y et analyse initiale des corrélations.

# Étape 2 – Séparation et normalisation

Split en 80% train / 20% test.

StandardScaler appliqué uniquement sur les données d’entraînement.

Vérification des shapes (X_train_scaled, X_test_scaled).

# Étape 3 – Entraînement du modèle XGBoost

GridSearchCV pour trouver les meilleurs hyperparamètres.

Recherche sur : n_estimators, max_depth, learning_rate, subsample.

Enregistrement du meilleur modèle avec pickle (best_xgb_model.pkl).

Log automatique sur MLflow (DagsHub).

Calcul des métriques : accuracy, precision, recall, f1-score, log-loss.


# Guide d’exécution et de déploiement – API FastAPI et Modèle ML

Ce document décrit étape par étape comment récupérer le projet, exécuter l’API localement, l'utiliser via Docker, comprendre la structure des fichiers, et accéder à la version déployée sur Google Cloud Run.

## 1. Récupération du projet
### 1.1. Cloner le projet depuis GitHub
git clone https://github.com/mon_compte/Air_Quality_Data_in_India.git
cd Air_Quality_Data_in_India

### 1.2. Ouvrir le projet

Ouvrir le dossier dans VS Code ou utiliser un terminal classique.

## 2. Exécution de l’API en local (sans Docker)
### 2.1. Créer un environnement virtuel (optionnel)
Windows :
python -m venv venv
venv\Scripts\activate

Mac/Linux :
python3 -m venv venv
source venv/bin/activate

### 2.2. Installer les dépendances
pip install -r requirements.txt

### 2.3. Lancer l’API FastAPI
uvicorn main:app --host 0.0.0.0 --port 8080

### 2.4. Accéder à la documentation Swagger

http://localhost:8080/docs

### 2.5. Endpoints disponibles
GET /health

Permet de vérifier si le service fonctionne.

POST /predict

Reçoit un JSON en entrée et retourne la prédiction du modèle ML.

## 3. Exécution via Docker
### 3.1. Construire l’image Docker
docker build -t mon_api .

### 3.2. Lancer le conteneur Docker
docker run -p 8000:8000 mon_api

### 3.3. Accéder à l’API Docker

http://localhost:8080

http://localhost:8080/docs

## 4. Explication des fichiers principaux
Dockerfile

Le Dockerfile réalise les actions suivantes :

Installation de Python dans l’image

Installation des dépendances

Copie du projet dans l’image

Lancement de FastAPI via Uvicorn

Exposition du port 8000

Il est utilisé pour l’exécution locale et le déploiement sur Google Cloud Run.

requirements.txt

Contient la liste des librairies Python nécessaires : FastAPI, Uvicorn, NumPy, Pandas, scikit-learn, XGBoost, etc.

main.py

Fichier principal de l’API FastAPI contenant :

La route /health

La route /predict

Le chargement du modèle best_xgb_model.pkl

best_xgb_model.pkl

Modèle XGBoost optimisé avec GridSearchCV, utilisé pour la prédiction.

## 5. Structure du projet
Air_Quality_Data_in_India/
│── main.py
│── best_xgb_model.pkl
│── requirements.txt
│── Dockerfile
│── .dockerignore
│── city_day.csv
│── Air_Quality_Data_in_India.ipynb
│── Projet_ia/
└── README.md

## 6. Accès à la version en ligne (Google Cloud Run)

L’API a été déployée sur Google Cloud Run à partir d’une image Docker stockée dans Artifact Registry.

URL publique de l’API

https://mon-api-957479726796.us-central1.run.app

Documentation Swagger

https://mon-api-957479726796.us-central1.run.app/docs

## 7. Exemple d’appel POST /predict
{
  "PM2_5": 52.3,
  "PM10": 87.1,
  "NO": 12.5,
  "NO2": 34.2,
  "NOx": 46.7,
  "NH3": 18.9,
  "CO": 0.64,
  "SO2": 9.3,
  "O3": 21.5,
  "Benzene": 2.1,
  "Toluene": 3.4,
  "Xylene": 1.8,
  "City_Frequency_Encoded": 0.068030,
  "annee": 2022,
  "mois": 11,
  "jour": 23
}
