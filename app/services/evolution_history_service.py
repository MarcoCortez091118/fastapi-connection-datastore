from app.repositories.evolution_history_repository import evolution_history_repository

class EvolutionHistoryService:
    def add_evolution_entry(self, patient_id: str, data: dict):
        if not patient_id:
            raise ValueError("Patient ID is required")
        return evolution_history_repository.add_evolution_entry(patient_id, data)

evolution_history_service = EvolutionHistoryService()
