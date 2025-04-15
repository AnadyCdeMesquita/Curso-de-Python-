#DICIONÁRIOS ANINHADOS

alunos = {
  'João': {
    'matematica' : 8.5,
    'portugues': 9.0,
    'historia': 7.5
  },
  
  'Maria': {
    'matematica' : 9.5,
    'portugues': 8.0,
    'historia': 8.7
  },
  'Pedro': {
    'matematica' : 7.0,
    'portugues': 7.5,
    'historia': 8.0,
    'geografia': 9.0
  },
    
}

#ACESSANDO A NOTA
#print(alunos['João']['matematica'])
#OU
nota_joao = alunos['João']['matematica']
#print(nota_joao)

#MODIFICANDO/ INCLUINDO A NOTA

nota_maria = alunos['Maria']['geografia'] = 9.8
#print(nota_maria)

#acessar
teste = alunos.get('João')
#print(teste)

nota_pedro = alunos['Pedro']['geografia'] = 5.5
#print(alunos)

estacionamento ={
  'A1': {
    'marca':'Toyota',
    'modelo': 'Corolla',
    'dono': 'Sr. Silva'
    },
  'B2': {
    'marca':'Honda',
    'modelo': 'Civic',
    'dono': 'Dona Maria'
    },
  'C3': {
    'marca':'Ford',
    'modelo': 'Mustang',
    'dono': 'Sr. Jorge'
    }
  
}
#CRIANDO UMA NOVA CHAVE
estacionamento['D4'] ={
  'marca':'Chevrolet',
  'modelo': 'Onix',
  'dono': 'Sr. Roberto'
  
  
}

print(estacionamento.get('D4'))
