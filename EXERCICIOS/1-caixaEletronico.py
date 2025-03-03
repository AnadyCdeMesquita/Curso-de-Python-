



saldo_total = 2000
while True:
  print('Escolha uma opção:  1 para verificar saldo;  2- Deposita dinheiro; 3- Sacar Dinheiro; 4-Sair: \n')
  opcao = int(input('Digite a opção: \n'))
  if opcao == 1:
    print(f'Seu saldo é R$ {saldo_total}')
  elif opcao == 2:
    depositar_dinheiro = float(input('Qual o valor do depósito: \n'))
    saldo_total += depositar_dinheiro
    print(f'O valor do depositado foi: R$ {depositar_dinheiro: .2f} e o saldo total é: R$ {saldo_total: .2f}')
  elif opcao == 3:
    saque = float(input('Qual o valor do saque: \n'))
    if saque < saldo_total:
      saldo_total -= saque
      print(f'O valor do saque foi: R$ {saque: .2f} e o saldo total é: R$ {saldo_total: .2f}')      
      
    else:
      print(f'Saque inválido. Saldo insuficiente.')  
  elif opcao == 4:
    print('Sistema finalizado')
    break
  else:
    print('Opção inválida, digite uma das opções sugeridas')