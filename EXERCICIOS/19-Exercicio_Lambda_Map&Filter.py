#EXERCICIO MAP E FILTER

numeros = [2, 5, 8, 10, 12, 15, 18, 20, 23, 25, 28]

numerando = list(filter(lambda x: x % 2 != 0, numeros))
print(numerando)

mapeando = list(map(lambda x: x**2, numerando))
print(mapeando)