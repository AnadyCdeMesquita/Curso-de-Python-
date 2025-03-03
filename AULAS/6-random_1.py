"""#random
import random
print(random.randrange(1,1000))
      
#1-gerar um número de ponto flutuante entre 0 e 1
print(random.random())

#2-gerar um numero inteiro  aleatório entre dois valores(inclusive)
print(random.randint(10,20)) #gerar um número entre 10 e 20, iclusive

#3-escolher aleatoriamente um elemento de uma lista
frutas = ['maçã', 'banana', 'cereja']

#4-Embaralhar aleatoriamente uma lista:
numeros = [1,2,3,4,5]
random.shuffle(numeros)
print(numeros) # a lista agora está embaralhada

#5- Gerar um número de ponto flutuante aleatório em um
#itervao específico:
print(random.uniform(5.5 , 9.5)) #gerar um número de ponto flutuante
pode se colocar também números inteiros e gerará um número flutuante

#Função Sample – Seleção Aleatória de Elementos Únicos
Para selecionar elementos aleatórios evitando a repetição de valores, podemos utilizar a função sample.

Essa função permite selecionar múltiplos elementos aleatoriamente dentro de uma lista, garantindo que não haja repetição de elementos selecionados.

Assim como a função choices, a função sample recebe como argumentos a sequência da qual selecionará os elementos e o parâmetro k.
"""
import random
print(random.randrange(0,5))
print(random.random())
print(random.randint(0,10))
#ver choice e choices 
frutas = ['maca', 'banana', 'pera']
print(random.choices(frutas, k=2))
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(random.choices(numeros, k=2))
num =[1, 2, 3, 4]
random.shuffle(num)
print(num)

print(random.uniform(5.5, 10.5))
