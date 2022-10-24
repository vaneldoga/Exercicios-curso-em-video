# Exercicio - Curso em vídeo - Exercício 035
'''
    Função: Desenvolva um programa que leia o comprimento de três
    retas e diga se elas podem ou não formar um triângulo

    V1.0

    Para que os três segmentos formem um triângulo, existe o que
    conhecemos como condição de existência, que é a seguinte: a soma
    de dois lados é sempre menor que o terceiro lado.
'''

r1 = float(input('informe o comprimento da primeira reta: '))
r2 = float(input('informe o comprimento da segunda reta: '))
r3 = float(input('informe o comprimento da terceira reta: '))

if r1+r2 > r3 and r2+r3 > r1 and r1+r3 > r2:
    print('Essas retas podem formar um triângulo.')
else:
    print('Essas retas não podem formar um triângulo.')