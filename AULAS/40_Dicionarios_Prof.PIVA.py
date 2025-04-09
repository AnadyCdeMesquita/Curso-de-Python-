f1 = {1:'Mercedez', 2:'Ferrari', 3:'Renault'}
# print(f1)

#HÁ FUNÇÃO DICT()
#primeiro exemplo, usa-se função como argumento
numero = dict (um = 1, dois=2, tres = 3) 
#print(numero) {'um': 1, 'dois': 2, 'tres': 3}
#segundo exemplo, com iteráveis
numeros = dict([('anady', 45),('João', 22),('Pedro', 50)])
#print(numeros) {'anady': 45, 'João': 22, 'Pedro': 50}

dic = {'anady': 45, 'João': 22, 'Pedro': 50}
#print(dic['anady'])
dic['João'] = 35
# print(dic)

#FUNÇÕES BUILT-IN (len, all, any e sorted)
#lembrando que sorted retorna uma lista

presidentes ={'Getulio':1961 , 'Color': 1994, 'Lula': 2020, 'Dilma':2024}
#print(len(presidentes)) {'anady': 45, 'João': 35, 'Pedro': 50}
print(sorted(presidentes))
print(sorted(presidentes, reverse=True))

#dic_logico = {0:True, 1:False, 3:True} #se somente uma for true
#print(any(dic_logico))True

# dic2 = {0:True, 1:True, 3:True}
# print(all(dic2))

#MÉTODOS DE UM DICIONÁRIO:
#1 - dic.clear = APAGA O DICIONARIO
# presidentes ={'Getulio':1961 , 'Color': 1994, 'Lula': 2020, 'Dilma':2024}
# presidentes.clear()
# print(presidentes)

#2 - .dic.fromkeys() = cria um dicionário a partir da sequencia dos elementos com um valor informado
presidentes ={'Getulio':1961 , 'Color': 1994, 'Lula': 2020, 'Dilma':2024}
# novo_presidente = presidentes.fromkeys(presidentes)
# print(novo_presidente)
# novo_presidente = presidentes.fromkeys(presidentes, 2013)
# print(novo_presidente)

# 3 - dic.get() = RETORNA O VALOR ASSOCIADO À CHAVE ESPECIFICADA NO DICIONÁRIO. SE A CHAVE NÃO ESTIVER PRESENTE
#ELA RETORNARÁ O VALOR PADRÃO. SE PADRÃO NÃO FOR FORNECIDO, O PADRÃO SERÁ NONE, PARA QUE ESSE
#MÉTODO NUNCA GERE UM KEYERROR.

# presidentes ={'Getulio':1961 , 'Color': 1994, 'Lula': 2020, 'Dilma':2024}
# novo_presidente = (presidentes.get('Bostanaro'))
# print(novo_presidente)

# 4 - .dic.items() = RETORNA UMA NOVA VISÃO DOS PARES DE CHAVE E VALOR DO DICIONÁRIO COMO TUPLAS:

presidentes ={'Getulio':1961 , 'Color': 1994, 'Lula': 2020, 'Dilma':2024}
novo_presidente = (presidentes.items())
print(novo_presidente)

for k, v in presidentes.items():
  print(k, v)
  
#5- dic.values() = RETORNA OS VALORES DOS DICIONÁRIOS
presidentes ={'Getulio':1961 , 'Color': 1994, 'Lula': 2020, 'Dilma':2024}
print(presidentes.values())
for v in presidentes.values():
  print(v)
  
#6- dic.keys() = RETORNA OS VALORES DOS DICIONÁRIOS
# presidentes ={'Getulio':1961 , 'Color': 1994, 'Lula': 2020, 'Dilma':2024}
# novato = presidentes.keys()
# print(novato)
# for k in presidentes.keys() :
#   print(f'Presidente: {k}')

#7- dic.update() =Método insere os itens especificados no dicionário.
# presidentes ={'Getulio':1961 , 'Color': 1994, 'Lula': 2020, 'Dilma':2024}
# presidentes.update({'FHC': 1990})
# print(presidentes)

#8 - setdefault() = método retorna o valor do item com a chave especificada.
presidentes ={'Getulio':1961 , 'Color': 1994, 'Lula': 2020, 'Dilma':2024}

x= presidentes.setdefault('hermes da fonseca', 1985)
print(x)
print(presidentes)

# 9 - pop() - Remove a chave que vc especificar
presidentes ={'Getulio':1961 , 'Color': 1994, 'Lula': 2020, 'Dilma':2024}
presidentes.pop('Getulio')
print(presidentes)

# 10 - popitem() - Remove a última chave 
presidentes ={'Getulio':1961 , 'Color': 1994, 'Lula': 2020, 'Dilma':2024}
presidentes.popitem()
print(presidentes)


