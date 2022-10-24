# Exercicio - Curso em vídeo - Exercício 032
'''
    Função: Faça um programa que leia um ano qualquer 
    e mostre se ele é BISSEXTO
'''

ano = int(input('Informe um ano: '))

if ano % 4 == 0:
    print(f'O ano {ano} é Bissexto')
else:
    print(f'O ano {ano} não é Bissexto')