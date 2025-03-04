#exercicio 1

# lista = list()
# maior = 0
# menor = 0
# for cont in range(0,5):
#   lista.append(int(input(f'Digite um valor para posição {cont}: \n')))
#   if cont == 0:
#     maior = menor = lista[cont]
#   else:
#     if lista[cont] > maior:
#       maior = lista[cont]
#     if lista[cont] < menor:
#       menor = lista[cont]
    
  
# print(f'Você digitou os valores {lista}.')
# print(f'O maior valor digitado é {maior}', end ='')
# for i, v in enumerate(lista):
#   if v == maior:
#     print(f'e a sua posição {i}')
# print(f'O menor valor digitado é {menor}', end ='')
# for i, v in enumerate(lista):
#   if v == menor:
#     print(f' e a sua posição {i}.')

#exercicio 2
# lista = list()
# while True:
#     n = int(input('Digite um valor:'))
#     if n not in lista:
#       lista.append(n)
#     else:
#       print('Não vou adicionar')
#     pergunta = str(input('Deseja continuar? [S/N]'))
#     if pergunta == 'N':
#       break

# print(f'Você digitou os valores {lista}')
    
#EXERCÍCIO 3
# lista = list()
# for i in range(0, 5):
#   n= int(input('Digite um número: \n'))
#   if i == 0 or n > lista[-1]:
#     lista.append(n)
#   else:
#     pos = 0
#     while pos < len(lista):
#       if n <= lista[pos]:
#         lista.insert(pos, n)
#         break
#       pos += 1
      
# print(f'{lista}')

#EXERCICIO 4

# lista = list()
# pares = list()
# impares = list()
# while True:
#   lista.append(int(input('Digite um número: \n')))
#   pergunta = str(input('Deseja continuar? S/N \n'))
#   if pergunta in 'Nn':
#     break
# for i, v in enumerate(lista):
#   if v % 2 == 0:
#     pares.append(v)
    
#   elif v % 2 == 1:
#     impares.append(v) 
    
    
# print(f'Os números da listas são {lista}.')   
# print(f'A lista de números pares é {pares}')
# print(f'A lista de números ímpares é {impares}')

#exercicio 5

# expressao = str(input('Digite uma expressão'))
# pilha= []
# for simbolo in expressao:
#   if simbolo == '(':
#     pilha.append(simbolo)
#   elif simbolo == ')':
#     if len(pilha) > 0:
#       pilha.pop()
#     else:
#       pilha.append(')')
#       break
# if len(pilha) == 0:
#   print('Sua expressão está válida')
# else:
#   print('Sua expressão está INválida')
  





    

