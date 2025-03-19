#EXERCICIO 1
# aluno = dict()
# aluno['nome'] = str(input('Digite o nome: '))
# aluno['media'] = float(input('Digite o nome: '))
# if aluno['media'] >= 7:
#   aluno['situacao'] = 'Aprovado'
# elif 5<= aluno['media'] < 7:
#   aluno ['situcao'] = 'Recuperação'
# else:
#   aluno['situacao'] = 'Reprovado'

# for k, v in aluno.items():
#   print(f'{k} é igual a {v}.')

#EXERCICIO 2

# from random import randint
# from time import sleep
# jogo = {'jogador1': randint(1,6), 'jogador2': randint(1,6), 'jogador3': randint(1,6)}
# lista = []
# for k, v in jogo.items():
#   print(f'{k} tirou {v} no dado')
#   sleep(1)
# lista.append(jogo.copy()) 
# lista.sort()
# print(lista)

#EXERCICIO 3:
# import datetime
# trabalhador = {}
# trabalhador['nome'] = str(input('Nome: '))
# trabalhador['ano'] = int(input('Ano Nascimento: '))
# trabalhador['ctps'] = int(input('Carteira de Trabalho: (0 não tem)'))

# if trabalhador['ctps'] != 0:
#   trabalhador['idade'] = datetime.date.today().year- trabalhador['ano']
#   trabalhador['contratacao'] = int(input('Digite o ano de contratação: '))
#   trabalhador['salario'] = int(input('Digite o seu salário: '))
#   trabalhador['aposentadoria'] = trabalhador['idade'] + (trabalhador['contratacao'] + 35) - datetime.date.today().year

# print(trabalhador)

# for k, v in trabalhador.items():
#   print(f'O {k} tem o valor de {v}')

#EXERCICIO 4
# jogador = {}
# gols = []
# jogador['nome'] = str(input('Nome do Jogador:   '))
# partidas = int(input(f'Quantas partidas {jogador["nome"]} jogos?  '))
# for p in range(0, partidas):
#   gols.append(int(input(f'Quantos gols na partida {p}?   ')))
# jogador['gol'] = gols[:]
# jogador['total'] = sum(gols)
# print(jogador)
# for k, v in jogador.items():
#   print(f'O campo {k} tem o valor de {v}.')
  
# print(f'O Jogador {jogador['nome']} jogou {partidas} partidas.')
# for k, v in enumerate(gols):
#   print(f'Na partida {k}, fez {v} gols.')
# print(f'Foi um total de {jogador['total']}.')

#EXERCÍCIO 5

# galera = list()
# pessoa = dict()
# soma = media = 0

# while True:
#   pessoa['nome'] = str(input('Nome:  '))
#   pessoa['sexo'] = str(input('SEXO M/F:  ')).strip().upper()[0]
#   while pessoa['sexo'] not in 'MmFf':
#     print('ERRO!Por favor, digite apenas M ou F')
#     pessoa['sexo'] =  str(input('Deseja continuar?? S/N:  '))
#   pessoa['idade'] = int(input('Idade:  '))
#   soma += pessoa['idade']
 
#   galera.append(pessoa.copy())
#   pessoa.clear()
#   question = str(input('Deseja continuar?? S/N:  ')).strip().upper()[0]
#   while question not in 'NnSs':
#     print('ERRO!Por favor, digite apenas Ss ou Nn')
#     question = str(input('Deseja continuar?? S/N:  ')).strip().upper()[0]
#   if question in 'Nn':
#     break
# print(galera)
# print(f'A) Ao todos temos {len(galera)} pessoas cadastradas.')
# media = soma / len(galera)
# print(f'A média de idade é {media}.')
# for p in galera:
#   if  p['idade'] >= media:
#     print(f'Maior ou igual a média {p["nome"]}')
#   else:
#     print(f'Menor que a média {p['nome']}')
# for p in galera:
#   if  p['sexo'] in 'Ff':
#     print(f'{p["nome"]}')
 
time = list()
jogador = dict()
partidas = list()

while True:
  jogador.clear()
  jogador['nome'] =  str(input('Nome:  '))
  total_partidas =  int(input(f'Quantas partidas o {jogador["nome"]} jogou?  '))
  partidas.clear()
  for c in range(0, total_partidas):
    partidas.append(int(input(f'Quantos gols na partida {c}?  ')))
  jogador['gols'] = partidas[:]
  jogador['total'] = sum(partidas)
  time.append(jogador.copy())
  resp = str(input('Deseja continuar? S/N  ')).strip().upper()[0]
  while resp not in 'SsNn':
      print('Erro!!! Responda somente Ss ou Nn')
      resp = str(input('Deseja continuar? S/N  ')).strip().upper()[0]  
  if resp in 'Nn':
      break
print(time)
print(f'O {jogador["nome"]} jogou {len(jogador)} partidas.')
for k, v in enumerate(jogador['gols']):
  print(f' Na partida {k}, fez {v} gols')
