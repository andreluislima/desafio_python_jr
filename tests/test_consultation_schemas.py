import pytest
from datetime import date, timedelta
from pydantic import ValidationError

from app.schemas.consultations import(
    ConsultationIn,
    PatientIn,
    AppointmentIn,
    MedicationIn
)

def test_consultation_in_valid_payload():
    payload = {
        "patient": {
            "name": "André Lima",
            "birth_date": "1995-05-10",
            "gender": "M",
        },
        "appointment": {
            "date": str(date.today()),
            "complaint": "Dor de cabeça",
            "notes": "Paciente relatou piora à noite",
        },
        "medications": [
            {"name": "Dipirona", "dosage": "500mg", "frequency": "8/8h"},
            {"name": "Omeprazol", "dosage": "20mg", "frequency": "1x ao dia"},
        ], 
    }

    model = ConsultationIn.model_validate(payload)

    assert model.patient.name == "André Lima"
    assert model.appointment.complaint == "Dor de cabeça"
    assert len(model.medications) == 2

    def test_patient_name_cannot_be_blank():
        payload = {
            "name": "  ",
            "birth_date": "1991-01-02",
            "gender": "F"
        }

        with pytest.raises(ValidationError) as exc:
            PatientIn.model_validate(payload)

    
    def test_patient_birth_date_cannot_be_future():
        tomorrow = date.today + timedelta(days=1)

        payload = {
            "name": "Maria Silva",
            "birth_date": str(tomorrow),
            "gender": "F",
        }
        with pytest.raises(ValidationError) as exc:
            PatientIn.model_validate(payload)

        errors = exc.value.errors()
        assert errors[0]["loc"] == ("birth_date")


    def test_appointment_date_cannot_be_future():
        tomorrow = date.today() + timedelta(days=1)

        payload = {
            "date": str(tomorrow),
            "complaint": "Febre",
            "notes": None,
        }

        with pytest.raises(ValidationError) as exc:
            AppointmentIn.model_validate(payload)

        errors = exc.value.errors()
        assert errors[0]["loc"] == ("date",)   

def test_medication_min_length_validation():
    payload = {"name": "AA", "dosage": "1", "frequency": "X"}

    with pytest.raises(ValidationError) as exc:
        MedicationIn.model_validate(payload)

    # Aqui geralmente virão 3 erros (name, dosage, frequency)
    errors = exc.value.errors()
    fields = {e["loc"][0] for e in errors}
    assert fields == {"name", "dosage", "frequency"}    