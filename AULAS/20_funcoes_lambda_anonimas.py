# def dobrar(n):
#   return n *2

# print(f'FUNÇÃO NORMAL: {dobrar(5)}')

# # função LAMBDA

# teste_lambda = lambda x: x * 2
# print(f'FUNÇÃO LAMBDA: {teste_lambda(5)}')

# def tipo_numero(n):
#   if n < 0:
#     return "negativo"
#   elif n == 0:
#     return 'zero'
#   else:
#     return "positivo"

# print(tipo_numero(5))
  
# teste_lambda = lambda n: 'negativo' if n < 0 else ("ZERO" if n == 0 else "positivo")
# print(teste_lambda(-2))

pessoas = [('João', 35), ('Allan', 25),('Pedro', 40)]
ordem_pessoas = sorted(pessoas, key=lambda y: y[1])
print(ordem_pessoas)