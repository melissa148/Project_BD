from .users import user_bp
from .posts import post_bp

def init_routes(app):
    app.register_blueprint(user_bp, url_prefix='/api')
    app.register_blueprint(post_bp, url_prefix='/api')

