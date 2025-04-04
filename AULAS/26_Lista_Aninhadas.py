matriz = [[1,2,3], [4,5,6],[7,8,9]]
# print(matriz[0][1]) # 0
#UTILIZANDO LOOPS ANINHADOS PARA ITERAR:
#PARA ITERAR SOBRE CADA  ELEMENTO DA MATRIZ, USAMOS LOOPS FOR ANINHADOS:
#LOOP EXTERNO: ITERA SOBRE CADA LINHA DA MATRIZ

for linha in matriz:
  
  for coluna in matriz:
    print(coluna)
  
print()

#vamos supor que queremos calcular a transposta dessa matriz:
#A transposta de uma matriz é obtida trocando suas linhas por colunas


matriz = [[1,2,3],[4,5,6],[7,8,9]]
# transposta = []
# for coluna in range(len(matriz[0])):#loop através de cada coluna da matriz original
#   linha_temporaria = []
#   for linha in range(len(matriz)): #loop através de cada linha da matriz original
#     linha_temporaria.append(matriz[coluna][linha])
#     #adiciona o elemento da posicao coluna, linha, transposto a linha temporária
    
#   transposta.append(linha_temporaria)
# print(transposta, end = '')
    
  