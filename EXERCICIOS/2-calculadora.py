print('CALCULADORA SIMPLES:\n')


while True:
  print('Digite a opção desejada: \n')
  print('1 PARA ADIÇÃO')
  print('2 PARA SUBTRAÇÃO')
  print('3 PARA MULTIPLICAÇÃO')
  print('4 PARA DIVISÃO')
  print('5 PARA SAIR \n')
  opcao = int(input('Digite a opção: \n'))
  if opcao == 1:
    numero1 = int(input('Digite um número: \n'))
    numero2 = int(input('Digite um número: \n'))
    soma = numero1 + numero2
    print(f'{numero1} + {numero2} = {soma} \n')
  elif opcao == 2:
    numero1 = int(input('Digite um número: \n'))
    numero2 = int(input('Digite um número: \n'))
    subtracao = numero1 - numero2
    print(f'{numero1} - {numero2} = {subtracao} \n')
  elif opcao == 3:
    numero1 = int(input('Digite um número: \n'))
    numero2 = int(input('Digite um número:  \n'))
    multiplicacao = numero1 * numero2
    print(f'{numero1} * {numero2} = {multiplicacao} \n')
  elif opcao == 4:
    numero1 = int(input('Digite um número:  \n'))
    numero2 = int(input('Digite um número:  \n'))
    divisao = numero1 / numero2
    print(f'{numero1} / {numero2} = {divisao} \n')
  elif opcao == 5:
    print('Sair')
    break
  else:
    print('Opção inválida.')
    break
    