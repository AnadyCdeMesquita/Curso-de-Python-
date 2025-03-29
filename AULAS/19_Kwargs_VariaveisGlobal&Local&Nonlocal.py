# variavel_local = 7
# def variavel(b):
#   b += variavel_local
#   return variavel_local, b

# res = variavel(5)
# print(res)

# x = 10
# def teste(a):
#   global x
#   x= 15
#   return x + a

# print(x)
# print(teste(20))
# print(x)

# def testando():
#   variavel_externa = 'sou uma variável externa'
#   print(variavel_externa)
#   def teste():
#     nonlocal variavel_externa
#     variavel_externa = 'sou variavel interna agora'
#     print(variavel_externa)

#   teste()
# testando()  
    

# def saudacao(nome):
#   return f' Olá, {nome}.'
# def cumprimentar(funcao, nome):
#   return funcao(nome)

# print(cumprimentar(saudacao, 'Anady'))

# def saudacao (nivel):
#     def saudacao_basica():
#       return "OI"
#     def saudacao_avancada():
#       return 'Olá, gente boa. Tudo bem?'
#     if nivel == 'basico':
#       return saudacao_basica
#     else:
#       return saudacao_avancada
    
# resultado = saudacao('basico')
# print(resultado())
# resultado = saudacao('teste')
# print(resultado())

