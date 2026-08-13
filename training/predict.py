
import joblib
import pandas as pd
 
from model_training import CATEGORICAL_COLUMNS, NUMERICAL_COLUMNS
 
def load_artifacts():
    model = joblib.load('artifacts/best_model.pkl')
    scaler = joblib.load('artifacts/scaler.pkl')
    target_encoder = joblib.load('artifacts/target_encoder.pkl')
    feature_columns = joblib.load('artifacts/feature_columns.pkl')
    return model, scaler, target_encoder, feature_columns
 
 
def predict_new(raw_row_df, model, scaler, target_encoder, feature_columns):
    df_encoded = pd.get_dummies(raw_row_df, columns=CATEGORICAL_COLUMNS, drop_first=True)
    # match training columns exactly (fills any missing dummy columns with 0)
    df_encoded = df_encoded.reindex(columns=feature_columns, fill_value=0)
    X_scaled = scaler.transform(df_encoded)
    pred_encoded = model.predict(X_scaled)
    pred_labels = target_encoder.inverse_transform(pred_encoded)
 
    # class probabilities, if the model supports it
    if hasattr(model, 'predict_proba'):
        proba = model.predict_proba(X_scaled)
        proba_df = pd.DataFrame(proba, columns=target_encoder.classes_)
        return pred_labels, proba_df
    return pred_labels, None
 
 
def example():
    new_patients = pd.DataFrame([
        {   "Age": 30, "Gender": "Male", "Medication": "ALBUTEROL", "Cholesterol": 180,
            "Respiratory_Rate": 25, "Oxygen_Saturation": 93.0, "Peak_Expiratory_Flow": 230,
            "Resting_Heart_Rate": 82, "Troponin_Level": 0.01, "Max_Heart_Rate_Achieved": 148,
            "Fasting_Blood_Sugar": 90, "HbA1c": 5.2, "Insulin_Level": 9.0,
            "Systolic_BP_Reading": 118, "Diastolic_BP_Reading": 76, "Sodium_Level": 140,
            "Wheezing_Present": "Yes", "Chest_Pain_Type": "Non-Anginal",
        },
        {  # looks like Diabetes
            "Age": 55, "Gender": "Female", "Medication": "METFORMIN", "Cholesterol": 200,
            "Respiratory_Rate": 16, "Oxygen_Saturation": 97.5, "Peak_Expiratory_Flow": 440,
            "Resting_Heart_Rate": 76, "Troponin_Level": 0.011, "Max_Heart_Rate_Achieved": 150,
            "Fasting_Blood_Sugar": 168, "HbA1c": 8.9, "Insulin_Level": 22.0,
            "Systolic_BP_Reading": 124, "Diastolic_BP_Reading": 80, "Sodium_Level": 139,
            "Wheezing_Present": "No", "Chest_Pain_Type": "Asymptomatic",
        },
    ])
 
    model, scaler, target_encoder, feature_columns = load_artifacts()
    labels, proba_df = predict_new(new_patients, model, scaler, target_encoder, feature_columns)
 
    for i, label in enumerate(labels):
        print(f'Patient {i}: predicted Condition = {label}')
        if proba_df is not None:
            print(proba_df.iloc[i].round(3).to_dict())
        print()
 
 
if __name__ == "__main__":
    example()
 