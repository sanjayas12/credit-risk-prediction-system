# Credit Risk Prediction System

## Project Overview
This project predicts whether a loan applicant is likely to default on a loan using machine learning.
The solution is built as an end-to-end ML system using PostgreSQL, XGBoost, and FastAPI.
---

## Business Problem
Financial institutions face significant losses when customers fail to repay loans.
The objective of this project is to predict customer default risk and classify applicants as:

* High Risk
* Low Risk
This helps lenders make better credit approval decisions.
---

## Dataset
Home Credit Default Risk Dataset

Source:
https://www.kaggle.com/competitions/home-credit-default-risk
---

## Tech Stack
* Python
* PostgreSQL
* Pandas
* NumPy
* Scikit-Learn
* XGBoost
* FastAPI
* Swagger UI
* Git
* GitHub

---

## Project Architecture
CSV Files
↓
PostgreSQL Database
↓
Feature Engineering
↓
Feature Store
↓
Data Preprocessing
↓
XGBoost Model
↓
Model Serialization
↓
FastAPI API
↓
Real-Time Predictions
---

## Features Implemented
### Data Engineering
* Loaded 11 source files into PostgreSQL
* Created feature engineering pipeline
* Built customer-level feature store

### Machine Learning
* Missing value handling
* Label Encoding
* Train/Test Split
* Logistic Regression
* Random Forest
* XGBoost

### Model Evaluation
Metrics used:
* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC

### Deployment
* FastAPI REST API
* Swagger Documentation
* Real-time customer risk prediction
---

## Sample API Response
{
"customer_id": 100002,
"default_probability": 0.88,
"prediction": "High Risk"
}
---

## Future Improvements
* Dockerization
* Hyperparameter Tuning
* Model Monitoring
* CI/CD Pipeline
* Cloud Deployment
---

## Author
Sanjay
Data Engineer | Aspiring Data Scientist
