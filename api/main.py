from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field


# ---------------------------------------------------------
# Create FastAPI application
# ---------------------------------------------------------

app = FastAPI(
    title="BrightCart Repeat Purchase Prediction API",
    description=(
        "Predicts whether a customer is likely to make "
        "a repeat purchase within 90 days."
    ),
    version="1.0"
)


# ---------------------------------------------------------
# Locate and load model
# ---------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "best_model.joblib"

model = joblib.load(MODEL_PATH)


# ---------------------------------------------------------
# Define input structure
# ---------------------------------------------------------

class CustomerFeatures(BaseModel):
    Recency_Days: float = Field(ge=0)
    Frequency: float = Field(ge=0)
    Monetary: float = Field(ge=0)
    Avg_Order_Value: float = Field(ge=0)
    Total_Quantity: float = Field(ge=0)
    Unique_Products: float = Field(ge=0)
    Tenure_Days: float = Field(ge=0)


# ---------------------------------------------------------
# Home endpoint
# ---------------------------------------------------------

@app.get("/")
def home():
    return {
        "message": "BrightCart Repeat Purchase Prediction API",
        "status": "running"
    }


# ---------------------------------------------------------
# Prediction endpoint
# ---------------------------------------------------------

@app.post("/predict")
def predict(customer: CustomerFeatures):

    input_data = pd.DataFrame([{
        "Recency_Days": customer.Recency_Days,
        "Frequency": customer.Frequency,
        "Monetary": customer.Monetary,
        "Avg_Order_Value": customer.Avg_Order_Value,
        "Total_Quantity": customer.Total_Quantity,
        "Unique_Products": customer.Unique_Products,
        "Tenure_Days": customer.Tenure_Days
    }])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0, 1]

    return {
        "prediction": int(prediction),
        "repeat_purchase_probability": round(
            float(probability),
            4
        ),
        "interpretation": (
            "Likely to repeat purchase within 90 days"
            if prediction == 1
            else "Unlikely to repeat purchase within 90 days"
        )
    }
