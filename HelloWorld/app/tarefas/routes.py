from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
# Adicionado User para buscar o usuário pelo ID
from ..models import db, Tarefa, User, Status, StatusTarefa
from .forms import TarefaForm

# Crie um novo Blueprint para tarefas
# O prefixo /tarefas foi removido para dar mais flexibilidade às rotas
tarefas_bp = Blueprint('tarefas', __name__)

def popular_status_form(form):
    status_escolhas = [(s.id, s.nome) for s in Status.query.order_by('nome').all()]
    print(status_escolhas)
    form.status.choices = status_escolhas


# A rota agora espera o ID do usuário para saber de quem são as tarefas
@tarefas_bp.route('/usuario/<int:user_id>/tarefas', methods=['GET', 'POST'])
def listarTarefasUsuario(user_id):
    """
    Exibe a lista de tarefas de um usuário específico e o formulário para criar uma nova.
    """
    user = User.query.get_or_404(user_id)
    print(user)
    form = TarefaForm()
    popular_status_form(form)
    
    if form.validate_on_submit():
        # Lógica para CRIAR uma nova tarefa
        titulo = form.titulo.data
        descricao = form.descricao.data
        status = form.status.data
        
        # Associa a tarefa ao usuário identificado pelo user_id da URL
        nova_tarefa = Tarefa(titulo=titulo, descricao=descricao, status_id=status, user_id=user.id)
        
        db.session.add(nova_tarefa)
        
        db.session.flush()
        log_inicial = StatusTarefa(tarefa_id=nova_tarefa.id, status_id=nova_tarefa.status_id)
        db.session.add(log_inicial)

        
        db.session.commit()
        
        flash('Tarefa criada com sucesso!', 'success')
        return redirect(url_for('tarefas.listarTarefasUsuario', user_id=user.id))
        
    # Lógica para LISTAR as tarefas do usuário
    # a depender do lazy altera aqui - joined? Subquery?!

    tarefas = Tarefa.query.filter_by(user_id=user.id).all()
    
    # Passa o objeto 'user' para o template
    return render_template('tarefas.html', form=form, tarefas=tarefas, user=user)



@tarefas_bp.route('/tarefas/editar/<int:tarefa_id>', methods=['GET', 'POST'])
def editarTarefa(tarefa_id):
    """
    Rota para editar uma tarefa existente.
    """
    tarefa = Tarefa.query.get_or_404(tarefa_id)
    form = TarefaForm(obj=tarefa, status=tarefa.status_id)
    popular_status_form(form)
    
    if form.validate_on_submit():
        # Lógica para ATUALIZAR a tarefa
        novo_status_id = form.status.data
        
        if tarefa.status_id != novo_status_id:
            novo_log_status = StatusTarefa(tarefa_id=tarefa.id, status_id=novo_status_id)
            db.session.add(novo_log_status)
            tarefa.status_id = novo_status_id
        
        tarefa.titulo = form.titulo.data
        tarefa.descricao = form.descricao.data
        
        db.session.commit()
        flash('Tarefa atualizada com sucesso!', 'success')
        # Redireciona de volta para a lista de tarefas do usuário dono da tarefa
        return redirect(url_for('tarefas.listarTarefasUsuario', user_id=tarefa.user_id))
        
    return render_template('editar_tarefas.html', form=form, tarefa=tarefa)

@tarefas_bp.route('/tarefas/remover/<int:tarefa_id>', methods=['POST'])
def removerTarefa(tarefa_id):
    """
    Rota para remover uma tarefa.
    """
    tarefa = Tarefa.query.get_or_404(tarefa_id)
    user_id_dono = tarefa.user_id # Guarda o ID antes de deletar
    
    db.session.delete(tarefa)
    db.session.commit()
    flash('Tarefa removida com sucesso!', 'info')
    
    # Redireciona de volta para a lista de tarefas do usuário que era dono da tarefa
    return redirect(url_for('tarefas.listarTarefasUsuario', user_id=user_id_dono))

