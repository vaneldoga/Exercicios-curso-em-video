# Exercicio - Curso em vídeo - Exercício 024
'''
    Função: crie um programa que leia o nome de uma cidade
    e diga se ela começa ou não com o nome "SANTO"
'''

cidade = (input('Digite o nome da sua cidade: '))
cidadeup = cidade.upper()
print(cidadeup)
print('Sua cidade começa com a palavra "Santo"? -> ',end='')
print('SANTO' in cidadeup.split()[0])