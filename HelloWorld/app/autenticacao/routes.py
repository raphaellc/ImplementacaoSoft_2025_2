from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user
from app.models import db, User
from .forms import LoginForm, RegistrationForm

# Definimos o Blueprint e especificamos uma pasta de templates modular
auth_bp = Blueprint('auth', __name__, template_folder='templates')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Rota de login do utilizador."""
    # Se o utilizador já estiver logado, redireciona para a página de tarefas
    if current_user.is_authenticated:
        return redirect(url_for('tarefas.listarTarefasUsuario'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        
        # Verifica se o utilizador existe e se a senha está correta
        if user is None or not user.check_password(form.password.data):
            flash('Email ou senha inválidos.', 'danger')
            return redirect(url_for('auth.login'))
        
        # Se tudo estiver correto, faz o login
        login_user(user, remember=form.remember_me.data)
        flash('Login efetuado com sucesso!', 'success')
        
        # Redireciona para a página de tarefas
        return redirect(url_for('tarefas.listarTarefasUsuario'))
        
    return render_template('login.html', title='Login', form=form)

@auth_bp.route('/logout')
def logout():
    """Rota de logout do utilizador."""
    logout_user()
    return redirect(url_for('auth.login'))

@auth_bp.route('/registrar', methods=['GET', 'POST'])
def registrar():
    """Rota de registo de novos utilizadores."""
    if current_user.is_authenticated:
        return redirect(url_for('tarefas.listarTarefasUsuario'))
        
    form = RegistrationForm()
    if form.validate_on_submit():
        # Cria o novo utilizador
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        
        flash('Registo concluído com sucesso! Pode agora fazer login.', 'success')
        return redirect(url_for('auth.login'))
        
    return render_template('registro.html', title='Registro', form=form)