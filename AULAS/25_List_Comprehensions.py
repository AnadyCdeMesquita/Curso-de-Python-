
"""
LISTA DE COMPREENSÃO:
SÃO UMA DAS CARACTERÍSTICAS MAIS ÚTEIS E ELEGANTES.
ELAS OFERECEM UMA MANEIRA MAIS CONCISA DE CRIAR LISTAS, E SÃO FREQUENTES, MAIS COMPREENSÍVEIS E MAIS
EFICIENTES DO QUE USAR LOOPS
SINTAXE =
A compreensão de listas é uma forma de criar uma nova lista aplicando uma expressão a cada item de um iterável, como uma lista ou um intervalo. 
nova_lista = [expressão para cada item] for item in iterável [condições]
"""
#Lista de compreensão
# quadrados = [x**2 for x in range(10)]
# print(quadrados)

#TRADICIONAL
# quadrados = []
# for i in range(10):
#   quadrados.append(i**3)

# print(quadrados)
#__________________________________________________________________#

# quadrados = list()
# for x in range(10):
#   if x % 2 == 0:
#     quadrados.append(x**2)

# print(quadrados)
  
# quadrados1 = [x**2 for x in range(10) if x % 2 == 0]

#________________________________________________________________________#

a = [1, 2, 3, 4, 5]
b= [1, 2, 3, 4, 5]
# combinacoes = []
# for x in a:
#   for y in b: 
#     if x + y == 5:
#       combinacoes.append((x,y))

# print(combinacoes)

    
# combinacoes = [(x,y) for x in a for y in b if x + y == 5]
# print(combinacoes)

# cubo = [x**3 for x in range(11)]
# print(cubo)

# triplo = [x for x in range(21) if x % 3 == 0]
# print(triplo)

# frutas = ['maca', 'banana', 'manga', 'uva', 'abacaxi', 'laranja']
# frutas_longas = []
# for frutinhas in frutas:
#   if len(frutinhas) >= 5:
#     frutas_longas.append(frutinhas)
    
# print(frutas_longas)
     

# notas = [89, 92, 56, 78, 45, 34, 90, 99, 6576, 80, 82] 
# notinhas = []
# for notas1 in notas:
#   if notas1 >= 75:
#     notinhas.append(notas1)
#print(notinhas)

# notinhas = [notas1 for notas1 in notas if notas1 >= 75]
# print(notinhas)


# lista = [1, 2, 3, 4, 5, 6, 7, 8]
# lista1 = []
# for numeros in lista:
#   if numeros % 2 == 0:  
#     lista1.append(numeros)

# print(lista1)

# lista2 = [x for x in lista if x % 2 == 0]
# print(lista2)

nomes = ['anady', 'fernando', 'soph', 'laura', 'ana', 'antonio', 'anady']

nomes1 = [x for x in nomes if x != 'anady']
print(nomes1)