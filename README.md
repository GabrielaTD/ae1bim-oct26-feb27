# ae1bim-oct25-feb26# Actividad Experimental 1: SQLAlchemy

Sistema de ejemplo para administrar una red de clínicas veterinarias usando Python, SQLite y SQLAlchemy.

## Entidades y relaciones

- **Clínica** tiene varios consultorios.
- **Consultorio** pertenece a una clínica y puede tener varios veterinarios.
- **Veterinario** pertenece a un consultorio y puede registrar varias historias clínicas.
- **Historia clínica** pertenece al veterinario que la elaboró.

La dirección de cada clínica incluye la ciudad y el campo `medico_responsable` registra el nombre solicitado en la actividad.

## Requisitos

- Python
- SQLAlchemy

En Windows, instala la dependencia desde PowerShell, dentro de esta carpeta:

```powershell
py -m pip install -r requirements.txt
## Complemento: archivo .gitignore

El archivo `.gitignore` contiene reglas para que Git omita archivos locales o temporales al registrar cambios. En este proyecto se excluyen la caché de Python, los entornos virtuales y la base SQLite generada localmente. La base de datos sigue en la computadora y puede volver a crearse ejecutando los scripts del proyecto.

### Referencia

GitHub Docs. (s. f.). *Ignorar archivos*. https://docs.github.com/es/get-started/git-basics/ignoring-files