from cleaning.clean_data import HealthcareDataCleaner
from cleaning.validate_data import DataValidator
import pandas as pd

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

if __name__ == "__main__":
    main()