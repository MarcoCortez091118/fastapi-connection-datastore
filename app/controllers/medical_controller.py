from fastapi import APIRouter, HTTPException
from app.services.medical_service import medical_service
from app.schemas.medical_record import MedicalRecordInput


router = APIRouter()

@router.get("/records")
def get_all_records():
    try:
        records = medical_service.get_all_medical_records()
        return {"records": records}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/records/{record_id}")
def get_record_by_id(record_id: str):
    try:
        record = medical_service.get_medical_record_by_id(record_id)
        return {"record": record}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/records/search")
def get_record_by_field(field: str, value: str):
    """
    Busca registros por un campo específico y un valor dado.
    """
    try:
        results = medical_service.get_medical_record_by_field(field, value)
        if not results:
            return {"detail": f"No se encontraron resultados para {field} = {value}"}
        return {"results": results}
    except Exception as e:
        return {"error": str(e)}

@router.post("/records")
def save_record(record: MedicalRecordInput):
    try:
        result = medical_service.save_medical_record(record.id, record.dict())
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))