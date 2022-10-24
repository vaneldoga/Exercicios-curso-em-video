# Exercicio - Curso em vídeo - Exercício 031
'''
    Desenvolva um programa que pergunte a distância de uma viagem
    em KM. Calcule o preço da passagam, cobrando R$0,50 por KM para
    viagens de até 200KM e R$0,45 para viagens mais longas
'''
dist = float(input('Informe a distância percorrida em Km: '))

if dist <= 200:
    preco = dist * 0.5
    print(f'''
        Você quer percorrer {dist}Km
        O preço da viagem será de {preco}
    ''')
else:
    preco = dist * 0.45
    print(f'''
        Você quer percorrer {dist}Km
        O preço da viagem será de {preco}
    ''')