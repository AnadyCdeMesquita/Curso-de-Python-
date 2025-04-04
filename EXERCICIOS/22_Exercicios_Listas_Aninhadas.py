matriz = [[1,2,3],[4,5,6],[7,8,9]]
# # print(matriz[1][2])
# soma = 0
# soma1 = 0
# soma2 = 0
# for v in matriz:
#   print(v)
#   soma += v[0] 
#   soma1 += v[1]
#   soma2 += v[2]
#   total = soma + soma1 + soma2
 
#print(total)
# # print(matriz[1][2])
# # print(matriz[1][2])
matriz = [[1,2,3],[4,5,6],[7,8,9]]
soma = 0
for linha in matriz:
  for numero in linha: 
    soma += numero
    
print(soma)

for linha in matriz:
  for numero in linha:
    print(numero, end=' \t')

