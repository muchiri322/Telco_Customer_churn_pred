import joblib
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

# Labels
labels = joblib.load('../models/target_labels.joblib')

#models
models = joblib.load('../models/ml_pipeline.joblib')

app = FastAPI(title = 'customer churn api', version = '1.0')

class input_data(BaseModel):
    gender: str
    seniorcitizen: int
    partner: str
    dependents: str
    tenure: int
    phoneservice: str
    multiplelines: str
    internetservice: str
    onlinesecurity: str
    onlinebackup: str
    deviceprotection: str
    techsupport: str
    streamingtv: str
    streamingmovies: str
    contract: str
    paperlessbilling: str
    paymentmethod: str
    monthlycharges: float
    totalcharges: float
    
@app.get('/health') 
def health_check():
    return {'status': 'ok'}

@app.post('/predict')
def predict_churn(payload: input_data):
    input_data_df = pd.DataFrame([payload.dict()])
    prediction = models.predict(input_data_df)[0]
    prediction_label = labels.inverse_transform(prediction)[0]
    return {'prediction': prediction_label}  
    
