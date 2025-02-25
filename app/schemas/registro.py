from datetime import datetime
from pydantic import BaseModel


class RegistroCreate(BaseModel):
    user_id: int      
    time_in: datetime  


class Ingresar_Salir(BaseModel):
    user_rut: str
    user_password: str

class MessageResponse(BaseModel):
    message : str
    
class RegistroResponse(BaseModel):
    id: int
    user_id: int
    time_in: datetime
    time_out: datetime
    time_inside: str
    
class RegistroResponseNice(BaseModel):
    user_name: str
    user_lastname: str
    user_rut : str
    user_company: str
    time_inside: str


    class Config:
        from_attributes = True  # Permite crear instancias desde objetos ORM