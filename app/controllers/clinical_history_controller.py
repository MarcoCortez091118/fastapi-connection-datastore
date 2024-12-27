from fastapi import APIRouter, HTTPException
from app.services.clinical_history_service import clinical_history_service
from app.schemas.clinical_history import ClinicalHistoryInput

router = APIRouter()

@router.post("/clinical-history")
def add_clinical_history(record: ClinicalHistoryInput):
    try:
        result = clinical_history_service.add_history(record.email, record.dict())
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/clinical-history/{email}")
def get_clinical_history(email: str):
    try:
        result = clinical_history_service.get_history(email)
        return result
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
