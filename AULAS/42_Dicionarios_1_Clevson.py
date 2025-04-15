#DICIONARIOS ANINHADOS: um dicionário pode conter outro dicionario
#(outros tipos de coleções como listas) como um valor. Isso é referido
#como um dicionário aninhado.
#exemplo de dicionario com subdicionários
familia ={
  #subdicionarios pai, mae e filho
  'pai':{
    'nome': 'Rodrigo Carvalho', #nome = chave , valor = Rodrigo
    'idade': 48
  },
  'mae':{
    'nome': 'Renata Grangeiro',
    'idade': 40  
  },
  'filho':{
    'nome':'Italo Grangeiro',
    'idade': 13
  }
  
}

# print(len(familia))
# print(familia['pai'])
# print(familia['pai']['nome'])

#exercicio
animal = {
  'tipo':'gato',
  'cor': 'branco',
  'idade': 3
}
# DICIONARIO VAZIO
estudante = {}
estudante = dict()

estudante ={
  'título': 'Carlos',
  'curso': 'Matemática',
  'semestre': 2  
}

#DICIONARIOS COM MÚLTIPLOS ITENS:
livro ={
  'titulo': 'A arte da guerra',
  'autor': 'Sun Tzu',
  'publicado': 500  
}

#DICIONARIO ANINHADO:
campus={
  'nome': 'Universidade Federal Fluminense',
  'localidade': {'Cidade':'Rio de Janeiro','Bairro': 'Centro'}

  
}

#print(campus)
#print(len(campus))
print(campus['nome'])
print(campus['localidade']['Cidade'])

#Acessando itens do dicionário de forma prática:
smarthphone = {
  'marca': 'Apple',
  'cor': 'azul',
  'capacidade':'128GB',
  'sistema': 'iOs' 
}

#MÉTODO DIRETO e MÉTODO GET
print(smarthphone['marca'])

print(smarthphone.get('marca'))
#SE TENTARMOS ACESSAR UMA CHAVE QUE NÃOE EXISTE,A RESPOSTA É UM KEYERROR

if 'sistema' in smarthphone:
  print('Sistema existe')
else:
  print("não existe")
  
sistemas = 'sistema' in smarthphone
#print(sistemas) #retorna false ou True

#for c in smarthphone:
  #print(c)
  #imprime só as chaves
smarthphone = {
  'marca': 'Apple',
  'cor': 'azul',
  'capacidade':'128GB',
  'sistema': 'iOs' 
}
for chaves in smarthphone.values():
  print(chaves)

smarthphone = {
  'marca': 'Apple',
  'cor': 'azul',
  'capacidade':'128GB',
  'sistema': 'iOs' 
} 
for valor in smarthphone.values():
  print(valor)
  
for c, v in smarthphone.items():
  print(f'{c}: {v}')
  
#EXERCICIO:

artista = {
  'nome': 'Ludwing bethoveen',
  'nascimento': 1770,
  'falecimento': 1827,
  'nacionalidade': 'Alemã',
  'estilo': 'Clássico'  
}

print(artista.get('nome'))
print(artista['nome'])
if 'estilo' in artista:
  print('O estilo musical é o:', artista['estilo'],'.')
else:
  print("Não possui estilo musical")
  