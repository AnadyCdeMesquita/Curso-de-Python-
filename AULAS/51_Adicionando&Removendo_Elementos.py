
"""
ADICIONANDO E REMOVENDO ALIMENTOS
add() - adiciona um elemento ao conjunto
remove() - Remove um elemento do conjunto. Gera um erro se o elemento não existir
discard () - Remove um elemento do conjunto se ele existir.
pop() - Remove e retorna um elemento do conjunto, como os sets são desor
denados, 
clear() - Remove todos os elementos do conjunto.

"""
#usando ADD
s= {1, 2, 3, 4}
s.add(10)
#print(s)
#s.add(3) - como já há o 3, não vai repetir na impressão, não aceita duplicados

#USANDO O REMOVE() - Remove um elemento, se o elemento não existir, GERA UM ERRO.
s.remove(10)

#s.remove(20)
#print(s)

#USANDO O DISCARD() - Remove um elemento, se o elemento não existir, NÃO GERA UM ERRO.
s.discard(25)
#print(s)

#USANDO O POP() - REMOVE ALEATORIAMENTE.

s.pop()
print(s)

#USANDO CLEAR() - REMOVE O SET

s.clear()
print(s)