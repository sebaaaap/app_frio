# Proyecto FastAPI con PostgreSQL y SQLAlchemy

Este proyecto utiliza **FastAPI** para la creación de APIs, **SQLAlchemy** como ORM y **PostgreSQL** como base de datos.

## Requisitos previos

Asegúrate de tener instalado:
- Python 3.8 o superior
- PostgreSQL

## Instalación

### 1. Crear un entorno virtual
```sh
python -m venv venv
source venv/bin/activate  # En macOS/Linux
venv\Scripts\activate    # En Windows
```

### 2. Clonar el repositorio
```sh
# Clona el repositorio (reemplaza con tu URL si es necesario)
git clone https://github.com/tu_usuario/tu_proyecto.git
cd tu_proyecto
```

### 3. Instalar dependencias
```sh
pip install --upgrade pip      
pip install "fastapi[standard]"
pip install psycopg2-binary
pip install sqlalchemy
```

### 4. Configurar la base de datos
Jonathan asegúrate de que PostgreSQL esté corriendo en tu contenedor de docker.

uno:
```sh
docker pull postgres
```

dos:
```sh
docker run --name nutrisco -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=nutrisco -p 5432:5432 -d postgres
```
tres, meterte a la bdd en el contenedor :
```sh
docker exec -it nutrisco bash
psql -U postgres -d nutrisco
```
ya aqui puedes ver las tablas, para ver las tablas:
```sh
\dt
```

para ver contenido de las tablas:
```sh
SELECT*FROM users;
SELECT*FROM registros;
```

### 5. Ejecutar el servidor FastAPI, asegurate de estar en la carpeta 'app' en donde este el main.py
```sh
fastapi dev main.py 
```

## Uso
Una vez ejecutado el servidor, accede a la documentación interactiva en:

- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Redoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)


## Contribución
hace el git clon noma

