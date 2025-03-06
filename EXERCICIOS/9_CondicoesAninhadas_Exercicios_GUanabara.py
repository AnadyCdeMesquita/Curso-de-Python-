#EXERCICIO 1

# valor_casa = float(input('Qual o valor da casa?\n'))
# salario = float(input('Qual o valor do seu salário?\n'))
# anos = int(input('Quantos anos vc deseja financiar?\n'))
# porcentagem = salario * (30 / 100)
# anos1 = anos * 12
# financiamento = valor_casa / anos1
# if financiamento < porcentagem:
#   print(f'Empréstimo Autorizado, dentro da margem dos 30% - {porcentagem: .2f}, valor da prestação por mês {financiamento: .2f}.')
# else:
#   print(f'Uma pena, empréstimo negado, ultrapassa o valor dos 30% - {porcentagem: .2f}, valor da prestação por mês {financiamento: .2f}.')

#EXERCICIO 2

# num = int(input('Digite um número inteiro?\n'))
# print('ESCOLHA UMAS DAS BASES PARA CONVERSÃO:')
# print('[1] Converter para BINÁRIO')
# print('[2] Converter para OCTAL')
# print('[3] Converter para HEXADECIMAL')
# opcao = int(input('Digite sua opção?\n'))

# if opcao == 1:
#   print(f'O {num} em binário é {bin(num)[2:]}.')
#   # A função bin() retorna uma string que começa com '0b', então [2:] é usado para remover os dois primeiros caracteres e exibir apenas a parte binária.
# elif opcao == 2:
#   print(f'O {num} em octal é {oct(num)[2:]}.')
#   #A função oct() retorna uma string que começa com '0o', então [2:] é usado para remover os dois primeiros caracteres e exibir apenas a parte octal.
# elif opcao == 3:
#   print(f'O {num} em hexadecimal é {hex(num)[2:0]}.')
#   #A função hex() retorna uma string que começa com '0x', então [2:] é usado para remover os dois primeiros caracteres e exibir apenas a parte hexadecimal.
# else:
#   print('Opção inválida, tente novamente')
#EXERCICIO 3
#import date
# from datetime import date
# atual = date.today().year
# ano = int(input('Qual o ano do seu nascimento? \n'))
# calculo_idade = atual - ano
# print(f'Quem nasceu {ano} tem {calculo_idade} em {atual}. \n')
# calculo_idade = atual - ano
# if calculo_idade > 18:
#   print(f'Vc ultrapassou a idade limite de alistamento - sua idade é {calculo_idade}.')
# elif calculo_idade < 18:
#   print(f'Alistamento a partir dos 18 anos completos, vc tem apenas {calculo_idade}, falta{18 - calculo_idade} .')
# else:
#   print(f'Vc já tem {calculo_idade} anos. Deve se alistar imediatamente.')

#EXERCICIO 4
# nota1 = float(input('Qual a sua nota 1: '))
# nota2 = float(input('Qual a sua nota 2: '))
# media = (nota1 + nota2) / 2
# if media < 5:
#   print('Você está reprovado, média: {media}.')
# elif 5 <=media <= 6.9:
#   print(f'Vc está em recuperação, média: {media}.')
# else: #pode usar também um elif
  
#   print(f'Media igual ou superior a 7. Vc está aprovado, média: {media}.')
  
#EXERCICIO 5
# import datetime
#mes = datetime.date.today().month
#dia = datetime.date.today().day
# data_nascimento = int(input('Qual a data do seu nascimento? \n'))
# ano = datetime.date.today().year 
# resultado = ano - data_nascimento
# if resultado <=9:
#   print('Atleta Mirim')
# elif  9 < resultado <= 14:
#   print('Atleta Infantil')
# elif  14 < resultado <= 19:
#   print('Atleta Júnior')
# elif  19 < resultado <= 25:
#   print('Atleta Sênior')
# elif resultado > 25:
#   print('Atleta Master')

