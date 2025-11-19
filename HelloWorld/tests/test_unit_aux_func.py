import pytest
from unittest.mock import patch, MagicMock
from app.tarefas.utils import popular_status_form 

# --- Objetos "Dublês" (Fakes) ---
# Criamos classes falsas para simular o comportamento do Flask-WTF
# e do SQLAlchemy sem realmente os usarmos.

class FakeStatus:
    """Um dublê para o modelo Status do SQLAlchemy."""
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

class FakeStatusField:
    """Um dublê para o campo SelectField do WTForms."""
    def __init__(self):
        self.choices = [] # A propriedade que a nossa função quer preencher

class FakeForm:
    """Um dublê para o objeto TarefaForm."""
    def __init__(self):
        self.status = FakeStatusField() # O formulário tem um campo 'status'

# --- Fim dos Dublês ---


# O decorador @patch "rapta" a chamada a 'Status.query'
# dentro do ficheiro 'tarefas.utils'
@patch('app.tarefas.utils.Status')
def test_popular_status_form(mock_status_query):
    """
    Testa a função popular_status_form em isolamento,
    simulando (mocking) a chamada à base de dados.
    """
    
    # 1. Preparação (Configurar o Mock)
    
    # Esta é a lista falsa que queremos que a "base de dados" retorne
    fake_statuses = [
        FakeStatus(id=0, nome='pendente'),
        FakeStatus(id=1, nome='iniciada'),
        FakeStatus(id=2, nome='Pendente'),
        FakeStatus(id=3, nome='finalizada')
        
    ]
    
    # Dizemos ao mock para retornar a nossa lista falsa
    # quando a cadeia .order_by(...).all() for chamada.
    #mock_status_query.order_by.return_value.all.return_value = fake_statuses
    
    mock_query = MagicMock()
    mock_order_by = MagicMock()

    # 2. Atribua os mocks
    mock_Status.query = mock_query
    mock_query.order_by.return_value = mock_order_by
    mock_order_by.all.return_value = fake_statuses
    # --- Fim da Correção ---
    # Criamos o nosso formulário falso
    form = FakeForm()
    
    # 2. Execução
    popular_status_form(form) # Executamos a função a ser testada
    
    # 3. Verificação
    
    # Verificamos se a propriedade 'choices' do formulário foi preenchida corretamente
    expected_choices = [
        (0, 'pendente'),
        (1, 'iniciada'),
        (2, 'Pendente'),
        (3, 'finalizada')
    ]
    assert form.status.choices == expected_choices
    
    # (Opcional) Verificamos se a função tentou ordenar por 'nome'
    mock_status_query.order_by.assert_called_with('nome')