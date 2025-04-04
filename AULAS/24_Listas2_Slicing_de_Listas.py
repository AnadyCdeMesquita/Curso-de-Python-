"""
SLICING = É UMA MANEIRA PODEROSA DE ACESSAR SUBCONJUNTOS DE LISTAS:
[inicio:fim:pass]
"""
minha_lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
subconjunto = minha_lista[1:4] #excliu o último índice, inclui o primeiro -> 1,2,3
primeiros_elementos = minha_lista[:4] # vai até o 3 -> 0, 1, 2, 3
ultimo_elementos = minha_lista[2:] # do índice 2 até o final
print(primeiros_elementos)
testando = minha_lista[4]
testando2 = minha_lista[5]
print(testando, testando2)
testando3 = minha_lista[::3] # pega do início ao fim com passo 3
print(testando3)
testando4 = minha_lista[2:8:2]
print(testando4)

