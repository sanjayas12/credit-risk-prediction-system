import joblib
import pandas as pd

from scripts.feature_fetcher import get_customer_feature

# Load artifacts
model = joblib.load(r"D:\ML PRoject\home_credit_data\models\xgb_model.pkl")
feature_columns = joblib.load(r"D:\ML PRoject\home_credit_data\models\feature_columns.pkl")
label_encoders = joblib.load(r"D:\ML PRoject\home_credit_data\models\label_encoders.pkl")
num_imputer = joblib.load(r"D:\ML PRoject\home_credit_data\models\num_imputer.pkl")
cat_imputer = joblib.load(r"D:\ML PRoject\home_credit_data\models\cat_imputer.pkl")


def predict_customer(customer_id):
    df = get_customer_feature(customer_id)

    if len(df) == 0:
        return {"error": "Customer not found"}

    # Remove columns not used during training
    df = df.drop(columns=["SK_ID_CURR", "TARGET"])

    # Fix typo column if present
    df.rename(
        columns={"refussed": "refused_count"},
        inplace=True
    )

    # Match training feature order
    df = df[feature_columns]

    # Apply label encoding
    for col, encoder in label_encoders.items():

        if col in df.columns:

            df[col] = encoder.transform(
                df[col].astype(str)
            )

    # Convert any remaining object columns to numeric
    object_cols = df.select_dtypes(
        include=["object"]
    ).columns

    print("\nRemaining Object Columns:")
    print(list(object_cols))

    for col in object_cols:

        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )

    print("\nData Types After Conversion:")
    print(df.dtypes.value_counts())

    probability = model.predict_proba(df)[0][1]

    prediction = (
        "High Risk"
        if probability >= 0.5
        else "Low Risk"
    )

    return {
        "customer_id": customer_id,
        "default_probability": round(
            float(probability),
            4
        ),
        "prediction": prediction
    }