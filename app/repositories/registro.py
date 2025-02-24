
from typing import Optional
from app.models.registro import RegistroModel
from sqlalchemy.orm import Session
from _datetime import datetime

class RegistroRepository: 
    def __init__(self, db : Session):
        self.db = db
        
    def create(self, regis_data = dict) -> Optional[RegistroModel]:
        regist_db = RegistroModel(**regis_data)
        
        self.db.add(regist_db)
        self.db.commit()
        self.db.refresh(regist_db)
        
        return regist_db

    #busca el usuario y verifica que la hora de salida este vacia, si esta vacia, devuelve el registro 
    def get_ultimo_registro(self, user_id: int) -> Optional[RegistroModel]:
        return self.db.query(RegistroModel).filter(
            RegistroModel.user_id == user_id,
            RegistroModel.tiempo_out.is_(None)  # Solo registros sin hora de salida
        ).order_by(RegistroModel.tiempo_in.desc()).first()

    #busca el registro, le actualiza la hora de salida y lo retorna
    def actualizar_salida(self, registro_id: int, tiempo_out: datetime) -> Optional[RegistroModel]:
        registro_db = self.db.query(RegistroModel).filter(RegistroModel.id == registro_id).first()
        if registro_db:
            registro_db.tiempo_out = tiempo_out
            self.db.commit()
            self.db.refresh(registro_db)
        return registro_db 