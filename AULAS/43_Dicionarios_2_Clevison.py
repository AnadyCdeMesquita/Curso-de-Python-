#adicionar chaves em dicionarios:
produto = {
  'id': 12345,
  'nome':'Camisa Gola Polo',
  'cor': 'Vermelho',
  'preco': 49.90,
  'estoque': 100  
}

#adicionando itens:
produto['marca'] = 'fashion brand'
produto["desconto"] = 10

#outra forma de adicionar produto:
produto.update({'fabricante': 'Faber Castell'})
#print(produto)
#atualizando:
produto["preco"] = 59.90
produto["desconto"] = 15

# print(produto)

# REMOVENDO ITENS - (del, pop(), popitem())
del produto["marca"]
#print(produto)
produto.pop('fabricante') #remove a chave que eu especificar
#print(produto)
produto.popitem() # remove o último item.
#print(produto)

#copiando dicionários (copy(), dict())
produto = {
  'id': 12345,
  'nome':'Camisa Gola Polo',
  'cor': 'Vermelho',
  'preco': 49.90,
  'estoque': 100  
}
produto2 = produto.copy()
#print(produto2)

produto3 = dict(produto)
#print(produto3)

#EXERCICIO
aluno = {
  'matricula': 'A12345',
  'nome': 'João Silva',
  'curso': 'Engenharia da Computação',
  'semestre': 5,
  'cr': 8.5 
}

aluno['hobbies'] = ['leitura', 'corrida', 'xadrez']
aluno['idade'] = 22
#print(aluno)

aluno['semestre'] = 6
aluno['cr'] = 8.7
#print(aluno)

del aluno['idade']
#print(aluno)
aluno.pop('hobbies')
#print(aluno)
aluno.popitem()
#print(aluno)

