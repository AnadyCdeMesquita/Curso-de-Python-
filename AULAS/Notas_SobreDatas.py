#import datetime # para importar toda a biblioteca
# import datetime as dt # substituindo o nome datetime por dt dentro do código
# from datetime import date # quando se quer apenas 1 dos submódulos

from datetime import date
# ano_atual = date.today().year
# data = date(2025,3,6)
# print(data)
# print(data.ctime())
# ano = data.year
# mes = data.month
# dia = data.day
# print(dia, mes, ano)
# #ALTERANDO UMA INFORMAÇÃO
# nova_data = data.replace(year=2022) #day #month
# print(nova_data)
# print(data)
import datetime
hoje = datetime.date.today()
print(hoje)

