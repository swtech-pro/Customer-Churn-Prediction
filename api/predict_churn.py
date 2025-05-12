from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import joblib
import requests
import io
import numpy as np

app = FastAPI()

# Load model from GitHub or other hosted location
print("Before Downloading model...")

MODEL_URL = "https://raw.githubusercontent.com/swtech-pro/Customer-Churn-Prediction/main/churn_model.pkl"

model = None
try:
    print("Downloading model...")
    response = requests.get(MODEL_URL)
    model = joblib.load(io.BytesIO(response.content))
    print("Model loaded successfully!")
except Exception as e:
    print(f"Model loading failed: {e}")

@app.post("/predict_churn")
async def predict_churn(request: Request):
    try:
        data = await request.json()
        features = np.array(data['features']).reshape(1, -1)
        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0][1]
        return {"churn": bool(prediction), "probability": round(float(probability), 3)}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
