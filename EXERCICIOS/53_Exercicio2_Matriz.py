alunos_lista = []
for i in range(3):
  nome = input(f'Digite o nome do {i+1} aluno? \n')
  nota_aluno = []
  for j in range(4):
    notas = float(input(f"Digite a {j +1} nota do aluno {nome}: \n"))
    nota_aluno.append(notas)
  
alunos_lista.append([nome],  nota_aluno)

for aluno in alunos_lista:
  nome = aluno[0]
  nota_aluno = aluno[1:]
  media = sum(nota_aluno)/4
  print('--------------------------------------------')
print(f'Nome: {nome}')
print(f'Nota: {nota_aluno}')
print(f'media: {media}')