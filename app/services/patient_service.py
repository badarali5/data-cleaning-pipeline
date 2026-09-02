import json
from fastapi import HTTPException

from app.schema.response import ResponseModel

FILE_PATH = "data/cleaned/healthcare_clean.json"

REQUIRED_FIELDS = [
    "patient_name",
    "age",
    "gender",
    "medication",
    "cholesterol",
    "respiratory_rate",
    "oxygen_saturation",
    "fasting_blood_sugar",
    "hba1c",
    "insulin_level",
    "systolic_bp_reading",
    "diastolic_bp_reading",
    "wheezing_present",
    "chest_pain_type",
]


def validate_required_fields(patient: dict):
    missing = [
        field for field in REQUIRED_FIELDS
        if patient.get(field) is None
    ]
    if missing:
        raise HTTPException(
            status_code=422,
            detail=f"Missing required fields: {', '.join(missing)}"
        )


def read_patients():
    with open(FILE_PATH, "r") as file:
        return json.load(file)


def write_patients(patients):
    with open(FILE_PATH, "w") as file:
        json.dump(patients, file, indent=4)


def get_all_patients():
    patients = read_patients()
    return ResponseModel(
        status_code=200,
        status="success",
        message="Patients retrieved successfully",
        data=patients
    )


def get_patient(patient_id: int):
    patients = read_patients()

    for patient in patients:
        if patient["patient_id"] == patient_id:
            return ResponseModel(
                status_code=200,
                status="success",
                message="Patient retrieved successfully",
                data=patient
            )

    raise HTTPException(status_code=404, detail="Patient not found")


def create_patient(patient: dict):
    validate_required_fields(patient)

    patients = read_patients()
    patient_id = patient["patient_id"]

    for existing_patient in patients:
        if existing_patient["patient_id"] == patient_id:
            raise HTTPException(
                status_code=400,
                detail={
                    "message": "Patient ID already exists",
                    "patient": existing_patient
                }
            )

    patients.append(patient)
    write_patients(patients)

    return ResponseModel(
        status_code=201,
        status="success",
        message="Patient created successfully",
        data=patient
    )


def update_patient(updated_patient: dict):
    validate_required_fields(updated_patient)

    patients = read_patients()

    for i, patient in enumerate(patients):
        if patient["patient_id"] == updated_patient["patient_id"]:
            patients[i] = updated_patient
            write_patients(patients)

            return ResponseModel(
                status_code=200,
                status="success",
                message="Patient updated successfully",
                data=updated_patient
            )

    raise HTTPException(status_code=404, detail="Patient not found")


def delete_patient(patient_id: int):
    patients = read_patients()

    for i, patient in enumerate(patients):
        if patient["patient_id"] == patient_id:
            deleted_patient = patients.pop(i)
            write_patients(patients)

            return ResponseModel(
                status_code=200,
                status="success",
                message="Patient deleted successfully",
                data=deleted_patient
            )

    raise HTTPException(status_code=404, detail="Patient not found")