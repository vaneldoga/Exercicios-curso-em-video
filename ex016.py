# Exercicio - Curso em vídeo - Exercício 016
# Função: ler um número real qualquer e exibir sua porção inteira

num = float(input('Digite um número real: '))

from math import trunc

print(f'O número {num} tem a parte inteira {trunc(num)}')