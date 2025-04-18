from sqlalchemy import *
from sqlalchemy.orm import *
from app.database.conexion import Base
from datetime import datetime

class RegistroRFModel(Base):
    __tablename__ = 'registros_rf'
    __table_args__ = {'quote': False}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    start_time = Column(DateTime, nullable=False, default=datetime.now)  # Fecha y hora de inicio
    end_time = Column(DateTime, nullable=True)                  # Fecha y hora de término (opcional)
    status = Column(Enum('Bueno', 'Malo', 'Regular', name='registro_status'), nullable=False)  # Estado de la pistola al devolverla
    comment = Column(String(255), nullable=True)               # Comentario opcional
    

    id_user = Column(Integer, ForeignKey('users.id'), nullable=False)  # Foreign Key a Users
    # Relación con la tabla Users (un registro está asociado a un usuario)
    user = relationship("UserModel", back_populates="registros_rf", lazy="joined")

    id_pistol = Column(Integer, ForeignKey('pistols.id'), nullable=False)  # Foreign Key a Pistols
    # Relación con la tabla Pistols (un registro está asociado a una pistola)
    pistols = relationship("PistolModel", back_populates="registros_rf", lazy="joined")

    def __repr__(self):
        return f"<RegistrosRF(id={self.id}, start_time={self.start_time}, end_time={self.end_time}, status={self.status})>"
