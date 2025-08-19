import random
from collections import deque

# --- Constantes de Configuração ---
# (Clean Code, Capítulo 17: Evite Números Mágicos)
# Definir constantes torna o código mais legível e fácil de modificar.
TAMANHO_VETOR = 10
VALOR_MINIMO = 1
VALOR_MAXIMO = 100


def gerar_vetor_aleatorio(tamanho: int, minimo: int, maximo: int) -> list[int]:
    """
    Gera um vetor (lista) de números inteiros aleatórios dentro de um intervalo.

    Args:
        tamanho: O número de elementos que o vetor deve ter.
        minimo: O valor mínimo (inclusivo) para os números aleatórios.
        maximo: O valor máximo (inclusivo) para os números aleatórios.

    Returns:
        Uma lista de inteiros preenchida com valores aleatórios.
    """
    return [random.randint(minimo, maximo) for _ in range(tamanho)]


def encontrar_extremos(vetor: list[int]) -> tuple[int, int]:
    """
    Encontra o menor e o maior valor em um vetor.

    Esta função tem a única responsabilidade de encontrar os extremos, tornando o
    código principal mais limpo.
    (Clean Code, Capítulo 3: Funções devem fazer uma única coisa).

    Args:
        vetor: A lista de números a ser analisada.

    Returns:
        Uma tupla contendo (menor_valor, maior_valor).
    """
    if not vetor:
        raise ValueError("O vetor não pode estar vazio para encontrar os extremos.")
    
    # Usar as funções nativas min() e max() é a forma mais limpa e eficiente.
    return min(vetor), max(vetor)


def rotacionar_vetor_a_esquerda_deque(vetor: list[int]) -> list[int]:
    """
    Realiza uma rotação à esquerda nos elementos do vetor de forma eficiente.

    Para operações de rotação, a estrutura 'deque' é otimizada e mais legível.
    (Think Python: Escolhendo a estrutura de dados correta).

    Args:
        vetor: O vetor original a ser rotacionado.

    Returns:
        Um novo vetor com os elementos rotacionados.
    """
    if not vetor:
        return []
    
    # Converte a lista para um deque para performance otimizada em rotações
    vetor_deque = deque(vetor)
    vetor_deque.rotate(-1)  # O argumento -1 indica uma rotação à esquerda
    
    return list(vetor_deque)


# --- Bloco Principal de Execução ---
# O ponto de entrada do script, orquestrando as chamadas de função.
if __name__ == "__main__":
    print("--- Operações com Vetores: Boas Práticas ---")

    # a. e b. Declara e preenche o vetor
    vetor_original = gerar_vetor_aleatorio(TAMANHO_VETOR, VALOR_MINIMO, VALOR_MAXIMO)
    print(f"\n[Passo 1] Vetor original gerado:\n{vetor_original}")

    # c. Imprime os valores de maneira invertida
    # O fatiamento (slicing) `[::-1]` é a forma mais "Pythonic" de inverter uma lista.
    print(f"\n[Passo 2] Vetor invertido:\n{vetor_original[::-1]}")

    # d. Mostra o maior e o menor valor
    try:
        menor, maior = encontrar_extremos(vetor_original)
        print("\n[Passo 3] Análise de valores:")
        print(f"   - Menor valor encontrado: {menor}")
        print(f"   - Maior valor encontrado: {maior}")
    except ValueError as e:
        print(f"Erro ao analisar o vetor: {e}")

    # e. Faz a rotação à esquerda
    vetor_rotacionado = rotacionar_vetor_a_esquerda_deque(vetor_original)
    print("\n[Passo 4] Rotação à esquerda:")
    print(f"   - Vetor antes da rotação:  {vetor_original}")
    print(f"   - Vetor após 1ª rotação:   {vetor_rotacionado}")

    # Exemplo de uma segunda rotação para demonstrar o comportamento
    vetor_rotacionado_2x = rotacionar_vetor_a_esquerda_deque(vetor_rotacionado)
    print(f"   - Vetor após 2ª rotação:   {vetor_rotacionado_2x}")