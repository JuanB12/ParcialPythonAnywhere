<div align="center">

# 🚐 API de Transporte Puerta a Puerta

**API REST en Python + Flask para gestionar pasajeros, vehículos, viajes, solicitudes, pagos y reportes de una empresa de transporte intermunicipal.**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=FFD43B)
![Flask](https://img.shields.io/badge/Flask-2.3-0B1220?style=flat-square&logo=flask&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-3776AB?style=flat-square&logo=sqlalchemy&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-0B1220?style=flat-square&logo=mysql&logoColor=FFD43B)
![PythonAnywhere](https://img.shields.io/badge/Deploy-PythonAnywhere-3776AB?style=flat-square&logo=pythonanywhere&logoColor=FFD43B)

</div>

---

## 📌 El problema

La empresa *Sistema Tecnológico de Innovación* transporta pasajeros puerta a puerta entre ciudades. La solicitud de vehículos y el registro de viajes se hacían a mano, lo que generaba errores en la administración financiera y pérdidas económicas.

**La solución:** una API que centraliza toda la operación (quién viaja, en qué vehículo, por qué ruta y cuánto pagó) para optimizar la recolección y el transporte de pasajeros.

> Proyecto del parcial de *Desarrollo Móvil 2*, desplegado en PythonAnywhere.

## ✨ Funcionalidades

- **CRUD completo** para 6 entidades: pasajeros, vehículos, viajes, solicitudes, pagos y reportes.
- **Consultas relacionadas** que cruzan pasajeros con viajes, vehículos y pagos.
- Serialización con **Marshmallow** y modelos con **SQLAlchemy**.
- Organización por **Blueprints**: un módulo por entidad.
- Colección de **Postman** lista para probar todos los endpoints.

## 🗂️ Estructura

```
├── app.py                # Punto de entrada: registra los blueprints
├── config/db.py          # Configuración de Flask, SQLAlchemy y Marshmallow
├── models/               # Modelos de las 6 entidades
├── api/                  # Endpoints (un blueprint por entidad)
├── postmant/             # Colección de Postman
└── diagrama/             # Diagrama entidad-relación
```

## 🧩 Modelo de datos

![Diagrama entidad-relación](diagrama/entidad_relacion.jpg)

## 🔌 Endpoints

Todos los endpoints usan el prefijo **`/parcial`**.

| Entidad | Listar | Crear | Actualizar | Eliminar |
|---|---|---|---|---|
| Pasajero | `GET /pasajero` | `POST /savepasajero` | `PUT /updatepasajero` | `DELETE /deletepasajero/<id>` |
| Vehículo | `GET /vehiculo` | `POST /savevehiculo` | `PUT /updatevehiculo` | `DELETE /deletevehiculo/<id>` |
| Viaje | `GET /viaje` | `POST /saveviaje` | `PUT /updateviaje` | `DELETE /deleteviaje/<id>` |
| Solicitud | `GET /solicitud` | `POST /savesolicitud` | `PUT /updatesolicitud` | `DELETE /deletesolicitud/<id>` |
| Pago | `GET /pago` | `POST /savepago` | `PUT /updatepago` | `DELETE /deletepago/<id>` |
| Reporte | `GET /reporte` | `POST /savereporte` | `PUT /updatereporte` | `DELETE /deletereporte/<id>` |

**Consultas relacionadas:**

| Endpoint | Qué devuelve |
|---|---|
| `POST /Relacion` | Pasajeros con su viaje y vehículo |
| `POST /RelacionViaje` | Solicitudes con su viaje |
| `POST /RelacionPasajero` | Pagos con su pasajero |

## 🚀 Cómo ejecutarlo

```bash
# 1. Clonar e ingresar
git clone https://github.com/JuanB12/ParcialPythonAnywhere.git
cd ParcialPythonAnywhere

# 2. Entorno virtual y dependencias
python -m venv venv
venv\Scripts\activate          # En Linux/Mac: source venv/bin/activate
pip install -r requirements.txt

# 3. Variables de entorno (ver .env.example)
set DATABASE_URL=mysql+pymysql://usuario:contraseña@localhost/parcialMovil
set SECRET_KEY=una-clave-larga-y-aleatoria

# 4. Ejecutar
python app.py
```

La API queda en `http://localhost:5000`. Las tablas se crean solas al iniciar.

Para probarla, importa en Postman la colección `postmant/Parcial2_Movil.postman_collection.json`.

## 📸 Pruebas en Postman

<details>
<summary>Ver capturas de los endpoints</summary>

![Postman](image.png)
![Métodos de Pago](image-1.png)
![Métodos de Pasajero](image-2.png)
![Métodos de Reporte](image-3.png)
![Métodos de Solicitud](image-4.png)
![Métodos de Vehículo](image-5.png)
![Métodos de Viaje](image-6.png)

</details>

---

<div align="center">

Hecho por **[Juan Barrios](https://github.com/JuanB12)** · Backend Developer 🐍

</div>
