# (O código da classe Produto da Parte 1 deve estar definido acima ou importado)
from Produto import Produto

if __name__ == "__main__":
    
    # a. Instanciando um objeto da classe Produto
    nome_produto = "Notebook Gamer"
    print(f"Criando produto: {nome_produto}")
    notebook = Produto(8000.00, 15)

    # b. Mostrando os valores iniciais
    print("\n--- Valores Iniciais do Produto ---")
    print(f"Preço: R$ {notebook.get_preco():.2f}")
    print(f"Estoque: {notebook.get_estoque()} unidades")
    
    # c. Atualizando os valores dos atributos
    print("\nAtualizando preço e estoque do produto...")
    novo_preco_valido = 8550.50
    novo_estoque_valido = 14 # Simulando uma venda
    notebook.set_preco(novo_preco_valido)
    notebook.set_estoque(novo_estoque_valido)

    # d. Mostrando os valores atualizados
    print("\n--- Valores Atualizados do Produto ---")
    print(f"Preço: R$ {notebook.get_preco():.2f}")
    print(f"Estoque: {notebook.get_estoque()} unidades")

    # e. Tentando definir valores inválidos
    print("\n--- Tentando Definir Valores Inválidos ---")
    preco_invalido = -500.00
    estoque_invalido = -10
    
    print(f"Tentando alterar o preço para R$ {preco_invalido:.2f}...")
    notebook.set_preco(preco_invalido)
    
    print(f"Tentando alterar o estoque para {estoque_invalido} unidades...")
    notebook.set_estoque(estoque_invalido)

    # Exibindo os valores novamente para confirmar que não foram alterados
    print("\n--- Valores Finais (Após Tentativas Inválidas) ---")
    print(f"Preço: R$ {notebook.get_preco():.2f}")
    print(f"Estoque: {notebook.get_estoque()} unidades")
    print("A lógica de proteção da classe funcionou corretamente.")