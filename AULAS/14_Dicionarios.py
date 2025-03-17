# dados = {'nome':'Anady', 'idade': 45, 'sexo':'feminino'}
#print(dados['nome'])
# dados['profissão'] = 'fiscal'
# print(dados)
# del dados['profissão'] #apagar uma chave
# dados.pop('idade') #apagar uma chave
# print(dados)
# for k, v in dados.items():
#   print(f'O {k} é {v}')

# print(dados.values())
# print(dados.keys())
# print(dados.items())

# for k in dados.keys():
#   print(k)
  
# for v in dados.values():
#   print(v)
  
# for k, v in dados.items():
#   print(f'O {k} é {v}')  


#exercicio
# brasil = []
# estado1 = {'UF': 'Rio de Janeiro', 'Sigla': 'RJ'}
# estado2 = {'UF': 'São Paulo', 'Sigla': 'SP'}
# brasil.append(estado1)
# brasil.append(estado2)
# print(brasil)
# print(len(brasil))
# print(brasil[0]['UF'])
# print(brasil[1]['Sigla'])

estados  = dict()
brasil = list()
soma = ''
for c in range(1,4):
  estados['uf'] = str(input('Digite o Estado: \n'))
  estados['sigla'] = str(input('Digite a sigla: \n'))
  brasil.append(estados.copy())
print(brasil)
for e in brasil: ##esse "e" representa a lista do dicionario
  for k, v in e.items(): ##esse "e" representa a lista do dicionario
    print(k, v)