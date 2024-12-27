from pydantic import BaseModel
from typing import Optional, List

# Modelo para la dirección
class Address(BaseModel):
    street: str
    number: str
    postalCode: str
    neighborhood: str
    city: str
    state: str
    country: str

# Modelo para personas relacionadas
class RelatedPerson(BaseModel):
    name: str
    relation: str
    profession: str

# Modelo para el registro médico completo
class MedicalRecordInput(BaseModel):
    firstName: str
    lastName: str
    birthDate: str
    gender: str
    patientType: str
    id: str
    patientStatus: str
    dataResponsible: str
    birthCity: str
    birthState: str
    nationality: str
    idType: str
    idNumber: str
    phone: str
    email: str
    additionalPhone: Optional[str]
    address: Address
    religion: Optional[str]
    maritalStatus: Optional[str]
    education: Optional[str]
    profession: Optional[str]
    consent: bool
    sendReminders: bool
    relatedPersons: List[RelatedPerson]
    authorizedPerson: Optional[str]
    legalRepresentative: Optional[str]
