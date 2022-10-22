# Exercicio - Curso em vídeo - Exercício 019
# Função: ler 4 nomes, sortear um desses 4 e exibir o escolhido

aluno1 = str(input('Nome do primeiro aluno: '))
aluno2 = str(input('Nome do segundo aluno: '))
aluno3 = str(input('Nome do terceiro aluno: '))
aluno4 = str(input('Nome do quarto aluno: '))

aluno = [aluno1, aluno2, aluno3, aluno4]

from random import choice

print(f'O aluno escolhido foi: {choice(aluno)}')