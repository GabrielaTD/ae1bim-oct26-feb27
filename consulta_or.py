from sqlalchemy import or_

from configuracion import SessionLocal
from crear_base_entidades import HistoriaClinica, crear_tablas


def consultar_con_or():
    crear_tablas()

    with SessionLocal() as session:
        # La consulta encuentra diagnósticos que contengan dermatitis u otitis.
        historias = (
            session.query(HistoriaClinica)
            .filter(
                or_(
                    HistoriaClinica.diagnostico_principal.ilike("%dermatitis%"),
                    HistoriaClinica.diagnostico_principal.ilike("%otitis%"),
                )
            )
            .all()
        )

        if not historias:
            print("No se encontraron historias de dermatitis u otitis.")
            return

        for historia in historias:
            print(f"Mascota: {historia.mascota_atendida}")
            print(f"Diagnóstico: {historia.diagnostico_principal}")
            print(f"Fecha: {historia.fecha_atencion}")
            print("-" * 45)


if __name__ == "__main__":
    consultar_con_or()