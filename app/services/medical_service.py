from app.repositories.medical_repository import medical_repository

class MedicalService:
    def get_all_medical_records(self):
        return medical_repository.get_all_records()

    def get_medical_record_by_id(self, record_id: str):
        record = medical_repository.get_record_by_id(record_id)
        if not record:
            raise ValueError(f"Medical record with ID {record_id} not found")
        return record

    def get_medical_record_by_field(self, field: str, value: str):
        results = medical_repository.get_record_by_field(field, value)
        if not results:
            raise ValueError(f"No records found with {field} = {value}")
        return results

    def save_medical_record(self, record_id: str, data: dict):
        if not data.get("firstName") or not data.get("lastName"):
            raise ValueError("First name and last name are required")
        return medical_repository.save_record(record_id, data)

medical_service = MedicalService()