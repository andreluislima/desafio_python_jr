from fastapi import APIRouter, status

from app.schemas.consultations import ConsultationIn, ConsultationSummaryOut
from app.services.consultation_service import process_consultation

router = APIRouter()

@router.post("/", response_model=ConsultationSummaryOut, status_code=status.HTTP_201_CREATED)
async def create_consultation(payload: ConsultationIn):
    return process_consultation(payload)