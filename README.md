# 🧠 Customer Churn Prediction API (FastAPI + Vercel)

This project provides a serverless AI API for predicting customer churn using a logistic regression model trained on the Telco Customer Churn dataset. It is designed using FastAPI and deployed seamlessly on [Vercel](https://vercel.com) for instant cloud accessibility.

## 🔍 Features

- 🔁 Predicts customer churn probability (Yes/No + confidence score)
- 🚀 Powered by FastAPI and joblib-trained ML model
- ☁️ Serverless deployment on Vercel (zero infra config)
- 📦 Ready-to-use endpoint: `/predict_churn`

## 📈 Model Details

- Model: Logistic Regression
- Dataset: [Telco Customer Churn (Hugging Face)](https://huggingface.co/datasets/aai510-group1/telco-customer-churn)
- Input: 16 key customer attributes (e.g., age, monthly charge, tenure, internet service)
- Output: JSON with predicted churn status and probability

## 🚀 Deployment

1. Clone this repo:
   ```bash
   git clone https://github.com/swtech-pro/Customer-Churn-Prediction.git
   cd Customer-Churn-Prediction
   ```

2. Add your `churn_model.pkl` file to the root (or use the provided one).

3. Push to GitHub and connect repo to Vercel.

4. Vercel auto-deploys using:
   - `vercel.json`
   - `api/predict_churn.py`

## 🔗 Example Request (POST `/predict_churn`)

```json
{
  "features": [45, 60.5, 12, 1, 0, 3, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1]
}
```

## 🧪 Example Response

```json
{
  "churn": true,
  "probability": 0.78
}
```

## 📁 Project Structure

```
.
├── api/
│   └── predict_churn.py     # FastAPI endpoint
├── churn_model.pkl          # Trained model file
├── requirements.txt         # Dependencies
└── vercel.json              # Vercel config
```

## 📜 License

MIT License
