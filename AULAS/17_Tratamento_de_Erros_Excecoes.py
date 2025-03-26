try:
  a = int(input('Digite um número: \n'))
  b = int(input('Digite um número: \n'))
  r= a/ b
except (ValueError, TypeError):
  print(" Tivemos um problemaa com os tipos de dados que vc digitou")
except ZeroDivisionError:
  print("Não é possível dividir o número por zero")
except KeyboardInterrupt:
  print("Usuário preferiu não informar os dados")
except Exception as erro:
  print(f'O erro encontrado foi {erro._cause_}')
else:
  print(f'O resultado é {r}')
finally:
  print('Volte sempre, muito obrigada(o)')