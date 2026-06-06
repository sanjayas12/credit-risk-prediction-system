import pandas as pd
import os
from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://postgres:Leodas@localhost:5432/credit_risk_db;")

query = """ 
select * from feature_store.customer_training_dataset"""

df = pd.read_sql(query,engine)
print(df.shape)
df.to_csv(r"D:\ML PRoject\home_credit_data\data\training_dataset.csv", index=False)
print("dataset loaded successfully")