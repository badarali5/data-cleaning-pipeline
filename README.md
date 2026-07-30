# Data Cleaning Pipeline

A Python-based data cleaning and validation pipeline that transforms messy datasets into clean, reliable, and analysis-ready data.

## Features

- Import CSV, Excel, and JSON datasets
- Handle missing values
- Remove duplicate records
- Standardize column names and text formatting
- Convert data types
- Validate dataset structure and quality
- Generate validation reports
- Export cleaned datasets


## Installation

### Clone the repository

```bash
git clone https://github.com/your-username/data-cleaning-pipeline.git

cd data-cleaning-pipeline
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the virtual environment

**Windows**

```bash
.venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Dataset

Place your dataset inside:

```text
data/raw/
```

## Usage

### Clean the dataset

```bash
python cleaning/clean_data.py
```

### Validate the cleaned dataset

```bash
python cleaning/validate_data.py
```

---

## Data Cleaning

The pipeline performs tasks such as:

- Handling missing values
- Removing duplicate records
- Standardizing text formatting
- Renaming columns
- Converting data types
- Removing unnecessary whitespace
- Cleaning inconsistent values

---

## Data Validation

Validation checks include:

- Required columns
- Missing values
- Duplicate records
- Data types
- Numeric ranges
- Invalid or inconsistent values

---

## Output

After execution, the project generates:
cleaned_dataset.csv
validation_report.csv

---

## Technologies Used

- Python
- Pandas
- NumPy
- OpenPyXL