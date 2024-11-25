from flask import Blueprint, request, jsonify
from app import db, neo4j
from app.models import Publicacion

post_bp = Blueprint('post_bp', __name__)

@post_bp.route('/posts', methods=['POST'])
def create_post():
    data = request.json
    new_post = Publicacion(
        url=data['url'],
        esEspecial=data.get('esEspecial', False),
        persona_id=data['persona_id']
    )
    db.session.add(new_post)
    db.session.commit()

    # Crear nodo de Publicación en Neo4j
    query = (
        "MATCH (u:Persona) WHERE ID(u) = $persona_id "
        "CREATE (p:Publicacion {url: $url, esEspecial: $esEspecial}) "
        "CREATE (u)-[:CREA]->(p) "
        "RETURN p"
    )
    parameters = {
        'persona_id': data['persona_id'],
        'url': data['url'],
        'esEspecial': data.get('esEspecial', False)
    }
    neo4j.query(query, parameters)

    return jsonify({"message": "Post created successfully in both databases"}), 201

