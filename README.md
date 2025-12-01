

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


# 1. Exécution de l’API localement
## 1.1. Installation des dépendances

Dans un environnement virtuel ou non :

pip install -r requirements.txt

## 1.2. Lancer l’API FastAPI
uvicorn main:app --host 0.0.0.0 --port 8000

## 1.3. Accéder à l'interface Swagger
http://localhost:8000/docs


Vous pouvez tester les endpoints :

/health (vérification du service)

/predict (prédiction du modèle ML)

# 2. Construction et exécution du Docker en local
2.1. Construire l’image Docker
docker build -t mon_api .

## 2.2. Exécuter le conteneur
docker run -p 8000:8000 mon_api


L’API sera alors disponible à :

http://localhost:8000/

# 3. Explication des fichiers principaux
Dockerfile

Installe Python et les dépendances

Copie le projet dans l’image

Lance FastAPI avec Uvicorn

Expose le port 8000
Ce fichier permet de créer l’image Docker utilisée en local et sur Google Cloud Run.

requirements.txt

Liste toutes les librairies Python nécessaires :
FastAPI, Uvicorn, NumPy, Pandas, scikit-learn, xgboost, etc.

main.py

Fichier principal contenant l’API FastAPI :

/health → Vérification du service

/predict → Retourne la prédiction

Charge également le modèle sauvegardé : best_xgb_model.pkl

best_xgb_model.pkl

Modèle XGBoost optimisé via GridSearchCV et sauvegardé en local.

# 4. Structure du projet
Air_Quality_Data_in_India/
│── main.py
│── best_xgb_model.pkl
│── requirements.txt
│── Dockerfile
│── .dockerignore
│── city_day.csv
│── Air_Quality_Data_in_India.ipynb
│── Projet_ia/
│   
└── README.md

# 5. Accès à la version en ligne (Google Cloud Run)

L’API a été déployée via Google Cloud Run, à partir d’une image Docker stockée dans Artifact Registry.

URL publique de l’API

https://mon-api-957479726796.us-central1.run.app

Documentation Swagger

https://mon-api-957479726796.us-central1.run.app/docs

Exemple d’appel POST /predict :
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

# 6.  Erreurs rencontrées et solutions
Problème : PORT incorrect pour Cloud Run

Cloud Run impose le port 8080.
✔ Correction :

uvicorn main:app --host 0.0.0.0 --port 8080

Problème : commandes Cloud Run sous Windows

Les commandes multi-lignes avec \ ne fonctionnent pas.
✔ Solution : entrer toutes les commandes sur une seule ligne.

Problème : conteneur ne démarrait pas

✔ Solution : corriger le Dockerfile pour exposer et utiliser le port correct.

# 7. Conclusion

Ce projet montre une chaîne complète de déploiement IA :

Préparation des données

Entraînement XGBoost

Création d'une API FastAPI

Conteneurisation avec Docker

Déploiement public via Google Cloud Run
