from fastapi import APIRouter, status

from app.schema.patient import PatientCreate, PatientUpdate
from app.schema.response import ResponseModel

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


@router.get( "/",status_code=status.HTTP_200_OK,response_model=ResponseModel)
def get_patients():

    return get_all_patients()


@router.get("/{patient_id}",status_code=status.HTTP_200_OK,response_model=ResponseModel)
def get_patient_by_id(patient_id: int):

    return get_patient(patient_id)


@router.post("/",status_code=status.HTTP_201_CREATED,response_model=ResponseModel)
def create_new_patient(patient: PatientCreate):

    return create_patient(patient.model_dump())


@router.put("/",status_code=status.HTTP_200_OK,response_model=ResponseModel)
def update_existing_patient(patient: PatientUpdate):

    return update_patient(patient.model_dump())


@router.delete("/{patient_id}",status_code=status.HTTP_200_OK,response_model=ResponseModel)
def delete_existing_patient(patient_id: int):

    return delete_patient(patient_id)