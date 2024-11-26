from flask import Blueprint, request, jsonify
from app import db
from app.models import Notificacion, Persona

# Definir el Blueprint para notificaciones
notification_bp = Blueprint('notification_bp', __name__)

# Ruta para crear una nueva notificación
@notification_bp.route('/', methods=['POST'])
def create_notification():
    data = request.json
    if 'texto' not in data or 'fechaNotificacion' not in data:
        return jsonify({"message": "Texto y fecha de notificación son requeridos"}), 400
    
    # Crear notificación en la base de datos MySQL
    new_notification = Notificacion(
        texto=data['texto'],
        fechaNotificacion=data['fechaNotificacion'],
        persona_id=data.get('persona_id')  # Asociar la notificación a un usuario
    )
    db.session.add(new_notification)
    db.session.commit()

    return jsonify({"message": "Notification created successfully"}), 201

# Ruta para obtener las notificaciones de un usuario
@notification_bp.route('/<int:user_id>', methods=['GET'])
def get_notifications(user_id):
    # Obtener las notificaciones asociadas al usuario
    notifications = Notificacion.query.filter_by(persona_id=user_id).all()
    return jsonify([{'id': n.id, 'texto': n.texto, 'fecha': n.fechaNotificacion} for n in notifications]), 200
