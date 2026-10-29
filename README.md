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

---

# Práctica #3 — Métodos HTTP

## Descripción
En esta práctica se agregaron nuevos endpoints a la misma API **estudiantes** (Python y Flask) para conocer el funcionamiento de los métodos HTTP más utilizados: GET, POST, PUT y DELETE. Los endpoints son simulados: no usan base de datos ni almacenan información, solo devuelven un mensaje indicando que la operación se realizó correctamente.

## Tecnologías utilizadas
- Python
- Flask
- Postman

## Endpoints

### 1. Obtener todos los estudiantes
- **Método:** GET
- **Ruta:** `/estudiantes/api/v1/estudiantes`
- **Descripción:** Devuelve la lista de estudiantes (simulada).
- **Respuesta exitosa (200 OK):**

```json
{
  "mensaje": "Lista de estudiantes obtenida correctamente.",
  "estudiantes": ["Ana", "Carlos", "María"]
}
```

### 2. Agregar un estudiante
- **Método:** POST
- **Ruta:** `/estudiantes/api/v1/estudiantes`
- **Descripción:** Recibe el nombre de un estudiante en formato JSON y simula agregarlo.
- **Body (JSON):**

```json
{
  "nombre": "Pedro"
}
```

- **Respuesta exitosa (201 Created):**

```json
{
  "mensaje": "Estudiante agregado correctamente.",
  "estudiante": "Pedro"
}
```

- **Si falta el nombre (400 Bad Request):**

```json
{
  "error": "Debe enviar el campo 'nombre' en el JSON."
}
```

### 3. Actualizar un estudiante
- **Método:** PUT
- **Ruta:** `/estudiantes/api/v1/estudiantes/1`
- **Descripción:** Recibe el id en la ruta y el nuevo nombre en formato JSON, y simula la actualización.
- **Body (JSON):**

```json
{
  "nombre": "Pedro Ramírez"
}
```

- **Respuesta exitosa (200 OK):**

```json
{
  "mensaje": "Estudiante actualizado correctamente.",
  "id": 1
}
```

- **Si falta el nombre (400 Bad Request):**

```json
{
  "error": "Debe enviar el campo 'nombre' en el JSON."
}
```

### 4. Eliminar un estudiante
- **Método:** DELETE
- **Ruta:** `/estudiantes/api/v1/estudiantes/1`
- **Descripción:** Recibe el id en la ruta y simula la eliminación.
- **Respuesta exitosa (200 OK):**

```json
{
  "mensaje": "Estudiante eliminado correctamente.",
  "id": 1
}
```

## Pruebas en Postman
Todos los endpoints fueron probados en Postman. La colección exportada se encuentra en la carpeta `Postman/` del repositorio (`Estudiantes.postman_collection.json`).

## Ejecución
1. Abrir una terminal dentro de la carpeta `v1`.
2. Ejecutar la aplicación:

   `python run.py`

La API se ejecuta localmente en `http://127.0.0.1:5000`.

## Autor
Rafael Gómez