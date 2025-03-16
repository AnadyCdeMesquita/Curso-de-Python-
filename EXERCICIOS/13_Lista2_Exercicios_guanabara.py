#EXERCICIO 1 
# mais = 0
# menos = 0
# lista = list()
# principal = list()
# while True:
#   lista.append(str(input('Nome:  ')))
#   lista.append(float(input('peso: ')))
#   if len(principal) == 0:
#     mais = menos = lista[1]
#   else:
#     if lista[1] > mais:
#       mais = lista[1] 
#     if lista[1] < menos:
#       menos =  lista[1] 
#   principal.append(lista[:])
#   lista.clear()   
#   question = (str(input('Quer continuar??'))).strip().upper()
#   if question not in 'Ss':
#     break 
# print(f'O principal foi {principal}')     
# print(f'Ao todo, vc cadastrou {len(principal)} pessoas.') # len(principal)
# print(f'O maior peso foi {mais}.')
# for p in principal:
#   if p[1]==mais:
#     print(p[0], end='')
# print(f'O menor peso foi {menos}.')

#EXERCICIO 1 - OUTRA FORMA DE FAZER
# lista1 = list()
# principal1 = list()
# while True:
#   lista1.append(str(input('Nome:  ')))
#   lista1.append(float(input('peso: ')))
#   principal1.append(lista1[:])
#   lista1.clear()   
#   question = (str(input('Quer continuar??'))).strip().upper()
#   if question not in 'Ss':
#     break 
# print(f'O principal foi {principal1}')     
# print(f'Ao todo, vc cadastrou {len(principal1)} pessoas.') # len(principal)
# print(f'O maior peso foi {max(principal1)}.')
# print(f'O menor peso foi {min(principal1)}.')

#EXERCICIO 2

# numeros = [[], []]
# for i in range(1,8):
#   valor = int(input(f'Digite o {i}º número: '))
#   if valor % 2 == 0:
#     numeros[0].append(valor)
#   else:
#     numeros[1].append(valor)
  
# print(numeros[0])
# print(numeros[1])

#EXERCICIO 3 #MATRIZ
# matriz = [[0,0,0], [0,0,0], [0,0,0]]
# for l in range(0,3): #linha
#   for c in range(0,3): #coluna
#     matriz[l][c]= int(input(f'Digite um valor para {l, c}: '))
# print(matriz)   

# for l in range(0,3): #linha
#   for c in range(0,3): #coluna
#     print(f'[{matriz[l][c]}]', end='') 
#   print()

#EXERCÍCIO 4
#JOGOS DA MEGA SENA
# from random import randint
# n = int(input('Quantos jogos vc quer que eu sorteie?:  '))
# print(f'Sorteando {n} jogos...')
# lista = list()
# jogos = list()
# cont = 0
# total = 0
# while total <= n:
#   cont = 0
#   while True:
#     num = randint(1,60)
#     if num not in lista:
#       lista.append(num)    
#       cont +=1
#     if cont >=6:
#       break
# lista.sort()
# jogos.append(lista[:])
# lista.clear()
# print(f'{jogos}')

#EXERCICIO 5
# lista = []
# while True:  
#   nome = str(input('Nome: '))
#   nota1 = float(input('Nota 1:  ')) 
#   nota2 = float(input('Nota 2:  '))
#   media = (nota1 + nota2) / 2
#   lista.append([nome, [nota1, nota2], media])
#   resp = str(input('Deseja continuar? S/N?  '))
#   if resp in "Nn":
#     break
# print(lista)
# for i, v in enumerate(lista):
#   print(i, v[0], v[2])
  
# lista = []
# while True:
#     nome = str(input('Nome: '))
#     idade = int(input('Idade: '))
#     profissão1 = str(input('Profissão: '))
#     profissão2 = str(input('Profissão: '))
#     resp = str(input('Deseja continuar? S/N?  '))
#     lista.append([nome, idade, [profissão1, profissão2]])
#     if resp in "Nn":
#       break
# print(len(lista))
# print(lista[0][0])
# print(lista[0][1])
# print(lista[0][2][0])
# print(lista[0][2][1])






    

