from flask import Flask
from config.settings import Config
from app.controllers.product_controller import product_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    app.register_blueprint(product_bp, url_prefix='/api')
    
    return app