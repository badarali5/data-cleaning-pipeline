import json
from fastapi import HTTPException

FILE_PATH = "data/cleaned/healthcare_clean.json"

def read_patients():
    with open(FILE_PATH, "r") as file:
        return json.load(file)

def write_patients(patients):
    with open(FILE_PATH, "w") as file:
        json.dump(patients, file, indent=4)

def get_all_patients():
    return read_patients()

def get_patient(patient_id: int):
    patients = read_patients()
    for patient in patients:
        if patient["patient_id"] == patient_id:
            return patient
    raise HTTPException(status_code=404, detail="Patient not found")

def create_patient(patient: dict):
    patients = read_patients()

    new_id = max([p["patient_id"] for p in patients],default=0) + 1

    patient["patient_id"] = new_id
    patients.append(patient)
    write_patients(patients)
    return patient

def update_patient(patient_id: int, updated_fields: dict):
    patients = read_patients()
    
    for i, patient in enumerate(patients):
        if patient["patient_id"] == patient_id:
            updated_fields["patient_id"] = patient_id
            patients[i] = updated_fields
            write_patients(patients)
            return updated_fields
    raise HTTPException(status_code=404, detail="Patient not found")

def delete_patient(patient_id: int):
    patients = read_patients()
    for i, patient in enumerate(patients):
        if patient["patient_id"] == patient_id:
            deleted_patient = patients.pop(i)
            write_patients(patients)
            return deleted_patient

    raise HTTPException(status_code=404, detail="Patient not found")