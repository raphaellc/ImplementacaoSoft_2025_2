# Arquivo: produto_refatorado.py

class Produto:
    """
    Representa um produto com encapsulamento e validação de dados.

    Utiliza properties para um acesso mais limpo e natural aos atributos,
    enquanto mantém a lógica de validação. Lança exceções para entradas
    inválidas, permitindo que o código cliente decida como lidar com o erro.
    """
    
    def __init__(self, nome: str, preco_inicial: float, estoque_inicial: int):
        """Construtor da classe Produto."""
        self._nome = nome
        # Ao atribuir a self.preco e self.estoque, estamos chamando os setters
        # que contêm a lógica de validação. (Princípio DRY - Don't Repeat Yourself)
        self.preco = preco_inicial
        self.estoque = estoque_inicial

    @property
    def nome(self) -> str:
        """Property que atua como 'getter' para o nome do produto."""
        return self._nome

    @property
    def preco(self) -> float:
        """
        Property que atua como 'getter' para o preço.
        Retorna o valor do atributo privado _preco.
        """
        return self._preco

    @preco.setter
    def preco(self, novo_preco: float):
        """
        Setter para o preço. Valida se o valor não é negativo.
        
        Lança:
            ValueError: Se o novo_preco for negativo.
            (Clean Code: Use exceções em vez de retornar códigos de erro/mensagens).
        """
        if novo_preco < 0:
            raise ValueError("O preço não pode ser um valor negativo.")
        self._preco = novo_preco

    @property
    def estoque(self) -> int:
        """Property que atua como 'getter' para o estoque."""
        return self._estoque

    @estoque.setter
    def estoque(self, nova_quantidade: int):
        """
        Setter para o estoque. Valida se a quantidade não é negativa.

        Lança:
            ValueError: Se a nova_quantidade for negativa.
        """
        if nova_quantidade < 0:
            raise ValueError("O estoque não pode ser um valor negativo.")
        self._estoque = nova_quantidade

    def __repr__(self) -> str:
        """
        Representação oficial do objeto, útil para debugging.
        (Boa prática de Python: Fornecer uma representação clara do objeto).
        """
        return f"Produto(nome='{self.nome}', preco={self.preco}, estoque={self.estoque})"