# 🚑 MediRoute API

REST API para gestión de transporte médico, construida con Python, Django REST Framework y PostgreSQL.

## 🛠️ Tech Stack

- Python 3.11 + Django 5.2
- Django REST Framework
- PostgreSQL
- JWT Authentication (SimpleJWT)
- Celery + Redis (tareas asíncronas)
- Docker + Docker Compose
- pytest (6 tests passing)
- Swagger/OpenAPI (drf-spectacular)

## 🚀 Instalación local

git clone https://github.com/NahuelProgram17/mediroute-api.git
cd mediroute-api
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

## 🐳 Instalación con Docker

docker-compose up --build

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

## 📖 Documentación

Swagger UI disponible en: http://localhost:8000/api/docs/

## 🔐 Autenticación

La API usa JWT. Para acceder a los endpoints protegidos:

1. Obtené tu token en POST /api/auth/token/
2. Incluilo en el header:

Authorization: Bearer <tu_token>

## ✅ Tests

pytest trips/tests.py -v

6 tests passing ✅