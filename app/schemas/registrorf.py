from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class RegistroRFBase(BaseModel):
    start_time: datetime = Field(..., description="Fecha y hora de inicio")
    end_time: Optional[datetime] = Field(None, description="Fecha y hora de término")
    status: str = Field(..., description="Estado de la pistola al devolverla (Bueno, Malo, Regular)")
    comment: Optional[str] = Field(None, description="Comentario opcional")
    id_user: int = Field(..., description="ID del usuario que usó la pistola")
    id_pistol: int = Field(..., description="ID de la pistola usada")

class RegistroRFCreate(RegistroRFBase):
    pass

class RegistroRFUpdate(BaseModel):
    end_time: Optional[datetime] = Field(None, description="Fecha y hora de término")
    status: Optional[str] = Field(None, description="Estado de la pistola al devolverla (Bueno, Malo, Regular)")
    comment: Optional[str] = Field(None, description="Comentario opcional")

class RegistroRFResponse(RegistroRFBase):
    id = int
    

    class Config:
        from_attributes = True  # Habilita la compatibilidad con ORM