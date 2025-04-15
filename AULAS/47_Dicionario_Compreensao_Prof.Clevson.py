

"""
SINTAXE BÁSICA
{chave: valor for elemento in iteravel}
Agora respira que vamos entender cada ponto:

chave: será a chave de cada elemento do dicionário resultante.
valor: valor daquela chave.
elemento: é a unidade de iteração do iterável iterável (se for uma lista, por exemplo, elemento irá receber o valor iteração à iteração)
iteravel: conjunto de dados que estão sendo iterados (pode ser uma lista ou um set, por exemplo)

"""

#exemplo:
quadrado = {x: x**2 for x in range(1, 5)}
print(quadrado)

quadrado1 = dict()
for x in range(1, 5):
  quadrado1[x] = x**2
print(quadrado1)

#converter chaves em valores e valores em chaves
original = {'a': 1, 'b': 2, "c": 3}
inverso = { valor: chave for chave, valor in original.items()}
print(inverso)

inverso1 = dict()
for chave, valor in original.items():
  inverso1[valor] = chave
  
print(inverso1)

#filtrando itens em dicionários:

precos ={
  'laptop': 1000,
  'mouse': 25,
  'monitor': 200,
  'teclado': 30,
  'hdmi': 10 
}
#formula normal
caros1 = { c: v for c, v in precos.items() if v > 50 }
print(caros1)

#tradicional
caros = {}
for c, v in precos.items():
  if v > 50:
    caros[c] = v
print(caros)
  
palavras = {'python', 'dicionarios', 'compreensao'}
palavras1 = {palavra: len(palavra) for palavra in palavras} 
print(palavras1)
palavras2 = {}
for palavra in palavras:
  palavras2[palavra] = len(palavra)

print(palavras2)

#EXERCICIOS

numeros = {1, 2, 3, 4, 5}
novo_numero = {x: x**2 for x in numeros}
print(novo_numero)

novo_numero1 = {}
for numero in numeros:
  novo_numero1[numero] = numero**2

print(novo_numero1)


