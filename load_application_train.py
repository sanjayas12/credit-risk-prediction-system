import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL connection
engine = create_engine(
    "postgresql+psycopg2://postgres:Leodas@localhost:5432/credit_risk_db;"
)

# Read CSV
file_path = r"D:\ML PRoject\home_credit_data\application_train.csv"

df = pd.read_csv(file_path)

print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")

# Load into PostgreSQL
df.to_sql(
    name="application_train",
    con=engine,
    if_exists="replace",
    index=False,
    chunksize=5000
)

print("Data loaded successfully!")