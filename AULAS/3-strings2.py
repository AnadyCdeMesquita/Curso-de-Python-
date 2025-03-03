# texto_upper = 'hello world'
# print(texto_upper.upper()) #maiúscula todas as letras

# texto_upper2 = 'HellO mUNDO'
# print(texto_upper2.lower()) # minúscula todas as letras

# texto_upper3 = 'hello mundo'
# print(texto_upper3.capitalize()) # fica maiúscula apenas a 1ª letra

# texto_upper = 'hellO world'
# print(texto_upper.count('O')) #COUNT CONTA A QUANTIDADE DE LETRAS, SENSITIVE CASE, FAZ DISTINÇÃO MAIÚSCULA E MINÚSCULA

# texto_upper2 = 'hellO world'
# print(texto_upper2.replace("hellO", "alô"))

#EXERCICIOS
# nome = 'Anady'
# sobrenome = 'Carvalho'
# idade = 30
# nomeCompleto = nome + ' ' + sobrenome
# print(nomeCompleto)

# mensagem = f'O nome completo é: {nomeCompleto} e tem {idade} anos.'
# print(mensagem)

frase = 'Python é uma linguagem de programação poderosa e versátil.'
print(len(frase)) # 57
palavra = frase[0:6]
print(palavra)

frase_maiuscula = frase.upper()
print(frase_maiuscula)

substituicao = frase.replace('poderosa', 'incrível')
print(substituicao)