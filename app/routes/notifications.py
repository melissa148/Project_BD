from flask import Blueprint, request, jsonify
from app import neo4j
from app.models import db, Persona
from app.neo4j_connection import Neo4jConnection

# Crear Blueprint para las notificaciones
notification_bp = Blueprint('notification_bp', __name__)

neo4j = Neo4jConnection(uri='bolt://localhost:7687', user='neo4j', password='password')

# Ruta para crear una nueva notificación
@notification_bp.route('/notifications', methods=['POST'])
def create_notification():
    data = request.json
    # Validar datos recibidos
    if 'texto' not in data or 'fechaNotificacion' not in data:
        return jsonify({"message": "Texto y fecha de notificación son requeridos"}), 400
    
    # Crear notificación en Neo4j
    query = (
        "CREATE (n:Notificacion {id: $id, texto: $texto, fechaNotificacion: $fechaNotificacion}) "
        "RETURN n"
    )
    parameters = {
        'id': data['id'],
        'texto': data['texto'],
        'fechaNotificacion': data['fechaNotificacion']
    }
    result = neo4j.query(query, parameters)
    
    return jsonify({"message": "Notification created successfully", "data": data}), 201

# Ruta para obtener las notificaciones de un usuario
@notification_bp.route('/users/<int:user_id>/notifications', methods=['GET'])
def get_notifications(user_id):
    # Consultar las notificaciones del usuario
    query = (
        "MATCH (p:Persona)-[:RECIBE]->(n:Notificacion) WHERE p.id = $user_id "
        "RETURN n.texto AS texto, n.fechaNotificacion AS fecha"
    )
    parameters = {'user_id': user_id}
    result = neo4j.query(query, parameters)

    # Preparar las notificaciones para devolverlas
    notifications = [{"texto": record["texto"], "fecha": record["fecha"]} for record in result]
    
    return jsonify(notifications), 200

