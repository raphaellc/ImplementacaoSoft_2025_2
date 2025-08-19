import random

def criar_tabuleiro(linhas, colunas, letras):
    """
    Cria um tabuleiro com n linhas e m colunas, preenchido com
    cinco letras distribuídas aleatoriamente.

    Args:
        linhas (int): O número de linhas do tabuleiro.
        colunas (int): O número de colunas do tabuleiro.
        letras (list): Uma lista contendo as cinco letras a serem usadas.

    Returns:
        list: Uma lista de listas representando o tabuleiro preenchido.
    """
    if not letras or len(letras) != 5:
        raise ValueError("A lista de letras deve conter exatamente 5 elementos.")

    # Cria uma lista com todas as coordenadas possíveis (linha, coluna)
    posicoes = [(l, c) for l in range(linhas) for c in range(colunas)]
    
    # Embaralha as posições para garantir a aleatoriedade
    random.shuffle(posicoes)
    
    # Cria um tabuleiro vazio preenchido com None
    tabuleiro = [[None for _ in range(colunas)] for _ in range(linhas)]
    
    # Itera sobre as posições embaralhadas para preencher o tabuleiro
    indice_letra = 0
    for linha, coluna in posicoes:
        # Atribui uma letra à posição atual
        tabuleiro[linha][coluna] = letras[indice_letra]
        # Cicla através das 5 letras usando o operador de módulo
        indice_letra = (indice_letra + 1) % len(letras)
        
    return tabuleiro

def imprimir_tabuleiro(tabuleiro):
    """
    Imprime o tabuleiro formatado no console.
    """
    print("\n--- Tabuleiro Gerado ---")
    for linha in tabuleiro:
        # Usa ' '.join() para imprimir cada linha com espaços entre as letras
        print(" ".join(linha))
    print("------------------------")

# --- Bloco Principal de Execução ---
if __name__ == "__main__":
    # 1. Coletar as dimensões do tabuleiro do usuário
    while True:
        try:
            n_linhas = int(input("Digite o número de linhas (n): "))
            m_colunas = int(input("Digite o número de colunas (m): "))
            if n_linhas > 0 and m_colunas > 0:
                break
            else:
                print("Erro: O número de linhas и colunas deve ser maior que zero.")
        except ValueError:
            print("Erro: Por favor, digite um número inteiro válido.")

    # 2. Coletar as cinco letras do usuário
    letras_usuario = []
    print("\nDigite as 5 letras que irão preencher o tabuleiro.")
    while len(letras_usuario) < 5:
        letra = input(f"Digite a {len(letras_usuario) + 1}ª letra: ").strip()
        
        # Validação da entrada
        if not letra.isalpha() or len(letra) != 1:
            print("Erro: Por favor, digite uma única letra do alfabeto.")
        elif letra.upper() in letras_usuario:
            print("Erro: Essa letra já foi informada. Tente outra.")
        else:
            letras_usuario.append(letra.upper())
            
    # 3. Criar e imprimir o tabuleiro
    try:
        tabuleiro_final = criar_tabuleiro(n_linhas, m_colunas, letras_usuario)
        imprimir_tabuleiro(tabuleiro_final)
    except ValueError as e:
        print(f"Ocorreu um erro: {e}")