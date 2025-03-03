
# n= 10
# while n <= 30:
#   print(n)
#   n+=2
# else:
#   print("Trabalho realizado com sucesso")

# n= 10
# while n <= 30:
#   n+=1
#   print(n)
#   if n == 20:
#     break
  
# linha = 0
# while linha < 3:
#   coluna = 0
  
#   while coluna < 3:
#     print('linha: ', linha, '-coluna: ', coluna)
#     coluna+=1
#   linha+=1   

# ninicial = 1
# nfinal = int(input('Dgite o número final: \n'))

# while ninicial < nfinal:
#   print(ninicial)
#   ninicial += 2

# print('Digite número de 1 a 10')
# n = 1
# max = int(input('Digite o número: \n'))

# while n <= max:
#   if n % 2 == 0:
#     print(n, end=' ')
#   n+=1

# senha = '110580'
# senha_digitada = input('Digite uma senha de 4 dígitos: \n')
# while (senha != senha_digitada):
#     print('Senha incorreta')
#     senha_digitada = input('Digite uma senha de 4 dígitos: \n')
# print('Senha correta')
   
# senha = '110580'
# senhausuarios = input('Digite uma senha: ')
# while (senha != senhausuarios):
#   print('senha incorreta')
#   senhausuarios = input('Digite uma senha novamente: ')
# print('senha correta')

# while True:
#   usuário = input('Digite sair para encerrar programa: \n')
#   if usuário == 'sair':
#     print('programa encerrado.')
#     break

# import random
# randomico = random.randint(1, 100)
# tentativa = 0
# print(randomico)
# while True:
#   numero_sugerido = int(input('Digite o número sugerido: '))
#   tentativa =+1
#   if numero_sugerido > randomico:
#     print('Vc errou, tente novamente')
#   elif numero_sugerido < randomico:
#      print('Vc errou, tente novamente')
#   else:
#      print(f'Vc acertou.')
#      break
# n_digitados = 0
# soma = 0
# while True:
#   n= int(input('Digite de 1 a 20: \n'))
#   n_digitados += 1
#   soma = soma + n
#   if n == 0:
#     print(f'Vc acertou a idade da boneca durante {n_digitados} tentativas e soma deles é {soma}.')
#     break
# senha = '110580'
# tentativas = 0
# while True:
#    Senha_Digitada = input('Digite a sua senha: \n')
#    tentativas += 1
#    if (senha != Senha_Digitada) and (tentativas == 3):
#      print('Senha inválida')
#      break
#    elif (senha == Senha_Digitada):
#      print('senha válida')
#      break
  
# maior_numero = 0
# while True:
#   n_digitado = int(input('Digite numero interior maior que zero: \n'))
#   if n_digitado < 0:
#     print('programa encerrado')
#     break
#   if n_digitado > maior_numero:
#      maior_numero = n_digitado

# print(f"O maior número digitado foi: {maior_numero}")


# menor_numero = None
# while True:
#   n_digitado = int(input('Digite numero interior maior que zero: \n'))
#   if n_digitado < 0:
#     print('programa encerrado')
#     break
#   if menor_numero is None or n_digitado < menor_numero:
#      menor_numero = n_digitado

# print(f"O menor número digitado foi: {menor_numero}")

# x, y = 5, 25

# while x < 10 and y > 10:
#   print(f" x = {x}, y = {y}")
#   x+=1
#   y-=1
# print('Loop Concluído')
# print(f'Valores Finais: x = {x}, y = {y}.')

numeroSecreto1 = 7
numeroSecreto2 = 3
tentativas = 5

# while True:
#   palpite1 = int(input('Digite numero 1 a 10: \n'))
#   if palpite1 == 7:
#    print('Vc adivinhou o primeiro número')
#   else:
#     print('Vc errou')
#   palpite2 = int(input('Digite numero 1 a 10: \n'))
#   if palpite2 == 3:
#    print('Vc adivinhou o segunddo número.')
#   else:
#     print('Vc errou')
#   tentativas -=1 
#   print(f'Restam: {tentativas} tentativas')
  
  

contador = 5
soma = 0

while True:
  n = int(input('Digite um número: '))
  if n % 2 != 0:
    soma += n
    contador -= 1
    print(f'soma = {soma}')
    print(f'tentativas: {contador}')  
  else:
    print(' Loop interrompido, número par.')
    break
  if contador == 0:
    print('fim das tentativas')
    break
    
  