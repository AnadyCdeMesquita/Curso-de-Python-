"""
MATRIZES: Inicializando as duas matrizes e a matriz resultado.
USANDO O LOOP FOR ANINHADOS PARA SUBTRAIR ELEMENTOS CORRESPONDENTES.
A subtração de matrizes, elas devem ter as mesmas dimensões.
O resultado é uma nova matriz com a mesma dimensao, onde cada elemento é a 
diferença dos elementos correspondentes das duas matrizes originais.

"""

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#print(A)

# for linha in A:
#     for elemento in linha:
#       print(elemento, end=" ")
#     print()

for linha in range(3):
  for coluna in range(3):
    print(f'{A[linha][coluna]}', end = '  ')
  print()
  
B = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
#print(B)
for linha1 in range(3):
  for coluna1 in range(3):
    print(f"{B[linha1][coluna1]}", end = "  ")
  print()
  
  #SUBTRÇÃO DE MATRIZES
D = [[0, 0,0 ], [0, 0, 0], [0, 0, 0]]

for linha3 in range(3):
  for coluna3 in range(3):
    D[linha3][coluna3] = B[linha1][coluna1] - A[coluna][linha] 

for linha in D:
  print(linha)

#ADICAO DE MATRIZES

D = [[0, 0,0 ], [0, 0, 0], [0, 0, 0]]

for linha in range(3):
  for coluna in range(3):
    D[linha][coluna] =  A[linha][coluna] + B[linha][coluna]
    print(f'{D[linha][coluna]}', end = ' ')
  print()
  
soma_diagonal = 0
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(3):
  soma_diagonal += A[i][i]
print(f'O resultado é {soma_diagonal}')