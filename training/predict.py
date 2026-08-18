import joblib
import pandas as pd

CATEGORICAL_COLUMNS = ["Gender", "Medication", "Wheezing_Present", "Chest_Pain_Type"]


def load_artifacts():
    model = joblib.load("artifacts/best_model.pkl")
    scaler = joblib.load("artifacts/scaler.pkl")
    target_encoder = joblib.load("artifacts/target_encoder.pkl")
    feature_columns = joblib.load("artifacts/feature_columns.pkl")

    return model, scaler, target_encoder, feature_columns


def predict_new(raw_row_df, model, scaler, target_encoder, feature_columns):
    df_encoded = pd.get_dummies(raw_row_df, columns=CATEGORICAL_COLUMNS, drop_first=True)
    df_encoded = df_encoded.reindex(columns=feature_columns, fill_value=0)

    X_scaled = scaler.transform(df_encoded)
    pred_encoded = model.predict(X_scaled)
    pred_labels = target_encoder.inverse_transform(pred_encoded)


    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(X_scaled)
        proba_df = pd.DataFrame(proba, columns=target_encoder.classes_)
        return pred_labels, proba_df

    return pred_labels, None