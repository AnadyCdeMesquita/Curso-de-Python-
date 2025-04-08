#EXERCICIO 1
def analisar_produtos(vendas_A, vendas_B):
  total_vendido = vendas_A + vendas_B
  mais_vendido = 'A' if vendas_A > vendas_B else "B"
  return total_vendido, mais_vendido

total = analisar_produtos(100, 85)
print(total)

#SUPONHA QUE VC TENHA UMA LISTA DE VENDAS DE AMBOS OS PRODDUTOS EM PARES PARA ALGUNS DIAS,
#E VC QUER IMPRIMIR AS VENDAS DE CADA DIA.

vendas = [(100,90), (110,115), (105, 100)]
for vendas_a, vendas_b in vendas:
  print(f'Vendas A: {vendas_a}, vendas B: {vendas_b}')

#troca de valores  
vendas_a = 100
vendas_b = 85

vendas_a, vendas_b = vendas_b, vendas_a
print(vendas_a, vendas_b)

#EXERCICIO 2

def resumo_vendas(vendas_smartphone, vendas_smartwatch):
  if vendas_smartphone > vendas_smartwatch:
      print('A quantidade de venda de smartphones é maior.')
  else:
    print('A quantidade de vendas smartwatch é maior.')
  #vendastop = 'smartphone' if vendas_smartphone > smartwatch else smartwatch
  #return soma, vendastop
  soma = vendas_smartphone + vendas_smartwatch
  return soma 

resumao = resumo_vendas(100, 50)
print(f'A soma total de celulares vendidos {resumao}.')

#EXERCÍCIO 3
vendas_semana = [(70,65), (80,82), (90,88)]

for a, b in vendas_semana:
  print(f"A venda de Smartphone: {a} e a venda de SmartWatch: {b}")
  
vendas_semana = [(70,65), (80,82), (90,88)]
vendasA= 70
vendasB = 65
vendasA,vendasB  = vendasB, vendasA
print(vendasA, vendasB)

