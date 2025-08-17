import logging
import os
from typing import List, Optional

import joblib
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Bienvenido a la API de predicción de viajes, revisa la documentación en /docs"}


# Cargar el modelo de predicción
model_path = os.path.join("model", "random_forest_model.joblib")
model = joblib.load(model_path)


# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
# validacion de los datos de entrada con Pydantic
class PredictionRequest(BaseModel):
    pickup_weekday: int
    pickup_hour: int
    work_hours: float
    pickup_minute: int
    passenger_count: int
    trip_distance: float
    trip_time: float
    trip_speed: float
    PULocationID: int
    DOLocationID: int
    RatecodeID: float

@app.post("/predict")
def predict(request: PredictionRequest):
    features = [
        request.pickup_weekday,
        request.pickup_hour,
        request.work_hours,
        request.pickup_minute,
        request.passenger_count,
        request.trip_distance,
        request.trip_time,
        request.trip_speed,
        request.PULocationID,
        request.DOLocationID,
        request.RatecodeID,
    ]
    logger.debug(f"Received prediction request with features: {features}")
    prediction = model.predict_proba([features])
    logger.debug(f"Prediction result: {prediction[0]}")
    return {"prediction": float(prediction[0][1])}

