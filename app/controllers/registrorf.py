from fastapi import *
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.schemas.registrorf import *
from app.services.registrorf import *


router = APIRouter()

@router.post(
    "/llevar",
    response_model= RegistroRFResponse,  
    status_code=status.HTTP_201_CREATED
)
def registro_rf_start(data : RegistroRFCreate, db: Session = Depends(get_db)):
        service = RegistroRFService(db)
        return service.create_register_rf(data)

@router.post(
    "/devolver/{id}",
    response_model= RegistroRFResponse, 
    status_code=status.HTTP_201_CREATED
)
def registro_rf_start(data : RegistroRFUpdate, id: int,  db: Session = Depends(get_db)):
        service = RegistroRFService(db)
        a = data.__dict__
        time = a["end_time"]
        return service.end_time(id, time )


            
            

