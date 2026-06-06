import joblib

encoders = joblib.load(
    r"D:\ML PRoject\home_credit_data\models\label_encoders.pkl"
)

for col in [
    "NAME_CONTRACT_TYPE",
    "CODE_GENDER",
    "NAME_EDUCATION_TYPE"
]:
    print("\n", col)
    print(encoders[col].classes_)