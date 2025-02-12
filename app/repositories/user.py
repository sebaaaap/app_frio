from typing import Optional
from sqlalchemy import *
from sqlalchemy.orm import Session
from app.models.user import UserModel

class UserRepository: 
    
    def __init__(self, db : Session):
        self.db = db

    def get_by_nombre(self, user_name : str)-> Optional[UserModel]:
        return self.db.query(UserModel).filter(UserModel.name == user_name).first()
    
    def create(self, user_data: dict) -> Optional[UserModel]:
        user_db = UserModel(**user_data)
        
        self.db.add(user_db)
        self.db.commit()
        self.db.refresh(user_data)
        
        return user_db
    
    def verificar_existencia_by_rut(self, user_rut : str) ->Optional[UserModel]:
        return self.db.query(UserModel).filter(UserModel.rut == user_rut).first()
    
    def get_all(self) ->Optional[UserModel]:
        return self.db.query(UserModel).all()
