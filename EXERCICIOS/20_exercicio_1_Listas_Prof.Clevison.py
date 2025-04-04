"""
EXERCICIO 1
animais = []
animais.append('gato')
animais.append("cachorro")  
animais.append('pássaro')
print(animais)
animais.insert(2, 'peixes')
print(animais)
animais.pop()
animal_removido = 'passaro'

novos_animais = ['tartaruga', 'hamster']
todos_animais = animais + novos_animais
#print(todos_animais)
animais_duplicados = ['gato', 'cachorro', 'peixes', 'tartaruga', 'hamster'] *2
print(animais_duplicados)
if 'cachorro' in animais_duplicados:
  print("O cachorro está na lista.")
else:
  print("O cacchorro não está na lista.")
  """
  
#EXERCICIO 2
numeros = [23, 11, 89, 34, 11, 56, 78, 90, 23, 45]
numeros.sort()
print(numeros)
numeros.sort(reverse=True)
print(numeros)
numeros.reverse()
print(numeros)

teste = numeros.count(11)
print(teste)
testando = numeros.index(78)
print(testando)
print(len(numeros) + 1)

# if 100 in numeros:
#   print("Esse numero existe")
# else:
#   print("Esse index não existe")

# try:
#   indice_existe = numeros.index(78)
# except ValueError:
#   print('Esse valor não existe...')
# else:
#   print('Esse valor existe...')
# finally:
#   print('Volte sempre!!!!')
    
 