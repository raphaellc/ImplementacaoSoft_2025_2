def func(y):
    """
    Esta é uma função recursiva que calcula a soma dos inteiros de 1 até y.
    """
    # Caso a recursão continue: y é maior que 0
    if y > 0:
        # A função chama a si mesma com um valor menor (y - 1)
        # e soma o resultado com o valor atual de y.
        res = y + func(y - 1)
        # Imprime o resultado parcial a cada passo da "volta" da recursão.
        print(res)
    # Caso base: quando y chega a 0, a recursão para.
    else:
        res = 0
    return res

# Imprime uma linha de título
print("\nResultado da soma recursiva:")

# Chama a função com o valor inicial 3
# A saída impressa será:
# 1
# 3
# 6
func(3)