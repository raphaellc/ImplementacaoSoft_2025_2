import random

# a. e b. Declara e preenche o vetor
vetor = [random.randint(1, 100) for _ in range(10)]

print("Vetor original:", vetor)
print("Vetor invertido:", vetor[::-1])
print(f"Maior: {max(vetor)}, Menor: {min(vetor)}")

# Função de rotação inline
rotacionado = vetor[1:] + vetor[:1]
print("Rotacionado:", rotacionado)
print("2ª rotação:", rotacionado[1:] + rotacionado[:1])