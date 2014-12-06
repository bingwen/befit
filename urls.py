from controllers.main import main_bp

def register_blueprint(app):
    app.register_blueprint(main_bp, url_prefix='/m')
