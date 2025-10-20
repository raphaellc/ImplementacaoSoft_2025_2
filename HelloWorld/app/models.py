# app/models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    tarefa = db.relationship('Tarefa', back_populates='users')


class Tarefa(db.Model):
    __tablename__ = 'tarefas'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(120), nullable=False)
    descricao = db.Column(db.String(200), nullable=True)
    status = db.Column(db.String(50), default='Pendente')
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    users = db.relationship('User', back_populates='tarefa')

    def __init__(self, titulo, descricao, status, user_id):
        self.titulo = titulo
        self.descricao = descricao
        self.status = status
        self.user_id = user_id

    def __repr__(self):
        return f'Tarefa<{self.description} : {self.user_id}>'
    



