import os
import joblib
import pandas as pd

from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier


CATEGORICAL_COLUMNS = [
    "Gender",
    "Medication",
    "Wheezing_Present",
    "Chest_Pain_Type"
]

NUMERICAL_COLUMNS = [
    "Age",
    "Cholesterol",
    "Respiratory_Rate",
    "Oxygen_Saturation",
    "Peak_Expiratory_Flow",
    "Resting_Heart_Rate",
    "Troponin_Level",
    "Max_Heart_Rate_Achieved",
    "Fasting_Blood_Sugar",
    "HbA1c",
    "Insulin_Level",
    "Systolic_BP_Reading",
    "Diastolic_BP_Reading",
    "Sodium_Level"
]


def load_data():
    df = pd.read_json("data/cleaned/healthcare_clean.json")
    return df.dropna(subset=["Condition"])


def build_features_target(df):
    df = pd.get_dummies(
        df,
        columns=CATEGORICAL_COLUMNS,
        drop_first=True
    )

    feature_columns = NUMERICAL_COLUMNS + [
        column
        for column in df.columns
        if any(column.startswith(cat + "_") for cat in CATEGORICAL_COLUMNS)
    ]

    X = df[feature_columns]
    y = df["Condition"]

    return X, y, feature_columns


def get_models():
    return {
        "Logistic Regression": LogisticRegression(max_iter=1000),
        "KNN": KNeighborsClassifier(),
        "Decision Tree": DecisionTreeClassifier(random_state=42),
        "Random Forest": RandomForestClassifier(
            n_estimators=200,
            random_state=42
        ),
        "SVM": SVC(),
        "Naive Bayes": GaussianNB()
    }


def evaluate_models(models, X_train, X_test, y_train, y_test):
    results = {}

    for name, model in models.items():
        model.fit(X_train, y_train)

        predictions = model.predict(X_test)
        test_accuracy = accuracy_score(y_test, predictions)

        cv_scores = cross_val_score(
            model,
            X_train,
            y_train,
            cv=5
        )

        print(f"\n{name}")
        print(f"Test Accuracy: {test_accuracy:.4f}")
        print(f"CV Accuracy: {cv_scores.mean():.4f}")
        print(classification_report(y_test, predictions))

        results[name] = {
            "model": model,
            "test_accuracy": test_accuracy,
            "cv_mean": cv_scores.mean()
        }

    return results


def save_best_model(results, scaler, target_encoder, feature_columns):
    best_name = max(
        results,
        key=lambda name: results[name]["cv_mean"]
    )

    best_model = results[best_name]["model"]

    print(
        f"\nBest Model: {best_name} "
        f"({results[best_name]['cv_mean']:.4f} CV accuracy)"
    )

    os.makedirs("artifacts", exist_ok=True)

    joblib.dump(best_model, "artifacts/best_model.pkl")
    joblib.dump(scaler, "artifacts/scaler.pkl")
    joblib.dump(target_encoder, "artifacts/target_encoder.pkl")
    joblib.dump(feature_columns, "artifacts/feature_columns.pkl")

    print("Model artifacts saved.")

