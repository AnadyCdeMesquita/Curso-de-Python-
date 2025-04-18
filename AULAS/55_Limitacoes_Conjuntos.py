#Conjuntos não suportam indexação, fatiamento ou outras operações de sequencia:
#Não podem conter elementos duplicados

#1- SEM INDEXAÇÃO E SEM FATIAMENTO:
#CONJUNTOS NÃO SÃO SEQUENCIAS ORDENADAS, ENTÃO VC NÃO PODE ACESSAR OU MODIFICAR UM ELEMENTO DE UM CONJUNTO USANDO INDEXAÇÃO OU FATIAMENTO

conjunto = {1, 2, 3, 4}
#print(conjunto.index(2))
#print(conjunto[1:2])

#2 - Não permite duplicatas

conjunto2 = {1, 2, 2, 4, 5, 6, 6, 8, 10, 8}
#print(conjunto2) Não imprime repetidos

#3- Elementos dos Conjuntos São Imutáveis:
"""
ISSO SIGNIFICA  QUE VC NÃO PODE TER , POR EXEMPLO, LISTAS OU DICIONÁRISO COMO ELEMENTOS DE UM CONJUNTO,
POIS SÃO TIPOS MUTÁVEIS
"""
#exemplo = {[1,2,3], (1,2,3,4), 'socorreth', 1, 2}
#print(exemplo)
#exemplo2 = {{1,2,3}, {'anady', 'soph'}} #não suporta conjuntos também
#print(exemplo2)