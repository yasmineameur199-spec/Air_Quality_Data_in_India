from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pickle

# Charger le modèle XGBoost optimisé
with open("best_xgb_model.pkl", "rb") as f:
    model = pickle.load(f)

# Initialiser FastAPI
app = FastAPI()

# Définir la structure des données envoyées à /predict
class InputData(BaseModel):
    PM2_5: float
    PM10: float
    NO: float
    NO2: float
    NOx: float
    NH3: float
    CO: float
    SO2: float
    O3: float
    Benzene: float
    Toluene: float
    Xylene: float
    City_Frequency_Encoded: float
    annee: float
    mois: float
    jour: float

# Endpoint de test
@app.get("/health")
def health():
    return {"status": "ok"}

# Endpoint de prédiction
@app.post("/predict")
def predict(input_data: InputData):

    data = np.array([[
        input_data.PM2_5,
        input_data.PM10,
        input_data.NO,
        input_data.NO2,
        input_data.NOx,
        input_data.NH3,
        input_data.CO,
        input_data.SO2,
        input_data.O3,
        input_data.Benzene,
        input_data.Toluene,
        input_data.Xylene,
        input_data.City_Frequency_Encoded,
        input_data.annee,
        input_data.mois,
        input_data.jour
    ]])

    prediction = model.predict(data)[0]

    return {"prediction": float(prediction)}
