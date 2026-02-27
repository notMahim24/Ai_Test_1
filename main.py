from fastapi import FastAPI
import joblib
import pandas as pd
from pydantic import BaseModel

# Initialize FastAPI
app = FastAPI(title="California Housing Predictor")

# Load the Brain (Model) and the Filter (Scaler)
# We load these OUTSIDE the functions so they stay in memory
model = joblib.load("Codes/house_model.pkl")
scaler = joblib.load("Codes/scaler.pkl")

# Define what the input should look like (Validation)
class HouseInput(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float

@app.get("/")
def home():
    return {"status": "Server is running", "message": "Go to /docs for the UI"}

@app.post("/predict")
def predict(data: HouseInput):
    # 1. Convert incoming JSON to a DataFrame
    input_data = pd.DataFrame([data.dict()])
    
    # 2. Scale the data (The model expects scaled values!)
    scaled_data = scaler.transform(input_data)
    
    # 3. Make the prediction
    prediction = model.predict(scaled_data)
    
    # 4. Return as JSON (Price is in $100,000s, so we multiply by 100k)
    return {
        "prediction_raw": float(prediction[0]),
        "estimated_price_usd": round(float(prediction[0]) * 100000, 2)
    }