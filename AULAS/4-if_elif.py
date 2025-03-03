# import random
# boli = random.randint(0, 10)
# if boli == 7:
#   print('Vc acertou, o número é 7.')
# else:
#   print('Vc errou, o número não é', boli, '.')
  
# numero_secreto = 7
# n = int(input('Digite um número de 1 a 10: \n'))
# if n == 7:
#   print('Vc acertou, o número é 7.')
# else:
#   print('Vc errou, o número não é', n, '.')

# idade = int(input('Qual a sua idade? \n'))
# if idade >= 18:
#   print('Vc está apta(o) a votar.')
# else:
#   print('Vc não irá a votar.')

# nota = int(input('Insira nota de 0 a 100: \n'))

# if nota >=90 and nota <= 100:
#   print('Excelente')
# elif nota >=70 and nota <= 89:
#   print('Bom')
# elif nota >=50 and nota <= 69:
#   print('Satisfatório')
# else:
#   print('Insatisfatório, nota de 0-49')

p1 = (input('Vc recebeu o convite? '))
p2 = (input('Vc está na lista de convidados? '))
p3 = (input('Vc é um membro do clube? '))

if p1 == 'sim' or p2 == 'sim' or p3 == 'sim':
  print('Vc está liberado')
else:
  print('barrado')