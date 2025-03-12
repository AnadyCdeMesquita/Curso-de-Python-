#EXERCICIO 1

# sexo = str(input('Qual o seu sexo? M/F \n')).strip().lower()[0]
# idade = int(input('Qual a sua idade? M/F \n'))
# while True: 
#   if sexo not in 'MF':
#     sexo = str(input('Tente novamente, informe seu sexo: M/F \n')).strip().lower()[0]
#     print(f'seu sexo é {sexo}')
#   if idade >= 18:
#     print('de maior')
#     break
#   else:
#     print('de menor')
  #Em Python, a expressão not in é usada para verificar se um elemento não está presente em uma sequência, como uma lista, tupla, string, dicionário, etc. Ela retorna True se o elemento não estiver presente e False caso contrário.

#EXERCICIO 2
# from random import randint
# print('Sou o seu computador ...')
# print('Acabei de pensar em um número de 0 a 10')
# print('Será que vc consegue advinhar qual foi?')
# cont = 0
# computador = randint(0, 10)
# print(computador)
# palpite = int(input('Qual o seu palpite? \n'))
# while True:
#   if computador < palpite :
#     print('Menos...Tente mais uma vez.')
#     palpite = int(input('Qual o seu palpite? \n'))
#     cont+=1
#   elif computador > palpite :
#       print('Mais...Tente mais uma vez.')
#       palpite = int(input('Qual o seu palpite? \n'))
#       cont+=1
#   else:
#     print('VC acertou...')
#     print(f'Vc acertou com {cont} tentativas...Parabéns') 
#     break

#EXERCICIO 3

# valor1 = int(input('Digite um número? \n'))
# valor2 = int(input('Digite um número? \n'))
# print(f'{"***" * 10} MENU {"***" * 10}')
# print('             [1]SOMAR, [2]MULTIPLICAR') 
# print('             [3]MAIOR [4]NOVOS NÚMEROS')
# print('             [5] SAIR DO PROGRAMA')
# opcao = int(input('Digite uma opção: \n'))
# while True:
#       if opcao == 1:
#             soma = valor1 + valor2
#             print(f'O valor da soma é {soma}')
#       elif opcao == 2:
#             multiplicacao = valor1 * valor2
#             print(f'O valor da multiplicação é {multiplicacao}')
#       elif opcao == 3:
#             if valor1 > valor2:
#                   print(f'O maior valor é {valor1}.')
#             else:
#                   print(f'O menor valor é {valor2}')
#       elif opcao == 4:
#             valor1 = int(input('Digite novos números? \n'))
#             valor2 = int(input('Digite novos números? \n'))
#       elif opcao == 5:
#             print('Sair do Programa')
#             break     
#       else: 
#             print('Opção Inválida... Tente Novamente')
#       opcao = int(input('Digite uma opção: \n'))


# from math import factorial
# valor1 = int(input('Digite um número? \n'))
# print(factorial(valor1))

#EXERCICIO 4  ### fatorial 
# n = int(input('Digite um número? \n'))
# plus = 1
# for i in range (n, 0, -1):
#       plus *= i     
# print(plus)     

#EXERCICIO 5
# primeiro = int(input('Digite o primeiro termo:\n'))
# razao = int(input('Digite a razão:\n'))
# termo = primeiro
# cont = 1
# while cont < 10:
#       termo += razao
#       cont +=1
#       print(f'{termo}->', end='')
# print('fim')

#EXERCICIO 6
# primeiro = int(input('Digite o primeiro termo:\n'))
# razao = int(input('Digite a razão:\n'))
# termo = primeiro
# cont = 1
# mais = 0
# total = 0
# while mais != 0:
#   total = total + mais
#   while cont <= total:
#       termo += razao
#       cont +=1
#       print(f'{termo}->', end='')
# print('PAUSA')
# mais = int(input('Quantos termos vc quer mostrar a mais?'))
# print('fim')


#EXERCICIO 7
#números fibonacci
# termos = int(input('Quanto termos vc quer mostrar:\n'))
# t1 = 0
# t2 = 1
# cont = 3
# print(f'{t1} -> {t2}->', end='')
# while cont <= termos:
#   t3 = t1 + t2 
#   t1=t2
#   t2=t3
#   print(F'{t3} ->', end= '')
#   cont +=1
# print('FIM')

#EXERCICIO 8
# soma = 0
# n = int(input('Digite Números:\n'))
# cont = 0
# while n != 999:
#   soma += n
#   cont += 1
#   n = int(input('Digite Números:\n'))
# print(f'Quantidade de números digitados foi {cont}.')

#EXERCICIO 9
opcao = 'S'
maior = 0
menor = 0
cont = 0
soma = 0
while opcao in 'sS':
  n = int(input('Digite Números:\n'))
  if cont == 1:
    maior = menor = n
  else:
    if n > maior:
      maior = n
    if n < menor:
      menor = n
  opcao = str(input('Deseja continuar? s/n \n')).strip().upper()
  soma += n
  cont+=1
  media = soma / 3
print(f'Vc digitou {cont} e a média é {media}.')
print(f'O número maior é {maior}')
print(f'O número maior é {menor}')
  
  
  
  
  




