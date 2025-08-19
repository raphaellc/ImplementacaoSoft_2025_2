import random

# a. e b. Declara e preenche o vetor em uma linha
vetor = [random.randint(20, 50) for _ in range(10)]

# c. Imprime o vetor e a soma
print("Vetor:", vetor)
print("Soma:", sum(vetor))