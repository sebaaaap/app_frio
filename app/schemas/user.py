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

    class Config:
        from_attributes = True 

class MessageResponse(BaseModel):
    message: str

    # Configuración para Pydantic V2
    model_config = {
        "from_attributes": True  # Permite crear instancias desde objetos ORM
    }