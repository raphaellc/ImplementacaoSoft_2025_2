from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

# ... (outros forms como UsuarioForm podem estar aqui)

class TarefaForm(FlaskForm):
    """
    Formulário para criar e editar tarefas.
    """
    titulo = StringField('Título',
                         validators=[DataRequired(message="O título é obrigatório.")])
    
    descricao = TextAreaField('Descrição') # Descrição é opcional
    
    status = SelectField('Status',
                         coerce=int,
                         validators=[DataRequired()])
    
    submit = SubmitField('Salvar Tarefa')