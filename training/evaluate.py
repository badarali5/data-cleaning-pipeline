from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

import numpy as np


def evaluate_classification(y_test, predictions):

    print("Accuracy:", accuracy_score(y_test, predictions))
    print("Precision:", precision_score(
        y_test, predictions, average="weighted", zero_division=0
    ))
    print("Recall:", recall_score(
        y_test, predictions, average="weighted", zero_division=0
    ))
    print("F1:", f1_score(
        y_test, predictions, average="weighted", zero_division=0
    ))


def evaluate_regression(y_test, predictions):

    mae = mean_absolute_error(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, predictions)

    print("MAE:", mae)
    print("MSE:", mse)
    print("RMSE:", rmse)
    print("R2:", r2)