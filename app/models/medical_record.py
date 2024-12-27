from pydantic import BaseModel
from typing import Optional

class MedicalRecord(BaseModel):
    id: Optional[str]
    nationality: Optional[str]
    number: Optional[str]
    observations: Optional[str]
    other_information: Optional[str]
    phone: Optional[str]
    precedents: Optional[str]
    profession: Optional[str]
    religion: Optional[str]
    signed_data_marketing: bool
    signed_data_privacy: bool
    status: str
    type: Optional[str]
