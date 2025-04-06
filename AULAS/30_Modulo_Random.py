#random()- Gera um decimal aleatório entre [0 e 1] - o 1 nuca será sorteado
#uniform(a,b) - Gera um número decimal aleatório entre a e b
#radint(a,b ) - Gera um número inteiro entre a e b
#choice(i) - mostra um valor aleatório entre um iterável
#shuffle(x, [,random]) - embaralha a sequencia x
#import random 
from random import random
numero_randomico = random() # numero de 0 a 1, só que 1 não entra.
#print(numero_randomico)

from random import uniform #numero decimal
# numero_uniform = uniform(5, 20)
# print(numero_uniform)

for i in range(1, 6):
  numero_uniform = uniform(5, 20)
# print(numero_uniform)

from random import randint #numero inteiros
variavel_randint = randint(0, 10)
# print(variavel_randint)

# for i in range(1, 7):
#   variavel_randint = randint(1, 61) # o ultimo número na gera o último numero
#   print(variavel_randint)
  
#CHOICE = TRABALHA COM LISTA, TUPLA, CONJUNTOS, DICIONARIOS, iteráveis
#iteráveis = qualquer estrutura de dados que contenha mais de um elemento
#A função choice do módulo random em Python escolhe aleatoriamente um elemento de uma sequência, como uma lista, tupla ou conjunto. 
from random import choice
escolha = ['pedra', 'papel', 'tesoura', 'guarda-roupa']
# print(choice(escolha))
numeracao = [1, 2, 3, 4, 5, 6]
frase = 'batatinha quando nasce'

# print(choice(numeracao))
print(choice(frase)) #escolhe uma letra

from random import shuffle #não aceita tupla pq tupla é imutável

#random.shuffle()embaralha uma lista no lugar e random.sample()retorna uma nova lista aleatória. random.sample()também é aplicável a tipos de dados imutáveis, como strings e tuplas.

testando = ["anady", "rodrigo", "fernando", 'soph']
shuffle(testando)
print(testando)

from random import sample

testando1 = ["anady", "rodrigo", "fernando", 'soph']
sample(testando1)
print(testando1)
