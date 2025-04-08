vendas = (101, 102, 103, 101, 104,105, 101, 102, 102, 101)
indexador = vendas.index(101) + 1
# print(indexador)
contador = vendas.count(101)
# print(contador)

#EXERCICIOS
avaliacoes = (5, 4, 4, 3, 5, 2, 4, 3, 5, 5, 1, 4, 3, 5, 2)

estrelas = avaliacoes.count(5)
estrela_1 = avaliacoes.count(1)
estrela_pont1 = avaliacoes.index(1)

print(f'O filme foi avaliado com 5 estrelas {estrelas} vezes.')
print(f"O filme foi avaliado com 1 estrela {estrela_1} vezes, posição {estrela_pont1 + 1}.")