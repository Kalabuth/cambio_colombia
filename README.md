#  Django REST API – CMS Editorial para Cambio Colombia

Proyecto desarrollado con Django y Django REST Framework para gestionar artículos, redactores y suscripciones en un sistema editorial tipo CMS.

---

## Tecnologías

- Python 3.11+
- Django
- Django REST Framework
- Postgres
- Pytest

---

## Instalación local

### 1. Clona el repositorio

```bash
git clone https://github.com/Kalabuth/cambio_colombia.git
cd cambio_colombia
````

---

### 2. Crea un entorno virtual

```bash
python -m venv venv
source venv/bin/activate
```

---

### 3. Instala dependencias

```bash
pip install poetry
poetry install
```

---

### 4. Aplica migraciones y levanta el servidor

```bash
python manage.py migrate
python manage.py runserver
```

---

## Modelos y funcionalidades

### Modelos principales

* `User`: modelo de usuario de Django.
* `UsuarioRedactor`: representa un redactor del medio (nombre, correo, activo).
* `Articulo`: título, contenido, estado (`borrador` / `publicado`), autor (redactor) y fecha.
* `Suscripcion`: relacionada con un `User`, con tipo (`gratuita` / `pago`) y fechas.

---

## Exportar artículos como CSV

Puedes exportar los artículos **publicados** desde una fecha específica (o todos, si no pasas fecha):

```bash
python manage.py exportar_articulos --fecha 2024-06-01
```

Esto genera el archivo `articulos.csv`, omitiendo el campo `contenido`.

---

## Endpoints principales (REST)

Todos los endpoints están bajo `/api/`

### Usuarios

* `POST /api/users/` – Crear usuario (auth.User)
* `GET /api/users/` – Listar usuarios creados

### UsuarioRedactor

* `POST /api/redactores/` – Crear nuevo redactor
* `GET /api/redactores/` – Listar redactores

### Artículos

* `GET /api/articulos/` – Listar artículos
* `POST /api/articulos/` – Crear nuevo artículo
* `GET /api/articulos/<id>/` – Obtener detalle
* Soporta filtros:

  * `?estado=publicado` – filtrar por estado
  * `?search=texto` – búsqueda por contenido o título

### Suscripciones

* `POST /api/suscripciones/` – Crear nueva suscripción
* Incluye validación: **no permite suscripciones activas duplicadas** para un usuario.

---

## Ejecutar tests

### Opción 1: Entorno local

```bash
pytest
```

### Opción 2: Con Docker

```bash
docker-compose exec web pytest
```


Incluye tests para:

* Creación, detalle y filtro de artículos
* Validación de suscripciones activas
* Creación y listado de usuarios
* Creación y listado de redactores
* Exportación de artículos (comando management)

---

## Estructura del proyecto

```
cms_project/
├── core/
│   ├── models/
│   │   ├── articulo_model.py
│   │   ├── redactor_model.py
│   │   └── suscripcion_model.py
│   ├── views/
│   │   ├── articulo_view.py
│   │   ├── redactor_view.py
│   │   └── suscripcion_view.py
│   ├── serializers/
│   │   ├── articulo_serializer.py
│   │   ├── redactor_serializer.py
│   │   └── suscripcion_serializer.py
│   ├── urls.py
│   ├── admin.py
│   └── management/
│       └── commands/
│           └── exportar_articulos.py
├── core/tests/
│   └── test_views.py
├── cambio_colomba/
│   └── settings.py, .env, urls.py, wsgi.py...
├── requirements.txt / pyproject.toml
└── README.md
```

---

## Preguntas requeridas por la prueba técnica

### 1. ¿Qué buenas prácticas aplica al versionar código utilizando Git?

* Commits pequeños y claros (`feat:`, `fix:`, `refactor:`).
* Uso de ramas para nuevas features (`feature/`), bugs (`bugfix/`), releases (`release/`).
* Ignorar `.env`, migraciones y archivos temporales con `.gitignore`.
* Uso de `pull requests` y revisión entre pares.

---

### 2. ¿Cómo abordaría el despliegue de este proyecto en un entorno productivo?

* Dockerización con Gunicorn y Nginx.
* Base de datos PostgreSQL.
* Uso de archivos `.env` o servicios secretos.
* Certificados SSL (HTTPS).
* Logs estructurados.
* Backups automáticos.

---

### 3. ¿Tiene experiencia previa trabajando en plataformas CMS o CRM?

Sí, he trabajado con:

* **HubSpot CRM**: gestión de contactos, flujos de trabajo automatizados y segmentación. Esto me dio experiencia directa en el modelado de datos comerciales.

---

### 4. ¿Utilizó modelos built-in como `auth.User`?

Sí. El modelo `Suscripcion` está relacionado con el modelo `User` que ofrece Django por defecto (`django.contrib.auth.models.User`). Esto permite aprovechar su sistema de autenticación y administración de usuarios.

---

## Archivo `.env`

Este repositorio incluye el archivo `.env` **solo por motivos prácticos de revisión**, dado que se trata de una prueba técnica.

En un entorno profesional, este archivo estaría en `.gitignore` y las credenciales se manejarían con herramientas seguras.

---

## Autor
GitHub: [@kalabuth](https://github.com/kalabuth)
