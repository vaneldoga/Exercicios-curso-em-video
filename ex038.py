# Exercicio - Curso em vídeo - Exercício 038
'''
    Função: Escreva um programa que leia dois números inteiros
    e compare-os, mostrando na tela uma mensagem.

    - O primeiro valor é MAIOR
    - O segundo valor é MAIORR
    - Não existe valor maior, os dois são iguais.
'''

a = int(input('Digite um número inteiro: '))
b = int(input('Digite outro número inteiro: '))

if a>b:
    print(f'{a} é o maior valor')
elif b>a:
    print(f'{b} é o maior valor')
elif a==b:
    print('Não existe valor maior, os dois são iguais')