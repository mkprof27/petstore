from pydantic import BaseModel, field_validator
from typing import Optional, List

class PetModel(BaseModel):
    id: Optional[int] = None
    name: str
    status: Optional[str] = None
    photoUrls: List[str] = []

    @field_validator("name", "status")
    @classmethod
    def fields_not_empty(cls, value):
        if value is None or value == "":
            raise ValueError("Поле не должно быть пустым")
        return value
