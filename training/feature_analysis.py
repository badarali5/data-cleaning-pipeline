import pandas as pd
from scipy.stats import chi2_contingency, f_oneway

def load_data():
    df = pd.read_json("data/cleaned/healthcare_clean.json")
    df = df.dropna(subset=["Condition"])
    return df


def get_categorical_columns():
    return [
        "Gender",
        "Medication",
        "Wheezing_Present",
        "Chest_Pain_Type"
    ]


def get_numerical_columns():
    return [
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


def analyze_categorical_columns(df, categorical_columns):
    selected_columns = []

    for column in categorical_columns:

        table = pd.crosstab(df[column],df["Condition"])
        chi2, p_value, dof, expected = chi2_contingency(table)

        print("Categorical Column:", column)
        print("Chi-square:", round(chi2, 4))
        print("P-value:", round(p_value, 6))

        if p_value < 0.05:
            selected_columns.append(column)
            print("Selected: Yes")
        else:
            print("Selected: No")

        print()

    return selected_columns


def analyze_numerical_features(df, numerical_columns):
    selected_columns = []

    condition_labels = df["Condition"].unique()

    for column in numerical_columns:

        groups = [
            df[df["Condition"] == label][column].dropna()
            for label in condition_labels
        ]

        f_statistics, p_value = f_oneway(*groups)

        print("Numerical Column:", column)
        print("F-statistics:", round(f_statistics, 4))
        print("P-value:", round(p_value, 6))

        if p_value < 0.05:
            selected_columns.append(column)
            print("Selected: Yes")
        else:
            print("Selected: No")

        print()

    return selected_columns


def analyze_correlation(df, numerical_columns):
    correlation_matrix = df[numerical_columns].corr()

    print("Correlation Matrix:")
    print(correlation_matrix)


def get_selected_features(df):
    categorical_columns = get_categorical_columns()
    numerical_columns = get_numerical_columns()

    print("\n CATEGORICAL FEATURE ANALYSIS \n")

    selected_categorical = analyze_categorical_columns(df,categorical_columns)

    print("\n NUMERICAL FEATURE ANALYSIS \n")

    selected_numerical = analyze_numerical_features(df,numerical_columns)

    print("\n CORRELATION ANALYSIS \n")

    analyze_correlation(df,numerical_columns)

    print("\n SELECTED FEATURES \n")

    print("Selected categorical features:")
    print(selected_categorical)

    print("\nSelected numerical features:")
    print(selected_numerical)

    return selected_categorical, selected_numerical