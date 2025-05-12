from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import joblib
import numpy as np

app = FastAPI()
model = joblib.load("churn_model.pkl")

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
