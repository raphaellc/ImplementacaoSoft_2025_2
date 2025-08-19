# Arquivo: main_refatorado.py
from Produto_refatorado import Produto

def exibir_status_produto(produto: Produto):
    """
    Função auxiliar para exibir os detalhes de um produto.
    (Clean Code: Funções devem ser pequenas e fazer apenas uma coisa).
    """
    print(f"--- Status do Produto: {produto.nome} ---")
    # Acesso aos atributos de forma limpa e direta graças às properties
    print(f"Preço: R$ {produto.preco:.2f}")
    print(f"Estoque: {produto.estoque} unidades")
    print("-" * (30 + len(produto.nome)))

# --- Bloco Principal de Execução ---
if __name__ == "__main__":
    
    # a. Instanciando o objeto com valores válidos
    try:
        notebook = Produto(nome="Notebook Gamer", preco_inicial=8000.00, estoque_inicial=15)
        exibir_status_produto(notebook)
    except ValueError as e:
        print(f"Erro ao criar o produto: {e}")

    # c. Atualizando os valores dos atributos
    print("\n>>> Atualizando preço e estoque após uma venda...")
    notebook.preco = 8550.50  # Uso do setter de forma natural
    notebook.estoque -= 1     # O acesso também funciona para operações aritméticas
    
    # d. Mostrando os valores atualizados
    exibir_status_produto(notebook)

    # e. Tentando definir valores inválidos com tratamento de erro
    print("\n>>> Tentando definir valores inválidos...")
    try:
        preco_invalido = -500.00
        print(f"Tentando alterar o preço para R$ {preco_invalido:.2f}...")
        notebook.preco = preco_invalido
    except ValueError as e:
        # (Clean Code: O código que chama decide como lidar com o erro)
        print(f"   Falha controlada: {e}")

    try:
        estoque_invalido = -10
        print(f"Tentando alterar o estoque para {estoque_invalido} unidades...")
        notebook.estoque = estoque_invalido
    except ValueError as e:
        print(f"   Falha controlada: {e}")

    # Exibindo os valores finais para confirmar a proteção
    print("\n>>> Verificando valores finais...")
    exibir_status_produto(notebook)
    print("A lógica de proteção da classe funcionou e os erros foram tratados.")