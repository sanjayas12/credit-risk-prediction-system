from fastapi import FastAPI

from scripts.predictor import predict_customer

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Credit Risk API Running"}

@app.get("/predict/{customer_id}")
def predict(customer_id: int):

    try:
        return predict_customer(customer_id)

    except Exception as e:
        return {
            "customer_id": customer_id,
            "error": str(e)
        }