import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

engine = create_engine("postgresql+psycopg2://postgres:Leodas@localhost:5432/credit_risk_db;")
data_path = Path(r"D:\ML PRoject\home_credit_data")

for csv_file in data_path.glob("*.csv"):
    table_name = csv_file.stem.lower()
    print(f"\n loading {table_name}")

    try:
        df = pd.read_csv(csv_file)
        print(f"rows {len(df)}")
        df.to_sql(
            table_name, 
            engine,
            if_exists = "replace",
            index = False,
            chunksize = 5000
        )
        print(f"{table_name} Loaded successfuly")

    except Exception as e:
        print(f"Error loading {table_name}: {e}")
        print(e)
print("\n all tables loaded")
              

