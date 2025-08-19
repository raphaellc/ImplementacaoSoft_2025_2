import random

# a. Declara um vetor de inteiros de 10 posições
vetor = [0] * 10

# b. Preenche com valores entre 20 e 50
for i in range(10):
    vetor[i] = random.randint(20, 50)

# c. Calcula e imprime a soma
soma = sum(vetor)
print("Vetor:", vetor)
print("Soma dos valores:", soma)