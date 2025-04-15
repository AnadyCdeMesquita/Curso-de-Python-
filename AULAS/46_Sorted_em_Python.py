"""
A função sorted() em Python
A função sorted() é uma função embutida do Python que retorna uma nova lista contendo todos os itens do iterável fornecido em ordem crescente (por padrão).

Sintaxe básica:

sorted(iterable, key=None, reverse=False)
Parâmetros:
iterable: Sequência (string, tupla, lista) ou coleção (conjunto, dicionário) a ser ordenada

key (opcional): Função que serve como critério para ordenação

reverse (opcional): Se True, a ordenação é decrescente (padrão é False)

Características importantes:
Retorna sempre uma nova lista com os itens ordenados

Não modifica o iterável original

Funciona com qualquer iterável (listas, strings, tuplas, dicionários, etc.)

Exemplos:
Ordenação básica de lista:
python
Copy
numeros = [5, 2, 9, 1]
ordenados = sorted(numeros)
print(ordenados)  # [1, 2, 5, 9]
print(numeros)    # [5, 2, 9, 1] (original não modificado)
Ordenação decrescente:

sorted([5, 2, 9, 1], reverse=True)  # [9, 5, 2, 1]
Ordenação de strings:

sorted("python")  # ['h', 'n', 'o', 'p', 't', 'y']
Usando o parâmetro key:

palavras = ["banana", "maçã", "laranja", "abacaxi"]
sorted(palavras, key=len)  # Ordena pelo tamanho: ['maçã', 'banana', 'laranja', 'abacaxi']
Ordenação de dicionários:

pessoas = [{'nome': 'João', 'idade': 25}, {'nome': 'Maria', 'idade': 30}]
sorted(pessoas, key=lambda x: x['idade'])  # Ordena pela idade
Diferença entre sorted() e list.sort():
sorted() retorna uma nova lista e funciona com qualquer iterável
list.sort() modifica a lista original e só funciona com listas

lista = [3, 1, 2]
lista.sort()      # Modifica a lista original
sorted(lista)     # Retorna nova lista, original não muda
A função sorted() é uma ferramenta versátil e poderosa para ordenação em Python.
"""

lista = [3, 1, 2]
lista.sort()
print(lista)
sorted(lista)
print(lista)