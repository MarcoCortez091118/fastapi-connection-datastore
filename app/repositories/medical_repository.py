from app.core.firebase import firebase
from app.models.medical_record import MedicalRecord

class MedicalRepository:
    def __init__(self):
        self.db = firebase.get_db()

    def get_all_records(self):
        collection = self.db.collection("medical_records")
        docs = collection.stream()
        return [doc.to_dict() for doc in docs]

    def get_record_by_id(self, record_id: str):
        doc = self.db.collection("medical_records").document(record_id).get()
        if doc.exists:
            return doc.to_dict()
        return None

    def get_record_by_field(self, field: str, value: str):
        try:
            print(f"Buscando documentos donde {field} = {value}")
            collection = self.db.collection("medical_records")
            query = collection.where(field, "==", value).stream()
            results = [doc.to_dict() for doc in query]
            print(f"Documentos encontrados: {len(results)}")
            return results
        except Exception as e:
            print(f"Error durante la búsqueda: {str(e)}")
            return []

    def save_record(self, record_id: str, data: dict):
        """
        Guarda un nuevo registro o actualiza uno existente.
        """
        doc_ref = self.db.collection("medical_records").document(record_id)
        doc_ref.set(data)
        return {"message": "Record saved successfully", "id": record_id}


medical_repository = MedicalRepository()
