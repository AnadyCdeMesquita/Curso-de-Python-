#OBS: AS COMPARAÇÕES ENTRE TUPLAS, LEVA EM CONSIDERAÇÃO SEMPRE O PRIMEIRO ELEMENTO.

t1 = (1,2)
t2 = (1,3)
#print(t1 > t2) #false
t1 = (1,2,3)
t2 = (1,2,4)
#print(t1 < t2) #true

t1 = (1,2)
t2 = (1,2,3)
#print(t1 < t2) #true

t1 = (1,6)
t2 = (1,2,3)
#print(t1 < t2) #true

t1 = (1, 'apple')
t2 = (2, 'Orange')  
#print(t1 < t2) #true, ler primeiro o inteiro

#EXERCICIO 1
t1 = (3,5)
t2 = (3, 4, 10)
t3 = (3, 6)
t4 = (2, 100)
t5 = (3, 5)
#Responda as seguintes questões:
print(t1 > t2) #true
print(t3 > t1) #true
print(t4 > t1) #false
print(t1 == t5)
