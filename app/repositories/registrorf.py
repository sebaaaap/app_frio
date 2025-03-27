from datetime import datetime
from sqlalchemy.orm import Session
from app.models.registrorf import RegistroRFModel
from app.schemas.registrorf import RegistroRFCreate, RegistroRFUpdate

class RegistroRFRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_registro_rf(self, registro_id: int):
        return self.db.query(RegistroRFModel).filter(RegistroRFModel.id == registro_id).first()

    def get_registros_rf(self, skip: int = 0, limit: int = 100):
        return self.db.query(RegistroRFModel).offset(skip).limit(limit).all()

    def create_registro_rf(self, registro: RegistroRFCreate):
        db_registro = RegistroRFModel(**registro.model_dump())
        self.db.add(db_registro)
        self.db.commit()
        self.db.refresh(db_registro)
        
        db_registro = (
        self.db.query(RegistroRFModel)
        .filter(RegistroRFModel.id == db_registro.id)
        .first()
        )

        return db_registro
    
    def end_time(self, id : int, time_end : datetime):
        db_registro = self.db.query(RegistroRFModel).filter(RegistroRFModel.id == id).first()
        db_registro.end_time = time_end
        self.db.commit()
        self.db.refresh(db_registro)
        return db_registro
        

    def update_registro_rf(self, registro_id: int, registro: RegistroRFUpdate):
        db_registro = self.get_registro_rf(registro_id)
        if db_registro:
            for key, value in registro.model_dump().items():
                setattr(db_registro, key, value)
            self.db.commit()
            self.db.refresh(db_registro)
        return db_registro

    def delete_registro_rf(self, registro_id: int):
        db_registro = self.get_registro_rf(registro_id)
        if db_registro:
            self.db.delete(db_registro)
            self.db.commit()
        return db_registro