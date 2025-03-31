# A função filter() do Python filtra elementos de uma sequência com base em uma condição. É uma função integrada que pode ser usada com listas, dicionários, e outros iteráveis. 
# 
# 
# lista = [0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# numeros_pares = list(filter(lambda x: x % 2 == 0, lista))
# print(numeros_pares)

# lista = ['anady', 'socorro', 'alice', 'bob', 'antonio', 'charles', 'tom']
# nome_filter = list(filter(lambda x: x == "alice", lista))
# print(nome_filter)

# lista1 = ['anady', 'socorro', 'alice', 'bob', 'antonio', 'charles', 'tom']
# nome_filter1 = list(filter(lambda x: x[0] == 'a', lista1))
# print(nome_filter1)


### MAP Sintaxe
##A sintaxe geral para a função map é: map(function, iterable, [iterable1, iterable2, . . . ]). 
#A função map em Python é uma função nativa que aplica uma função a cada item de uma sequência, como uma lista ou um dicionário. Ela retorna uma nova sequência com os resultados. 

# numeros = [1, 2, 3, 4, 5]
# quadrados = list(map(lambda x: x**2, numeros))
# print(quadrados)

palavras = ['maca', 'banana', 'pera', 'uva']
palavras_contagem = list(map(lambda x: len(x),palavras))
print(palavras_contagem)