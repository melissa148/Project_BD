from flask import Blueprint, request, jsonify
from app import db
from app.models import Persona

# Definir el Blueprint para seguir personas
follow_bp = Blueprint('follow_bp', __name__)

# Ruta para que una persona siga a otra
@follow_bp.route('/<int:follower_id>/follow/<int:followee_id>', methods=['POST'])
def follow_user(follower_id, followee_id):
    follower = Persona.query.get(follower_id)
    followee = Persona.query.get(followee_id)

    if not follower or not followee:
        return jsonify({"message": "Usuario no encontrado"}), 404
    
    # Relacionar en la base de datos (MySQL) y en Neo4j
    follower.following_count += 1
    followee.followers_count += 1
    db.session.commit()

    # Aquí deberías agregar la lógica para crear las relaciones en Neo4j
    # (como SIGUE y SEGUIDO_POR)

    return jsonify({"message": f"{follower.nombre} sigue a {followee.nombre}"}), 200

# Ruta para obtener los seguidores de una persona
@follow_bp.route('/<int:user_id>/followers', methods=['GET'])
def get_followers(user_id):
    user = Persona.query.get(user_id)
    if not user:
        return jsonify({"message": "Usuario no encontrado"}), 404
    
    followers = Persona.query.filter(Persona.following_count > 0).all()
    return jsonify([{'id': f.id, 'nombre': f.nombre} for f in followers]), 200

