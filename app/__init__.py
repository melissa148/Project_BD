from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_migrate import Migrate  # Importar Flask-Migrate para las migraciones
from app.neo4j_connection import Neo4jConnection

# Inicializar la base de datos SQLAlchemy (MySQL)
db = SQLAlchemy()

# Inicializar Flask-Migrate
migrate = Migrate()

# Inicializar la conexión a Neo4j
neo4j = Neo4jConnection(uri='bolt://50.16.13.108:7687', user='neo4j', password='pond-dolly-shot')

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')  # Configurar la aplicación con los valores en config.py
    
    # Inicializar la base de datos SQLAlchemy
    db.init_app(app)
    
    # Inicializar Flask-Migrate con la app y db
    migrate.init_app(app, db)
    
    # Configurar Flask-RESTful para las APIs
    api = Api(app)

    # Registrar rutas
    from app.routes import init_routes
    init_routes(app)

    return app
