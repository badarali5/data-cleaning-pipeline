from fastapi import APIRouter, status

from app.schema.patient import PatientCreate, PatientUpdate
from app.services.patient_service import (
    get_all_patients,
    get_patient,
    create_patient,
    update_patient,
    delete_patient
)

router = APIRouter(
    prefix="/patients",
    tags=["Patients"]
)


@router.get("/")
def get_patients():
    patients = get_all_patients()
    return {
        "status": "success",
        "message": "Patients retrieved successfully",
        "data": patients
    }


@router.get("/{patient_id}")
def get_patient_by_id(patient_id: int):
    patient = get_patient(patient_id)
    return {
        "status": "success",
        "message": "Patient retrieved successfully",
        "data": patient
    }


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_new_patient(patient: PatientCreate):
    new_patient = create_patient(patient.model_dump())
    return {
        "status": "success",
        "message": "Patient created successfully",
        "data": new_patient
    }


@router.put("/{patient_id}")
def update_existing_patient(patient_id: int, patient: PatientUpdate):
    updated_patient = update_patient(patient_id, patient.model_dump())
    return {
        "status": "success",
        "message": "Patient updated successfully",
        "data": updated_patient
    }


@router.delete("/{patient_id}")
def delete_existing_patient(patient_id: int):
    deleted_patient = delete_patient(patient_id)
    return {
        "status": "success",
        "message": "Patient deleted successfully",
        "data": deleted_patient
    }