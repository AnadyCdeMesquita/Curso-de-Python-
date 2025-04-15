# notas ={ 'matematica': 8, 
# 'portugues':9,
#  'historia': 7,
#  'geografia': 8,
#  'quimica': 9}

# # loop for = por padrao é feita pelas chaves
# print(f'As disciplinas cursadas são:')
# for disciplinas in notas:
#   print(f'{disciplinas}')

# print(f'As disciplinas cursadas são:')  
# for k in notas.keys():
#   print(f"{k}")
  
# print(f'As notas obtidas são:') 
# soma = 0
# for v in notas.values():
#   print(v)
#   soma += v
#   media = soma / len(notas)
# print(f'A média é {media}')

#EXERCICIOS:
vendas = {'Janeiro': 120,
'Fevereiro': 150,
'Março': 80,
'Abril': 190,
'Maio': 210 
}
# print('Meses que a livraria registrou vendas:')
# for c in vendas.keys(): # 1 exercicio
#   #print(c)

#print('Venda total do mês')


# for v in vendas.values():
#   total = sum(vendas.values())
# print(total)
# maior = max(vendas, key=vendas.get)
# print(maior)
# menor = min(vendas, key = vendas.get)
# print(menor)

segundo = sorted(vendas.values(), reverse=True)
print(segundo[-1])
 
    
# for c, v in vendas.items():
#   print(f'Em {c}, {v} livros foram vendidos')