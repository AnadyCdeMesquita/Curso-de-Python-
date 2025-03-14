
# lista = ['arroz', 'feijao', 'macarrao', 'carne', 'ovos']

# lista.sort() # ordem alfabética ou crescente
# lista.sort(reverse=True) #ordem decrescente 
# lista.remove('feijao') # com remove usa-se o conteúdo
# lista.pop(3)
# print(lista)

# valores = list(range(1, 11)) 
# print(valores)
# print(len(valores))
# if 10 in valores:
#   print('sim')
# else:
#   print('não')

# lista = [2, 5, 9, 1]
# lista.pop(1) #remove pelo indice
# print(lista)
# lista[2] = 7 # substitui o 2 da lista
# lista.insert(1,8) #diz a localização 1, no caso.
# lista.append(10) #insere no final.
# print(lista)

# lista = [2, 5, 9, 1]
# lista.insert(3,2)
# print(lista)
# lista.remove(2) #vai remover o primeiro da lista
# print(lista)

# valores = [] #list()
# valores.append(1) 
# valores.append(8) 
# valores.append(12) 
# valores.append(5) 

# for p, v in enumerate(valores):
#   print(f'Os índices são {p} e os valores são {v}')

# for posicao in range(1, 4):
#   print(posicao, end='')
  
# for v in valores:
#   print(v)

# teste = list()
# for i in range(0, 5):
#   teste.append(int(input('Digite um valor:\n')))

# print(teste)
  
# teste = [0, 14, 9 , 9 , 6]
# for p, v in enumerate(teste):
#   print(f'Os índices são {p} e os valores são {v}')

#CRIAÇÃO DE 2 LISTAS#
a = [1, 2, 3, 4, 5]
b = a # dessa forma cria uma ligação, tudo que muda em uma, muda na outra
b[1] = 9
print(b)
print(a)
b = a [:] #dessa forma, a alteração que fizer em uma, não alterará a outra
