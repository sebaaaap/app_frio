from fastapi import *
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.schemas.registrorf import *
from app.services.registrorf import *


router = APIRouter()

@router.post(
    "/create",
    response_model= RegistroRFResponse,  # Retornar un booleano
    status_code=status.HTTP_201_CREATED
)
def registro_rf_start(data : RegistroRFCreate, db: Session = Depends(get_db)):
        service = RegistroRFService(db)
        return service.create_register_rf(data)



            
            

