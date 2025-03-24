from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class PistolBase(BaseModel):
    number: int = Field(..., description="Número de identificación de la pistola")
    status: str = Field(..., description="Estado físico de la pistola (Bueno, Malo, Regular)")
    availability: str = Field(..., description="Disponibilidad de la pistola (Disponible, En uso, No disponible)")
    in_picking: bool


class PistolCreate(PistolBase):
    pass

class PistolUpdate(BaseModel):
    status: Optional[str] = Field(None, description="Estado físico de la pistola (Bueno, Malo, Regular)")
    availability: Optional[str] = Field(None, description="Disponibilidad de la pistola (Disponible, En uso, No disponible)")
    in_picking: Optional[bool]

class PistolResponse(PistolBase):
    id: int

    class Config:
        from_attributes = True  # Habilita la compatibilidad con ORM