# Telco_Customer_churn_pred

# Customer Churn Prediction API

A Machine Learning REST API built with FastAPI for predicting customer churn.

The API accepts customer information and predicts whether the customer is likely to churn.

---

## Features

- FastAPI REST API
- Machine Learning Pipeline using Scikit-Learn
- Label Encoder support
- Health Check Endpoint
- Prediction Endpoint
- Automatic Swagger Documentation

---

## Technologies Used

- Python
- FastAPI
- Scikit-Learn
- Pandas
- Joblib
- Uvicorn

---

## Project Structure

```
customer-churn-api
│
├── app
│   └── main.py
│
├── models
│   ├── ml_pipeline.joblib
│   └── target_labels.joblib
│
├── requirements.txt
├── .env
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/customer-churn-api.git
```

Move into the project

```bash
cd customer-churn-api
```

Create a virtual environment

Windows

```bash
python -m venv venv
```

Linux

```bash
python3 -m venv venv
```

Activate the environment

Windows

```bash
venv\Scripts\activate
```

Linux

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the API

Navigate to the project folder

```bash
uvicorn app.main:app --reload
```

Server starts on

```
http://127.0.0.1:8000
```

---

## Interactive Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

## API Endpoints

### Health Check

GET

```
/health
```

Response

```json
{
  "status": "ok"
}
```

---

### Predict Customer Churn

POST

```
/predict
```

Example Request

```json
{
  "gender":"Female",
  "seniorcitizen":0,
  "partner":"Yes",
  "dependents":"No",
  "tenure":12,
  "phoneservice":"Yes",
  "multiplelines":"No",
  "internetservice":"Fiber optic",
  "onlinesecurity":"No",
  "onlinebackup":"Yes",
  "deviceprotection":"No",
  "techsupport":"No",
  "streamingtv":"Yes",
  "streamingmovies":"Yes",
  "contract":"Month-to-month",
  "paperlessbilling":"Yes",
  "paymentmethod":"Electronic check",
  "monthlycharges":89.5,
  "totalcharges":1074.0
}
```

Response

```json
{
  "prediction":"Yes"
}
```

---

## Environment Variables

Create a `.env` file

```
MODEL_PATH=models/ml_pipeline.joblib
LABEL_PATH=models/target_labels.joblib
```

---

## Running Tests

Use Swagger UI or Postman to test the API.

---

## Requirements

Python 3.10+

---

## Author

MUCHIRI

---

## License

MIT License