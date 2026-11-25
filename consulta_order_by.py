from configuracion import SessionLocal
from crear_base_entidades import Veterinario, crear_tablas


def consultar_veterinarios_ordenados():
    crear_tablas()

    with SessionLocal() as session:
        # order_by() ordena los resultados por los campos indicados.
        veterinarios = (
            session.query(Veterinario)
            .order_by(Veterinario.apellidos, Veterinario.nombres)
            .all()
        )

        if not veterinarios:
            print("No hay veterinarios registrados.")
            return

        for veterinario in veterinarios:
            print(
                f"Veterinario: {veterinario.apellidos}, "
                f"{veterinario.nombres}"
            )
            print(f"Correo: {veterinario.correo_electronico}")
            print(f"Licencia: {veterinario.licencia_profesional}")
            print(f"Consultorio: {veterinario.consultorio.nombre_numero}")
            print("-" * 45)


if __name__ == "__main__":
    consultar_veterinarios_ordenados()