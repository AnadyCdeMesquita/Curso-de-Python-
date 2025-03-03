
#tupla é entre parêntese
# lanche = 'sanduba', 'suco', 'pizza', 'pudim'
# print(lanche[0:2]) #entra o primeiro e exclui o ultimo
# print(lanche[-1]) # pudim ( de trás para frente)
# print(lanche[:2]) # pudim ( do início até 1)
# print(lanche[2:]) # pudim ( do segundo  para frente)
# print(lanche[-2:]) # pudim ( dois para frente)
# print(lanche[-3:]) # pudim (terceiro para frente
# print(len(lanche)) # quantos objetos tem uma tupla
# lanche = 'sanduba', 'suco', 'pizza', 'pudim'
# for contador in range(0, len(lanche)):
#   print(f'Eu vou comer para caramba {lanche[contador]} -{contador}')

# print('comi para caramba')

#duas formas de usar o for:
# for cont in lanche:
#   print(f'Eu vou comer para caramba {cont}')

# for cont, comida in enumerate(lanche):
#   print(f'Eu vou comer para caramba {comida} na posição {cont}')

# lanche = 'sanduba', 'suco', 'pizza', 'pudim'
# print(sorted(lanche))
# print(lanche[0])

# a = 2, 5, 4
# b = 1, 8, 5 , 2
# c= a + b
# print(c)
# print(c.index(5, 2))
# print(c[5])
# print(c.count(9))
# print(len(c))

# pessoa = ('anady', 39, 'morena')
# del(pessoa)
# print(pessoa)

# cont = ('zero', 'um', 'dois', 'três','quatro', 'cinco',
#         'seis', 'sete','oito', 'nove', 'dez', 'onze', 'doze',
#         'treze','catorze', 'quinze', 'dezesseis','dezessete',
#         'dezoito', 'dezenove', 'vinte')

# while True:
#   num = int(input('Digite um número de 0 a 20: \n'))
#   if 0 <= num <= 20:
#     break
#   print('tente novamente') 
  
# print(f'Vc digitou o número {cont[num]}.')

# times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio','Cruzeiro', 'Flamengo', 'Vasco', 
#          'Chapecoense','Atlético','Botafogo', 'Atlético-PR', 'Bahia', 'SP','Fluminense','Sport',
#          'Vitória', 'Coritiba','Avaí', 'Ponte Preta', 'Atlético-GO')


# print('***' * 40)
# print(f'Lista de times do brasileirão: {times}')
# print('***' * 40)
# print(f'Os 5 primeiros colocados:{times[0:5]}')
# print(f'Os 4 últimos colocados:{times[-4:]}')
# print(f'Times em ordem alfabética: {sorted(times)}')
# print(f'A Chapecoense está na posição: {times.index('Chapecoense') + 1}.')
# print(f'Quem está na posição 10 é o : {times[10]}.')

# import random
# ou
# from random import randint
# n = (randint(1,10),randint(1,10), randint(1,10), randint(1,10), randint(1,10) )
# num = (random.randint(1, 10),random.randint(1, 10),random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))
# for n in num:
#   print(f'{n} ')
# print(f'O menor número é : {min(num)} e o maior número é: {max(num)}.')
# print(f'A média é : {sum(num)/len(num)}.')

# numero1 = int(input('Digite um número:\n'))
# numero2 = int(input('Digite um número:\n'))
# numero3 = int(input('Digite um número: \n' ))
# numero4 = int(input('Digite um número: \n'))

# tupla = (numero1, numero2, numero3,  numero4)
# print('tupla:', tupla)
# for n in tupla:
#   if n % 2 == 0:
#     print(f'{n} \n', end = ' ')  
# print('Quantas vezes apareceu o número 9?')
# print(f'O número 9 apareceu quantas vezes?: {tupla.count(9)} vezes')
# if 3 in tupla:
#   print(f'A posição do valor 3 é {tupla.index(3)}.')
# else:
#   print('Valor 3 não existe.')

# listagem = ('lapis', 1.75,
#              'Borracha', 2,
#              'Caderno', 15.90,
#              'Estojo', 25,
#              'Transferidor', 4.20,
#              'Compasso', 9.99,
#              'Mochila', 120.32,
#              'Canetas', 22.30,
#              'Livro', 34.90)

# print('-' * 50)
# print(f'{"LISTAGEM DE PREÇOS":^40}')
# print('-' * 50)
# for pos in range(0, len(listagem)):
#   if pos % 2 == 0:
#     print(f'{listagem[pos]:.<20}') # pontos alinhados à esquerda- 30 caracteres
   
#   else:
#     print(f'R$ {listagem[pos]:>7.2f}')
  
palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS',
            'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for p in palavras:
  print(f'\n A palavra {p} temos: ')
  for letra in p:
    if letra.upper() in 'AEIOU':
      print(letra , end = '')
  
  
  
  
  
  
  teste = 'palavra'
  
  