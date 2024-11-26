from flask import Blueprint, jsonify
from app import db
from app.models import Persona
from app.neo4j_connection import Neo4jConnection

# Definir el Blueprint para influencers
influencer_bp = Blueprint('influencer_bp', __name__)

# Conexión a Neo4j
neo4j = Neo4jConnection(uri='bolt://50.16.13.108:7687', user='neo4j', password='pond-dolly-shot')

# Ruta para marcar a una persona como influencer
@influencer_bp.route('/<int:user_id>/mark_influencer', methods=['POST'])
def mark_influencer(user_id):
    # Obtener el usuario desde la base de datos MySQL
    user = Persona.query.get(user_id)
    if not user:
        return jsonify({"message": "Usuario no encontrado"}), 404

    # Verificar si cumple con los requisitos para ser influencer
    if user.seguidores > 1000 and user.seguidos < (user.seguidores * 0.1):
        # Marcar como influencer en la base de datos MySQL
        user.is_influencer = True  # Asumimos que tienes un campo 'is_influencer' en la tabla Persona
        db.session.commit()

        # Crear la relación ES_INFLUENCER en Neo4j
        query = (
            "MATCH (p:Persona) WHERE p.id = $user_id "
            "CREATE (p)-[:ES_INFLUENCER]->(:Influencer {id: $user_id, nombre: $nombre, NumSeguidores: $numSeguidores}) "
            "RETURN p"
        )
        parameters = {
            'user_id': user_id,
            'nombre': user.nombre,
            'numSeguidores': user.seguidores
        }
        neo4j.query(query, parameters)

        return jsonify({"message": f"{user.nombre} ha sido marcado como influencer en ambas bases de datos."}), 200
    else:
        return jsonify({"message": f"{user.nombre} no cumple los requisitos para ser influencer."}), 400


# Ruta para obtener todos los influencers
@influencer_bp.route('/', methods=['GET'])
def get_influencers():
    influencers = Persona.query.filter(Persona.is_influencer == True).all()  # Asumimos que 'is_influencer' es un campo booleano

    return jsonify([{'id': influencer.id, 'nombre': influencer.nombre} for influencer in influencers]), 200

