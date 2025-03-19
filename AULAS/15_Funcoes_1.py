# def mostralinha():
#   print('--------------------')
 
# mostralinha()
# print('sistema de alunos')
# mostralinha()
# print('sistema de professores')
# mostralinha()

# def mensagem(msg):
#   print('***' * 20)
#   print(msg)
#   print('***' * 20)
  
# mensagem('hello world')
# mensagem('Vamos aprender Python')
# mensagem('Vamos aprender SQL')

# def soma (a, b):
#   s = a + b
#   print(s)
  
# soma(a=8, b=9)#se declarar 1, tem que declarar ambos.
# soma(b=8, a=10)
# soma(8, 11)
# soma(8, 12)

# def contador(*num):
#   for valor in num:
#     print(valor, end = ', ')

# contador(1, 2, 4, 5)
# contador(8, 2, 9, 8)
# contador(10, 2, 5, 11)

# def contador(*num):
#   tam = len(num)
#   print(f'Recebi os valores de {num} e tem {tam} números.')

# contador(1, 2, 4, 5)
# contador(8, 2, 9, 8, 10, 15, 20)
# contador(10, 2, 5, 11)

# def dobra(lista):
#   pos = 0
#   while pos < len(lista):
#     lista[pos] *= 2
#     pos+=1

# valores = [7, 2, 5, 0, 4]
# dobra(valores)
# print(valores)

def soma(*num):
  soma = 0
  for v in num:
    soma += v  
  print(soma)
soma(5, 7, 9)
soma(7, 7, 19)
soma(5, 7, 9, 8, 20)

