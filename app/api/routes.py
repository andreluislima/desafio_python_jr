from fastapi import APIRouter
from app.api.endpoints.consultations import router as consultation_router

api_router = APIRouter()

api_router.include_router(
    consultation_router,
    prefix="/consultations",
    tags=["Consultations"]
)
