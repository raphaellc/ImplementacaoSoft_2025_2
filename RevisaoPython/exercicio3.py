# Define constantes para "números mágicos", tornando o código mais legível e fácil de manter.
# (Clean Code, Capítulo 17: Evite Números Mágicos)
LIMITE_INFERIOR = 5
LIMITE_SUPERIOR = 15
VALOR_DE_SAIDA = 0

def solicitar_numero_inteiro(mensagem_prompt: str) -> int:
    """
    Solicita um número ao usuário e garante que a entrada seja um inteiro válido.

    Esta função separa a responsabilidade de interagir com o usuário e validar o tipo de dado.
    (Clean Code, Capítulo 3: Funções devem fazer uma única coisa).

    Args:
        mensagem_prompt: A mensagem a ser exibida para o usuário.

    Returns:
        O número inteiro fornecido pelo usuário.
    """
    while True:
        try:
            entrada_usuario = input(mensagem_prompt)
            return int(entrada_usuario)
        except ValueError:
            print("Erro: Por favor, digite um número inteiro válido.")

def esta_no_intervalo(numero: int, minimo: int, maximo: int) -> bool:
    """
    Verifica se um número está dentro de um intervalo inclusivo [minimo, maximo].
    
    O nome da função é claro e expressa sua intenção (Clean Code, Capítulo 2).
    
    Args:
        numero: O número a ser verificado.
        minimo: O limite inferior do intervalo.
        maximo: O limite superior do intervalo.

    Returns:
        True se o número estiver no intervalo, False caso contrário.
    """
    return minimo <= numero <= maximo

def processar_numeros():
    """
    Função principal que orquestra o loop de entrada e processamento de números.
    """
    print(f"Digite números inteiros positivos. Serão impressos apenas os que estiverem entre {LIMITE_INFERIOR} e {LIMITE_SUPERIOR}.")
    print(f"Digite '{VALOR_DE_SAIDA}' para encerrar o programa.")

    while True:
        numero = solicitar_numero_inteiro("Digite um número: ")

        if numero == VALOR_DE_SAIDA:
            print("Programa encerrado.")
            break # Encerra o loop

        if numero < 0:
            # Ignora números negativos conforme o requisito, mas informa o usuário.
            print("Aviso: Apenas números positivos são considerados.")
            continue # Pula para a próxima iteração

        if esta_no_intervalo(numero, LIMITE_INFERIOR, LIMITE_SUPERIOR):
            print(f"-> Número no intervalo: {numero}")

# O bloco `if __name__ == "__main__"` é uma convenção padrão em Python para
# indicar o ponto de entrada do script, garantindo que o código só seja
# executado quando o arquivo é rodado diretamente.
if __name__ == "__main__":
    processar_numeros()