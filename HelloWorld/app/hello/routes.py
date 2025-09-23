from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..models import User, db  # Importa a classe User do models.py
from .forms import UsuarioForm

hello_bp = Blueprint('hello', __name__, url_prefix='/hello')

@hello_bp.route('/')
def index():
    
    usuarios = User.query.all()
    form = UsuarioForm()
    return render_template('index.html', usuarios=usuarios, form=form)

@hello_bp.route('/novoUsuario', methods=['GET', 'POST'])
def novoUsuario():
    form = UsuarioForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data

        # Cria uma nova instância do modelo User
        novo_usuario = User(username=username, email=email)

        # Adiciona o novo usuário à sessão do banco de dados
        db.session.add(novo_usuario)

        # Salva as mudanças no banco de dados
        db.session.commit()
        flash('Usuário criado com sucesso!', 'success')
    else:
        #se a validação falhar, exibe erros
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Erro no campo '{getattr(form,field).label.text}': {error}", 'danger')
        # Redireciona para a página principal após a criação
    
    return redirect(url_for('hello.index'))
    


@hello_bp.route('/removerUsuario/<int:usuario_id>', methods=['POST'])
def removerUsuario(usuario_id):
    usuario = User.query.get_or_404(usuario_id)
    if usuario:
        db.session.delete(usuario)
        db.session.commit()
        flash('Usuário removido com sucesso!', 'success')
    return redirect(url_for('hello.index'))

@hello_bp.route('/editarUsuario/<int:usuario_id>', methods=['GET', 'POST'])
def editarUsuario(usuario_id):
    usuario = User.query.get_or_404(usuario_id)
    form = UsuarioForm(obj=usuario)
    if form.validate_on_submit():
        usuario.username = form.username.data
        usuario.email = form.email.data
        db.session.commit()
        flash('Usuário editado com sucesso!', 'success  ')
        return redirect(url_for('hello.index'))
    
    return render_template('editar_usuario.html', form=form, usuario_id=usuario_id)