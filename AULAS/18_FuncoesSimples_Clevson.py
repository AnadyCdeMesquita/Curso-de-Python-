
# def soma (a, b):
#   return a +b

# res = soma(8, 5)
# print(res)

# def msg(nome):
#   print(f'Olá pessoa, meu nome é {nome}, um prazer conhecer vcs.')
  
# msg("Anady Carvalho")

# def informacoes(nome, idade, cidade = 'desconhecida'):
#   print(f'nome: {nome}')
#   print(f'idade: {idade}')
#   print(f'cidade: {cidade}')
  
# informacoes('anady', 45)
# informacoes('Fernando', 64, 'Fortaleza')

# def soma(*args):
#   res = sum(args)
#   return res

# total = soma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
# print(total)

# lista = []
# def estatística(*args):
#   n1 = lista.append(int(input('Digite o número 1: ')))
#   n2 = lista.append(int(input('Digite o número 2: ')))
#   n3 = lista.append(int(input('Digite o número 3: ')))
#   n4 = lista.append(int(input('Digite o número 4: ')))
#   media = sum(lista) / len(lista)
#   maior = max(lista)
#   menor = min(lista)
#   return f'A média será: {media}, o maior é: {maior} e o menor é: {menor}.'

# teste = estatística(lista)
# print(teste)

def teste(*args):
  media = sum(lista) / len(lista)
  maior = max(lista)
  menor = min(lista)
  return media, maior, menor

lista = list(map(int, input('Digite o número: \n').split()))
res = teste(lista)
print(res)
 
  
 
 






