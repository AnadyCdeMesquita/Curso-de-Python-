
def mostra_menu():
  print("Menu")
  print('1- Adicionar Contato \n')
  print('2- Alterar Numero \n')
  print('3- Remover Contato \n')
  print('4- Listar Contato \n')
  print('5- SAIR \n')

agenda = {}
while True:
  opcao = int(input('Qual a opção escolhida: \n'))
  if opcao == 1:
    nome = input("Qual o nome do usuário: \n")
    telefone = input("Qual o telefone do usuário: \n")
    agenda[nome] = telefone
    print(f'O nome é {nome} e o telefone é {telefone}')
  elif opcao == 2:
    nome = input("Qual o nome do usuário: \n")
    if nome in agenda:
      telefone = input("Digite o novo número: \n")
      agenda[nome] = telefone
    print(f'O numero foi mudado para {agenda[nome]}')
  elif opcao == 3:
    nome = input("Qual o nome que você deseja remover: \n")
    agenda.pop(nome)
  elif opcao == 4:
    print(agenda)
  else:
    break
    