# Exercicio - Curso em vídeo - Exercício 034
'''
    Função: Escreva um programa que pergunte o salário de um funcionário
    e calcule o valor do seu aumento

    Para salários superiores a R$1.250,00, calcule um aumento de 10%

    Para os inferiores ou iguais, o aumento é de 15%
'''

salario = float(input('Qual o valor do salário? R$'))

if salario > 1250:
    aumento = salario * 0.1
    salario = salario + aumento
    print(f'O valor do aumento será de R${aumento} reais\nNovo salário: R${salario}')
else:
    aumento = salario * 0.15
    salario = salario + aumento
    print(f'O valor do aumento será de R${aumento} reais\nNovo salário: R${salario}')