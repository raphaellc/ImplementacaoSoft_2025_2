import random

# --- Constantes de Configuração ---
# (Clean Code, Capítulo 17: Evite Números Mágicos)
# Definir constantes torna o código mais legível e fácil de modificar.
TAMANHO_VETOR = 10
VALOR_MINIMO = 20
VALOR_MAXIMO = 50


def gerar_vetor_aleatorio(tamanho: int, minimo: int, maximo: int) -> list[int]:
    """
    Gera uma lista (vetor) de números inteiros aleatórios dentro de um intervalo.

    Esta função tem uma única responsabilidade: criar e retornar a lista,
    o que a torna reutilizável e fácil de testar.
    (Clean Code, Capítulo 3: Funções devem fazer uma única coisa).

    Args:
        tamanho: O número de elementos que o vetor deve ter.
        minimo: O valor mínimo (inclusivo) para os números aleatórios.
        maximo: O valor máximo (inclusivo) para os números aleatórios.

    Returns:
        Uma lista de inteiros preenchida com valores aleatórios.
    """
    # List comprehension é uma forma "Pythonic" e eficiente de criar listas.
    return [random.randint(minimo, maximo) for _ in range(tamanho)]


def calcular_soma(vetor: list[int]) -> int:
    """
    Calcula a soma de todos os elementos em uma lista de inteiros.

    O nome da função revela claramente sua intenção.
    (Clean Code, Capítulo 2: Use nomes que revelem a intenção).

    Args:
        vetor: A lista de números a ser somada.

    Returns:
        A soma total dos elementos da lista.
    """
    # Usar a função nativa sum() é a maneira mais limpa e eficiente.
    return sum(vetor)


# O bloco `if __name__ == "__main__"` é o ponto de entrada padrão para um script Python.
# Ele garante que o código só será executado quando o arquivo for invocado diretamente.
if __name__ == "__main__":
    # 1. Geração do vetor
    vetor_de_numeros = gerar_vetor_aleatorio(TAMANHO_VETOR, VALOR_MINIMO, VALOR_MAXIMO)

    # 2. Cálculo da soma
    soma_dos_valores = calcular_soma(vetor_de_numeros)

    # 3. Impressão dos resultados de forma clara
    print(f"Vetor gerado: {vetor_de_numeros}")
    print(f"A soma de todos os valores do vetor é: {soma_dos_valores}")