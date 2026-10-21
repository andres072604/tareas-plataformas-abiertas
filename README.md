# Práctica #2 — Desarrollo con Plataformas Abiertas

## Descripción
Desarrollo de una API REST utilizando Python y Flask para la práctica del curso Desarrollo con Plataformas Abiertas.

## Tecnologías utilizadas
- Python
- Flask
- Flask-CORS
- Thunder Client

## Endpoints

### 1. Hola
- **Método:** GET
- **Ruta:** `/estudiantes/api/v1/hola`
- **Descripción:** Muestra un mensaje de bienvenida.
- **Respuesta exitosa (200 OK):**

```json
{
  "message": "¡Bienvenido a la API de estudiantes!"
}
```

### 2. Saludo
- **Método:** GET
- **Ruta:** `/estudiantes/api/v1/saludo`
- **Descripción:** Recibe el nombre del estudiante y devuelve un saludo personalizado.

**Cuando se ingresa el nombre:**
- **Respuesta:** `Hola Rafael`
- **Código de estado:** 200 OK

**Cuando no se ingresa el nombre:**
- **Respuesta:** `Debe de ingresar el nombre del estudiante.`
- **Código de estado:** 400 Bad Request

## Ejecución
1. Abrir una terminal dentro de la carpeta `v1`.
2. Instalar las dependencias necesarias:

   `pip install flask flask-cors`

3. Ejecutar la aplicación:

   `python run.py`

La API se ejecuta localmente en `http://127.0.0.1:5000`.

## Autor
Rafael Gómez