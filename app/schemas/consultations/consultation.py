from pydantic import BaseModel, Field, field_validator
from consultations import patient
from consultations import appointament
from consultations import medication


class ConsultationIn(BaseModel):
    patient: patient.PatientIn
    appointament: appointament.AppointamentIn
    medication: List[medication.MedicationIn] = Field(default_factory=list)
    
    