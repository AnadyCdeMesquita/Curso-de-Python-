"""
BÁSICO DE LISTA
"""
# frutas = ['maca', 'banana', 'pera', 'uva', 'laranja']
# print(len(frutas))
# frutas[0] = "mamao"
# print(frutas[0])
# print(frutas[-1])
# print(frutas[-2])
# print(frutas[10])

"""
OPERAÇÕES BÁSICAS COM LISTAS:
ADICIONAR : append()  / insert()
obs: APPEND = ADICIONA O ITEM NO FINAL DE UMA LISTA
REMOVER: pop() / remove()
CONCATENAR LISTAS: + , extend()
REPETIR : *
VERIFICAR SE HÁ UM ITEM NA LISTA: in
"""

# #append = adiciona um item no final da lista
# frutas = ["maca", "banana"]
# frutas.append('goiaba')
# print(frutas)

#insert = insere numa posição especifica

# frutas1 = ['mamao', 'pera', 'figo', 'cereja']
# frutas1.insert(2, 'laranja')
# print(frutas1)

#REMOVE = REMOVE PELO NOME DO CONTEÚDO
# frutas1 = ['mamao', 'pera', 'figo', 'cereja']
# frutas1.remove('mamao')
# print(frutas1)

# #DEL = REMOVE PELO ÍNDICE
# frutas1 = ['mamao', 'pera', 'figo', 'cereja']
# del frutas1[1]
# print(frutas1)

#POP = GERALMENTE REMOVE O ÚLTIMO, CASO NÃO ESCOLHA O ÍNDICE

# frutas1 = ['mamao', 'pera', 'figo', 'cereja']
# frutas1.pop()
# print(frutas1)

#CONCATENAR LISTAS: + , extend()
# lista1 = [1, 2, 3, 4, 5]
# lista2 = [6, 7, 8, 9, 10]
# uniao = lista1 + lista2
# print(uniao)

#EXTEND = ADICIONA OS ELEMENTOS DE UMA LISTA (OU QUALQUER ITERÁVEL) AO FINAL DA LISTA ATUAL
# lista1 = [1, 2, 3, 4, 5]
# lista2 = [6, 7, 8, 9, 10]
# lista1.extend(lista2)
# print(lista1)

#REPETIR : *

# lista1 = ['a', 'b', 'c', 'd'] * 10
# print(lista1)

#IN = está em ...RETORNARÁ UM TRUE OR FALSE

# frutas1 = ['mamao', 'pera', 'figo', 'cereja']
# print('mamao' in frutas1)
# print('limao' in frutas1)

"""
MÉTODOS DE LISTAS
sort() = ORDENAR UM LISTA
reverse() = INVERTE A ORDEM DOS ELEMENTOS IN PLACE
count() = CONTA O NÚMERO DE OCORRÊNCIA  EM UM ELEMENTO
index() = RETORNA O ÍNDICE DA PRIMEIRA OCORRÊNCIA DE UM ELEMENTO

"""
#1-SORT = COLOCAR EM ORDEM CRESCENTE 
# numeros = [23, 1, 45, 6, 12]
# frutas = ['banana', 'maca', 'banana', 'cereja', 'maca', 'damasco']
# numeros.sort() #ordem numérica
# frutas.sort() #ordem alfabética
# print(numeros)
# print(frutas)
# #USA-SE O numeros.sort(reverse=True) = para ordem descrescente
# numeros.sort(reverse=True)
# print(numeros)

#2-REVERSE
# numeros = [23, 1, 45, 6, 12]
# numeros.reverse()
# print(numeros)

#3-COUNT = CONTA O NÚMERO DE OCORRENCIAS DE UM ELEMENTO
# frutas = ['banana', 'maca', 'banana', 'cereja', 'maca', 'damasco']
# quantidade = frutas.count('maca')
# print(quantidade)

#4- INDEX = RETORNA O ÍNDICE DA PRIMEIRA OCORRÊNCIA DE UM ELEMENTO
#SE O ELEMENTO NÃO ESTIVER PRESENTE, GERARÁ UM ERRO

# frutas = ['banana', 'maca', 'banana', 'cereja', 'maca', 'damasco']

# testando = frutas.index('cereja')
# testando1 = frutas.index('banana')
# print(testando)
# print(testando1)
