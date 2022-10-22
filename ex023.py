# Exercicio - Curso em vídeo - Exercício 023
'''
    função:
    fazer um programa que leia um número de 0 a 9999
    e mostre na tela cada um dos dígitos separados
    ex:
    digite um número: 1834

    unidade: 4
    dezena: 3
    centena: 8
    milhar: 1
'''

num = int(input('Digite um número: '))
numstr = str(num)
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

print(f'''
    unidade: {unidade}
    dezena: {dezena}
    centena: {centena}
    milhar: {milhar}
''')
