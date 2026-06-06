Deployment
Introduction
After selecting XGBoost as the final model, the next objective was to make predictions available through a real-time API.
Instead of requiring users to manually run notebooks, the model was deployed using FastAPI, allowing customer risk predictions through REST endpoints.
The deployment architecture combines PostgreSQL, feature retrieval, model inference, and API serving into a complete prediction workflow.
________________________________________
Deployment Architecture
Customer Request ↓ FastAPI Endpoint ↓ Feature Fetcher ↓ PostgreSQL Feature Store ↓ Predictor ↓ XGBoost Model ↓ Prediction Response
________________________________________
Deployment Objective
The primary goal of deployment is to enable real-time risk scoring for individual customers.
Users provide:
Customer ID
The system returns:
•	Default Probability
•	Risk Classification
Example:
{ “customer_id”: 100002, “default_probability”: 0.88, “prediction”: “High Risk” }
________________________________________
Model Serialization
Machine learning models exist in memory during training.
To reuse them in production, trained artifacts must be saved.
Joblib was used to serialize the trained objects.
________________________________________
Saved Artifacts
xgb_model.pkl
Final production XGBoost model.
Purpose:
Generates risk predictions.
________________________________________
feature_columns.pkl
Stores the feature order used during training.
Purpose:
Ensures inference data matches training structure.
________________________________________
label_encoders.pkl
Stores label encoding mappings.
Purpose:
Applies consistent category transformations.
________________________________________
num_imputer.pkl
Stores numerical missing value handling logic.
Purpose:
Ensures consistent preprocessing.
________________________________________
cat_imputer.pkl
Stores categorical missing value handling logic.
Purpose:
Maintains preprocessing consistency.
________________________________________
Database Layer
PostgreSQL
PostgreSQL acts as the central feature repository.
The feature store contains:
customer_training_dataset
Each row represents one customer.
The table includes:
•	Original application features
•	Bureau features
•	Previous application features
•	Target variable
________________________________________
Feature Retrieval
feature_fetcher.py
A dedicated module was created to retrieve customer-level features.
Responsibilities:
•	Connect to PostgreSQL
•	Query customer records
•	Return customer feature data
Example Process:
Customer ID ↓ SQL Query ↓ Customer Features
________________________________________
Prediction Engine
predictor.py
This module contains the prediction logic.
Responsibilities:
•	Load model artifacts
•	Retrieve customer features
•	Apply preprocessing
•	Generate prediction
•	Return response
________________________________________
Prediction Workflow
Step 1
Receive Customer ID
Example:
100002
________________________________________
Step 2
Fetch customer features from PostgreSQL.
________________________________________
Step 3
Remove non-feature columns.
Example:
SK_ID_CURR
TARGET
________________________________________
Step 4
Align feature order using:
feature_columns.pkl
________________________________________
Step 5
Apply label encoding.
________________________________________
Step 6
Pass processed features to XGBoost.
________________________________________
Step 7
Generate probability score.
Example:
0.88
________________________________________
Step 8
Convert probability into risk category.
Rules:
Probability ≥ 0.5
High Risk
________________________________________
Probability < 0.5
Low Risk
________________________________________
Step 9
Return API response.
________________________________________
FastAPI Layer
Why FastAPI?
FastAPI was selected because it provides:
•	High performance
•	Lightweight architecture
•	Automatic documentation
•	Easy integration
•	Production readiness
________________________________________
API Endpoint
Endpoint:
GET /predict/{customer_id}
Example:
GET /predict/100002
________________________________________
Example Response
{ “customer_id”: 100002, “default_probability”: 0.88, “prediction”: “High Risk” }
________________________________________
Swagger UI
FastAPI automatically generates Swagger documentation.
Benefits:
•	Interactive API testing
•	Endpoint exploration
•	Validation of predictions
•	Demonstration for stakeholders
________________________________________
Error Handling
The deployment pipeline includes validation checks.
Example:
Customer ID does not exist.
Response:
{ “error”: “Customer not found” }
This prevents invalid prediction requests.
________________________________________
Deployment Benefits
The deployment architecture provides:
•	Real-time prediction capability
•	Centralized feature access
•	Consistent preprocessing
•	Scalable inference workflow
•	Easy API integration
Business users no longer need direct access to notebooks or machine learning code.
________________________________________
Production Flow
Customer Request ↓ FastAPI ↓ Feature Fetcher ↓ PostgreSQL ↓ Predictor ↓ XGBoost ↓ Risk Score ↓ API Response
________________________________________
Challenges Encountered
Several deployment challenges were resolved during implementation:
•	Feature mismatch issues
•	Missing column handling
•	Label encoding inconsistencies
•	Data type conversion problems
•	API import path issues
•	Database connectivity issues
These challenges helped improve system reliability.
________________________________________
Conclusion
The deployment layer transformed the machine learning model into a usable prediction service.
By integrating PostgreSQL, FastAPI, and XGBoost, the project delivers real-time customer risk assessments through a scalable API-based architecture.
