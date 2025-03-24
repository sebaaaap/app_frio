from typing import Optional
from sqlalchemy.orm import Session
from app.models.pistol import PistolModel
from app.schemas.pistol import PistolCreate, PistolUpdate

class PistolRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_pistol_by_id(self, pistol_id: int):
        return self.db.query(PistolModel).filter(PistolModel.id == pistol_id).first()

    def create_pistol(self, pistol: PistolCreate):
        db_pistol = PistolModel(**pistol.model_dump())
        self.db.add(db_pistol)
        self.db.commit()
        self.db.refresh(db_pistol)
        return db_pistol

    def update_pistol(self, pistol_id: int, pistol: PistolUpdate):
        db_pistol = self.get_pistol_by_id(pistol_id)
        if db_pistol:
            for key, value in pistol.model_dump().items():
                setattr(db_pistol, key, value)
            self.db.commit()
            self.db.refresh(db_pistol)
        return db_pistol

    def delete_pistol(self, pistol_id: int):
        db_pistol = self.get_pistol(pistol_id)
        if db_pistol:
            self.db.delete(db_pistol)
            self.db.commit()
        return db_pistol
    
    def get_all_pistol(self) ->Optional[list[PistolModel]] :
        db_pistols = self.db.query(PistolModel).all()
        return db_pistols
    
    def get_all_pistol_disponibles(self) ->Optional[list[PistolModel]] :
        db_pistols = self.db.query(PistolModel).filter(PistolModel.in_picking == False).all()
        return db_pistols