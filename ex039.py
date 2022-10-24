# Exercicio - Curso em vídeo - Exercício 039
'''
    Função: Faça um programa que leia o ano de nascimento 
    de um jovem e informe, de acordo com sua idade:

    - Se ele ainda vai se alistar ao serviço militar
    - Se é a hora de se alistar
    - Se já passou do tempo do alistamento

    Seu programa também deverá mostrar o tempo que falta ou
    que passou do prazo
'''

anonasc = int(input('Qual o ano do seu nascimento? '))

from datetime import date       # Pegar o ano atual.
anoatual = date.today().year
idade = anoatual - anonasc

if idade < 18:
    print(f'Você ainda vai se alistar ao serviÇo militar.\nFaltam {18-idade} anos para você se alistar\nVocê deve se alistar em {anoatual+(18-idade)}')
elif idade == 18:
    print(f'Você deve completar o alistamento militar esse ano.')
elif idade > 18:
    print(f'Quem nasceu em {anonasc} tem {idade} anos\nVocê já passou do prazo para se alistar ao serviço militar.\n{idade-18} anos se passaram do prazo\nVocê se alistou em {anoatual-(idade-18)}')