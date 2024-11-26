from app import db
# modelo persona
class Persona(db.Model):
    __tablename__ = 'persona'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    correo = db.Column(db.String(120), unique=True, nullable=True)
    celular = db.Column(db.String(15), unique=True, nullable=True)
    fechaNacimiento = db.Column(db.Date, nullable=False)
    seguidores = db.Column(db.Integer, default=0)
    seguidos = db.Column(db.Integer, default=0)
    
    # Nuevo campo para marcar si la persona es un influencer
    is_influencer = db.Column(db.Boolean, default=False)

    # Relaciones con otras tablas
    publicaciones = db.relationship('Publicacion', backref='persona', lazy=True)
    notificaciones = db.relationship('Notificacion', backref='persona', lazy=True)

 #modelo publicación
class Publicacion(db.Model):
    __tablename__ = 'publicacion'
    
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable=False)
    esEspecial = db.Column(db.Boolean, default=False)
    persona_id = db.Column(db.Integer, db.ForeignKey('persona.id'), nullable=False)

# modelo notificacion

class Notificacion(db.Model):
    __tablename__ = 'notificacion'
    
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.String(255), nullable=False)
    fechaNotificacion = db.Column(db.DateTime, nullable=False)
    persona_id = db.Column(db.Integer, db.ForeignKey('persona.id'), nullable=False)
# modelo modelo seguidor
class Seguidor(db.Model):
    __tablename__ = 'seguidor'
    
    id = db.Column(db.Integer, primary_key=True)
    seguidor_id = db.Column(db.Integer, db.ForeignKey('persona.id'), nullable=False)
    seguido_id = db.Column(db.Integer, db.ForeignKey('persona.id'), nullable=False)
    
