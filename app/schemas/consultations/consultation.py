from typing import List

from pydantic import BaseModel, Field

from .patient import PatientIn, PatientSummaryOut
from .appointment import AppointmentIn, AppointmentSummaryOut
from .medication import MedicationIn


class ConsultationIn(BaseModel):
    patient: PatientIn
    appointment: AppointmentIn
    medications: List[MedicationIn] = Field(default_factory=list)


class ConsultationSummaryOut(BaseModel):
    patient: PatientSummaryOut
    appointment: AppointmentSummaryOut
    medications: List[str]
    text_summary: str
