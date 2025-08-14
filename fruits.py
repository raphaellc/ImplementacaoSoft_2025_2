fruits = ["maca", "banana", "morango"]

print("--- Método 1: Usando um loop 'while' com um índice ---")
i = 0
while i < len(fruits):
    print(fruits[i])
    i = i + 1

print("\n--- Método 2: Usando 'for' com range(len()) ---")
# Esta forma é útil quando você precisa do índice do elemento.
for i in range(len(fruits)):
    print(fruits[i])

print("\n--- Método 3: Usando o método 'join' para strings ---")
# O método join é muito eficiente para transformar uma lista de strings
# em uma única string. Aqui, usamos o caractere de nova linha '\n'
# como separador para imprimir cada fruta em sua própria linha.
print('\n'.join(fruits))

# Você também poderia usar outro separador, como uma vírgula e um espaço:
# print(', '.join(fruits))

#forma teste
print(fruits)
