
#EXERCICIO 1
# from random import randint
# pc = randint(0, 5)
# jogador = int(input('Qual o número vc pensou? \n'))

# if pc == jogador:
#   print(f'Vc acertou, o número é {pc}.')
# else:
#   print(f'Vc é um azalado, o número é {pc}.') 

#EXERCICIO 2
# velocidade = int(input('Qual a velocidade? \n'))
# valor = (velocidade - 80) * 7
# if velocidade <= 80:
#   print(f'Bom dia, continue nessa velocidade adequada')
# else:
#    print(f'A velocidade de {velocidade} ultrapassou o limite permitido, multa de R$ {valor: .2f}.')

#EXERCICIO 3

# numero = int(input('Qual o número? \n'))
# if numero % 2 == 0:
#   print(f'É um número par: {numero}')
# else:
#    print(f'É um número ímpar: {numero}')

#EXERCICIO 5

# distancia = float(input('Qual a distancia? \n'))
# passagem1 = distancia * 0.50
# passagem2 = distancia * 0.45
# if distancia <= 200:
#   print(f'O valor da passagem: {passagem1: .2f}')
# else:
#   print(f'O valor da passagem: R$ {passagem2: .2f}')

#EXERCICIO 6 +++ANO BISSEXTO+++
#Verificar se o ano é divisível por 4, 
# mas não por 100, ou se é divisível por 400
# ano = int(input('Qual ano vc nasceu? \n'))
# if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
#   print(f'{ano} é um ano bissexto.')
# else:
#   print(f'{ano} não é um ano bissexto.')

#exercicio 7
# n1 = int(input('Digite 3 números? \n'))
# n2 = int(input('Digite 3 números? \n'))
# n3 = int(input('Digite 3 números? \n'))

# if n1 < n2 and n2 < n3:
#   print(f'{n1} é menor e o {n3} é maior')
# if n2 < n1 and n1 < n3:
#   print(f'{n2} é menor e o {n3} é maior')
# if n3 < n1 and n1 < n2:
#   print(f'{n3} é menor e o {n2} é maior')
# if n2 < n3 and n3 < n1:
#   print(f'{n1} é maior e o {n2} é menor')
  
#EXERCICIO 8:
# salario = float(input('Qual o valor do seu salário? \n'))
# aumento = salario + (salario * 0.1)
# aumento2 = salario + (salario * 0.15)

# if salario > 1250:
#   print(f'O aumento do seu salário foi de {(salario * 0.1): .2f} e passou a ser {aumento: .2f}.')
# else:
#   print(f'O aumento do seu salário foi de {(salario * 0.15): .2f} e passou a ser {aumento2: .2f}.')

#exercicio 9
r1 = float(input('digite um lado do triangulo? \n'))
r2 = float(input('digite um lado do triangulo? \n'))
r3 = float(input('digite um lado do triangulo? \n'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
  print(f'Forma um triângulo perfeito.' )
else:
  print(f'Não forma um triângulo perfeito.' )
  
  



