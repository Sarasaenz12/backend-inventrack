# InvenTrack 📦
> Sistema de gestión de inventarios en tiempo real para organizaciones sin ánimo de lucro

Desarrollado para la **Fundación Manos Unidas De Dios**, InvenTrack permite administrar múltiples inventarios (medicamentos, alimentos, herramientas) con control de stock, trazabilidad de movimientos, alertas automáticas y exportación de reportes.

---

## ✨ Características

| Función | Descripción |
|---|---|
| 🔐 Roles y permisos | Admin, Maestro, Jefe, Estudiante con acceso diferenciado |
| 📦 Multi-inventario | Medicamentos, Alimentos, Herramientas y más |
| 🔄 Movimientos | Entradas y salidas con trazabilidad completa |
| 📊 Reportes | Exportación en CSV y PDF |
| 🚨 Alertas automáticas | Stock bajo y productos próximos a vencer |
| ⚙️ Configuración dinámica | Unidades, presentaciones y campos por inventario |
| 📱 Responsive | Adaptable a dispositivos móviles |
| 📈 Dashboard | KPIs en tiempo real |

---

## 🏗️ Arquitectura

```
inventrack/
├── apps/
│   ├── authentication/   # Autenticación JWT y gestión de usuarios
│   ├── inventory/        # Inventarios, categorías y productos
│   ├── movements/        # Entradas y salidas de stock
│   ├── reports/          # Generación y exportación de reportes
│   ├── alerts/           # Alertas de stock bajo y vencimiento
│   └── dashboard/        # KPIs y estadísticas en tiempo real
├── inventrack/           # Configuración principal del proyecto
├── static/               # CSS, JS e imágenes
├── templates/            # Templates HTML base
└── docs/                 # Documentación técnica
```

### Niveles de acceso

```
Nivel 1 — Administrador
  └── Vista global de todos los inventarios
  └── Gestión de personal y permisos
  └── Reportes globales y auditoría
  └── Configuración de inventarios

Nivel 2 — Personal (Maestro / Jefe / Estudiante)
  └── Acceso solo a inventarios asignados
  └── Registro de productos y movimientos
  └── Reportes por inventario
```

---

## 🚀 Instalación local

### Prerrequisitos

- Python 3.10+
- PostgreSQL 14+
- pip y virtualenv

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/inventrack.git
cd inventrack
```

### 2. Crear y activar entorno virtual

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

Crea un archivo `.env` en la raíz del proyecto:

```env
# Django
SECRET_KEY=tu-secret-key-super-segura-aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Base de datos
DATABASE_URL=postgres://postgres:tu-password@localhost:5432/inventrack_db

# Email (para recuperación de contraseña)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=tu-email@gmail.com
EMAIL_HOST_PASSWORD=tu-password-de-app

# Frontend
FRONTEND_URL=http://localhost:5173
```

### 5. Aplicar migraciones y crear superusuario

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 6. Ejecutar el servidor

```bash
python manage.py runserver
```

Accede en: [http://localhost:8000](http://localhost:8000)  
Documentación API: [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/)

---

## 🐳 Docker

```bash
# Construir imagen
docker build -t inventrack .

# Ejecutar contenedor
docker run -p 8000:8000 --env-file .env inventrack
```

---

## 🗄️ Base de datos (PostgreSQL)

```sql
CREATE DATABASE inventrack_db;
CREATE USER inventrack_user WITH PASSWORD 'tu_password';
ALTER ROLE inventrack_user SET client_encoding TO 'utf8';
ALTER ROLE inventrack_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE inventrack_user SET timezone TO 'America/Bogota';
GRANT ALL PRIVILEGES ON DATABASE inventrack_db TO inventrack_user;
```

---

## 🧪 Tests

```bash
# Ejecutar todos los tests
python manage.py test

# Tests de una app específica
python manage.py test apps.movements

# Con reporte de cobertura
coverage run --source='.' manage.py test
coverage report
coverage html
```

---

## 🌐 API

La API está construida con Django REST Framework y documentada con Swagger.

| Método | Endpoint | Descripción |
|---|---|---|
| POST | `/api/auth/login/` | Iniciar sesión |
| POST | `/api/auth/password-reset/` | Solicitar reset de contraseña |
| GET | `/api/inventory/` | Listar inventarios |
| GET | `/api/inventory/products/` | Listar productos |
| POST | `/api/movements/register/` | Registrar movimiento |
| GET | `/api/reports/movements/` | Generar reporte |
| GET | `/api/alerts/` | Ver alertas activas |
| GET | `/api/dashboard/stats/` | Estadísticas del dashboard |

Documentación interactiva disponible en `/api/docs/` (requiere autenticación de administrador).

---

## 🚢 Despliegue en producción

El proyecto está configurado para desplegarse en **Render** con base de datos en **Supabase**.

Variables de entorno requeridas en producción:

```env
SECRET_KEY=           # Clave secreta de Django (obligatoria)
DEBUG=False           # Siempre False en producción
DATABASE_URL=         # URL completa de PostgreSQL
ALLOWED_HOSTS=        # Dominio del servidor
CORS_ALLOWED_ORIGINS= # URL del frontend
FRONTEND_URL=         # URL del frontend
EMAIL_HOST_USER=      # Cuenta de correo para envío
EMAIL_HOST_PASSWORD=  # Contraseña de aplicación
```

---

## 📁 Modelo de datos

```
User ──────────────── assigned_inventories ──► Inventory
                                                    │
                                                    ├──► Category
                                                    │        └──► Product
                                                    │                 └──► Movement
                                                    └──► Alert
```

---

## 👩‍💻 Equipo

| Rol | Persona |
|---|---|
| Desarrolladora | Sara Valentina Sánchez Estrada |
| Docente asesora | Diana María Melo Taborda |
| Tutor empresarial | Gustavo Adolfo Gutiérrez |
| Organización | Fundación Manos Unidas De Dios |
| Área | Modelación y Arquitectura de Datos — Semestre V |

Este proyecto fue desarrollado y mantenido por  
**Sara Valentina Sánchez Estrada**.

Cuentas GitHub utilizadas durante el desarrollo:

- @Sarasaenz12
- @sarasanchez07

Ambas cuentas pertenecen a la misma desarrolladora y fueron utilizadas en distintos entornos académicos y personales.

---

## 📄 Licencia

Proyecto académico desarrollado en el marco de práctica universitaria.  
© 2026 Sara Valentina Sánchez Estrada — Fundación Manos Unidas De Dios.
