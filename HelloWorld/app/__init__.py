from flask import Flask
import os
from .hello.routes import hello_bp
from .tarefas.routes import tarefas_bp
from .autenticacao.routes import auth_bp

from .models import db, User  # Importa a instância 'db' do models.py
from flask_migrate import Migrate
from flask_login import LoginManager

def create_app():
    app = Flask(__name__)
    app.secret_key = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    db.init_app(app)
    migrate = Migrate(app, db)
    
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.init_app(app)
    # Define a rota para onde utilizadores não logados são redirecionados
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Por favor, faça login para aceder a esta página.'
    login_manager.login_message_category = 'warning'

    @login_manager.user_loader
    def load_user(user_id):
        # Callback para recarregar o utilizador a partir da sessão
        return User.query.get(int(user_id))




    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(hello_bp, url_prefix='/hello')
    app.register_blueprint(tarefas_bp, url_prefix='/tarefas')


    return app

