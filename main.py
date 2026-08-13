from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

from cleaning.clean_data import HealthcareDataCleaner
from cleaning.validate_data import DataValidator
import pandas as pd

from training.feature_analysis import analyze_catagorical_columns, analyze_correlation, analyze_numerical_features, get_catagorical_columns, get_numerical_columns
from training.model_training import build_features_target, evaluate_models, get_models, load_data, save_best_model
from training.predict import load_artifacts, predict_new

FILE_PATH = "data/cleaned/healthcare_cleaned.json"

    
def main():
    input_file = "data/raw/healthcare_messy_data.csv"
    output_file = "data/cleaned/healthcare_cleaned.json"

    cleaner = HealthcareDataCleaner(input_file)

    print("Original Dataset")
    cleaner.dataset_info()

    cleaner.clean_dataset()

    cleaner.save_dataset(output_file)

    validator = DataValidator(output_file)
    validator.validate()

    print("Cleaning Complete.")
    
    df = load_data()
    catagorical_columns = get_catagorical_columns()
    numerical_columns = get_numerical_columns()
    analyze_catagorical_columns(df, catagorical_columns)
    analyze_numerical_features(df, numerical_columns)
    analyze_correlation(df, numerical_columns)

    df = load_data()
    
    X, y, feature_columns = build_features_target(df)

    target_encoder = LabelEncoder()
    y = target_encoder.fit_transform(y)
    
    X_train, X_test, y_train, y_test = train_test_split(
        X,
            y,
            test_size=0.2,
            random_state=42,
            stratify=y
        )
    
    scaler = StandardScaler()
    
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    baseline = DummyClassifier(strategy="most_frequent")
    baseline.fit(X_train, y_train)
    
    baseline_accuracy = accuracy_score(
        y_test,
        baseline.predict(X_test)
        )
    
    print(f"Baseline Accuracy: {baseline_accuracy:.4f}")
    
    models = get_models()
    
    results = evaluate_models(
            models,
            X_train,
            X_test,
            y_train,
            y_test
        )
    
    save_best_model(
            results,
            scaler,
            target_encoder,
            feature_columns
        )
    
    new_patients = pd.DataFrame([
        {   "Age": 30, "Gender": "Male", "Medication": "ALBUTEROL", "Cholesterol": 180,
            "Respiratory_Rate": 25, "Oxygen_Saturation": 93.0, "Peak_Expiratory_Flow": 230,
            "Resting_Heart_Rate": 82, "Troponin_Level": 0.01, "Max_Heart_Rate_Achieved": 148,
            "Fasting_Blood_Sugar": 90, "HbA1c": 5.2, "Insulin_Level": 9.0,
            "Systolic_BP_Reading": 118, "Diastolic_BP_Reading": 76, "Sodium_Level": 140,
            "Wheezing_Present": "Yes", "Chest_Pain_Type": "Non-Anginal",
        },
        { "Age": 55, "Gender": "Female", "Medication": "METFORMIN", "Cholesterol": 200,
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
        main()