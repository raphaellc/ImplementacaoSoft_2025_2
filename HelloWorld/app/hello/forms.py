from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

class UsuarioForm(FlaskForm):
    """
    Formulário unificado para criar e editar usuários.
    """
    username = StringField('Nome de Usuário', 
                           validators=[DataRequired(message="O nome de usuário é obrigatório.")])
    email = StringField('Email', 
                        validators=[DataRequired(message="O email é obrigatório."), 
                                    Email(message="Por favor, insira um email válido.")])
    submit = SubmitField('Salvar')