from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from app.neo4j_connection import Neo4jConnection

# Inicializar la base de datos SQLAlchemy (MySQL)
db = SQLAlchemy()

# Inicializar la conexión a Neo4j
neo4j = Neo4jConnection(uri='bolt://localhost:7687', user='neo4j', password='password')

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    # Inicializar la base de datos SQLAlchemy
    db.init_app(app)

    # Configurar Flask-RESTful para las APIs
    api = Api(app)

    # Registrar rutas
    from app.routes import init_routes
    init_routes(app)

    return app

