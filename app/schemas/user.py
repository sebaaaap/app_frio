from typing import Optional
from pydantic import BaseModel, EmailStr

# Esquema para crear un User
class UserCreate(BaseModel):
    name: str
    lastname: str
    rut: str
    email: EmailStr
    password: str
    cargo: str

# Esquema para responder con los datos de un User
class UserResponse(BaseModel):
    id: int
    name: str
    lastname: str
    rut: str
    email: EmailStr
    password: str
    cargo: str

class UserUpdate(BaseModel):
    name: Optional[str] = None
    lastname: Optional[str] = None
    rut: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    cargo: Optional[str] = None

class MessageResponse(BaseModel):
    message: str


    model_config = {
        "from_attributes": True  # Configuración para Pydantic V2
    }
