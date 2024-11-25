from app import db

class Persona(db.Model):
    __tablename__ = 'persona'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    correo_electronico = db.Column(db.String(120), unique=True, nullable=True)
    telefono = db.Column(db.String(15), unique=True, nullable=True)
    
    # Relaciones con otras tablas
    publicaciones = db.relationship('Publicacion', backref='persona', lazy=True)

class Publicacion(db.Model):
    __tablename__ = 'publicacion'
    
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable=False)
    esEspecial = db.Column(db.Boolean, default=False)
    persona_id = db.Column(db.Integer, db.ForeignKey('persona.id'), nullable=False)

