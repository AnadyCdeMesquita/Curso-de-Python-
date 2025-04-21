A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15,16]]
soma1 = 0

for linha in range(4):
  for coluna in range(4):
    if A[linha][coluna] % 2 == 0:
      soma1 += A[linha][coluna]
print(f'O resultado é {soma1}')

