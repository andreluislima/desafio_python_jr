from datetime import date
from typing import Optional

from pydantic import BaseModel, Field, field_validator


class AppointmentIn(BaseModel):
    date: date
    complaint: str = Field(..., min_length=3)
    notes: Optional[str] = None

    @field_validator("date")
    @classmethod
    def validate_appointment_date(cls, value: date) -> date:
        if value > date.today():
            raise ValueError("Data de consulta não pode ser maior que a data de hoje")
        return value


class AppointmentSummaryOut(BaseModel):
    date: date
    complaint: str
    notes: Optional[str] = None
