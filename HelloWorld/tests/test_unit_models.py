import pytest
from app.models import User, Tarefa # Importamos os nossos modelos

def test_user_password_hashing():
    """
    Testa unitariamente os métodos set_password e check_password do modelo User.
    Este teste não precisa de base de dados nem de um app_context.
    """
    # 1. Preparação
    user = User(username='test_user', email='test@example.com')
    
    # 2. Execução
    user.set_password('uma_senha_secreta_123')
    
    # 3. Verificação
    assert user.password_hash is not None
    assert user.password_hash != 'uma_senha_secreta_123'
    assert user.check_password('uma_senha_secreta_123') is True
    assert user.check_password('senha_errada') is False

def test_user_repr():
    """Testa a representação em string do modelo User."""
    user = User(username='testuser')
    assert repr(user) == '<User testuser>'

def test_tarefa_repr():
    """Testa a representação em string do modelo Tarefa."""
    tarefa = Tarefa(titulo='Minha Tarefa')
    
    pass 