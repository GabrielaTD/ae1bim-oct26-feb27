from datetime import datetime

from configuracion import SessionLocal
from crear_base_entidades import (
    Clinica,
    Consultorio,
    Veterinario,
    HistoriaClinica,
    crear_tablas,
)


def poblar_base():
    # Asegura que existan las tablas antes de guardar información.
    crear_tablas()

    with SessionLocal() as session:
        # Evita duplicar los datos si el archivo se ejecuta más de una vez.
        if session.query(Clinica).first():
            print("La base ya contiene datos de ejemplo.")
            return

        # Creamos historias clínicas para la veterinaria Ana.
        historia_ana_1 = HistoriaClinica(
            fecha_atencion=datetime(2026, 11, 10, 9, 30),
            diagnostico_principal="Dermatitis alérgica",
            tratamiento_prescrito="Tratamiento tópico y control veterinario.",
            mascota_atendida="Luna",
        )
        historia_ana_2 = HistoriaClinica(
            fecha_atencion=datetime(2026, 11, 18, 10, 0),
            diagnostico_principal="Control de dermatitis",
            tratamiento_prescrito="Continuar el tratamiento por siete días.",
            mascota_atendida="Luna",
        )

        # Esta clínica tiene dos consultorios; cada uno tiene un veterinario.
        clinica_norte = Clinica(
            nombre_comercial="Huellitas del Norte",
            direccion="Av. Los Pastos 123, Tulcán",
            medico_responsable="Ana Belén Ruiz",
            consultorios=[
                Consultorio(
                    nombre_numero="Consultorio 1",
                    especialidad_principal="Medicina general",
                    veterinarios=[
                        Veterinario(
                            nombres="Ana Belén",
                            apellidos="Ruiz",
                            correo_electronico="ana.ruiz@ejemplo.com",
                            licencia_profesional="VET-1001",
                            historias_clinicas=[historia_ana_1, historia_ana_2],
                        )
                    ],
                ),
                Consultorio(
                    nombre_numero="Consultorio 2",
                    especialidad_principal="Dermatología",
                    veterinarios=[
                        Veterinario(
                            nombres="Diego",
                            apellidos="Mora",
                            correo_electronico="diego.mora@ejemplo.com",
                            licencia_profesional="VET-1002",
                            historias_clinicas=[
                                HistoriaClinica(
                                    fecha_atencion=datetime(2026, 11, 12, 11, 0),
                                    diagnostico_principal="Dermatitis por contacto",
                                    tratamiento_prescrito="Limpieza y medicación tópica.",
                                    mascota_atendida="Toby",
                                )
                            ],
                        )
                    ],
                ),
            ],
        )

        # Segunda clínica con atención de cirugía.
        clinica_valle = Clinica(
            nombre_comercial="Patitas del Valle",
            direccion="Calle Sucre y Bolívar, San Gabriel",
            medico_responsable="Mariela Paredes",
            consultorios=[
                Consultorio(
                    nombre_numero="Consultorio A",
                    especialidad_principal="Cirugía",
                    veterinarios=[
                        Veterinario(
                            nombres="Mariela",
                            apellidos="Paredes",
                            correo_electronico="mariela.paredes@ejemplo.com",
                            licencia_profesional="VET-2001",
                            historias_clinicas=[
                                HistoriaClinica(
                                    fecha_atencion=datetime(2026, 11, 16, 14, 0),
                                    diagnostico_principal="Otitis externa",
                                    tratamiento_prescrito="Limpieza ótica y medicación.",
                                    mascota_atendida="Max",
                                ),
                                HistoriaClinica(
                                    fecha_atencion=datetime(2026, 11, 20, 15, 30),
                                    diagnostico_principal="Control postoperatorio",
                                    tratamiento_prescrito="Revisión de la herida quirúrgica.",
                                    mascota_atendida="Rocky",
                                ),
                            ],
                        )
                    ],
                )
            ],
        )

        # Tercera clínica con atención de medicina general.
        clinica_vida = Clinica(
            nombre_comercial="Vida Animal",
            direccion="Av. Universitaria 45, Ibarra",
            medico_responsable="Carlos Andrade",
            consultorios=[
                Consultorio(
                    nombre_numero="Consultorio 1",
                    especialidad_principal="Medicina general",
                    veterinarios=[
                        Veterinario(
                            nombres="Carlos",
                            apellidos="Andrade",
                            correo_electronico="carlos.andrade@ejemplo.com",
                            licencia_profesional="VET-3001",
                            historias_clinicas=[
                                HistoriaClinica(
                                    fecha_atencion=datetime(2026, 11, 22, 8, 45),
                                    diagnostico_principal="Control de vacunación",
                                    tratamiento_prescrito="Aplicación de vacuna anual.",
                                    mascota_atendida="Milo",
                                )
                            ],
                        )
                    ],
                )
            ],
        )

        # Al añadir las clínicas, SQLAlchemy guarda también sus entidades relacionadas.
        session.add_all([clinica_norte, clinica_valle, clinica_vida])
        session.commit()

        print("Datos de ejemplo ingresados correctamente.")


if __name__ == "__main__":
    poblar_base()