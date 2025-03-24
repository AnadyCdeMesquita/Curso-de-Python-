# def contador (i, f, p):
#   """
#   Explicando o código:
#   1- O 'i' -Representa o Início;
#   2- O 'f' -Representa o Fim;
#   3- O 'p' -Representa o Passo;
#   return = não tem retorno
  
#   """
#   c= i
#   while c < f:
#     print(c)
#     c+=p
#   print('fim')
        
# contador(2, 10, 2)
# help(contador)

# """
#   Explicando o código:
#   1- O 'i' -Representa o Início;
#   2- O 'f' -Representa o Fim;
#   3- O 'p' -Representa o Passo;
#   return = não tem retorno

#   """
# a = 0, b = 0 (Parâmetros opcionais) A quantidade de parâmetros reais tem que ser a quantidade de parâmetros formais
# def somar(a = 0 , b = 0, c = 0):
#   soma = a + b + c
#   print(soma)

# somar(5, 8, 3)
# somar(5, 10)
# somar(0, 5 , 3)
# somar()
# VARIÁVEL GLOBAL E VARIÁVEL LOCAL

# def teste(b):
#   a = 8
#   b += 4
#   c=2
#   print(b)
#   print(c)
#   print(a)

# a=5
# teste(a)
# n1 = 10
# def variaveis ():
#   n1 = 15
#   print(n1) # imprimir variável local

# variaveis() #imprimir variável local
# print(n1) # imprimir variável global 

# def testando (b):
#   global a
#   a = 8
#   b += 4
#   c = 2
#   print(a) # imprimir 8
#   print(b)   
#   print(c)

# a = 5
# testando(5)
# print(f' variável {a}')  # imprimir 8

# def fatorial(num=1):
#   f = 1 
#   for c in range(num, 0, -1):
#     f *= c
#   return f
  
# n = int(input("Digite um número: "))
# print(f'O fatorial de {n} é {fatorial(n)}')
# ###OU###

# f1 = fatorial(5)
# f2 = fatorial(4)
# f3 = fatorial(3)
# print(f'Imprima: {f1}, {f2}, {f3}.')