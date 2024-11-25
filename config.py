class Config:
    # Configuración para MySQL (relacional)
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@localhost/db_name'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configuración para Neo4j (no relacional)
    NEO4J_URI = "bolt://localhost:7687"
    NEO4J_USER = "neo4j"
    NEO4J_PASSWORD = "password"

