# Column define los campos; ForeignKey conecta las tablas.
# DateTime guarda fechas y Text permite guardar textos más extensos.
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

# Usamos la clase base y la conexión que definimos en configuracion.py.
from configuracion import Base, engine


# Cada clase representa una tabla de la base de datos.
class Clinica(Base):
    __tablename__ = "clinicas"

    id = Column(Integer, primary_key=True)
    nombre_comercial = Column(String(120), nullable=False)
    direccion = Column(String(250), nullable=False)
    medico_responsable = Column(String(150), nullable=False)

    # Una clínica puede tener varios consultorios.
    consultorios = relationship("Consultorio", back_populates="clinica")


class Consultorio(Base):
    __tablename__ = "consultorios"

    id = Column(Integer, primary_key=True)
    nombre_numero = Column(String(80), nullable=False)
    especialidad_principal = Column(String(100), nullable=False)

    # Esta clave foránea hace obligatorio asociar el consultorio a una clínica.
    clinica_id = Column(
        Integer, ForeignKey("clinicas.id"), nullable=False
    )

    # Permite acceder a la clínica y a los veterinarios desde el consultorio.
    clinica = relationship("Clinica", back_populates="consultorios")
    veterinarios = relationship("Veterinario", back_populates="consultorio")


class Veterinario(Base):
    __tablename__ = "veterinarios"

    id = Column(Integer, primary_key=True)
    nombres = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    correo_electronico = Column(String(150), nullable=False)
    licencia_profesional = Column(String(50), nullable=False)

    # Cada veterinario pertenece a un solo consultorio.
    consultorio_id = Column(
        Integer, ForeignKey("consultorios.id"), nullable=False
    )

    # Un veterinario puede elaborar varias historias clínicas.
    consultorio = relationship("Consultorio", back_populates="veterinarios")
    historias_clinicas = relationship(
        "HistoriaClinica", back_populates="veterinario"
    )


class HistoriaClinica(Base):
    __tablename__ = "historias_clinicas"

    id = Column(Integer, primary_key=True)
    fecha_atencion = Column(DateTime, nullable=False)
    diagnostico_principal = Column(Text, nullable=False)
    tratamiento_prescrito = Column(Text, nullable=False)
    mascota_atendida = Column(String(120), nullable=False)

    # Guarda qué veterinario elaboró esta historia clínica.
    veterinario_id = Column(
        Integer, ForeignKey("veterinarios.id"), nullable=False
    )

    veterinario = relationship(
        "Veterinario", back_populates="historias_clinicas"
    )


# Crea las tablas si todavía no existen en el archivo SQLite.
def crear_tablas():
    Base.metadata.create_all(bind=engine)


# Este bloque se ejecuta solo al iniciar directamente este archivo.
if __name__ == "__main__":
    crear_tablas()
    print("Base de datos y tablas creadas correctamente.")