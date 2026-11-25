from sqlalchemy import func

from configuracion import SessionLocal
from crear_base_entidades import (
    Clinica,
    Consultorio,
    Veterinario,
    HistoriaClinica,
    crear_tablas,
)


def consultar_clinicas_y_contar_historias():
    # Aseguramos que las tablas existan antes de consultar.
    crear_tablas()

    with SessionLocal() as session:
        # Conectamos clínicas con consultorios, veterinarios e historias.
        # outerjoin permite mostrar también clínicas que aún no tengan historias.
        resultados = (
            session.query(
                Clinica,
                func.count(HistoriaClinica.id).label("numero_historias"),
            )
            .outerjoin(
                Consultorio,
                Consultorio.clinica_id == Clinica.id,
            )
            .outerjoin(
                Veterinario,
                Veterinario.consultorio_id == Consultorio.id,
            )
            .outerjoin(
                HistoriaClinica,
                HistoriaClinica.veterinario_id == Veterinario.id,
            )
            .group_by(
                Clinica.id,
                Clinica.nombre_comercial,
                Clinica.direccion,
                Clinica.medico_responsable,
            )
            .order_by(Clinica.nombre_comercial)
            .all()
        )

        if not resultados:
            print("No hay clínicas registradas. Primero ejecuta poblar_base.py.")
            return

        for clinica, numero_historias in resultados:
            print(f"Clínica: {clinica.nombre_comercial}")
            print(f"Dirección: {clinica.direccion}")
            print(f"Médico responsable: {clinica.medico_responsable}")
            print(f"Historias clínicas asociadas: {numero_historias}")
            print("-" * 45)


if __name__ == "__main__":
    consultar_clinicas_y_contar_historias()