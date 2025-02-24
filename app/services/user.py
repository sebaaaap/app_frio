from typing import List, Optional
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repositories.user import UserRepository
from app.repositories.registro import  RegistroRepository
from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.models.user import UserModel

class UserService:
    def __init__(self, db: Session):
        self.user_repo = UserRepository(db)
        self.registro_repo = RegistroRepository(db)

    def user_create(self, user: UserCreate):
        try:
            # Verificar si el usuario ya existe
            if self.user_repo.verificar_existencia_by_rut(user.rut):
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="El usuario ya existe"
                )

            # Crear el usuario
            user_dict = user.model_dump()  # Convertir el esquema Pydantic a un diccionario
            self.user_repo.create(user_dict)

            # Retornar True si el usuario se crea correctamente
            return True

        except HTTPException as http_exc:
            # Re-lanzar la excepción HTTPException para que FastAPI la maneje
            raise http_exc

        except Exception as e:
            # Manejar cualquier otro error inesperado
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error al crear el usuario: {str(e)}"
            )
    
    def users_get_all(self) -> List[UserResponse]:
        try:
            usuarios = self.user_repo.get_all()
            
            
            # Convertir los objetos SQLAlchemy a modelos Pydantic
            usuarios_response = [
                UserResponse(
                    id=usuario.id,
                    name=usuario.name,
                    lastname=usuario.lastname,
                    rut=usuario.rut,
                    email=usuario.email,
                    password= usuario.password,
                    position = usuario.position,
                    company = usuario.company
                   )
                for usuario in usuarios
            ]
            
            return usuarios_response
        
        except HTTPException as http_exc:
            # Re-lanzar la excepción HTTPException para que FastAPI la maneje
            raise http_exc

        except Exception as e:
            # Manejar cualquier error inesperado
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error al obtener los usuarios: {str(e)}"
            )

    def get_by_nombre(self, user_name: str) -> Optional[UserResponse]:
     try:
        # Obtener el usuario desde el repositorio
        usuario = self.user_repo.get_by_nombre(user_name)
        
        # Verificar si el usuario existe
        if usuario is None:
            return None
        
        # Convertir el objeto SQLAlchemy a un modelo Pydantic
        return UserModel(**usuario.to_dict())# 
        
     except HTTPException as http_exc:
        # Re-lanzar la excepción HTTPException para que FastAPI la maneje
        raise http_exc    
        
     except Exception as e:
        # Manejar cualquier error inesperado
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al obtener el usuario: {str(e)}"
        )
        
    def get_by_id(self, user_id : int)-> Optional[UserResponse]:
        try:
            user_db = self.user_repo.get_by_id(user_id)
            
            if user_db:
                return UserModel(**user_db.to_dict())
            
            return None
        
        except HTTPException as http_exc:
        # Re-lanzar la excepción HTTPException para que FastAPI la maneje
            raise http_exc    
        
        except Exception as e:
        # Manejar cualquier error inesperado
            raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al obtener el usuario: {str(e)}"
            )
    def delete(self, user_id : int) -> Optional[bool]:
        try:
            user_db = self.get_by_id(user_id)
            print(user_db)
            if user_db:
                user_delete  = self.user_repo.delete(user_db)
                if user_delete :
                    return False
                return True
            
            return False 
        
        except HTTPException as http_exc:
        # Re-lanzar la excepción HTTPException para que FastAPI la maneje
            raise http_exc    
        
        except Exception as e:
        # Manejar cualquier error inesperado
            raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al obtener el usuario: {str(e)}"
            )
        
    def update(self, user_id: int, user_data: UserUpdate) -> Optional[UserResponse]:
     try:
        # Verificar si el usuario existe
        user_db = self.user_repo.get_by_id(user_id)
        if not user_db:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")

        # Convertir el esquema Pydantic a un diccionario
        data_dict = user_data.model_dump(exclude_unset=True)

        # Actualizar el usuario en el repositorio
        updated_user = self.user_repo.update(user_id, data_dict)
        if not updated_user:
            raise HTTPException(status_code=500, detail="Error al actualizar el usuario")

        # Convertir el objeto SQLAlchemy a un diccionario usando to_dict
        user_dict = updated_user.to_dict()

        # Convertir el diccionario a UserResponse usando model_validate
        return UserResponse.model_validate(user_dict)  # ¡Aquí usamos model_validate!

     except HTTPException as http_exc:
        raise http_exc
     except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar el usuario: {str(e)}")

    def search_users_by_name(self, name: str):
        # Obtiene los usuarios del repositorio
        users = self.user_repo.get_users_by_name(name)
        # Convierte los modelos de SQLAlchemy a esquemas de Pydantic
        return [UserResponse.from_orm(user) for user in users]
