from datetime import date
from pydantic import BaseModel, Field, field_validator

from typing import Optional

class MedicationIn(BaseModel):
    name: str = Field(..., min_length=3)
    dosage: str = Field(..., min_length=3)
    frequency: str = Field(..., min_length=3)