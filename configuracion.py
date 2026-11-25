# Importamos las herramientas para conectar Python con SQLite
# y para crear sesiones de trabajo con la base de datos.
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# SQLite guardará el archivo de la base de datos en la carpeta del proyecto.
RUTA_BASE_DATOS = "sqlite:///clinicas_veterinarias.db"

# Crea la conexión que usarán las entidades y las consultas.
engine = create_engine(RUTA_BASE_DATOS, echo=False)

# Clase base de la que heredarán nuestras entidades.
Base = declarative_base()

# Permite abrir sesiones para guardar y consultar información.
SessionLocal = sessionmaker(bind=engine)