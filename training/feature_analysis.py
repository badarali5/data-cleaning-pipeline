import pandas as pd
from scipy.stats import chi2_contingency, f_oneway


def load_data():
    df = pd.read_json('data/cleaned/healthcare_clean.json')
    df = df.dropna(subset=['Condition'])  
    return df


def get_catagorical_columns():
    catagorical_columns = [
        "Gender",
        "Medication",
        "Wheezing_Present",
        "Chest_Pain_Type",
    ]
    return catagorical_columns


def analyze_catagorical_columns(df, catagorical_columns):
    for catagorical_column in catagorical_columns:
        table = pd.crosstab(
            df[catagorical_column],
            df['Condition']
        )
        print(table)
        chi2, p_value, dof, expected = chi2_contingency(table)
        print('Categorical Column:', catagorical_column)
        print('Chi_square:', round(chi2, 4))
        print('P_value:', round(p_value, 6))
        print()


def get_numerical_columns():
    numerical_columns = [
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
        "Sodium_Level",
    ]
    return numerical_columns


def analyze_numerical_features(df, numerical_columns):
    groups_labels = df['Condition'].unique()
    for numerical_column in numerical_columns:
        groups = [df[df['Condition'] == label][numerical_column] for label in groups_labels]
        f_statistics, p_value = f_oneway(*groups)
        print('Numerical Column:', numerical_column)
        print('F_statistics:', round(f_statistics, 4))
        print('P_value:', round(p_value, 6))
        print()


def analyze_correlation(df, numerical_columns):
    correlation_matrix = df[numerical_columns].corr()
    print('Correlation Matrix:\n', correlation_matrix)


def main():
    df = load_data()
    catagorical_columns = get_catagorical_columns()
    numerical_columns = get_numerical_columns()
    analyze_catagorical_columns(df, catagorical_columns)
    analyze_numerical_features(df, numerical_columns)
    analyze_correlation(df, numerical_columns)


if __name__ == "__main__":
    main()