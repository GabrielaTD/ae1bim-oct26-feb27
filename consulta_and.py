from datetime import datetime

from sqlalchemy import and_

from configuracion import SessionLocal
from crear_base_entidades import HistoriaClinica, crear_tablas


def consultar_con_and():
    crear_tablas()

    with SessionLocal() as session:
        fecha_minima = datetime(2026, 11, 15)

        # and_() exige que ambas condiciones se cumplan.
        historias = (
            session.query(HistoriaClinica)
            .filter(
                and_(
                    HistoriaClinica.fecha_atencion >= fecha_minima,
                    HistoriaClinica.diagnostico_principal.ilike("%control%"),
                )
            )
            .all()
        )

        if not historias:
            print("No se encontraron historias que cumplan ambas condiciones.")
            return

        for historia in historias:
            print(f"Mascota: {historia.mascota_atendida}")
            print(f"Fecha: {historia.fecha_atencion}")
            print(f"Diagnóstico: {historia.diagnostico_principal}")
            print("-" * 45)


if __name__ == "__main__":
    consultar_con_and()