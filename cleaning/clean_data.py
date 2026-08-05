import pandas as pd
import numpy as np


df = pd.read_csv("data/raw/student_performance_messy.csv")

print(f"Original Shape: {df.shape}")

def check_duplicates():
    duplicates = df.duplicated().sum()
    print(f"Duplicate rows found: {duplicates}")
    df = df.drop_duplicates()


def check_missing_values():
    missing_values = df.isnull().sum()
    print("Missing values per column:")
    print(missing_values)    