"""
OUTRAS FUNÇÕES E MÉTODOS:
len(): Retorna o número de elementos no conjunto
in : verifica a existência de um elemento no conjunto
copy()retorna uma cópia do conjunto
"""

frutas = {'maca', 'banana', 'laranja', 'uva', 'manga'}

#len()
frutas = {'maca', 'banana', 'laranja', 'uva', 'manga'}
numero_frutas = len(frutas)
print(numero_frutas)

#in = verificar se um elemento específico está no conjunto

frutas = {'maca', 'banana', 'laranja', 'uva', 'manga'}
frutas_desejadas = 'maçã'

if frutas_desejadas in frutas:
  print(f'A frutas desejada é: {frutas_desejadas}.')
else:
  print(f"Não há frutas desejadas.")
  
  #copy()
  novo_conjunto = frutas.copy()
  print(novo_conjunto)
  
#verificandi se os conjuntos são realmente diferentes em memória:
print(frutas is novo_conjunto)
  



