from datetime import date
from pydantic import BaseModel, Field, field_validator

from typing import Optional

class AppointamentIn(BaseModel):
    date = date
    complaint: str = Field(..., min_length=3)
    notes: Optional[str] = None
    
    @field_validator("date")
    @classmethod
    def validate_appointament_date(cls, value:date):
        if value > date.today():
            raise ValueError("Data de consulta não pode ser maior que a data de hoje")
        return value