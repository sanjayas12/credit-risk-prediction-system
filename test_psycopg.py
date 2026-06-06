import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="credit_risk_db;",
    user="postgres",
    password="Leodas"
)

print("Connected Successfully!")
conn.close()