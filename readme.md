# Proyecto FastAPI con PostgreSQL y SQLAlchemy

Este proyecto utiliza **FastAPI** para la creación de APIs, **SQLAlchemy** como ORM y **PostgreSQL** como base de datos.

## Requisitos previos

Asegúrate de tener instalado:
- Python 3.8 o superior
- PostgreSQL

## Instalación

### 1. Clonar el repositorio
```sh
# Clona el repositorio (reemplaza con tu URL si es necesario)
git clone https://github.com/tu_usuario/tu_proyecto.git
cd tu_proyecto
```

### 2. Crear un entorno virtual
```sh
python -m venv venv
source venv/bin/activate  # En macOS/Linux
venv\Scripts\activate    # En Windows
```

### 3. Instalar dependencias
```sh
pip install "fastapi[standard]"
pip install psycopg2
pip install sqlalchemy
```

### 4. Configurar la base de datos
Asegúrate de que PostgreSQL esté corriendo y crea una base de datos.

Ejemplo con `psql`:
```sh
CREATE DATABASE mi_base_de_datos;
```

Configura la conexión en un archivo `.env` o directamente en el código.

### 5. Ejecutar el servidor FastAPI
```sh
uvicorn main:app --reload
```

Reemplaza `main` por el nombre del archivo donde se instancia `FastAPI()`.

## Uso
Una vez ejecutado el servidor, accede a la documentación interactiva en:

- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Redoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Contribución
Si deseas contribuir, por favor abre un issue o pull request.

## Licencia
Este proyecto está bajo la licencia MIT.

