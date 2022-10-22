# Exercicio - Curso em vídeo - Exercício 022

'''
    função:
    Criar um programa que leia o nome completo de uma pessoa e mostre:
    * O nome com todas as letras maiúsculas
    * O nome com todas as letras minúsculas
    * Quantas letras ao todo (sem considerar os espaços)
    * Quantas letras tem o primeiro nome
'''

nome = input('Qual o seu nome? ')

nomeMai = nome.upper()
nomeMin = nome.lower()
listaNome = nome.split()
listaNome = ''.join(listaNome)
quant_total = len(listaNome)
quant_Pnome = len(nome.split()[0])

print('_'*20)
print(f'Seu nome com todas as letras maiúsculas: \n{nomeMai}')
print(f'Seu nome com todas as letras minúsculas: \n{nomeMin}')
print(f'Seu nome completo possui {quant_total} caracteres')
print(f'Seu primeiro nome possui {quant_Pnome} caracteres')