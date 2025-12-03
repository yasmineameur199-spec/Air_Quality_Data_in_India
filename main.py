from fastapi import FastAPI
from pydantic import BaseModel, Field
import numpy as np
import pickle

# Charger modèle
with open("best_xgb_model.pkl", "rb") as f:
    model = pickle.load(f)

# Charger scaler
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# Charger l'ordre des features
with open("features.pkl", "rb") as f:
    FEATURES = pickle.load(f)

app = FastAPI()

# IMPORTANT : alias pour accepter "PM2.5"
class InputData(BaseModel):
    PM2_5: float = Field(alias="PM2.5")
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

    class Config:
        allow_population_by_field_name = True   # <- ULTRA IMPORTANT !
        populate_by_name = True                 # <- Permet d'utiliser les alias


class PredictionResponse(BaseModel):
    prediction: float

@app.post("/predict", response_model=PredictionResponse)
def predict(input_data: InputData):
    # TRÈS IMPORTANT :
    data = input_data.dict(by_alias=True)

    print(">>> DATA RECUE :", data)

    # Construire ligne dans le bon ordre
    row = np.array([[data[col] for col in FEATURES]])

    print("ROW BEFORE SCALING:", row)

    # Normalisation
    row_scaled = scaler.transform(row)

    print("ROW AFTER SCALING:", row_scaled)

    # Prédiction
    pred = model.predict(row_scaled)[0]

    print("PREDICTION:", pred)

    return {"prediction": float(pred)}
