# x= 0
# while x <= 30:
#   print(x)
#   x+=1

# n= 10
# while n >= 0:
#   print(n)
#   n -= 1
# print('POOOOOWWWWWWW, PUUUUUMMMM')
# print('********' * 20)

# for i in range(1, 11, 1):
#   print(i)
# print('POOOOOWWWWWWW, PUUUUUMMMM')
  
# for i in range(11, 1, -1):
#   print(i)
# print('POOOOOWWWWWWW, PUUUUUMMMM')

#EXERCÍCIO 1

# from time import sleep
# for i in range(10, -1, -1): #chegar até o zero
#   print(i)
#   sleep(3)#essa função sleep pode ser dentro da função ou fora
#   #FORA, PEGAVA O PRINT DO POOOWWW, PUUMMMM.
# print('POOOOOWWWWWWW, PUUUUUMMMM')

#EXERCÍCIO 2
# for i in range(1, 52):
#   if i % 2 == 0:
#     print(i)
#OU 
# for i in range(2, 51):
#     print(i)

#EXERCICIO 3:
# soma = 0 #acumulador
# cont = 0
# for c in range(1, 501):
#   if c % 2 != 0 and c % 3 == 0:
#     cont +=1
#     soma += c

# print(f'A soma de todos os {cont} valores solicitados é {soma}.')

# n= int(input('Digite um número: \n'))
# print('**' * 20)
# for i in range(1, 11):
#   print(f'{n} x {i} = {n * i}')
  
# n = 0
# z= int(input('Digite um número: \n'))
# print('**' * 20)
# while n<=10:
#   print(f'{n} x {z} = {n*z}')
#   n+=1   

#EXERCICIO 4:

# print('**' * 20)
# cont = 0
# soma = 0
# for i in range(1, 7):
#   z= int(input('Digite um número: \n'))
#   if i % 2 == 0:
#       cont += 1
#       soma += z 
# print(f'Quantidade de números {cont} pares no intervalo.')
# print(f'A soma dos número são {soma}.')
  
#EXERCICIO 4
# print('***' * 20)
# print('10 TERMOS DE UMA PA')
# print('***' * 20)

# primeiro_termo= int(input('Digite o primeiro_termo: \n'))
# razao= int(input('Digite a razão: \n'))
# print(primeiro_termo)
# print(razao)
# for i in range(primeiro_termo, 20, razao):
#   print(i, end='->')
# print('ACABOU')

#EXERCICIO 5 

# number = int(input('Numero: '))
# total = 0
# for i in range(1, number + 1):
#   if number % i == 0:
#     total +=1
#     print('\033[31m {i}', end='')
# print(f'O {number} foi divisível por {total} vezes.')

#exercicio 6 
# frase = str(input('Digite a palavra: \n')).strip().upper()
# palavras = frase.split()
# junto = ''.join(palavras)
# inverso = ''
# # print(junto[::-1]) # reverter ao contrário uma string
# for letra in range(len(junto)-1, -1, -1):
#   inverso += junto[letra] 
# if inverso == junto:
#   print('É um palíndromo')
# else:
#   print('Não um palíndromo')
  

# nome = 'anady carvalho de mesquita'
# divisão = nome.split()
# print(divisão)
# print(f'Seu primeiro nome é {divisão[0].capitalize()} e o último é {divisão[-1].capitalize()}.')
# print(f'Bem-vinda, Senhora {divisão[0].capitalize()} {divisão[-1].capitalize()}.')


#EXERCICIO 7

# import datetime
# cont = 0
# for pessoa in range(1, 8):
#   ano_nascimento = int(input(f'Qual a data do nascimento da {pessoa} pessoa? \n'))
#   idade = datetime.date.today().year - ano_nascimento
#   if idade >= 18:
#     cont += 1
#     print('Vc é de maior')
#   else:
#    print('Vc é de menor')
   
# print(f'A quantidade de pessoas maiores é {cont}')
# print(f'A quantidade de pessoas menores é {7- cont } ')
# ***************************************************
# peso = []
# for pessoa in range(1, 6):
#     peso.append(float(input(f'Qual o peso da {pessoa}ª pessoa? \n')))

# print(peso)
# print(f'O peso máximo foi:{max(peso)}. O peso mínimo foi {min(peso)}')
  #**********************************************************
maior = 0
menor = 0
for p in range(1, 6):
  peso = float(input(f'Qual o peso da {p}ª pessoa? \n'))
  if p == 1:
    peso = maior
    peso = menor
  else:
    if peso > maior:
      maior = peso
    if peso < menor:
      menor = peso
    
print(f'O maior peso é {maior}')
print(f'O menor peso é {menor}')

#EXERCICIO 8

# media = 0
# maioridadehomem = 0
# nomevelho = ''
# totmulher = 0
# for p in range(1, 5):
#   print(f'{"****" * 10} {p} pessoa {"****" * 10}')
#   nome = str(input(f'NOME: \n')).strip()
#   idade = int(input(f'IDADE: \n'))
#   sexo = str(input(f'SEXO [M/F]: \n')).strip()
#   media += idade
#   media1 = media / 4
#   if p==1 and sexo in 'Mm':
#     maioridadehomem = idade
#     nomevelho = nome
#   if sexo in 'Mn' and idade > maioridadehomem[p]:
#     maioridadehomem[p] = idade
#     nomevelho = nome[p]
#   if sexo in 'Ff' and idade < 20:
#     totmulher +=1
  
  
  
# print(f'A média de idade é {media1}')
# print(f'O homem mais velho tem {maioridadehomem} e se chama {nomevelho}. ')
# print(f'Ao todo são o total de {totmulher} menor que 20.')


  
  
    