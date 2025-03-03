#fazendo LOOP EM WHILE E FOR
# soma = 0
# i = 0
# while i < 10:
#   i += 1
#   if i % 2 != 0:
#     soma += i
# print(f'O valor total de ímpares é {soma}.')
# soma = 0
# for i in range(1, 11, 2):
#   print(i)
#   soma += i
# print(f'A soma total de ímpares {soma}.')

# plus = 1
# for i in range(1, 6):
#   print(f'O valor é {i}.')
#   plus *= i
# print(f'O valor total de {plus}.')
# plus = 1  
# i = 0
# while i < 5:
#   i+=1
#   print(i)
#   plus *= i
# print(plus) 
# soma = 0
# n = int(input('Digite um numero inteiro: \n'))
# for i in range(1,n+1): 
#   if i % 2 == 0:
#     print(i)
#     soma += i
# print(f"A soma dos números pares de 1 até {n} é: {soma}")

# n= int(input('Digite um numero inteiro: \n')) 
# i = 5
# while i < 11:
#   i+=1
#   print(f'O resultado {n} * {i} = {n*i}')
# print(i)
  
  

# n= int(input('Digite um numero inteiro: \n'))
# for i in range(1, 11):
#   print(f'O resultado {n} * {i} = {n*i} \n')

n= int(input('Digite um numero inteiro: \n'))
soma = 0
for i in range(1, n+1):
  print(f'O quadrado de {i} = {i**2}')
  soma += i**2
print(f'A soma dos quadrados do numero 1 até o {n} = {soma}')  
  