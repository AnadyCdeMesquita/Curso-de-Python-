"""
Os conjuntos (set) em Python exigem que seus elementos sejam imutáveis.
Isso significa que vc pode ter uma string, int, float ou tuple como elemento de um
conjunto, mas não pode ter tipos mutáveis, como list ou outro set.
"""
#conjunt_invalido = {0, 1, 'texto', (0,2,), [5,2,10]} 
#print(conjunt_invalido) - gerará um erro pq não aceita lista

#FROZENSET: É UMA VERSÃO IMUTÁVEL DE UM CONJUNTO EM PYTHON. UMA VEZ QUE 
#VC CRIA FROZENSET, NÃO PODE MAIS ADICIONAR OU REMOVER ELEMENTOS DELE.

#A PRINCIPAL UTILIDADE DE UM FROZENSET É QUE ELE PODE SER USADO COMO ELEMENTO DE OUTRO CONJUNTO, DEVIDO À SUA IMUTABILIDADE.
frozen = frozenset([1, 2, 3])
conjunto_contendo_frozenset = {frozenset([1, 2, 3]), frozenset([4, 5, 6])}

print(frozen)
print(conjunto_contendo_frozenset)

f1 =frozenset([1, 2, 3])
f2 =frozenset([4,5,6])
f3 ={f1, f2}
print(f3)