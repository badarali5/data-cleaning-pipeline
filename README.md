# Data Cleaning and Machine Learning Pipeline

A Python-based data processing and machine learning pipeline that cleans and validates healthcare data, performs feature analysis, trains classification models, and generates predictions for patient conditions.

## Project Overview

This project follows a complete machine learning workflow:

1. Load raw healthcare data
2. Clean and preprocess the dataset
3. Validate data quality
4. Analyze feature relationships with the target variable
5. Train multiple classification models
6. Evaluate model performance
7. Generate predictions for new patient data

The target variable is **Condition**, which contains the following classes:

* Asthma
* Diabetes
* Heart Disease
* Hypertension

## Project Structure

```text
data-cleaning-pipeline/
│
├── artifacts/
│   └── Trained models and related artifacts
│
├── cleaning/
│   ├── clean_data.py
│   └── validate_data.py
│
├── data/
│   ├── raw/
│   │   └── Original dataset
│   └── cleaned/
│       └── Cleaned dataset
│
├── training/
│   ├── feature_analysis.py
│   ├── model_training.py
│   └── predict.py
│
├── validation_report/
│   └── Generated validation reports
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Features

### Data Cleaning

* Import raw CSV datasets
* Handle missing values
* Remove duplicate records
* Standardize column names
* Remove unnecessary whitespace
* Standardize inconsistent text values
* Convert columns to appropriate data types
* Export cleaned datasets

### Data Validation

The validation pipeline checks:

* Required columns
* Missing values
* Duplicate records
* Data types
* Numeric ranges
* Invalid or inconsistent values
* Overall dataset structure and quality

Validation results are stored in the `validation_report/` directory.

### Feature Analysis

The project analyzes the relationship between input features and the target variable, `Condition`.

For categorical features, **Chi-Square tests** are used to evaluate whether there is a significant relationship with the target.

For numerical features, **ANOVA** is used to compare differences between condition groups.

This analysis helps identify which features may be useful for classification.

### Machine Learning

The training pipeline supports multiple classification algorithms, including:

* Logistic Regression
* K-Nearest Neighbors (KNN)
* Decision Tree
* Random Forest
* Support Vector Machine (SVM)
* Gaussian Naive Bayes

The models are trained using the cleaned dataset and evaluated using classification metrics.

### Prediction

The `predict.py` script loads the trained model and generates predictions for new patient records.

Example:

```text
Patient 0: predicted Condition = Asthma
Patient 1: predicted Condition = Diabetes
```

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/data-cleaning-pipeline.git
cd data-cleaning-pipeline
```

### Create a Virtual Environment

```bash
python -m venv .venv
```

### Activate the Virtual Environment

**Windows:**

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Dataset

Place the original dataset inside:

```text
data/raw/
```

The cleaned dataset will be generated inside:

```text
data/cleaned/
```

## Usage

### 1. Clean the Dataset

```bash
python cleaning/clean_data.py
```

This processes the raw dataset and generates a cleaned version.

### 2. Validate the Dataset

```bash
python cleaning/validate_data.py
```

This performs data-quality checks and generates validation results.

### 3. Perform Feature Analysis

```bash
python training/feature_analysis.py
```

This analyzes relationships between the available features and the target variable, `Condition`.

### 4. Train the Models

```bash
python training/model_training.py
```

This trains the supported classification models and evaluates their performance.

Trained models and related files are stored in:

```text
artifacts/
```

### 5. Generate Predictions

```bash
python training/predict.py
```

This loads the trained model and predicts the condition for new patient records.

## Machine Learning Workflow

```text
Raw Dataset
     │
     ▼
Data Cleaning
     │
     ▼
Data Validation
     │
     ▼
Feature Analysis
     │
     ▼
Feature Selection / Preprocessing
     │
     ▼
Model Training
     │
     ▼
Model Evaluation
     │
     ▼
Trained Model
     │
     ▼
Prediction
```

## Target Variable

The model predicts the patient's **Condition**.

| Condition     |
| ------------- |
| Asthma        |
| Diabetes      |
| Heart Disease |
| Hypertension  |

## Output

The project generates several types of output.

### Cleaned Data

```text
data/cleaned/
```

Contains the processed dataset ready for analysis and machine learning.

### Validation Reports

```text
validation_report/
```

Contains reports describing the quality and validity of the dataset.

### Model Artifacts

```text
artifacts/
```

Contains trained machine learning models and other files required for prediction.

### Predictions

The prediction script outputs the predicted condition for each input patient.

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* SciPy
* Matplotlib
* Seaborn

## Project Goal

The goal of this project is to demonstrate an end-to-end data processing and machine learning workflow, from raw healthcare data to validated data, statistical feature analysis, trained classification models, and patient condition predictions.
