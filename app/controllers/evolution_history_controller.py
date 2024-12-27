from fastapi import APIRouter, HTTPException
from app.services.evolution_history_service import evolution_history_service
from app.schemas.evolution_history import EvolutionHistoryInput

router = APIRouter()

@router.post("/evolution-history/{patient_id}")
def add_evolution_history(patient_id: str, entry: EvolutionHistoryInput):
    try:
        result = evolution_history_service.add_evolution_entry(patient_id, entry.dict())
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
