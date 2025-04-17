#EXERCICIO 1:

numeros = [10, 20, 30, 10, 40, 20]
print(set(numeros))

#EXERCICIO 2

try:
  conjunto = {[10, 20, 30, 10, 40, 20]}
except (ValueError, TypeError):
  print('Há um erro')
finally:
  print('Volte sempre, muito obrigada(o)')
  
#EXERCICIO 3

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

união = a.union(b)
print(união)
inter = a.intersection(b) #&
print(inter)
diferenca = a.difference(b) # 
print(diferenca)
simetria =a.symmetric_difference(b)
print(simetria)