from typing import Optional
from fastapi import *
from sqlalchemy.orm import Session
from app.repositories.registro import RegistroRepository
from app.repositories.user import UserRepository
from _datetime import datetime
from app.schemas.registro import *

class RegistroService : 
    def __init__(self, db : Session):
        self.registro_repo = RegistroRepository(db)
        self.user_repo = UserRepository(db)
        
    def ingresar(self, rut : str, password : str):
        try:
            user_db = self.user_repo.verificar_credenciales(rut,password)
            if not user_db:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Credenciales inválidas"
                )
                
            registro_data = {
                'user_id' : user_db.id,      
                'tiempo_in':  datetime.now()
            }
            registro = self.registro_repo.create(registro_data)
            
            return True
        
        except HTTPException as http_exc:
            raise http_exc
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error al registrar la salida: {str(e)}"
            )
    
    def salir(self, user_rut: str, user_password: str) -> Optional[RegistroResponse]:
        try:
            # Verificar las credenciales del usuario
            user_db = self.user_repo.verificar_credenciales(user_rut, user_password)
            if not user_db:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Credenciales inválidas jonathan"
                )

            # Obtener el último registro de entrada del usuario
            registro_db = self.registro_repo.get_ultimo_registro_por_user(user_db.id)
            if not registro_db or registro_db.tiempo_out:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="no hay registro de entrada"
                )

            # Actualizar el tiempo de salida
            tiempo_out = datetime.now()
            self.registro_repo.actualizar_salida(registro_db.id, tiempo_out)

            # Calcular el tiempo dentro de la cámara
            tiempo_dentro = registro_db.tiempo_dentro()

            # Retornar la información en el formato esperado
            return {
                "id": registro_db.id,
                "user_id": registro_db.user_id,
                "time_in": registro_db.tiempo_in,
                "time_out": tiempo_out,
                "time_inside": str(tiempo_dentro)  # Convertir a cadena
            }
            # print(registro_db)
            # Response = RegistroResponse.model_validate(registro_db)
            
            # return Response

        except HTTPException as http_exc:
            raise http_exc
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error al registrar la : {str(e)}"
            )
    
    def response_bonito(self, data = RegistroResponse) -> Optional[RegistroResponseNice]:
        user_db = self.user_repo.get_by_id(data["user_id"])
        string_time = data["time_inside"]
        lista_time= string_time.split('.')
        tiempo_bonito = lista_time[0]
        
        return RegistroResponseNice(
            user_name= user_db.name,
            user_lastname= user_db.lastname,
            user_rut= user_db.rut,
            user_company= user_db.company,
            time_inside= tiempo_bonito
        )