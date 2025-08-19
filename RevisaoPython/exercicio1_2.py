import random

def criar_tabuleiro(n, m, letras):
    # Verifica se foram fornecidas exatamente 5 letras
    if len(letras) != 5:
        print("Por favor, forneça exatamente 5 letras.")
        return None
    
    # Cria o tabuleiro vazio
    tabuleiro = []
    
    # Preenche o tabuleiro com letras aleatórias
    for i in range(n):
        linha = []
        for j in range(m):
            # Escolhe uma letra aleatória das fornecidas
            letra = random.choice(letras)
            linha.append(letra)
        tabuleiro.append(linha)
    
    return tabuleiro

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(linha))

# Solicita as dimensões do tabuleiro
n = int(input("Digite o número de linhas (n): "))
m = int(input("Digite o número de colunas (m): "))

# Solicita as 5 letras
letras = input("Digite 5 letras separadas por espaço (ex: A B C D E): ").split()

# Cria e imprime o tabuleiro
tabuleiro = criar_tabuleiro(n, m, letras)
if tabuleiro:
    print("\nTabuleiro Gerado:")
    imprimir_tabuleiro(tabuleiro)