from pydantic import BaseModel
from typing import Optional


class PatientBase(BaseModel):
    patient_name: str
    age: int
    gender: str
    condition: Optional[str] = None
    medication: str
    cholesterol: float
    respiratory_rate: int
    oxygen_saturation: float
    fasting_blood_sugar: float
    hba1c: float
    insulin_level: float
    systolic_bp_reading: float
    diastolic_bp_reading: float
    wheezing_present: str
    chest_pain_type: str


class PatientCreate(PatientBase):
    pass


class PatientUpdate(PatientBase):
    pass


class Patient(PatientBase):
    patient_id: int