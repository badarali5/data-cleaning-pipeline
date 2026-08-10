import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def prepare_data(file_path, target):
    df = pd.read_json(file_path)
    df = df.drop(
        columns=["Patient Name", "Email", "Phone Number", "Visit Date"],
        errors="ignore"
    )

    df = df.dropna(subset=[target])

    X = df.drop(target, axis=1)
    y = df[target]

    for col in X.select_dtypes(include="object"):
        encoder = LabelEncoder()
        X[col] = encoder.fit_transform(X[col].astype(str))

    if y.dtype == "object":
        encoder = LabelEncoder()
        y = encoder.fit_transform(y.astype(str))

    return train_test_split(
        X, y, test_size=0.2, random_state=42
    )