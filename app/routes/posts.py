from flask import Blueprint, request, jsonify
from app import db
from app.models import Publicacion, Persona

# Definir el Blueprint para publicaciones
post_bp = Blueprint('post_bp', __name__)

# Ruta para crear una nueva publicación
@post_bp.route('/', methods=['POST'])
def create_post():
    data = request.json
    
    if 'url' not in data or 'persona_id' not in data:
        return jsonify({"message": "URL y persona_id son requeridos"}), 400
    
    # Crear publicación en la base de datos MySQL
    persona = Persona.query.get(data['persona_id'])
    if not persona:
        return jsonify({"message": "Persona no encontrada"}), 404
    
    new_post = Publicacion(
        url=data['url'],
        esEspecial=data.get('esEspecial', False),
        persona_id=data['persona_id']
    )
    db.session.add(new_post)
    db.session.commit()
    
    return jsonify({"message": "Post created successfully"}), 201

# Ruta para obtener todas las publicaciones
@post_bp.route('/', methods=['GET'])
def get_posts():
    posts = Publicacion.query.all()
    return jsonify([{'id': post.id, 'url': post.url, 'esEspecial': post.esEspecial, 'persona_id': post.persona_id} for post in posts]), 200
