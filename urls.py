from controllers.main import main_bp
from controllers.admin import admin_bp
from controllers.user import user_bp


def register_blueprint(app):
    app.register_blueprint(main_bp, url_prefix='/m')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(user_bp, url_prefix='/user')
