# Exercicio - Curso em vídeo - Exercício 018
# Função: ler um ângulo qualquer e exibir o valor do seno, cosseno e tangente desse ângulo

ang = int(input('Informe o valor de um ângulo: '))

from math import radians, sin, cos, tan

print(f'Seno de {ang}°: {sin(radians(ang)):.2f}\nCosseno de {ang}°: {cos(radians(ang)):.2f}\nTangente de {ang}°: {tan(radians(ang)):.2f}')
