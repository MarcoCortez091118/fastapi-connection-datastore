from app.core.firebase import firebase

class EvolutionHistoryRepository:
    def __init__(self):
        self.db = firebase.get_db()

    def add_evolution_entry(self, patient_id: str, data: dict):
        """
        Agrega un nuevo registro de evolución asociado a un paciente.
        """
        doc_ref = self.db.collection("evolution_history").document(patient_id)
        doc = doc_ref.get()

        if doc.exists:
            existing_data = doc.to_dict()
            if "history" not in existing_data:
                existing_data["history"] = []
            existing_data["history"].append(data)
            doc_ref.set(existing_data)
        else:
            doc_ref.set({"history": [data]})
        return {"message": "Evolution entry added successfully", "patient_id": patient_id}

evolution_history_repository = EvolutionHistoryRepository()
