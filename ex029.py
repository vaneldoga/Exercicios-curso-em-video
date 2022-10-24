# Exercicio - Curso em vídeo - Exercício 029
'''
    Função: Escreva um programa que leia a velocidade de um carro

    * Se ele ultrapassar 80km/h, mostre uma mensagem dizendo 
    que ele foi multado

    * A multa vai custar R$ 7,00 por cada Km acima do limite.
'''

velocidade = float(input('Informe a velocidade do carro em Km/h: '))

if velocidade <= 80:
    print('Você não foi multado.')
else:
    kmAcidaDoLimite = velocidade - 80
    multa = kmAcidaDoLimite * 7
    print(f'''
        Você ultrapassou o limite (80Km/h)
        Você deve pagar uma multa de R${multa:.2f}
    ''')