import pandas as pd

class DataValidator:

    def __init__(self, dataframe):
        self.df = dataframe

    def validate_missing(self):

        print("Missing Values")
        print(self.df.isnull().sum())

    def validate_age(self):
        invalid = self.df[
            (self.df["Age"] < 0) |
            (self.df["Age"] > 120)
        ]
        print(f"Invalid Ages: {len(invalid)}")

    def validate_duplicates(self):
        duplicates = self.df.duplicated().sum()
        print(f"Duplicate Rows: {duplicates}")

    def validate(self):
        self.validate_missing()
        self.validate_age()
        self.validate_duplicates()

        print("\nValidation Complete.")