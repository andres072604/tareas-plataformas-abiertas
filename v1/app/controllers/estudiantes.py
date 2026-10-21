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