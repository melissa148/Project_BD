from flask import Blueprint, request, jsonify
from app import db
from app.models import Persona

# Definir el Blueprint para usuarios
user_bp = Blueprint('user_bp', __name__)

# Ruta para crear un nuevo usuario
@user_bp.route('/', methods=['POST'])
def create_user():
    data = request.json
    if 'nombre' not in data or 'fechaNacimiento' not in data:
        return jsonify({"message": "Nombre y fecha de nacimiento son requeridos"}), 400
    
    # Crear usuario en la base de datos MySQL
    new_user = Persona(
        nombre=data['nombre'],
        correo=data.get('correo'),
        celular=data.get('celular'),
        fechaNacimiento=data['fechaNacimiento']
    )
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "User created successfully"}), 201

# Ruta para obtener todos los usuarios
@user_bp.route('/', methods=['GET'])
def get_users():
    users = Persona.query.all()
    return jsonify([{'id': user.id, 'nombre': user.nombre, 'correo': user.correo} for user in users]), 200
