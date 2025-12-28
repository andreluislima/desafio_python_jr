from pydantic import BaseModel, Field


class MedicationIn(BaseModel):
    name: str = Field(..., min_length=3)
    dosage: str = Field(..., min_length=3)
    frequency: str = Field(..., min_length=3)
