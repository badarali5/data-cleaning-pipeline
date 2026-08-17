import os
import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier


def load_data():
    df = pd.read_json("data/cleaned/healthcare_clean.json")
    return df.dropna(subset=["Condition"])


def build_features_target(df, categorical_columns, numerical_columns):
    df = pd.get_dummies(df, columns=categorical_columns, drop_first=True)

    categorical_features = [
        column
        for column in df.columns
        if any(column.startswith(cat + "_") for cat in categorical_columns)
    ]

    feature_columns = numerical_columns + categorical_features

    X = df[feature_columns]
    y = df["Condition"]

    return X, y, feature_columns


def get_models():
    return {
        "Logistic Regression": LogisticRegression(max_iter=1000),
        "KNN": KNeighborsClassifier(),
        "Decision Tree": DecisionTreeClassifier(random_state=42),
        "Random Forest": RandomForestClassifier(n_estimators=200, random_state=42),
        "SVM": SVC(),
        "Naive Bayes": GaussianNB(),
    }


def evaluate_models(models, X_train, X_test, y_train, y_test):
    results = {}

    for name, model in models.items():
        model.fit(X_train, y_train)

        predictions = model.predict(X_test)

        test_accuracy = accuracy_score(y_test, predictions)
        cv_scores = cross_val_score(model, X_train, y_train, cv=5)
        cv_accuracy = cv_scores.mean()

        print(f"\n{name}")
        print(f"Test Accuracy: {test_accuracy:.4f}")
        print(f"CV Accuracy: {cv_accuracy:.4f}")
        print(classification_report(y_test, predictions))

        results[name] = {
            "model": model,
            "test_accuracy": test_accuracy,
            "cv_mean": cv_accuracy,
        }

    return results


def save_best_model(results, scaler, target_encoder, feature_columns):
    best_name = max(results, key=lambda name: results[name]["cv_mean"])
    best_model = results[best_name]["model"]

    print(f"\nBest Model: {best_name} ({results[best_name]['cv_mean']:.4f} CV accuracy)")

    os.makedirs("artifacts", exist_ok=True)

    joblib.dump(best_model, "artifacts/best_model.pkl")
    joblib.dump(scaler, "artifacts/scaler.pkl")
    joblib.dump(target_encoder, "artifacts/target_encoder.pkl")
    joblib.dump(feature_columns, "artifacts/feature_columns.pkl")

    print("Model artifacts saved.")