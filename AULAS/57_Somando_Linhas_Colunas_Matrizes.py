a= [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
soma = 0
# for linha in range(3):
#   for col in range(3):
#       print(a[linha][col], end = '  ')
#   print()
  
#SOMANDO COLUNA
for linha in range(3):
  soma += a[linha][2] #somando coluna
print(f'O resultado da coluna {soma}.')

soma1 = 0
#SOMANDO LINHA
for col in range(3):
  soma1 += a[2][col] #somando coluna
print(f'O resultado da linha é  {soma1}.')