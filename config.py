class Config:
    # Configuración para MySQL (relacional)
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:xTuMaNptdsOzYlHUbeDPiCfnbfpiMAVy@junction.proxy.rlwy.net:12553/railway'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configuración para Neo4j (no relacional)
    NEO4J_URI = "bolt://50.16.13.108:7687"
    NEO4J_USERNAME = "neo4j"
    NEO4J_PASSWORD = "pond-dolly-shot"
    NEO4J_DATABASE = "neo4j"

