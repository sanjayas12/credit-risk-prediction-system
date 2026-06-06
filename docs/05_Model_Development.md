Model Development
Introduction
After creating the customer-level feature store, the next phase involved preparing the data for machine learning model training.
The objective was to build a classification model capable of predicting whether a customer would default on a loan.
The target variable used for prediction was:
TARGET
Where:
TARGET = 0
Customer did not default.
Low Risk Customer.
________________________________________
TARGET = 1
Customer experienced payment difficulties or defaulted.
High Risk Customer.
________________________________________
Data Extraction
The final feature store:
customer_training_dataset
was extracted from PostgreSQL into a Pandas DataFrame.
The dataset contained:
•	307,511 customers
•	112 input features
•	1 target variable
The target column was separated from the feature columns before model training.
________________________________________
Data Preprocessing
Machine learning models require clean numerical input data.
Several preprocessing steps were performed before training.
________________________________________
Missing Value Handling
Many features contained missing values.
Examples:
•	Employment information
•	Credit bureau details
•	External credit scores
Machine learning algorithms cannot reliably process missing values.
________________________________________
Numerical Features
Numerical columns were imputed using:
Median Imputation
Reason:
•	Robust to outliers
•	Preserves feature distribution
•	Suitable for skewed financial data
Artifact Saved:
num_imputer.pkl
________________________________________
Categorical Features
Categorical columns were imputed using:
Most Frequent Imputation
Reason:
•	Maintains category consistency
•	Simple and effective for categorical data
Artifact Saved:
cat_imputer.pkl
________________________________________
Label Encoding
Many features contained text values.
Examples:
•	Gender
•	Contract Type
•	Education Type
•	Housing Type
Machine learning models require numerical input.
Label Encoding was applied to convert categorical values into integer representations.
Example:
Contract Type
Cash Loans → 0
Revolving Loans → 1
Artifact Saved:
label_encoders.pkl
________________________________________
Train-Test Split
The dataset was divided into:
Training Data
80%
Used to train models.
________________________________________
Testing Data
20%
Used to evaluate model performance.
________________________________________
Why Train-Test Split?
A model should be evaluated on unseen data.
Testing on the same data used for training can lead to overfitting and unrealistic performance estimates.
The train-test split provides a more realistic measure of model quality.
________________________________________
Class Imbalance
The dataset contained significantly more non-default customers than default customers.
Distribution:
TARGET = 0
282,686 customers
________________________________________
TARGET = 1
24,825 customers
________________________________________
Problem:
The model may learn to predict the majority class and ignore default customers.
________________________________________
Example
If a model predicts:
TARGET = 0
for every customer,
accuracy will appear high despite failing to identify risky customers.
Therefore, accuracy alone is insufficient.
________________________________________
Baseline Model: Logistic Regression
The first model trained was Logistic Regression.
Purpose:
•	Establish baseline performance
•	Provide interpretability
•	Compare against advanced models
________________________________________
Class Weight
The parameter:
class_weight=‘balanced’
was used.
Reason:
The dataset is highly imbalanced.
This instructs the model to place greater emphasis on the minority class (default customers).
________________________________________
max_iter = 1000
Logistic Regression uses an optimization process to find the best coefficients.
max_iter determines the maximum number of optimization iterations.
Increasing this value helps ensure convergence for large datasets.
________________________________________
Random Forest Classifier
The second model trained was Random Forest.
Random Forest combines multiple decision trees to improve prediction performance.
Benefits:
•	Handles non-linear relationships
•	Robust to noise
•	Reduces overfitting compared to a single decision tree
________________________________________
XGBoost Classifier
The final model selected was XGBoost.
XGBoost is a gradient boosting algorithm that builds trees sequentially, with each new tree correcting the errors of previous trees.
Benefits:
•	High predictive performance
•	Handles complex patterns
•	Works well on structured tabular data
•	Industry-standard algorithm for credit risk problems
________________________________________
Model Evaluation Metrics
Several evaluation metrics were used.
________________________________________
Accuracy
Measures overall prediction correctness.
Formula:
Correct Predictions / Total Predictions
Limitation:
Can be misleading for imbalanced datasets.
________________________________________
Precision
Measures:
Of all customers predicted as High Risk, how many were actually High Risk?
High precision reduces false alarms.
________________________________________
Recall
Measures:
Of all actual High Risk customers, how many were identified correctly?
In credit risk problems, recall is highly important because missing risky customers can result in financial losses.
________________________________________
F1 Score
Harmonic mean of Precision and Recall.
Provides balanced evaluation.
________________________________________
ROC-AUC
Primary evaluation metric.
Measures the model’s ability to distinguish between risky and non-risky customers across multiple classification thresholds.
Benefits:
•	Works well for imbalanced datasets
•	Threshold independent
•	Widely used in credit risk modeling
________________________________________
Model Comparison
Logistic Regression
Provided baseline performance.
________________________________________
Random Forest
Improved predictive capability.
________________________________________
XGBoost
Delivered the strongest overall balance of:
•	Recall
•	Precision
•	ROC-AUC
Therefore, XGBoost was selected as the final production model.
________________________________________
Feature Importance
Feature importance analysis was performed on the XGBoost model.
Some of the most influential features included:
•	EXT_SOURCE_2
•	EXT_SOURCE_3
•	DAYS_BIRTH
•	DAYS_EMPLOYED
•	AMT_CREDIT
•	EDUCATION_TYPE
These features contributed significantly to risk prediction.
________________________________________
Model Serialization
To support deployment, model artifacts were saved using Joblib.
Saved Artifacts:
xgb_model.pkl
Final production model.
________________________________________
label_encoders.pkl
Encoding mappings.
________________________________________
num_imputer.pkl
Numerical preprocessing.
________________________________________
cat_imputer.pkl
Categorical preprocessing.
________________________________________
feature_columns.pkl
Feature order consistency.
These artifacts ensure the same preprocessing logic is applied during inference.
________________________________________
Final Model Selection
XGBoost was selected because it achieved the best overall performance and demonstrated strong capability in identifying high-risk customers while maintaining acceptable precision and recall.
The trained model became the foundation for the production prediction API.
________________________________________
Conclusion
The model development phase transformed engineered customer features into a production-ready machine learning solution capable of predicting loan default risk.
Through preprocessing, class imbalance handling, model comparison, and evaluation, XGBoost emerged as the most effective solution for the business problem.
