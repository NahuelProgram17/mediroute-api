# 🚑 MediRoute API

REST API para gestión de transporte médico, construida con Python, Django REST Framework y PostgreSQL.

## 🛠️ Tech Stack

- Python 3.11
- Django 5.2 + Django REST Framework
- PostgreSQL
- Git & GitHub

## 🚀 Features

- CRUD completo de viajes médicos
- Filtros por paciente, estado y dirección
- Ordenamiento por fecha y estado
- Interfaz navegable de la API (DRF Browsable API)

## 📦 Instalación

```bash
git clone https://github.com/NahuelProgram17/mediroute-api.git
cd mediroute-api
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## 📡 Endpoints

| Método | URL | Descripción | Auth |
|--------|-----|-------------|------|
| POST | /api/auth/token/ | Obtener token JWT | ❌ |
| POST | /api/auth/token/refresh/ | Renovar token JWT | ❌ |
| GET | /api/trips/ | Listar todos los viajes | ✅ |
| POST | /api/trips/ | Crear un viaje | ✅ |
| GET | /api/trips/{id}/ | Ver un viaje | ✅ |
| PUT | /api/trips/{id}/ | Actualizar un viaje | ✅ |
| DELETE | /api/trips/{id}/ | Eliminar un viaje | ✅ |

## 🔐 Autenticación

La API usa JWT. Para acceder a los endpoints protegidos:

1. Obtené tu token en `POST /api/auth/token/`
2. Incluilo en el header de cada request:
```
Authorization: Bearer <tu_token>
```
## 🔜 Próximamente

- Tareas asíncronas con Celery + Redis
- Docker & Docker Compose
- Tests con pytest
- Integración Google Maps API