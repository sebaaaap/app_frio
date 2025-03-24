from fastapi import *
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.schemas.pistol import *
from app.services.pistol import PistolService


router = APIRouter()

@router.post(
    "/create",
    response_model=PistolResponse,  # Retornar un booleano
    status_code=status.HTTP_201_CREATED
)
def ingresar_camara(pistol_data : PistolCreate, db: Session = Depends(get_db)):
    service = PistolService(db)
    return service.create_pistol(pistol_data)


@router.get(
    "/get_pistols_availability",
    status_code=status.HTTP_200_OK,
    response_model= list[PistolResponse]

)
def get_pistols_disponibles(db : Session = Depends(get_db)):
    servicio = PistolService(db)
    return servicio.get_pistols_disponibles()

@router.put(
    "/utilizar_devolver/{id}",
    status_code= status.HTTP_202_ACCEPTED,
    response_model= PistolResponse
)
def update_picking(id : int, data: PistolUpdate, db :  Session = Depends(get_db)):
    servicio = PistolService(db)
    return servicio.actualizar_estados_pistola(id, data)

            
            

