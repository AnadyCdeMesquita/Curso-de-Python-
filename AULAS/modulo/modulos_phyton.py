# import uteis

# n = int(input("Digite um numero:  "))
# fat = uteis.fatorial(n)
# print(f'O fatorial de {n} é {fat}')
# dobrado = uteis.dobro(n)
# print(f'O dobro é {dobrado}')
# triplicado = uteis.triplo(n)
# print(f'O triplo é {triplicado}')

# OU

from uteis import fatorial, dobro, triplo
# não é muito indicada pelo python

n = int(input("Digite um numero:  "))
fat = fatorial(n)
print(f'O fatorial de {n} é {fat}')
dobrado = dobro(n)
print(f'O dobro é {dobrado}')
triplicado = triplo(n)
print(f'O triplo é {triplicado}')