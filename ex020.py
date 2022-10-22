# Exercicio - Curso em vídeo - Exercício 020
# Função: ler 4 nomes, e exibir a ordem de apresentação sorteada

aluno1 = str(input('Nome do primeiro aluno: '))
aluno2 = str(input('Nome do segundo aluno: '))
aluno3 = str(input('Nome do terceiro aluno: '))
aluno4 = str(input('Nome do quarto aluno: '))

aluno = [aluno1, aluno2, aluno3, aluno4]

from random import shuffle
shuffle(aluno)
print('A ordem de apresentação será:')
print(aluno)