from flask import Blueprint, request, jsonify
from app import db, neo4j
from app.models import Persona
from app.neo4j_connection import Neo4jConnection

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.json
    # Crear persona en MySQL
    new_persona = Persona(
        nombre=data['name'],
        fecha_nacimiento=data['birth_date'],
        correo_electronico=data.get('email'),
        telefono=data.get('phone')
    )
    db.session.add(new_persona)
    db.session.commit()

    # Crear nodo en Neo4j
    query = (
        "CREATE (u:Persona {nombre: $nombre, fecha_nacimiento: $fecha_nacimiento, correo_electronico: $correo_electronico, telefono: $telefono}) "
        "RETURN u"
    )
    parameters = {
        'nombre': data['name'],
        'fecha_nacimiento': data['birth_date'],
        'correo_electronico': data.get('email'),
        'telefono': data.get('phone')
    }
    neo4j.query(query, parameters)
    
    return jsonify({"message": "User created successfully in both databases"}), 201

