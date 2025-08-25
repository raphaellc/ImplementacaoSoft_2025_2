from flask import Blueprint

hello_bp = Blueprint('hello', __name__, url_prefix='/hello')

@hello_bp.route('/')
def index():
    return 'Hello, World!'