#exercicio 1

# import math

# num = float(input('Digite um número Real:\n'))

# print(f'O {num} tem a parte inteira {int(num)}.')
# print(f'O {num} tem a parte inteira {math.trunc(num)}.')

#exercicio 2
# import math

# b = float(input('Digite o comprimento do cateto oposto:\n'))
# c = float(input('Digite o comprimento do cateto adjacente:\n'))
# a = b**2 + c**2
# print(f'A raiz quadrada de "a" é {math.sqrt(a): .2f}.')
# print(f'A raiz quadrada de "a é {math.hypot(b,c): .2f}')

#exercicio 3

# angulo =  float(input('Digite o ângulo:\n'))
# tangente = math.tan(math.radians(angulo))
# coseno = math.cos(math.radians(angulo))
# seno = math.sin(math.radians(angulo))
# print(f'Os ângulos são {tangente: .2f}, {coseno: .2f} e {seno: .2f}.')

#exercicio 4

# from random import choice # OU import random

# alunos = ['Anady', 'Soph', 'Socorreth', 'Fernando']
# escolhido = choice(alunos)
# print(f'O aluno sorteado foi {escolhido}.')

#EXERCICIO 5:
# import random

# a1 =  str(input('Digite o nome de um aluno:\n'))
# a2 =  str(input('Digite o nome de um aluno:\n'))
# a3 =  str(input('Digite o nome de um aluno:\n'))
# a4 =  str(input('Digite o nome de um aluno:\n'))
# alunos = [a1, a2, a3, a4]
# random.shuffle(alunos)
# print(alunos)

import pygame
pygame.init()
pygame.mixer.music.load('aula.mp3')
pygame.mixer.music.play()
pygame.event.wait()

