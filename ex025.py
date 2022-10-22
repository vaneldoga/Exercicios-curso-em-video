# Exercicio - Curso em vídeo - Exercício 025
'''
    Função: Crie um programa que leia o nome de uma pessoa
    e diga se ela tem "SILVA" no nome
'''

nome = input('Qual o seu nome? ')
nomeup = nome.upper()

print('Você tem "Silva" no nome? -> ', end='')
print("SILVA" in nomeup)