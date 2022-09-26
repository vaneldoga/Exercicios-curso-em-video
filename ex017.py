# Exercicio - Curso em vídeo - Exercício 017
# Função: ler o comprimeto do cateto oposto e do cateto adjacente de um triângulo retângulo
# calcular a área e exibir o comprimento da hipotenusa

''' 
modo "tradicional":
    #catetoOp = float(input('Digite o comprimento do cateto oposto: '))
    #catetoAd = float(input('Digite o comprimento do cateto adjacente: '))

    #hipotenusa = ((catetoOp ** 2) + (catetoAd ** 2)) ** 0.5

    #print(f'Comprimento da hipotenusa: {hipotenusa:.3f}')

 UTILIZANDO A BIBLIOTECA MATH:
'''

catetoOp = float(input('Digite o comprimento do cateto oposto: '))
catetoAd = float(input('Digite o comprimento do cateto adjacente: '))

from math import hypot

print(f'Comprimento da hipotenusa: {hypot(catetoOp, catetoAd)}')
