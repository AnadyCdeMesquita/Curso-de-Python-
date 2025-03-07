# x= 0
# while x <= 30:
#   print(x)
#   x+=1

# n= 10
# while n >= 0:
#   print(n)
#   n -= 1
# print('POOOOOWWWWWWW, PUUUUUMMMM')
# print('********' * 20)

# for i in range(1, 11, 1):
#   print(i)
# print('POOOOOWWWWWWW, PUUUUUMMMM')
  
# for i in range(11, 1, -1):
#   print(i)
# print('POOOOOWWWWWWW, PUUUUUMMMM')

#EXERCÍCIO 1

# from time import sleep
# for i in range(10, -1, -1): #chegar até o zero
#   print(i)
#   sleep(3)#essa função sleep pode ser dentro da função ou fora
#   #FORA, PEGAVA O PRINT DO POOOWWW, PUUMMMM.
# print('POOOOOWWWWWWW, PUUUUUMMMM')

#EXERCÍCIO 2
# for i in range(1, 52):
#   if i % 2 == 0:
#     print(i)
#OU 
# for i in range(2, 51):
#     print(i)

#EXERCICIO 3:
# soma = 0 #acumulador
# cont = 0
# for c in range(1, 501):
#   if c % 2 != 0 and c % 3 == 0:
#     cont +=1
#     soma += c

# print(f'A soma de todos os {cont} valores solicitados é {soma}.')

# n= int(input('Digite um número: \n'))
# print('**' * 20)
# for i in range(1, 11):
#   print(f'{n} x {i} = {n * i}')
  
# n = 0
# z= int(input('Digite um número: \n'))
# print('**' * 20)
# while n<=10:
#   print(f'{n} x {z} = {n*z}')
#   n+=1   

#EXERCICIO 4:

# print('**' * 20)
# cont = 0
# soma = 0
# for i in range(1, 7):
#   z= int(input('Digite um número: \n'))
#   if i % 2 == 0:
#       cont += 1
#       soma += z 
# print(f'Quantidade de números {cont} pares no intervalo.')
# print(f'A soma dos número são {soma}.')
  
