import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
class HealthcareDataCleaner:

    def __init__(self, file_path):
        self.file_path = file_path
        self.df = pd.read_csv(file_path)

    def dataset_info(self):
        print("Dataset Information:")
        self.df.info()

    def remove_duplicates(self):
        self.df.drop_duplicates(inplace=True)
        print("Removed duplicate rows.")

    def clean_patient_names(self):
        self.df["Patient Name"] = (
            self.df["Patient Name"]
            .astype(str)
            .str.strip()
            .str.title()
        )

    def clean_gender(self):
        self.df["Gender"] = (
            self.df["Gender"]
            .astype(str)
            .str.strip()
            .str.title()
        )

    def clean_age(self):
        self.df["Age"] = (
            self.df["Age"]
            .astype(str)
            .str.strip()
        )

        self.df["Age"] = pd.to_numeric(
            self.df["Age"],
            errors="coerce"
        )

        median_age = self.df["Age"].median()
        self.df["Age"] = self.df["Age"].fillna(median_age)

    def clean_cholesterol(self):
        self.df["Cholesterol"] = (
            self.df["Cholesterol"]
            .astype(str)
            .str.strip()
        )

        self.df["Cholesterol"] = pd.to_numeric(
            self.df["Cholesterol"],
            errors="coerce"
        )

        median = self.df["Cholesterol"].median()
        self.df["Cholesterol"] = self.df["Cholesterol"].fillna(median)

    def clean_blood_pressure(self):
        self.df["Blood Pressure"] = (
            self.df["Blood Pressure"]
            .astype(str)
            .str.strip()
        )

    def clean_email(self):
        self.df["Email"] = (
            self.df["Email"]
            .fillna("Unknown")
            .astype(str)
            .str.strip()
        )

    def clean_phone(self):
        self.df["Phone Number"] = (
            self.df["Phone Number"]
            .fillna("Not Provided")
            .astype(str)
            .str.strip()
        )

    def clean_dates(self):
        self.df["Visit Date"] = pd.to_datetime(
            self.df["Visit Date"],
            errors="coerce"
        )

    def save_dataset(self, output_file):
        self.df.to_json(output_file, orient="records", indent=4, date_format="iso")
        print(f"\nCleaned dataset saved as '{output_file}'")

    def outliers():
        df=pd.read_json('data/cleaned/healthcare_clean.json')
        plt.boxplot(df["Age"])
        plt.ylabel('Age')
        plt.show


    def clean_dataset(self):
        self.remove_duplicates()
        self.clean_patient_names()
        self.clean_gender()
        self.clean_age()
        self.clean_cholesterol()
        self.clean_blood_pressure()
        self.clean_email()
        self.clean_phone()
        self.clean_dates()