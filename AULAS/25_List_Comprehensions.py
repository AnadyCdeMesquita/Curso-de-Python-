
"""
LISTA DE COMPREENSÃO:
SÃO UMA DAS CARACTERÍSTICAS MAIS ÚTEIS E ELEGANTES.
ELAS OFERECEM UMA MANEIRA MAIS CONCISA DE CRIAR LISTAS, E SÃO FREQUENTES, MAIS COMPREENSÍVEIS E MAIS
EFICIENTES DO QUE USAR LOOPS

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

cubo = [x**3 for x in range(11)]
print(cubo)

triplo = [x for x in range(21) if x % 3 == 0]
print(triplo)

frutas = ['maca', 'banana', 'manga', 'uva', 'abacaxi', 'laranja']
frutas_longas = []
for frutinhas in frutas:
  if len(frutinhas) >= 5:
    frutas_longas.append(frutinhas)
    
print(frutas_longas)
     

notas = [89, 92, 56, 78, 45, 34, 90, 99, 6576, 80, 82] 
# notinhas = []
# for notas1 in notas:
#   if notas1 >= 75:
#     notinhas.append(notas1)
#print(notinhas)

notinhas = [notas1 for notas1 in notas if notas1 >= 75]
print(notinhas)