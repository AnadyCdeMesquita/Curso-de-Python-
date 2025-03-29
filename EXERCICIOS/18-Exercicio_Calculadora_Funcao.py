# while True:
#   print('ESCOLHA A OPÇÃO 1- SOMA 2- SUBTRAIR 3- MULTIPLICAR 4-DIVIDIR')
#   opcao = int(input("\n Digite a opção desejada :  "))
#   if opcao == 1:
#     a = int(input('Digite um primeiro número 1 : '))
#     b = int(input('Digite um primeiro número 2: '))
#     def somar(a, b):
#       soma = a + b
#       return f'O resultado de {a} + {b} = {soma}'
#     res = somar(a, b)
#     print(res)
#     print("Deseja continuar?")
#     escolha = int(input(" Digite 1-Sim ou 2-Não: \n"))
#     if escolha == 2:
#       break
#   elif opcao == 2:
#     a = int(input('Digite um primeiro número: '))
#     b = int(input('Digite um primeiro número: '))
#     def subtracao(a, b):
#       subtrair = a - b
#       return f'O resultado de {a} - {b} = {subtrair}'
#     res = subtracao(a, b)
#     print(res)
#     print("Deseja continuar?")
#     escolha = int(input(" Digite 1-Sim ou 2-Não: \n"))
#     if escolha == 2:
#       break
#   elif opcao == 3:
#     a = int(input('Digite um primeiro número: '))
#     b = int(input('Digite um primeiro número: '))
#     def multiplicar(a, b):
#       plus = a * b
#       return f'O resultado de {a} * {b} = {plus}'
#     res = multiplicar(a, b)
#     print(res)
#     print("Deseja continuar?")
#     escolha = int(input(" Digite 1-Sim ou 2-Não: \n"))
#     if escolha == 2:
#       break
#   elif opcao == 4:
#     a = int(input('Digite um primeiro número: '))
#     b = int(input('Digite um primeiro número: '))
#     def dividir(a, b):
#       divisao = a / b
#       return f'O resultado de {a} / {b} = {divisao}'
#     res = dividir(a, b)
#     print(res)
#     print("Deseja continuar?")
#     escolha = int(input(" Digite 1-Sim ou 2-Não: \n"))
#     if escolha == 2:
#       break
#   else:
#     print("Opção inválida- Tente Novamente")
    
while True:
  print('\n DIGITE A OPÇÃO DESEJADA: ')
  print('\n 1- somar / 2-subtrair / 3-Multiplicar / 4-Dividir')
  opcao = int(input('\n Digite a opção desejada: \n'))
  if opcao == 1:
    lista = list(map(int, input("Digite os números que vc deseja somar: ").split()))
    def somar(*args):
      soma = sum(lista)
      return f'A soma é {soma}.'
    resp = somar(lista)
    print(resp)
  elif opcao == 2:
    lista = list(map(int, input("Digite os números que vc deseja subtrair: ").split()))
    def subtracao(*args):
      resultado = lista[0]
      for num in lista[1:]:
        resultado -= num
        return resultado
    resp = subtracao(lista)
    print(resp)
  elif opcao == 3:
    lista = list(map(int, input("Digite os números que vc deseja multiplicar: ").split()))
    def multiplicar(*args): 
      resultado = lista[0]
      for num in lista[1:]:
        resultado *= num
      return resultado
    resp = multiplicar(lista)
    print(resp)
  elif opcao == 4:
    lista = list(map(int, input("Digite os números que vc deseja multiplicar: ").split()))
    def dividir(*args): 
      resultado = lista[0]
      for num in lista[1:]:
        resultado /= num
      return resultado
    resp = dividir(lista)
    print(resp)
      
        
      
  


