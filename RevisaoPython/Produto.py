class Produto:
    """
    Representa um produto em um sistema CRM, com controle de preço e estoque.
    Atributos privados garantem que os valores de preço e estoque não se tornem negativos.
    """
    
    def __init__(self, preco: float, estoque: int):
        """
        Construtor da classe Produto.

        Args:
            preco (float): O preço inicial do produto.
            estoque (int): A quantidade em estoque inicial do produto.
        """
        # Validação no construtor para não permitir valores negativos na criação
        self.__preco = preco if preco >= 0 else 0.0
        self.__estoque = estoque if estoque >= 0 else 0

    # --- Métodos de Acesso (Getters) ---
    
    def get_preco(self) -> float:
        """Retorna o preço atual do produto."""
        return self.__preco

    def get_estoque(self) -> int:
        """Retorna a quantidade em estoque atual do produto."""
        return self.__estoque

    # --- Métodos de Modificação (Setters) ---

    def set_preco(self, novo_preco: float):
        """
        Atualiza o preço do produto.
        Não permite a atribuição de um valor negativo.
        """
        if novo_preco >= 0:
            self.__preco = novo_preco
        else:
            print("Erro: O preço não pode ser negativo. O valor não foi alterado.")

    def set_estoque(self, nova_quantidade: int):
        """
        Atualiza a quantidade em estoque do produto.
        Não permite a atribuição de um valor negativo.
        """
        if nova_quantidade >= 0:
            self.__estoque = nova_quantidade
        else:
            print("Erro: O estoque não pode ser negativo. O valor não foi alterado.")