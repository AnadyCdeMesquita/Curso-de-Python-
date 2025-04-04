# Aqui, primeiramente, converti a string para float, e depois para int, porque diretamente mão podemos converter string 7.9 para int
# numero_decimal = '7.9'
# numero_inteiro = int(float(numero_decimal))
# teste = '7'
# testando = int(teste)
# print(teste)

#FLOAT(): CONVERTE UM VALOR PARA PONTO FLUTUANTE(decimal)
# num_str = '5.6'
# num_float = float(num_str)
# print(num_float)
# print(type(num_float))

"""
*FUNÇÕES QUE CHAMAM A SI MESMAS;
*PROBLEMAS CLÁSSICOS, COMO O CÁLCULO DO FATORIAL
*RISCOS E LIMITAÇÕES DA RECURSÃO PYTHON
"""
# def contar_regressivamente(n):
#   if n > 0:
#     print(n)
    
#   contar_regressivamente(n-1)
  
# contar_regressivamente(5)
  
# def fatorial(n):
#   if n == 0:
#     return 1
#   else:
#     return n * fatorial(n - 1) # fatorial(n-1) é uma chamada recursiva

# print(fatorial(5))

# def fator(n):
#   plus = 1
#   for i in range(1, n+1):
#     plus *= i
#   return plus
    
# teste =fator(5)
# print(teste)

#RISCOS E LIMITAÇÕES DA RECURSÃO EM PYTHON:

# def recursao_infinita(n):
#   print(n)  
#   return recursao_infinita(n+1)

# recursao_infinita(1)
#OBS: VAI DAR UM LOOP INFINITO