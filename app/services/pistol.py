from fastapi import *
from sqlalchemy.orm import *
from app.repositories.pistol import PistolRepository
from app.schemas.pistol import * 

class PistolService:
    def __init__(self, db : Session):
        self.pistol_repo = PistolRepository(db)
        
    def create_pistol(self, pistol_data : PistolCreate):
        try: 
            
             return self.pistol_repo.create_pistol(pistol_data)
            
        except HTTPException as http_exc:
            # Re-lanzar la excepción HTTPException para que FastAPI la maneje
            raise http_exc

        except Exception as e:
            # Manejar cualquier error inesperado
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error al crear la pistola: {str(e)}"
            )
    
    def get_pistol_by_id(self, pistol_id : int):
        try: 
        
            return self.pistol_repo.get_pistol_by_id(pistol_id)
        except HTTPException as http_exc:
            # Re-lanzar la excepción HTTPException para que FastAPI la maneje
            raise http_exc

        except Exception as e:
            # Manejar cualquier error inesperado
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error al obtener la pistola: {str(e)}"
            )
            
    def actualizar_estados_pistola(self, pistol_id: int, data = PistolUpdate):
        try:
            
            return self.pistol_repo.update_pistol(pistol_id, data)
        except HTTPException as http_exc:
            # Re-lanzar la excepción HTTPException para que FastAPI la maneje
            raise http_exc

        except Exception as e:
            # Manejar cualquier error inesperado
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error al actualizar pistola: {str(e)}"
            )
    
    def get_pistols_disponibles(self):
        try: 
            
            return self.pistol_repo.get_all_pistol_disponibles()
        
        except HTTPException as http_exc:
            # Re-lanzar la excepción HTTPException para que FastAPI la maneje
            raise http_exc

        except Exception as e:
            # Manejar cualquier error inesperado
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error al actualizar pistola: {str(e)}"
            )
    
    def pistol_update(self, id_pistol: int, data : PistolUpdate):
        try:
            return self.pistol_repo.update_pistol(id_pistol, data)
        
        except HTTPException as http_exc:
            # Re-lanzar la excepción HTTPException para que FastAPI la maneje
            raise http_exc

        except Exception as e:
            # Manejar cualquier error inesperado
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error al actualizar pistola: {str(e)}"
            )