from pydantic import BaseModel
from typing import Optional, List, Dict

class FamilyHistory(BaseModel):
    Diabetes: Optional[Dict[str, bool]]
    Hipertensión: Optional[Dict[str, bool]]
    Colesterol_alto: Optional[Dict[str, bool]]
    Infartos: Optional[Dict[str, bool]]

class ClinicalHistoryInput(BaseModel):
    email: str  # Este es obligatorio
    phoneNumber: str  # Este también
    fullName: Optional[str] = None
    birthDate: Optional[str] = None
    age: Optional[str] = None
    city: Optional[str] = None
    occupation: Optional[str] = None
    maritalStatus: Optional[str] = None
    religion: Optional[str] = None
    otherReligion: Optional[str] = None
    gender: Optional[str] = None
    otherGender: Optional[str] = None
    familyHistory: Optional[FamilyHistory] = None
    smoke: Optional[str] = None
    smokeHistory: Optional[str] = None
    smokeOther: Optional[str] = None
    alcohol: Optional[str] = None
    alcoholHistory: Optional[str] = None
    alcoholOther: Optional[str] = None
    drug: Optional[str] = None
    drugHistory: Optional[str] = None
    exercise: Optional[str] = None
    allergicMedicine: Optional[str] = None
    allergicFood: Optional[str] = None
    surgery: Optional[str] = None
    surgeryHistory: Optional[List[str]] = None
    diagnosedDiseases: Optional[List[str]] = None
    reasonConsultation: Optional[List[str]] = None
    consultationOther: Optional[str] = None
