# from cleaning.clean_data import HealthcareDataCleaner
# from cleaning.validate_data import DataValidator
# import pandas as pd

# from training.train_classification import train_classification
# from training.train_regression import train_regression
# from training.evaluate import evaluate_classification, evaluate_regression
# from training.preprocess import prepare_data

# FILE_PATH = "data/cleaned/healthcare_cleaned.json"

#     # input_file = "data/raw/healthcare_messy_data.csv"
#     # output_file = "data/cleaned/healthcare_cleaned.json"

#     # cleaner = HealthcareDataCleaner(input_file)

#     # print("Original Dataset")
#     # cleaner.dataset_info()

#     # cleaner.clean_dataset()

#     # cleaner.save_dataset(output_file)

#     # validator = DataValidator(output_file)
#     # validator.validate()

#     # print("Cleaning Complete.")
# def main():
#     X_train, X_test, y_train, y_test = prepare_data(
#         FILE_PATH,
#         "classification"
#     )

#     classification_results = train_classification(
#         X_train,
#         X_test,
#         y_train,
#         y_test
#     )

#     for name, (model, predictions) in classification_results.items():
#         print(f"\n{name}")
#         evaluate_classification(
#             y_test,
#             predictions
#         )

#     X_train, X_test, y_train, y_test = prepare_data(
#         FILE_PATH,
#         "regression"
#     )

#     regression_results = train_regression(
#         X_train,
#         X_test,
#         y_train,
#         y_test
#     )

#     for name, (model, predictions) in regression_results.items():
#         print(f"\n{name}")
#         evaluate_regression(
#             y_test,
#             predictions
#         )

# if __name__ == "__main__":
#     main()