from sqlalchemy import * 
from sqlalchemy.orm import *
from app.database.conexion import Base

class PistolModel(Base):
    __tablename__ = 'pistols'
    __table_args__ = {'quote': False}
    
    id = Column(Integer, primary_key= True, autoincrement= True)
    number = Column(Integer, unique= True, nullable=False)
    status = Column(String, nullable=False)
    availability = Column(Enum('Disponible', 'En uso', 'No disponible', 
                               name='pistol_availability'), nullable=False)
    
    registrosrf = relationship("RegistroRFModel", back_populates="pistols")