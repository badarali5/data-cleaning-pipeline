import pandas as pd
import json


class DataValidator:

    def __init__(self, file_path):
        self.df = pd.read_json(file_path)

    def validate(self):

        report = {}

        report["rows"] = len(self.df)
        report["columns"] = len(self.df.columns)

        report["missing_values"] = self.df.isnull().sum().to_dict()

        report["duplicate_rows"] = int(self.df.duplicated().sum())

        report["data_types"] = {
            col: str(dtype)
            for col, dtype in self.df.dtypes.items()
        }

        report["validation_passed"] = (
            report["duplicate_rows"] == 0
            and sum(report["missing_values"].values()) == 0
        )

        with open( "validation_report/validation_report.json","w") as file:
            json.dump(report, file, indent=4)

        print("Validation report generated successfully.")