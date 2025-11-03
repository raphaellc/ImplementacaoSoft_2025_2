# app/models.py
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData # 1. Importe o MetaData
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


# 2. Defina a convenção de nomenclatura
# Isto é crucial para que o Alembic (especialmente com SQLite) funcione corretamente
naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

# 3. Passe a convenção de nomenclatura ao inicializar o SQLAlchemy
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    tarefas = db.relationship('Tarefa', back_populates='user')
     
     # 2. Adicionado campo de hash de senha
    password_hash = db.Column(db.String(256))

    # 4. Métodos para gerir a senha
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'



class Tarefa(db.Model):
    __tablename__ = 'tarefas'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(120), nullable=False)
    descricao = db.Column(db.String(200), nullable=True)

    #relacionamento com status_tarefa
    status_id = db.Column(db.Integer, db.ForeignKey('status.id'), nullable=False)
    historico_status = db.relationship('StatusTarefa', back_populates='tarefa', cascade ="all, delete-orphan")

    status_atual = db.relationship('Status', back_populates='tarefas_com_este_status')

    #relacionamento com users
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates='tarefas')

    def __repr__(self):
        return f'Tarefa<{self.description} : {self.user_id}>'

class Status(db.Model):
    __tablename__ = 'status'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    tarefas_com_este_status = db.relationship('Tarefa', back_populates='status_atual')
    logs_de_historico_status = db.relationship('StatusTarefa', back_populates='status')


    
class StatusTarefa(db.Model):
    __tablename__ = 'status_tarefas'
    id = db.Column(db.Integer, primary_key=True)
    
    # Relacionamento com Tarefa
    tarefa_id = db.Column(db.Integer, db.ForeignKey('tarefas.id'), nullable=False)
    tarefa = db.relationship('Tarefa', back_populates='historico_status')
    
    # Relacionamento com Status 
    status_id = db.Column(db.Integer, db.ForeignKey('status.id'), nullable=False)
    status = db.relationship('Status', back_populates='logs_de_historico_status')
    
    dt_modificacao_status = db.Column(db.DateTime, default=db.func.current_timestamp())

    def alteracaoStatus(self, tarefa_id, status_id):
        self.tarefa_id = tarefa_id
        self.status_id = status_id
        

    