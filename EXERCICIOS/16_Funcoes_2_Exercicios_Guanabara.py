#EXERCICIO 1
# ano = int(input("Qual a data do seu nascimento? \n "))
# def voto(ano):
#   import datetime
#   idade = datetime.date.today().year - ano
#   if  idade < 16:
#     return 'Vc não é obrigado a votar, vc tem {idade} anos.'
#   elif idade > 16 and idade <= 17 or idade > 65:
#     return f'Votar é opcional, vc tem {idade} anos.'
#   else:
#     return f'Acima de 18 anos é obrigatório, vc tem {idade} anos.'
    
# print(voto(ano))

#EXERCICIO 2:

# n = int(input("Digite um número? \n "))
# def fatorial (n):
#   fat = 1
#   for c  in range(n, 1, -1):
#     fat *= c
#   return fat

# teste = fatorial(n)
# print(f'O fatorial de {n} é {teste}.')

#EXERCICIO 3

# nome  = str(input("Qual o nome do jogador? \n "))
# gols  = int(input("Quantos gols ele fez? \n "))
# def ficha(nome = '', gols = 0):
#   if nome == None and gols == None:
#     return "Jogador desconhecido e zero gols"
#   else:
#     return nome, gols

# ficha(nome, gols)
# print(f'O nome do jogador é {nome} e fez {gols} gols.' )

##OUTRA FORMA DE FAZER
# nome  = str(input("Qual o nome do jogador? \n "))
# gols  = str(input("Quantos gols ele fez? \n "))
# def ficha(nome = '', gols = 0):

#   if gols.isnumeric():
#     g = int(g)
#   else:
#     gols = 0
#   if nome.strip() == "":
#     ficha(gols = nome)
#   else:
#     ficha(nome, gols)

# print(f'O jogador {nome} fez {gols} gols no campeonato')

#EXERCICIO 4

# n = 0
# def leiaInt(n):
#   while True:
#     n = str(input("Digite um número: \n "))
#     if n.isnumeric():
#       print('É um número')
#     else:
#       print("Não é um número")

# teste = leiaInt(n)
# print(teste)

#EXERCICIO 5
# def notas (*n, sit = False):
#   r = dict()
#   r['total'] = len(n)
#   r["maxima"] = max(n)
#   r['minimo'] = min(n)
#   r['media'] = sum(n) / len(n)
#   if sit:
#     if r['media'] >= 7:
#       r['situação'] = 'BOA'
#     elif r['media'] >= 5:
#       r['situação'] = 'RAZOÁVEL'
#     else:
#       r['situação'] = 'RUIM'
      
#   return r
  
# resp = notas(9, 10, 8, 7, sit=True)
# print(resp)
# resp1 = notas(5, 7, 2, 1, sit = True)
# print(resp1)



