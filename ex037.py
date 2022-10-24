# Exercicio - Curso em vídeo - Exercício 037
'''
    Função: Escreva um programa que leia um número ineiro 
    qualquer e peça para o usuário escolher qual será a base
    de conversão:

    - 1 para binário -> bin(x)
    - 2 para octal   -> oct(x)
    - 3 para hexadecimal -> hex(x)
'''

numero = int(input('Digite um número: '))

print(f'''
    Conversor de bases numéricas
    Escolha que conversão você deseja fazer:
    digite [1] para converter para binário
    digite [2] para converter para octal
    digite [3] para converter para hexadecimal
''')

escolha = int(input('Digite o número da conversão que você deseja realizar:'))
if escolha == 1:
    print(f'{numero} convertido para binário: {bin(numero)[2:]}')
elif escolha == 2:
    print(f'{numero} convertido para octal: {oct(numero)[2:]}')
elif escolha == 3:
    print(f'{numero} convertido para hexadecimal: {hex(numero)[2:]}')