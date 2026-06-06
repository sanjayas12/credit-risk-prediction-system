Feature Engineering
Introduction
Feature Engineering is the process of transforming raw data into meaningful input variables that improve machine learning model performance.
In this project, the raw Home Credit dataset consists of multiple relational tables containing customer information, credit history, loan applications, payment history, and financial records.
Since machine learning models require one row per customer, feature engineering was performed to aggregate and transform raw transactional data into customer-level features.
________________________________________
Why Feature Engineering?
The source dataset contains multiple records for each customer.
Example:
Customer ID: 100001
May have:
•	Multiple bureau records
•	Multiple previous loan applications
•	Multiple installment payments
•	Multiple credit card transactions
Machine learning models cannot directly consume these one-to-many relationships.
Therefore, customer-level aggregations were created.
________________________________________
Feature Engineering Strategy
The overall strategy was:
1.	Load source tables into PostgreSQL.
2.	Analyze table relationships.
3.	Create aggregated customer-level features.
4.	Merge all engineered features.
5.	Build a centralized feature store.
________________________________________
Source Tables Used
The following tables were used during feature engineering:
application_train
Primary customer dataset.
Contains:
•	Customer demographics
•	Loan amount
•	Income
•	Employment information
•	Housing details
This table acts as the base table.
________________________________________
bureau
Contains customer credit bureau history.
Example information:
•	Previous loans
•	Credit amounts
•	Credit status
•	Active loans
•	Closed loans
________________________________________
previous_application
Contains historical loan applications submitted by customers.
Example:
•	Approved applications
•	Refused applications
•	Loan types
•	Requested amounts
________________________________________
Bureau Feature Engineering
Objective
Summarize customer credit history.
The bureau table contains multiple rows per customer.
Aggregation was performed using:
GROUP BY SK_ID_CURR
________________________________________
Features Created
bureau_count
Total bureau records for a customer.
Business Meaning:
Number of historical credit relationships.
________________________________________
active_loans
Count of active loans.
Business Meaning:
Current debt obligations.
________________________________________
closed_loans
Count of closed loans.
Business Meaning:
Successfully completed credit history.
________________________________________
avg_credit_sum
Average credit amount across bureau records.
Business Meaning:
Typical borrowing behavior.
________________________________________
max_credit_sum
Maximum credit amount.
Business Meaning:
Largest historical borrowing exposure.
________________________________________
Previous Application Feature Engineering
Objective
Summarize historical loan application behavior.
The previous_application table contains multiple records per customer.
Aggregation was performed at customer level.
________________________________________
Features Created
previous_application_count
Total historical applications.
Business Meaning:
Customer borrowing frequency.
________________________________________
approved_count
Number of approved applications.
Business Meaning:
Previous successful loan approvals.
________________________________________
refused_count
Number of refused applications.
Business Meaning:
Past credit approval challenges.
________________________________________
approval_rate
Approved applications divided by total applications.
Business Meaning:
Historical approval success ratio.
________________________________________
Feature Store Creation
After feature generation, all datasets were merged using:
SK_ID_CURR
Customer Identifier
________________________________________
Final Dataset
Table:
customer_training_dataset
Contains:
•	Original customer features
•	Bureau features
•	Previous application features
•	Target variable
Each row represents one customer.
________________________________________
Benefits of Feature Store
The feature store provides:
•	Reusable engineered features
•	Consistent training data
•	Consistent inference data
•	Centralized feature management
Instead of recreating features repeatedly, all downstream processes use the same feature repository.
________________________________________
SQL Aggregation Example
Example logic:
Count active loans per customer.
SQL Concept:
SELECT SK_ID_CURR, COUNT(*) FROM bureau WHERE CREDIT_ACTIVE = ‘Active’ GROUP BY SK_ID_CURR;
This converts multiple bureau records into a customer-level feature.
________________________________________
Merge Strategy
The merge sequence:
application_train LEFT JOIN bureau_features LEFT JOIN previous_application_features
Using:
SK_ID_CURR
This ensured that every customer remained in the final dataset.
________________________________________
Feature Engineering Challenges
One-to-Many Relationships
Challenge:
Customers had multiple records in bureau and previous_application tables.
Solution:
Aggregation using SQL GROUP BY.
________________________________________
Missing Values
Challenge:
Some customers lacked bureau or application history.
Solution:
Missing values handled during preprocessing.
________________________________________
Feature Consistency
Challenge:
Training and prediction require identical feature structures.
Solution:
Feature store design and feature_columns.pkl were used to maintain consistency.
________________________________________
Impact on Model Performance
Feature engineering significantly improved model quality.
Raw application data alone provides limited information.
By incorporating:
•	Credit history
•	Borrowing behavior
•	Loan approval history
the model gains deeper insight into customer risk patterns.
These engineered features became some of the most important predictors in the final XGBoost model.
________________________________________
Conclusion
Feature Engineering transformed raw relational datasets into a customer-level feature store suitable for machine learning.
This process enabled the model to leverage historical credit behavior, borrowing patterns, and approval history, ultimately improving the ability to predict customer default risk accurately.
