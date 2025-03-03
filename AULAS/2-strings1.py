#IMPRIMINDO A POSIÇÃO DA LETRA
# posicaodaLetra = 'anady'
# print(posicaodaLetra[0])
# print(posicaodaLetra[1])
# print(posicaodaLetra[2])
# print(posicaodaLetra[3])
# print(posicaodaLetra[4])

# frase = 'Olá, mundo!'
# parte = frase[4:8]
# print(parte)

# teste = 'Vamos comecar'
# testando = teste[4:8]
# print(testando) #s co

# teste1 = 'Vamos comecar'
# testando1 = teste1[:8] #termina no 7, pois exclui o último
# print(testando1)  #vamos co

# teste2 = 'Vamos comecar'
# testando2 = teste2[2:5:2]
# print(testando2)  

# teste3 = 'Vamos comecar'
# testando3 = teste3[-3]
# print(testando3)  

# teste4 = 'kalinigrado'
# testando4 = teste4[-3:]
# print(testando4)  

# frase = 'programando em python'
# fatia = frase[-6]
# print(fatia)

# frase1 = 'programando em python'
# fatia1 = frase1[-6:]
# print(fatia1)

#split = usado para dividir uma string em palavras ou partes menores 
# frase = 'Nós vamos viajar, amanhã'
# print(frase.split()) # [nós, vamos, viajar, , amanhã]

# #strip = retira os espaços em branco no início e no fim
# frase1 = '   Nós vamos viajaremos neste fim de semana.  '
# print(frase1.strip())

# fraseando = ' Meu nome é Anady Carvalho e estudo Python'
# print('Anady' in fraseando) #True or False

# if 'Anady' in fraseando:
#   print('Anady está contida na variável Fraseando...')

#JOIN = Ela permite combinar elementos de uma lista em uma única string, utilizando um separador específico. 
palavras = ["bola", "casa", "carro"]
palavras_com_prefixo = "-".join(palavras)
print(palavras_com_prefixo)