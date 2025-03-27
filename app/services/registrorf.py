from fastapi import *
from app.repositories.registrorf import RegistroRFRepository
from app.repositories.pistol import PistolRepository
from sqlalchemy.orm import Session
from app.schemas.registrorf import *
from app.schemas.pistol import *
 
class RegistroRFService: 
    
    def __init__(self, db : Session):
        self.registro_rf_repo = RegistroRFRepository(db)
        self.pistol_repo = PistolRepository(db)
        
    
    def create_register_rf(self, data:RegistroRFCreate ):
        try: 
            
            
            registro_init =  self.registro_rf_repo.create_registro_rf(data)
            pistola = self.pistol_repo.get_pistol_by_id(registro_init.id_pistol)
            
           # Actualizar el campo in_picking usando el método update_pistol
            updated_pistol = self.pistol_repo.update_pistol(
                    pistol_id=pistola.id,
                    pistol=PistolUpdate(
                        in_picking=True,
                        status=pistola.status,  # Mantener el valor actual
                        availability=pistola.availability  # Mantener el valor actual
                    )
                )

            dataa = PistolResponse.model_validate(updated_pistol)
            print(dataa)
        
            # pistol_model =self.pistol_repo.get_pistol_by_id(pistola_id)
            # pist_response = PistolUpdate.model_validate(pistol_model)
            # print('pistola antes de update'.pist_response)
            # self.pistol_repo.update_pistol(pistola_id, pist_response )
            # # self.pistol_repo.update_pistol(pistola_id,)
            return registro_init
            
           
            
        
        except HTTPException as http_exc:
            # Re-lanzar la excepción HTTPException para que FastAPI la maneje
            raise http_exc

        except Exception as e:
            # Manejar cualquier error inesperado
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error al crear el registro: {str(e)}"
            )
            
    def end_time(self, id : int, time_end: datetime):
        try:
            
            register_end =  self.registro_rf_repo.end_time(id, time_end)
            print(register_end)
            pistola = self.pistol_repo.get_pistol_by_id(register_end.id_pistol)
            print(pistola)
            
            pistola_update = self.pistol_repo.update_pistol(
                pistola.id, pistol =PistolUpdate(
                        in_picking=False,
                        status=pistola.status,  # Mantener el valor actual
                        availability=pistola.availability  # Mantener el valor actual
                    ) )
            
            print(pistola_update)
            # id = register_end.id_pistol
            # pistol_data = self.pistol_repo.get_pistol_by_id(id)
            # self.pistol_repo.update_pistol(id, pistol_data)
            return register_end
            
        except HTTPException as http_exc:
            # Re-lanzar la excepción HTTPException para que FastAPI la maneje
            raise http_exc

        except Exception as e:
            # Manejar cualquier error inesperado
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error al finalizar registro: {str(e)}"
            )
        
    