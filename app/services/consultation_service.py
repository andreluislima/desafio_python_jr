from __future__ import annotations

from datetime import date
from typing import List

from app.schemas.consultations import ConsultationIn, ConsultationSummaryOut


def calculate_age(birth_date: date, reference_date: date) -> int:
    years = reference_date.year - birth_date.year

    had_birthday = (
        reference_date.month, reference_date.day
        ) >= (birth_date.month, birth_date.day)

    if had_birthday:
        return years
    return years -1


def normalize_gender(raw: str) -> str:
    value = (raw or "").strip().lower()

    female_set = {"f", "female", "feminino", "mulher"}
    male_set = {"m", "male", "masculino", "homem"}

    if value in female_set:
        return "female"
    if value in male_set:
        return "male"
    return "other"


def process_consultation(payload: ConsultationIn) -> ConsultationSummaryOut:
    age = calculate_age(payload.patient.birth_date, payload.appointment.date)
    gender_norm = normalize_gender(payload.patient.gender)

    medications_fmt: List[str] = [
        f"{m.name} {m.dosage} ({m.frequency})"
        for m in payload.medications
    ]

    gender_pt = {"female": "feminino", "male": "masculino", "other": "outro"}[gender_norm]
    text_summary = (
        f"Paciente {payload.patient.name}, {age} anos, sexo {gender_pt}. "
        f"Queixa principal: {payload.appointment.complaint}."
    )

    return ConsultationSummaryOut(
        patient={
            "name": payload.patient.name,
            "age": age,
            "gender": gender_norm,
        },
        appointment={
            "date": payload.appointment.date,
            "complaint": payload.appointment.complaint,
            "notes": payload.appointment.notes,
        },
        medications=medications_fmt,
        text_summary=text_summary,
    )