#EXERCICIO 6
# r1 = float(input('digite um lado do triangulo? \n'))
# r2 = float(input('digite um lado do triangulo? \n'))
# r3 = float(input('digite um lado do triangulo? \n'))

# if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
#     print(f'Forma um triângulo:', end='' ) # triângulo perfeitos
#     if r1 == r2 == r3:
#       print('Equilátero')
#     elif r1 != r2 != r3 != r1:
#       print('Escaleno')
#     else:
#       print('Isósceles')
# else:
#   print(f'Não forma um triângulo perfeito.' )
  
#exercicio 7

# peso = float(input('Qual o seu peso? \n'))
# altura = float(input('Qual a sua altura? \n'))
# imc = peso/(altura * altura)
# print(f'Seu IMC é {imc: .2f}', end='' )
# if imc < 18.5:
#   print(f'- Vc está abaixo do peso')
# elif 18.5 <= imc < 25:
#   print(f'-Vc está no Peso Ideal')
# elif 25 <= imc < 30:
#   print(f'- Vc está com Sobrepeso')
# elif 30 <= imc < 40:
#   print(f'- Vc está com Obesidade')
# else:
#   print(f'- Obesidade Mórbida')

#Exercício 8

# valor = float(input('Qual o valor do produto?\n'))
# desconto10 = valor - (valor *  0.1)
# desconto5 = valor - (valor *  0.05)
# aumento20 = valor + (valor * 0.2)
# print('**' * 30)
# print('DIGITE UMA OPÇÃO: 1-À VISTA(DINHEIRO), 2-À VISTA(CARTÃO), 3-2 X NO CARTÃO(PREÇO NORMAL), 4- 3x OU MAIS NO CARTÃO: 20% DE JUROS' )
# print('**' * 50)
# opcao = int(input('Digite uma opção: \n'))
# print('**' * 50)
# if opcao == 1:
#   print(f'O valor total com desconto de 10% é {desconto10: .2f} ')
# elif opcao == 2:
#   print(f'O valor total com desconto de 5% é {desconto5: .2f} ')
# elif opcao == 3:    
#   print(f'O valore total sem desconto parcelado em duas vezes é {valor/2: .2f} ')
# elif opcao == 4:
#   parcelas = int(input('Quantas parcelas deseja parcelar?'))
#   print(f'O valor total com aumento de 20%, parcelado em {parcelas} é{aumento20/parcelas: .2f} ')
# else:
#   print('Opcão Inválida. Tente Novamente!')

#Exercicio 9
#PODE SE FAZER COM CHOICE
# from random import choice
# itens = ('pedra', 'papel', 'tesoura')
# computador = choice(itens)
# print(computador)

# from random import randint
# itens = ('pedra', 'papel', 'tesoura')
# computador = randint(0,2)
# print(f'{"*" * 20} SUAS OPÇÕES {"*" * 20}')
# print('Suas opções [0]PEDRA [1]PAPEL [2]TESOURA')
# jogador = int(input('Qual a sua jogada?\n'))
# print(f'O computador escolheu {itens[computador]}.')
# print(f'O jogadorescolheu {itens[jogador]}.')

# if computador == 0:
#   if jogador == 0:
#     print('EMPATE')
#   elif jogador == 1:
#     print('JOGADOR VENCEU')
#   elif jogador == 2:
#     print('COMPUTADOR VENCEU')
# if computador == 1:
#   if jogador == 0:
#     print('JOGADOR VENCEU')
#   elif jogador == 1:
#     print('EMPATE')
#   elif jogador == 2:
#     print('COMPUTADOR VENCEU')
# if computador == 2:
#   if jogador == 0:
#     print('JOGADOR VENCEU')
#   elif jogador == 1:
#     print('COMPUTADOR VENCEU')
#   elif jogador == 2:
#     print('EMPATE')


