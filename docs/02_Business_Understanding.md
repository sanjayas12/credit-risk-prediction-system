Business Understanding
Introduction
The primary objective of this project is to predict whether a customer is likely to default on a loan.
In the banking and financial industry, lending money to customers is a core business activity. However, not every customer repays the loan successfully. Some customers fail to make repayments, resulting in financial losses for the lender.
This project helps financial institutions identify risky customers before approving loans.
________________________________________
What is Credit Risk?
Credit Risk refers to the possibility that a customer may fail to repay a loan according to the agreed terms.
When a bank lends money, there is always a risk that the customer might:
•	Miss payments
•	Delay payments
•	Stop payments completely
•	Default on the loan
The higher the probability of repayment failure, the higher the credit risk.
________________________________________
What is Default?
Default occurs when a borrower fails to meet the repayment obligations of a loan.
In simple terms:
A customer takes a loan but does not repay it within the agreed period.
This results in financial loss for the lender.
Examples:
•	Missing multiple EMI payments
•	Long-term non-payment
•	Loan becoming overdue beyond the acceptable threshold
________________________________________
What Does TARGET Mean?
The TARGET column is the dependent variable used for prediction.
Values:
TARGET = 0
Customer successfully repaid the loan.
Low Risk Customer.
________________________________________
TARGET = 1
Customer experienced payment difficulties or defaulted.
High Risk Customer.
________________________________________
Business Objective
The goal is to predict TARGET before approving a loan application.
If the model predicts:
TARGET = 1
The customer is considered risky.
The bank may:
•	Reject the loan
•	Reduce loan amount
•	Increase interest rate
•	Request additional verification
________________________________________
If the model predicts:
TARGET = 0
The customer is considered lower risk.
The bank can approve the loan with greater confidence.
________________________________________
Why is This Important?
Incorrect lending decisions can cause significant financial losses.
Two types of mistakes can occur:
False Positive
Model predicts High Risk.
Actual customer is Low Risk.
Impact:
A good customer may be rejected.
Potential business opportunity is lost.
________________________________________
False Negative
Model predicts Low Risk.
Actual customer is High Risk.
Impact:
Loan may be approved to a risky customer.
Financial loss may occur.
This is generally the more expensive business mistake.
________________________________________
Why Machine Learning?
Traditional rule-based systems cannot effectively capture complex relationships between:
•	Customer income
•	Employment history
•	Credit history
•	Previous loans
•	Repayment behavior
Machine Learning can analyze historical customer behavior and identify patterns associated with future default risk.
________________________________________
Project Prediction Output
The model predicts:
1.	Probability of Default
Example:
0.88
Meaning:
88% probability that the customer may default.
________________________________________
2.	Risk Category
Example:
High Risk
or
Low Risk
This makes the output easier for business users to understand.
________________________________________
Example
Customer ID: 100002
Prediction:
Probability of Default = 0.88
Risk Category = High Risk
Business Interpretation:
This customer has a high likelihood of repayment difficulties and should be reviewed carefully before loan approval.
________________________________________
Success Criteria
A successful model should:
•	Identify risky customers accurately
•	Minimize financial losses
•	Improve loan approval decisions
•	Support risk management teams
•	Provide interpretable risk scores
________________________________________
Business Value Delivered
The Credit Risk Prediction System helps financial institutions:
•	Reduce loan default losses
•	Improve risk assessment
•	Automate credit decision support
•	Increase operational efficiency
•	Make data-driven lending decisions
The final output is a probability-based risk assessment system that supports smarter credit approval processes.
