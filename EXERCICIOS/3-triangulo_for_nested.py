# altura = 3
# largura = 5
# for linha in range(altura):
#   for coluna in range(largura):
#       print('*', end='')
#   print()

# altura = 3
# largura = 9
# for linha in range(altura):
#   for coluna in range(largura):
#      print('*', end='')
#   print()

# consegue-se calcular linha 3 coluna 5
# for linha in range(3): 
#    print('*' * 5)

#taboada
# for linha in range(1, 11):
#   for coluna in range(0, 11):
#      print(f'{linha} * {coluna} = {linha * coluna}')

# n1= 5
# for n in range(1, 11):
#   print(f'{n1} * {n} = {n1 * n}')

# n= 1
# x= 1
# while n <=10:
#   n+=1
#   x+=n
#   print(x)
altura = 5
for i in range(altura):
  espacos = altura - i - 1
  asteriscos = 2 * i + 1
  print('' * espacos + '*' * asteriscos)
  print(espacos, asteriscos)
  
  