import random

# a. e b. Declara e preenche o vetor de 10 posições
vetor = []
for _ in range(10):
    vetor.append(random.randint(1, 100))

print(f"Vetor original: {vetor}")

# c. Imprime o vetor de maneira invertida
print(f"Vetor invertido: {vetor[::-1]}")

# d. Mostra o maior e o menor valor
print(f"Menor valor: {min(vetor)}")
print(f"Maior valor: {max(vetor)}")

# e. Faz a rotação à esquerda
# Pega todos os elementos do segundo em diante e adiciona o primeiro no final
vetor_rotacionado = vetor[1:] + vetor[:1]
print(f"Após 1ª rotação: {vetor_rotacionado}")

# Faz uma nova rotação no vetor que já foi rotacionado
vetor_rotacionado_2x = vetor_rotacionado[1:] + vetor_rotacionado[:1]
print(f"Após 2ª rotação: {vetor_rotacionado_2x}")