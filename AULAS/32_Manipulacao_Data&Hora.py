from datetime import datetime, timedelta
# dois datetimes diferente: a 1 é biblioteca a 2 é a função. Usou-se os dois nomes
#https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
#site com abreviatura ddas datas


hoje = datetime.now()
print(hoje)
#print(hoje.date()) # só a data de hoje
# print(hoje.year) #o restante sem parênteses
# print(hoje.month)
# print(hoje.day)
# print(hoje.hour)
# print(hoje.minute)
# print(hoje.microsecond)

#TIMEDELTA = SOMAR E SUBTRAIR DATAS
amanha = hoje + timedelta(days=10) # somar e subtrair datas
print(amanha)
data_contrato = datetime(year = 2024, month = 4, day = 1)
atraso = hoje - data_contrato
print(atraso.days)

#EXTRAIR DATAS EM OUTROS FORMATOS:

#strptime = pega um texto e transforma em data
#https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
#site com abreviatura ddas datas
datadocontrato = '01/09/2022' #pode ser barra ou traço
datadocontrato = datetime.strptime(datadocontrato,"%d/%m/%Y")
print(datadocontrato)

#DATA EM FORMATO BRASILEIRO
#strftime = pega um data e transforma em texto
hoje = datetime.now()
print(hoje.strftime("%d/%m/%Y"))
print(hoje.strftime("%A"))

#FUSO HORÁRIO
hoje = datetime.now()
hoje = hoje - timedelta(hours=1)

#FUSO HORÁRIO
import zoneinfo
zonas_nos_locais = zoneinfo.available_timezones()
# print(zonas_nos_locais)
zona = zoneinfo.ZoneInfo('Singapore')
agora_sinpapore = hoje.astimezone(zona)
print(agora_sinpapore
      )