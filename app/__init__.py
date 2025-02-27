from flask import Flask
from config.settings import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from app.controllers.product_controller import product_bp
    app.register_blueprint(product_bp, url_prefix='/api')

    return app