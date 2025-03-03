for i in range(1, 4): #linha
  for j in range(1, 4): #coluna
    print(f' {i} x {j} = {i * j}')
    

# quadrado = [x**2 for x in range(10) if x%2 !=0]
# print(quadrado)

# quadrado_impares =[]
# for x in range(1, 10):
#   if x % 2 != 0:
#     quadrado_impares.append(x**2)
#     print(quadrado_impares)

#MANEIRA MODERNA:
texto = 'hello world'
# consoante = [char for char in texto if char not in 'aeiou']
# print(consoante)

# MANEIRA ANTIGA:
# texto = 'hello world'
# consoante = []
# for char in texto:
#   if char.lower() not in 'aeiou':
#     consoante.append(char)
#     print(consoante)
  
# n = int(input('Digite um numero: \n'))

# if n < 0:
#   print('Número inválido')
# else:
#   plus = 1
#   for n in range(n, 0, -1):
#     print(n)
#     if n > 0:
#       plus *= n
#   print(f'O fatorial de {n} é {plus}.')

# n = int(input('Digite um numero: \n'))
# for n in range(10):
#   print(f'{n * "*"}') 

# n = int(input('Digite um numero: \n'))
# if n % 2 != 0:
#   print('É um número ímpar')
# else:
#   for n in range(1, n + 1):
#     if n % 2 == 0:
#       print(n * '*')