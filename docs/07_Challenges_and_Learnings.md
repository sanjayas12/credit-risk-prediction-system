Challenges and Learnings
Introduction
Building an end-to-end Credit Risk Prediction System involved multiple challenges across data engineering, machine learning, deployment, and version control.
Each challenge provided valuable learning opportunities and helped improve the overall robustness of the solution.
This document summarizes the major issues encountered and the approaches used to resolve them.
________________________________________
Challenge 1: Loading Large Datasets into PostgreSQL
Problem
The Home Credit dataset contains multiple large CSV files with millions of records.
Examples:
•	bureau.csv
•	installments_payments.csv
•	previous_application.csv
•	credit_card_balance.csv
Loading large files directly into PostgreSQL required careful handling of schema creation and data types.
________________________________________
Solution
•	Created PostgreSQL tables for each dataset.
•	Loaded data incrementally.
•	Verified row counts after ingestion.
•	Performed validation queries to ensure successful loading.
________________________________________
Learning
Large datasets require database-based processing rather than relying solely on in-memory operations.
________________________________________
Challenge 2: Wrong Schema Loading
Problem
Some tables were initially loaded into an unexpected schema.
This created confusion when querying tables.
________________________________________
Solution
•	Verified schema locations.
•	Updated SQL references.
•	Standardized table access using correct schema names.
________________________________________
Learning
Always verify database schema structure before building downstream dependencies.
________________________________________
Challenge 3: One-to-Many Relationships
Problem
Tables such as:
•	bureau
•	previous_application
contained multiple records per customer.
Machine learning models require one row per customer.
________________________________________
Solution
Created aggregated features using:
GROUP BY SK_ID_CURR
Examples:
•	bureau_count
•	active_loans
•	approved_count
•	refused_count
________________________________________
Learning
Feature engineering is often more important than model selection.
________________________________________
Challenge 4: Feature Store Creation
Problem
Data existed across multiple tables.
A single customer profile was required for model training.
________________________________________
Solution
Created:
customer_training_dataset
by joining:
•	application_train
•	bureau_features
•	previous_application_features
________________________________________
Learning
Feature stores improve consistency between training and inference.
________________________________________
Challenge 5: Class Imbalance
Problem
Target distribution was highly imbalanced.
TARGET = 0
282,686 customers
TARGET = 1
24,825 customers
A model could achieve high accuracy by predicting only the majority class.
________________________________________
Solution
Used:
class_weight=‘balanced’
for Logistic Regression.
Focused on:
•	Recall
•	F1 Score
•	ROC-AUC
instead of relying only on Accuracy.
________________________________________
Learning
Accuracy can be misleading for imbalanced classification problems.
________________________________________
Challenge 6: Poor Initial Logistic Regression Results
Problem
The initial Logistic Regression model produced:
•	High Accuracy
•	Near-zero Recall
•	Near-zero Precision
The model failed to identify risky customers.
________________________________________
Solution
Introduced:
class_weight=‘balanced’
to increase emphasis on minority class examples.
________________________________________
Learning
Business-relevant metrics are more important than accuracy alone.
________________________________________
Challenge 7: Feature Mismatch During Inference
Problem
The trained model expected a specific feature structure.
During prediction:
KeyError errors occurred due to missing or renamed columns.
Example:
refused_count
versus
refussed
________________________________________
Solution
Standardized feature names.
Used:
feature_columns.pkl
to enforce consistent feature ordering.
________________________________________
Learning
Training and inference must use identical feature structures.
________________________________________
Challenge 8: Label Encoding Issues
Problem
During deployment:
ValueError
occurred because label encoders received unexpected category values.
________________________________________
Solution
Verified encoding mappings.
Ensured encoded features matched the structure used during training.
________________________________________
Learning
Preprocessing consistency is critical in production systems.
________________________________________
Challenge 9: Data Type Conversion Errors
Problem
XGBoost requires numerical inputs.
Some columns were returned as object type during inference.
Example:
EXT_SOURCE_3
________________________________________
Solution
Identified problematic columns.
Converted values to appropriate numerical types before prediction.
________________________________________
Learning
Database outputs may not always match model expectations.
Data validation is necessary before inference.
________________________________________
Challenge 10: FastAPI Import Issues
Problem
Multiple ModuleNotFoundError exceptions occurred due to project structure and import paths.
Examples:
•	predictor imports
•	database imports
•	script module references
________________________________________
Solution
Created package structure using:
init.py
and corrected import paths.
________________________________________
Learning
Project organization becomes increasingly important as applications grow.
________________________________________
Challenge 11: API Prediction Errors
Problem
Some customer IDs produced predictions successfully while others generated runtime errors.
________________________________________
Solution
Added validation checks.
Implemented data type handling.
Improved preprocessing consistency.
________________________________________
Learning
Testing with multiple real-world inputs is essential.
________________________________________
Challenge 12: Git and GitHub Setup
Problem
Git was completely new.
Initial confusion included:
•	Git initialization
•	Repository setup
•	.gitignore usage
•	Commit process
•	Push and pull operations
________________________________________
Solution
Configured Git.
Created GitHub repository.
Implemented version control workflow.
________________________________________
Learning
Version control is an essential skill for production machine learning projects.
________________________________________
Major Technical Learnings
Through this project, the following concepts were learned and reinforced:
Data Engineering
•	PostgreSQL
•	SQL Aggregations
•	Feature Store Design
•	Relational Data Modeling
________________________________________
Machine Learning
•	Missing Value Handling
•	Label Encoding
•	Class Imbalance
•	Model Evaluation
•	XGBoost
________________________________________
Deployment
•	FastAPI
•	Swagger UI
•	Model Serialization
•	Real-Time Inference
________________________________________
Software Engineering
•	Git
•	GitHub
•	Project Structures
•	Dependency Management
________________________________________
Key Takeaway
The most important lesson from this project is that successful machine learning solutions require much more than model training.
Real-world projects involve:
•	Data engineering
•	Feature engineering
•	Model development
•	Deployment
•	Debugging
•	Version control
Building and troubleshooting each component provided a deeper understanding of the complete machine learning lifecycle.
________________________________________
Conclusion
The challenges encountered throughout this project transformed theoretical knowledge into practical experience.
Resolving real-world issues across data, machine learning, deployment, and software engineering significantly improved both technical skills and project implementation capabilities.
