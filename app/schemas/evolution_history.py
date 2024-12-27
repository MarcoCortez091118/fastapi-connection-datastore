from pydantic import BaseModel
from typing import Optional

class EvolutionHistoryInput(BaseModel):
    presentation: Optional[str]
    evolution: Optional[str]
    notes: Optional[str]
    tasks: Optional[str]
    comments: Optional[str]
    prognostic: Optional[str]
