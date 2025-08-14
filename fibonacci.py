# Define uma classe que pode ser iterada
class xptoClass:
    """
    Esta classe implementa um iterador que gera uma sequência
    semelhante à de Fibonacci.
    """

    def __iter__(self):
        """
        O método __iter__ é chamado quando a iteração começa.
        Ele inicializa a lista da sequência com o primeiro valor.
        """
        self.a = [0]
        return self

    def __next__(self):
        """
        O método __next__ é chamado em cada passo da iteração.
        Ele calcula o próximo número da sequência e o adiciona à lista.
        """
        # Se a lista tem mais de um elemento, o próximo é a soma dos dois últimos.
        # Caso contrário (no segundo passo), o próximo número é 1.
        if len(self.a) > 1:
            next_value = self.a[-1] + self.a[-2]
        else:
            next_value = 1
        
        self.a.append(next_value)
        
        # O método retorna a lista inteira a cada passo.
        return self.a

# Cria uma instância da classe
xpto = xptoClass()

# Obtém o objeto iterador a partir da instância
xptoIter = iter(xpto)

# Itera 5 vezes, imprimindo o resultado de cada chamada a __next__
print("Iterando e imprimindo a lista a cada passo:")
for k in range(5):
    print(next(xptoIter))

