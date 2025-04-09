proprietarios = {}
while True:
  apto = int(input('Qual o NÚMERO do apartamento? \n'))
  if apto != -1:
    condonomo = (input("Qual NOME do proprietário: \n"))
    proprietarios.update({apto: condonomo})
  else:
    break

# print(proprietarios)
teste = dict(sorted(proprietarios.items())) #sorted converte em lista 
print(teste)
for k, v in teste.items():
  print(k, v)