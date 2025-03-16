from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # Importa el middleware CORS
from app.database.conexion import Base, engine
from app.models.registro import RegistroModel
from app.models.user import UserModel
from app.models.pistol import PistolModel
from app.models.registrorf import RegistroRFModel
from app.controllers.registro import router as registro_router
from app.controllers.user import router as user_router

# Crea la instancia de FastAPI
app = FastAPI()

# Configura CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todos los orígenes (en desarrollo)
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos los headers
)

# Crea las tablas en la base de datos
#imporatnte importalas, como arriba
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"chupalo"}

# Monta las rutas
# app.include_router(user_router, prefix="/adecco/users")
# Monta las rutas
app.include_router(user_router, prefix="/api/users")
app.include_router(registro_router, prefix="/api/registro")
