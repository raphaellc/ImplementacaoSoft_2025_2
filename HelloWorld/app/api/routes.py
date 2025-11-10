from flask import Blueprint, request, jsonify, current_app, abort
from functools import wraps
import jwt
from datetime import datetime, timedelta, UTC, timezone
from app.models import User, Tarefa, Status, db # Importamos os modelos existentes

api_bp = Blueprint('api', __name__, url_prefix='/api')

# --- DECORADOR DE AUTENTICAÇÃO ---

def token_required(f):
    """
    Decorador para proteger rotas que exigem um JWT válido.
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # O token é esperado no cabeçalho 'Authorization'
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            
            try:
                # O formato é "Bearer <token>"
                token = auth_header.split(" ")[1].strip()
            except IndexError:
                return jsonify({"erro": "Formato de token inválido. Use 'Bearer <token>'"}), 401
        
        if not token:
            return jsonify({"erro": "Token não encontrado no cabeçalho Authorization"}), 401

        try:
            # Decodifica o token usando a SECRET_KEY da aplicação
            print(token)
            data = jwt.decode(
                token, 
                current_app.config['SECRET_KEY'].encode('utf-8'), 
                algorithms=["HS256"],
                leeway=10
            )
            
            # Busca o utilizador no banco de dados com base no 'sub' (subject) do token
            current_user = User.query.get(int(data['sub']))
            
            if not current_user:
                return jsonify({"erro": "Utilizador do token não encontrado"}), 401

        except jwt.ExpiredSignatureError:
            return jsonify({"erro": "Token expirado"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"erro": "Token inválido"}), 401
        
        # Passa o utilizador carregado para a rota protegida
        return f(current_user, *args, **kwargs)

    return decorated

# --- ROTA DE LOGIN DA API ---

@api_bp.route('/login', methods=['POST'])
def api_login():
    """
    Endpoint de login. Recebe JSON, verifica credenciais e retorna um JWT.
    """
    data = request.get_json()
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({"erro": "Email e senha são obrigatórios"}), 400

    # Usa o modelo User e os métodos de senha existentes
    user = User.query.filter_by(email=data['email']).first()

    if not user or not user.check_password(data['password']):
        return jsonify({"erro": "Credenciais inválidas"}), 401
        
    # Cria o Payload do token
    payload = {
        'sub': str(user.id), # 'sub' (Subject) é o ID do utilizador
        'iat': datetime.now(timezone.utc).timestamp(), # 'iat' (Issued At)
        'exp': (datetime.now(timezone.utc) + timedelta(days=1)).timestamp() # 'exp' (Expiration)
    }
    
    # Gera o Token
    token = jwt.encode(
        payload,
        current_app.config['SECRET_KEY'].encode('utf-8'),
        algorithm="HS256"
    )
    print(token)
    return jsonify({"mensagem": "Login bem-sucedido", "token": token})

# --- ROTA DE API PROTEGIDA ---

@api_bp.route('/tarefas', methods=['GET'])
@token_required
def get_tarefas(current_user):
    """
    Retorna a lista de tarefas (em JSON) APENAS do utilizador autenticado
    via JWT.
    """
    
    # current_user é injetado pelo decorador @token_required
    tarefas_db = Tarefa.query.filter_by(user_id=current_user.id).all()
    
    tarefas_lista = []
    for t in tarefas_db:
        tarefas_lista.append({
            'id': t.id,
            'titulo': t.titulo,
            'descricao': t.descricao,
            'status': t.status_atual.nome
        })
        
    return jsonify(tarefas_lista)