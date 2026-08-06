from cleaning.clean_data import HealthcareDataCleaner
from cleaning.validate_data import DataValidator


def main():
    
    input_file = "data/raw/healthcare_messy_data.csv"
    output_file = "data/cleaned/healthcare_cleaned.json"

    cleaner = HealthcareDataCleaner(input_file)

    print("Original Dataset")
    cleaner.dataset_info()

    cleaner.clean_dataset()
    validator = DataValidator(cleaner.df)
    validator.validate()

    cleaner.save_dataset(output_file)

    print("\nCleaning Complete.")


if __name__ == "__main__":
    main()