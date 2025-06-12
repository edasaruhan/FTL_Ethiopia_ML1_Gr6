# print("services/predictor.py loaded")

import joblib
import pandas as pd
import os

MODEL_DIR = os.path.join("models", "predictor")

clf = joblib.load(os.path.join(MODEL_DIR, "predictor.pkl"))
scaler = joblib.load(os.path.join(MODEL_DIR, "scaler.pkl"))
feature_cols = joblib.load(os.path.join(MODEL_DIR, "feature_columns.pkl"))

def predict_level(input_data: dict) -> str:
    df_input = pd.DataFrame([input_data])

    for col in feature_cols:
        if col not in df_input.columns:
            df_input[col] = 0

    df_input = df_input[feature_cols]
    scaled_input = scaler.transform(df_input)
    prediction = clf.predict(scaled_input)[0]
    return prediction
