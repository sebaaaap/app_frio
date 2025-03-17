from fastapi import *
from app.repositories.registrorf import RegistroRFRepository
from sqlalchemy.orm import Session
from app.schemas.registrorf import *
 
class RegistroRFService: 
    
    def __init__(self, db : Session):
        self.registro_rf_repo = RegistroRFRepository(db)
        
    
    def create_register_rf(self, data:RegistroRFCreate ):
        try: 
            
            
            return self.registro_rf_repo.create_registro_rf(data)
            
        
        except HTTPException as http_exc:
            # Re-lanzar la excepción HTTPException para que FastAPI la maneje
            raise http_exc

        except Exception as e:
            # Manejar cualquier error inesperado
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error al crear el registro: {str(e)}"
            )
    