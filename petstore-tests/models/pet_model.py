from pydantic import BaseModel, field_validator
from typing import Optional, List

class PetModel(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    status: Optional[str] = None
    photoUrls: List[str] = []