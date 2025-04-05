#LIST () USANDO A FUNÇÃO LIST() EM UMA STRING , CADA CARACTERE DE UMA STRING,
#SERÁ UM ELEMENTO DE UMA LISTA

# palavra = 'anady'
# testando = list(palavra)
# print(testando)
# print(len(testando))


#SPLIT = CONVERSÃO DE FRASES PARA LISTAS.
# frase = 'Anady Carvalho de Mesquita'
# testando1 = frase.split()
# print(f'Sra. {testando1[-1]}, {testando1[0]}, {len(testando1)}')

# data = '11/05/2025'
# datando = data.split('/')
# print(datando)

#JOIN = CONNVERSÃO DE LISTA PARA STRINGS
# lista = ['python', 'é', 'incrivel']
# testando3 = ' '.join(lista)
# print(testando3)

# data1 = ['11','05','1980']
# datando1 = '/'.join(data1)
# print(datando1)

#exercicios

# palavras1 = 'python'
# listando = list(palavras1)
# print(listando)

# fraseando = 'Aprendendo python é divertido'
# frase2 = fraseando.split()
# print(frase2)

# data_aniversario = '20/12/60'
# nando = data_aniversario.split('/')
# print(nando)

# banana_split = list(map(int, input("Qual o número: \n").split()))
# print(banana_split)
# print(type(banana_split))

frutas=['banana', 'maca', 'pera', 'laranja']
frutass = ' , '.join(frutas)
print(frutass)