Technical Architecture
System Overview
The Credit Risk Prediction System is designed as an end-to-end machine learning solution that transforms raw customer data into real-time loan default risk predictions.
The architecture consists of four major layers:
1.	Data Layer
2.	Feature Engineering Layer
3.	Machine Learning Layer
4.	Deployment Layer
________________________________________
High-Level Architecture
Home Credit Dataset ↓ PostgreSQL Database ↓ Feature Engineering ↓ Feature Store ↓ Data Preprocessing ↓ Machine Learning Models ↓ Model Artifacts ↓ FastAPI ↓ Swagger UI / End Users
________________________________________
1. Data Layer
Source Dataset
The project uses the Home Credit Default Risk dataset.
The dataset contains 11 relational CSV files containing:
•	Customer information
•	Credit history
•	Previous applications
•	Bureau records
•	Installment payments
•	Credit card history
•	POS cash balance data
These files contain millions of records.
________________________________________
Why PostgreSQL?
The raw CSV files were loaded into PostgreSQL.
Benefits:
•	Structured storage
•	SQL querying capability
•	Faster aggregation
•	Better data management
•	Scalability compared to working directly with CSV files
PostgreSQL acts as the central data repository for the project.
________________________________________
2. Feature Engineering Layer
Objective
Machine learning models require customer-level features.
However, many source tables contain multiple records per customer.
Example:
One customer may have:
•	Multiple loans
•	Multiple bureau records
•	Multiple installments
These records must be aggregated before model training.
________________________________________
Bureau Features
The bureau table contains customer credit history.
Example features created:
•	Number of bureau records
•	Active loan count
•	Closed loan count
•	Average credit amount
These features summarize a customer’s historical credit behavior.
________________________________________
Previous Application Features
The previous_application table contains prior loan applications.
Example features created:
•	Total previous applications
•	Approved applications
•	Refused applications
These features help understand customer borrowing behavior.
________________________________________
Feature Store
After feature engineering, all customer-level features were merged into a single table:
customer_training_dataset
This table contains one record per customer.
Purpose:
•	Training machine learning models
•	Providing data for inference
•	Creating a reusable feature repository
________________________________________
3. Machine Learning Layer
Data Extraction
The feature store was extracted from PostgreSQL into Pandas DataFrames.
The target variable:
TARGET
was separated from input features.
________________________________________
Data Preprocessing
The following preprocessing steps were performed:
Missing Value Handling
Numerical columns:
Median Imputation
Categorical columns:
Most Frequent Imputation
________________________________________
Encoding
Categorical columns were converted into numerical values using Label Encoding.
Machine learning algorithms require numerical inputs.
________________________________________
Train-Test Split
Data was divided into:
•	Training Dataset
•	Testing Dataset
Purpose:
Evaluate model performance on unseen data.
________________________________________
Models Trained
Three models were evaluated:
Logistic Regression
Baseline model.
Provides interpretability and serves as a benchmark.
________________________________________
Random Forest
Ensemble learning algorithm based on multiple decision trees.
Provides improved predictive performance.
________________________________________
XGBoost
Gradient boosting algorithm.
Selected as the final model because it achieved the best overall performance.
________________________________________
Evaluation Metrics
Models were evaluated using:
•	Accuracy
•	Precision
•	Recall
•	F1 Score
•	ROC-AUC
ROC-AUC was prioritized because the dataset is highly imbalanced.
________________________________________
4. Model Artifacts
After training, the following artifacts were saved:
xgb_model.pkl
Final production model.
________________________________________
label_encoders.pkl
Saved label encoders.
________________________________________
num_imputer.pkl
Saved numerical imputer.
________________________________________
cat_imputer.pkl
Saved categorical imputer.
________________________________________
feature_columns.pkl
Saved feature order used during training.
These artifacts ensure consistency between training and inference.
________________________________________
5. Deployment Layer
FastAPI
FastAPI was selected to expose the model as a REST API.
Benefits:
•	Lightweight
•	High performance
•	Easy integration
•	Automatic documentation
________________________________________
Prediction Flow
User Request ↓ Fetch Customer Features ↓ Apply Preprocessing ↓ Load Trained Model ↓ Generate Prediction ↓ Return Risk Score
________________________________________
API Output
Example:
{ “customer_id”: 100002, “default_probability”: 0.88, “prediction”: “High Risk” }
________________________________________
Swagger UI
Swagger UI provides:
•	Interactive API testing
•	Endpoint documentation
•	Real-time prediction validation
This simplifies testing and demonstration.
________________________________________
Architecture Benefits
The architecture provides:
•	Separation of concerns
•	Reusable feature store
•	Scalable data processing
•	Consistent model inference
•	Real-time prediction capability
•	Easy deployment and maintenance
________________________________________
Conclusion
The Credit Risk Prediction System combines data engineering, feature engineering, machine learning, and deployment components into a complete end-to-end solution capable of predicting customer loan default risk in real time.
