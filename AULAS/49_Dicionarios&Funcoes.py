# usuario = {
#   'nome': 'Anady Carvalho',
#   'idade': 25,
#    'email': 'anady@email.com'
  
# }

# def funcoes_dicts(perfil):
#   for c, v in perfil.items():
#     print(f'{c}: {v}')
    
# funcoes_dicts(usuario)

# #RETORNA DICIONARIOS DE FUNCOES:

# def criar_perfil(nome, idade, email):
#   return {
#     'nome': nome,
#     "idade": idade,
#     "email": email
#     }
  
# testando = criar_perfil('Anady', 45, 'anadygeo@gmail.com')

#REGISTRO DE UM LIVRO:

def novo_livro(titulo, autor, ano):
  return {
    "título": titulo,
    "auto": autor,
    "ano": ano,
  }
  
nova = novo_livro('O Diário de Anne Frank', 'Otto Von Bismark', 1939)
print(nova)

##_______________________######

#NOVA FUNCAO
dados ={
    "título": 'O Diario de Anne Frank',
    "auto": 'Otton Von Bismark',
    "ano": 1939
  }

def novo_livro2(perfil):
  for c, v in perfil.items():
    print(f'{c}: {v}')
    
novo_livro2(dados)
  




