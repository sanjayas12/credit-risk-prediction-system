import pandas as py
import joblib

#load saved model
model=joblib.load(r"D:\ML PRoject\home_credit_data\models\xgb_model.pkl")
label_encoders=joblib.load(r"D:\ML PRoject\home_credit_data\models\label_encoders.pkl")
num_imputer=joblib.load(r"D:\ML PRoject\home_credit_data\models\num_imputer.pkl")
cat_imputer=joblib.load(r"D:\ML PRoject\home_credit_data\models\cat_imputer.pkl")
feature_columns=joblib.load(r"D:\ML PRoject\home_credit_data\models\feature_columns.pkl")

customers = {
    "NAME_CONTACT_TYPE":"Cash Loans",
    "CODE_GENDERS": "M",
    "FLAG_OWN_CAR": "Y",
    "FLAG_OWN_REALTY": "Y",
    "CNT_CHILDREN": 0,
    "AMT_INCOME_TOTAL": 80000,
    "AMT_CREDIT":500000 }

#Removed these 2 columns which not used 
customer_df = customer_df.drop(columns=["SK_ID_CURR", "TARGET"])

