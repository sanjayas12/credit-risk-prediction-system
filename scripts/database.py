from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:Leodas@localhost:5432/credit_risk_db;"
)

print("Database Engine Created Successfully")