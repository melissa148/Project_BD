from .users import user_bp
from .posts import post_bp
from .followers import follow_bp
from .notifications import notification_bp

def init_routes(app):
    # Registrar los Blueprints de cada módulo
    app.register_blueprint(user_bp, url_prefix='/api/users')
    app.register_blueprint(post_bp, url_prefix='/api/posts')
    app.register_blueprint(follow_bp, url_prefix='/api/follow')
    app.register_blueprint(notification_bp, url_prefix='/api/notifications')

