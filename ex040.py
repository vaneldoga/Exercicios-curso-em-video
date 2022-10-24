# Exercicio - Curso em vídeo - Exercício 039
'''
    Função: Crie um programa que leia duas notas de um aluno e calcule sua méida,
    mostrando uma mensagem no final, de acordo com a média atingida:

    - Média abaixo de 5.0: REPROVADO
    - Média entre 5.0 e 6.9: RECUPERAÇÃO
    - Média 7.0 ou superior: APROVADO
'''

nota1 = float(input('Informe a nota da primeira avaliação: '))
nota2 = float(input('Informe a nota da segunda avaliação: '))
media = (nota1+nota2) / 2

if media < 5:
    print('REPROVADO')
elif 5.0 <= media <= 6.9: 
    print('RECUPERAÇÃO')
elif media >= 7:
    print('APROVADO')