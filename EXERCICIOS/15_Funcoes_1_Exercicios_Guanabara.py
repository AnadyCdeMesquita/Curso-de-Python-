#EXERCICIO 1

# c = float(input('Qual o comprimento  do terreno?'))
# l = float(input('Qual o largura  do terreno?'))

# def area(compr, larg):
#   calculo = compr * larg
#   print(f'A área mede {calculo} metros2.')
  
# area(c, l)

#EXERCICIO 2

# def escreva(texto):
#   tam = len(texto)
#   print('*' * tam)
#   print(texto)
#   print('*' * tam)
  
  
# escreva('oi')

#EXERCICIO 3:
# print(f'\n Contagem de 1 a 10, de 1 em 1.')
# for i in range(1, 11):
#   print(f'{i}', end= '  ')
# print(f'\n Contagem de 10 a 0, de 2 em 2.')
# for i in range(10, -1, -2):
#   print(f'{i}', end= '  ')
  

def contador(i, f, p):
  print(f'Contagem de {i} até {f} em {p}')
  if i < f:
    cont = i
    while cont <= f:
      print(cont, end = '')
    cont += p
  else:
    cont = i
    while cont >= f:
      print(cont, end= '')
    cont -= p
    
    
contador(1, 10, 5)

#exercicio 4:
# from time import sleep
# def maior(*num):
#   cont = mais = 0
#   print(' \n Analisando valores passados')
#   for v in (num):
#     print(f'{v}', end ='  ', flush= True)
#     sleep(0.3)
#   if cont == 0:
#     mais = v
#   else:
#     if v > mais:
#       v = mais
#   cont+=1
#   print(f'Foram informados {cont} valores ao todo.')
#   print(f'O maior {mais}.')
  
  
# maior(0, 5, 9, 10)
# maior(8, 15, 50, 17)
# maior(15, 0, 20,25, 80)
# maior(None)


        
  
