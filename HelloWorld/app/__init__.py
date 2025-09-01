from flask import Flask
from .hello.routes import hello_bp
from flask_sqlalchemy import SQLAlchemy




def create_app():
    app = Flask(__name__)
    app.register_blueprint(hello_bp, url_prefix='/hello')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    db = SQLAlchemy(app)

    #definindo um modelo de dados
    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(80), unique=True, nullable=False)
        email = db.Column(db.String(120), unique=True, nullable=False)
        
    with app.app_context():
        db.create_all()

    

    return app

