frutas = []
while True:
  print("DIGITE 1- PARA ADICIONAR PRODUTO")
  print("DIGITE 2- PARA REMOVER PRODUTO")
  print("DIGITE 3- PARA EXIBIR PRODUTO")
  print("DIGITE 4- PARA SAIR")
  opcao = int(input("\nDigite a opção desejada:  \n"))

  if opcao == 1:  
    adicionar = frutas.append(str(input('Quais as frutas vc deseja adicionar? \n').lower()))
    print(f'A fruta adicionada no carrinho foi {frutas[-1]}.')
   
  elif opcao == 2:
    remover = str(input("Qual a frutas vc deseja remover? \n"))
    frutas.remove(remover)  
    print(f'A fruta removida foi {remover}')
  elif opcao == 3:
    juntando = ', '.join(frutas)
    print(f'Os item que há no carrinho são: {juntando}')
  elif opcao == 4:
    print('sair')
    break
  else:
    print('Tente novamente')
  