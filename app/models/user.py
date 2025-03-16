from app.database.conexion import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import *

class UserModel(Base):
    __tablename__ = 'users'
    __table_args__ = {'quote': False}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    rut = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    position = Column(String, nullable=False )
    company = Column(String, nullable= False)
    
    # Relación con Registro
    registros = relationship("RegistroModel", back_populates="user")
    
    # Relacion con pistols
    
    pistols = relationship("PistolModel", back_populates="user")
    
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    


    