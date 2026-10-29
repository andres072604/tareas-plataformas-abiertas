from flask import Blueprint, jsonify, request


estudiantes_endpoints = Blueprint(
    'estudiantes_endpoints',
    __name__
)

@estudiantes_endpoints.route('/hola', methods=['GET'])
def hola():
    return jsonify({
        "message": "¡Bienvenido a la API de estudiantes!"
    }), 200

@estudiantes_endpoints.route('/saludo', methods=['GET'])
def saludar():
    data = request.get_json(silent=True) or {}

    nombre = data.get('nombre')

    if not nombre:
        return jsonify({
            "error": "Debe de ingresar el nombre del estudiante."
        }), 400

    saludo = f"Hola {nombre}"

    return jsonify({
        "saludo": saludo
    }), 200

#--- Practica 3 ---
@estudiantes_endpoints.route('/estudiantes', methods=['GET'])
def obtener_estudiantes():
    return jsonify({
        "mensaje": "Lista de estudiantes obtenida correctamente.",
        "estudiantes": ["Rafael", "Marco", "Pedro"]
    }), 200

@estudiantes_endpoints.route('/estudiantes', methods=['POST'])
def agregar_estudiante():
    data = request.get_json(silent=True)

    if not data or 'nombre' not in data:
        return jsonify({
            "error": "Debe enviar el campo 'nombre' en el JSON."
        }), 400

    return jsonify({
        "mensaje": "Estudiante agregado correctamente.",
        "estudiante": data['nombre']
    }), 201

@estudiantes_endpoints.route('/estudiantes/<int:id>', methods=['PUT'])
def actualizar_estudiante(id):
    data = request.get_json(silent=True)

    if not data or 'nombre' not in data:
        return jsonify({
            "error": "Debe enviar el campo 'nombre' en el JSON."
        }), 400

    return jsonify({
        "mensaje": "Estudiante actualizado correctamente.",
        "id": id
    }), 200

@estudiantes_endpoints.route('/estudiantes/<int:id>', methods=['DELETE'])
def eliminar_estudiante(id):
    return jsonify({
        "mensaje": "Estudiante eliminado correctamente.",
        "id": id
    }), 200