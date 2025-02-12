from datetime import datetime
from pydantic import BaseModel


class RegistroCreate(BaseModel):
    user_id: int      
    tiempo_in: datetime  


class Ingresar_Salir(BaseModel):
    user_rut: str
    user_password: str
    
class RegistroResponse(BaseModel):
    id: int
    user_id: int
    tiempo_in: datetime
    tiempo_out: datetime
    tiempo_dentro: str


    class Config:
        from_attributes = True  # Permite crear instancias desde objetos ORM