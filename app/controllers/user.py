from typing import List
from fastapi import *
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.services.user import UserService

router = APIRouter()

# Endpoint para crear un usuario
@router.post(
    "/create",
    response_model= bool,
    status_code=status.HTTP_201_CREATED
)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.user_create(user)

# Endpoint para obtener un usuario por ID
@router.get(
    "/get_by_id/{user_id}",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK
)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.get_by_id(user_id)

@router.get(
    "/get_all",
    response_model= List[UserResponse],
    status_code=status.HTTP_200_OK
)
def users_get_all( db: Session = Depends(get_db)):
    service = UserService(db)
    return service.users_get_all()

@router.get(
    "/get_by_nombre/{user_name}",
    response_model= UserResponse,
    status_code=status.HTTP_200_OK
)
def users_get_by_name( user_name : str,db: Session = Depends(get_db)):
    service = UserService(db)
    return service.get_by_nombre(user_name)


@router.delete(
    "/delete/{user_id}",
    response_model= bool,
    status_code= status.HTTP_200_OK
)
def user_delete(user_id : int, db : Session = Depends(get_db)):
    service = UserService(db)
    return service.delete(user_id)

@router.put("/update/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int,
    user_data: UserUpdate,
    db : Session = Depends(get_db)):
    
    service = UserService(db)
    return service.update(user_id, user_data)