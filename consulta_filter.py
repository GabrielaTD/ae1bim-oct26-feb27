from configuracion import SessionLocal
from crear_base_entidades import Consultorio, crear_tablas


def consultar_por_especialidad():
    crear_tablas()

    with SessionLocal() as session:
        # filter() devuelve solo los consultorios que cumplen la condición.
        consultorios = (
            session.query(Consultorio)
            .filter(Consultorio.especialidad_principal == "Medicina general")
            .all()
        )

        if not consultorios:
            print("No se encontraron consultorios de Medicina general.")
            return

        for consultorio in consultorios:
            print(f"Consultorio: {consultorio.nombre_numero}")
            print(f"Especialidad: {consultorio.especialidad_principal}")
            print(f"Clínica: {consultorio.clinica.nombre_comercial}")
            print("-" * 45)


if __name__ == "__main__":
    consultar_por_especialidad()