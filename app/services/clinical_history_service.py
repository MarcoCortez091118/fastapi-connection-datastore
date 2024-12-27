from app.repositories.clinical_history_repository import clinical_history_repository

class ClinicalHistoryService:
    def add_history(self, email: str, data: dict):
        if not email:
            raise ValueError("Email is required")
        return clinical_history_repository.add_history(email, data)

    def get_history(self, email: str):
        if not email:
            raise ValueError("Email is required")
        history = clinical_history_repository.get_history(email)
        if not history:
            raise ValueError(f"No clinical history found for {email}")
        return history

clinical_history_service = ClinicalHistoryService()
