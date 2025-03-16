from fastapi import *
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.schemas.registro import *
from app.services.registro import RegistroService
from app.services.user import UserService

router = APIRouter()

@router.post(
    "/ingresar",
    response_model=RegistroResponseNice,  # Retornar un booleano
    status_code=status.HTTP_201_CREATED
)
def ingresar_camara(request: Ingresar_Salir, db: Session = Depends(get_db)):
        service = RegistroService(db)
        return service.ingresar(request.user_rut, request.user_password)


@router.post(
    "/salir",
    response_model=RegistroResponseNice,  
    status_code=status.HTTP_200_OK
)
def salir_camara(request: Ingresar_Salir, db: Session = Depends(get_db)):
        service = RegistroService(db)
        user_service = UserService(db)
        ## esto tiene el 'Registro_response'
        registro_db = service.salir2(request.user_rut, request.user_password)
        print(registro_db)
        
        return registro_db
        # # user_id = registro_db.get("user_id")
        # # user_db = user_service.get_by_id(user_id)
        # registro = service.response_bonito(registro_db)
        
        # if registro_db:
        #     return registro


@router.post("/{accion}", 
             response_model=bool,
             status_code= status.HTTP_200_OK)
def ingreso_salida(request : Ingresar_Salir, accion : str, db : Session = Depends(get_db)):
        service = RegistroService(db)
        if accion == 'ingresar':     
            return service.ingresar(request.user_rut, request.user_password)
        elif accion == 'salir':
            return service.salir(request.user_rut, request.user_password)
            

