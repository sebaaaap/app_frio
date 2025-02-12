from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # Importa el middleware CORS
from app.database.conexion import Base, engine
from app.models.registro import RegistroModel
from app.models.user import UserModel


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
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"chupalo"}

# Monta las rutas
# app.include_router(user_router, prefix="/adecco/users")
