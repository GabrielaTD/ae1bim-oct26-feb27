# Actividad Experimental 1: SQLAlchemy

Sistema de ejemplo para administrar una red de clínicas veterinarias usando Python, SQLite y SQLAlchemy.

## Entidades y relaciones

- **Clínica** tiene varios consultorios.
- **Consultorio** pertenece a una clínica y puede tener varios veterinarios.
- **Veterinario** pertenece a un consultorio y puede registrar varias historias clínicas.
- **Historia clínica** pertenece al veterinario que la elaboró.

La dirección de cada clínica incluye la ciudad y el campo `medico_responsable` registra el nombre solicitado en la actividad.

## Requisitos e instalación

Se necesita Python y SQLAlchemy. En Windows, abre PowerShell desde esta carpeta y ejecuta:

```powershell
py -m pip install -r requirements.txt
```

## Crear la base e ingresar datos

Ejecuta los archivos en este orden:

```powershell
py crear_base_entidades.py
py poblar_base.py
```

La base SQLite se guarda en `clinicas_veterinarias.db`. Si ya tiene datos, `poblar_base.py` evita insertarlos otra vez.

## Consultas

Ejecuta las consultas desde esta carpeta:

```powershell
py consulta_all.py
py consulta_filter.py
py consulta_order_by.py
py consulta_or.py
py consulta_and.py
```

- `consulta_all.py`: presenta todas las clínicas y cuenta sus historias clínicas.
- `consulta_filter.py`: filtra consultorios por especialidad.
- `consulta_order_by.py`: ordena veterinarios por apellido y nombre.
- `consulta_or.py`: busca historias cuyo diagnóstico menciona dermatitis u otitis.
- `consulta_and.py`: busca historias desde una fecha determinada cuyo diagnóstico también contenga “control”.

## Complemento: archivo `.gitignore`

El archivo `.gitignore` contiene reglas para que Git omita archivos locales o temporales al registrar cambios (GitHub Docs, s. f.). En este proyecto se excluyen la caché de Python, los entornos virtuales y la base SQLite generada localmente. La base de datos permanece en la computadora y puede volver a crearse ejecutando los scripts del proyecto.

### Referencia

GitHub Docs. (s. f.). *Ignorar archivos*. https://docs.github.com/es/get-started/git-basics/ignoring-files