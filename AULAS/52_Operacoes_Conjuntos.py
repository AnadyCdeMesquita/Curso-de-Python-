"""
OPERAÇÕES COM CONJUNTOS:
*UNIÃO = c1.union(C2)
*INTERSECÇÃO = c1.intersection(c2)
*DIFERENÇA = c1.difference(c2)
*DIFERNÇA SIMÉTRICA = c1.symmetric_difference(c2)
*SUBSET = c1.issubset(c2)
*SUPERSET = c1.issuperset(c2)

"""
#CRIANDO UM CONJUNTO
s1 = {1, 2, 3, 4}
s2 ={3, 4, 5, 6}
#União
união = s1.union(s2)
#print(união)
#intersecção
s1 = {1, 2, 3, 4}
s2 ={3, 4, 5, 6}

teste = s1 & s2
#OU
inter = s1.intersection(s2)
#print(inter)

#diferença = retorna os elementos que estão no primeiro conjunto, mas não no segundo.
s1 = {1, 2, 3, 4}
s2 ={3, 4, 5, 6}
diference = s1 - s2
#ou
diferenca = s1.difference(s2)
print(diferenca)

#DIFERENÇA SIMETRICA = Mostra os elementos que não são iguais entre um e outro conjunto
s1 = {1, 2, 3, 4}
s2 ={3, 4, 5, 6}
simetrica = s1 ^ s2
#ou
simetric = s1.symmetric_difference(s2)
#print(simetric) #1, 2, 5, 6

#issubset() =Subconjunto #VERIFICA SE O PRIMEIRO CONJUNTO É SUBCONJUNTO DO SEGUNDO
#Um conjunto A é subconjunto de um conjunto B se TODO elemento de A é também elemento de B.
#retorna falso ou true
s1 = {1, 2, 3, 4}
s2 ={3, 4, 5, 6}
s3 = {1,2}
sub = s1.issubset(s2)
#print(sub)

sub1 = s3.issubset(s1)
#print(sub1)


#issuperset()
#Um conjunto de A é considerado um superconjunto de B se A contiver *TODOS* os elementos de B.

s1 = {1, 2, 3, 4, 5, 6}
s2 ={3, 4, 5, 6}

super = s1.issuperset(s2)
#print(super)

