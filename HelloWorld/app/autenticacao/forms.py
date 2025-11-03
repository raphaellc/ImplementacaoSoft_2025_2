from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.models import User

class LoginForm(FlaskForm):
    """Formulário para login de utilizadores."""
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired()])
    remember_me = BooleanField('Lembrar-me')
    submit = SubmitField('Entrar')

class RegistrationForm(FlaskForm):
    """Formulário para registo de novos utilizadores."""
    username = StringField('Nome de Utilizador', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired()])
    password2 = PasswordField(
        'Repetir Senha', validators=[DataRequired(), EqualTo('password', message='As senhas devem ser iguais.')])
    submit = SubmitField('Registar')

    def validate_username(self, username):
        """Verifica se o nome de utilizador já existe."""
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Este nome de utilizador já está a ser utilizado.')

    def validate_email(self, email):
        """Verifica se o email já existe."""
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Este email já está registado.')
