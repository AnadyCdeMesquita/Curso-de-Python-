#setdefault()
#Retorna o valor da chave especificada. Se a chave não existir, insere a chave com um valor
#especificado (ou padrão se nenhum valor fornecido).
produto = {
  'id': 12345,
  'nome':'Camisa Gola Polo',
  'cor': 'Vermelho',
  'preco': 49.90,
  'estoque': 100  
}
produto['nome'] = 'saia'
teste = produto.setdefault('cor', 'azul')
testando = produto.setdefault("age", None)
testando = produto.setdefault("ano", 1990)
# print(teste)
# print(produto)
# print(testando)

#clear()

#fromkeys()
#O método fromkeys() do Python cria um dicionário com chaves especificadas e um valor padrão para todas elas. 
# É uma forma eficiente de inicializar um dicionário a partir de uma lista de chaves. 

# chaves = ['titulo', 'autor', 'sinopse']

# novo_livro = dict.fromkeys(chaves, 'desconhecido')
# print(novo_livro)

# racas = {'yorkshare', 'pitbull', 'pastor alemao'}
# idades = dict.fromkeys(racas, 'sem idade')
# print(idades)


#EXERCICIOS:
filme = {'titulo': 'Inception',
  'diretor': 'Cristhoper Nelon',
  'ano': 2010,
  'genero': 'Ficção Científica'}

# for k in filme.keys():
#   # print(k)
  
# for v in filme.values():
#   # print(v)
  
# for k, v in filme.items():
#   # print(k, v)
#UTILIZANDO O CLEAR
# novo_filme = filme.copy()
# print(novo_filme)
# novo_filme.clear()
# print(novo_filme)

#SETDEFAULT():
filme = {'titulo': 'Inception',
  'diretor': 'Cristhoper Nelon',
  'ano': 2010,
  'genero': 'Ficção Científica'}

filme.setdefault('elenco', ['Leonardo de Caprio', 'Ellen Page'])
print(filme)

#UPDATE()

filme.update({'duracao': '148 minutos'})
filme.update({'idioma': 'inglês'})
print(filme)

#FROMKEYS

chaves = ['nome', 'idade', 'ocupação']
novo_dic = dict.fromkeys(chaves, 'dados desconhecidos')
print(novo_dic)