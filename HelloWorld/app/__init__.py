from flask import Flask
from .hello.routes import hello_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(hello_bp, url_prefix='/hello')
    return app
    