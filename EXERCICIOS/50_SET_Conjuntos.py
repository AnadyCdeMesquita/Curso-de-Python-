#CONJUNTOS = É uma coleçao desordenada de elementos únicos. Isso significa que não permite duplicatas.
#São mutáveis, mas os elementos contidos neles devem ser imutáveis (por exemplo, números, strings e tuplas)

#1-OBS: AS LISTAS NÃO SÃO ADICIONADAS A CONJUNTOS, SOMENTE NO CASO ABAIXO PARA EVITAR DUPLICATAS.
lista = [1,1, 2, 3, 3, 5, 5, 10, 10, 15, 15]
conjunto = set(lista)
#print(conjunto)

#2-CRIANDO CONJUNTO DE ELEMENTOS IMUTÁVEIS:
conjunto1 = {1, 2, 'Neves', ('a', 'b')}
#print(conjunto1)
# Quando se imprime um conjunto, não  garante necessariamente a ordem.

#3-NÃO PODEMOS ADICIONAR LISTAS E DICIONÁRIOS A CONJUNTOS. OS ELEMENTOS DENTRO DE  CONJUNTS DEVEM
#SER IMUTÁVEIS.
lista = [1, 2, 3, 4, 5, 5, 10, 15]
conjunto2 = set()
#conjunto3 = conjunto2.add(lista)
#print(conjunto3)

#EXERCICIOS

frutas_chaves = {'maçã', 'manga', 'banana', 'cereja'}
print(frutas_chaves)
print(type(frutas_chaves))

frutas_lista = set(['uva', 'manga', 'manga', 'cereja'])
print(frutas_chaves == frutas_lista)

intersecao = frutas_chaves.intersection(frutas_lista)
print(intersecao)

if intersecao:
  print(f'As frutas em comum são {intersecao}')
else:
  print(f"Não existe frutas em comum")