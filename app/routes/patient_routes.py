from typing import Dict, Any
from fastapi import APIRouter, HTTPException, Body


from app.services.patient_service import (
    get_all_patients,
    get_patient,
    create_patient
)

router = APIRouter(
    prefix="/patients",
    tags=["Patients"]
)


@router.get("/")
def get_patients():
    return get_all_patients()


@router.get("/{patient_id}")
def get_patient_by_id(patient_id: int):

    patient = get_patient(patient_id)

    if patient is None:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )


    return patient


@router.post("/")
def create_new_patient(patient: Dict[str, Any] = Body(...)):

    return create_patient(patient)