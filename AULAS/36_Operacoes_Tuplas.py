### soma das listas
lista  = [6,7,8,9,10]
numero_lista =  6 in lista
print(numero_lista)
lista2 = [0,1,2,3,4]
lista3 = lista + lista2
lista = lista2[:]
print(lista3)
print(lista)
lista2[3] =12
print(lista2)
# lista2[1] = 10
# print(lista2)
#print(lista2)

#SOMA TUPLAS:

primeiras_cidades = (1, 2)
proximas_cidades = (3, 4)

soma = primeiras_cidades + proximas_cidades
print(soma)
multiplicar_tupla = soma * 3
print(multiplicar_tupla)
#if 4 in multiplicar_tupla:
  #print('Existe')
  #OU
numero_variavel = 4 in multiplicar_tupla
print(numero_variavel)

for c in multiplicar_tupla:
  print(c)
  

