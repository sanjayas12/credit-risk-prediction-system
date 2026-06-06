import pandas as pd
from scripts.database import engine

def get_customer_feature(customer_id):
    query = f"""
    select * from feature_store.customer_training_dataset where "SK_ID_CURR" = {customer_id} """
    df = pd.read_sql(query, engine)
    return df