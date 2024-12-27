from app.core.firebase import firebase

class ClinicalHistoryRepository:
    def __init__(self):
        self.db = firebase.get_db()

    def add_history(self, email: str, data: dict):
        """
        Agrega un nuevo registro al historial clínico de un paciente.
        """
        doc_ref = self.db.collection("clinical_history").document(email)
        doc = doc_ref.get()

        if doc.exists:
            existing_data = doc.to_dict()
            if "history" not in existing_data:
                existing_data["history"] = []
            existing_data["history"].append(data)
            doc_ref.set(existing_data)
        else:
            doc_ref.set({"history": [data]})
        return {"message": "Record added to history successfully", "email": email}

    def get_history(self, email: str):
        """
        Recupera el historial clínico completo de un paciente.
        """
        doc_ref = self.db.collection("clinical_history").document(email)
        doc = doc_ref.get()

        if doc.exists:
            return doc.to_dict()
        return None

clinical_history_repository = ClinicalHistoryRepository()
