# Exercicio - Curso em vídeo - Exercício 028
'''
    Função: Escreva um programa que faça o computador 'pensar'
    em um número inteiro entre 0 e 5 e peça para o usuário tentar
    descobrir qual foi o número escolhido pelo computador

    O programa deverá escrever na tela se o usuário venceu ou perdeu 
'''

print('¨'*50)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar!')
print('¨'*50)

'''
from random import choice

num = [0, 1, 2, 3, 4, 5] 
numEscolhido = choice(num)

inpUser = int(input('Eu pensei em qual número? '))

if inpUser == numEscolhido:
    print('Você venceu!')
else:
    print(f'Você perdeu!\nEu escolhi o número {numEscolhido}')
'''

from random import randint
numEscolhido = randint(0,5)

inpUser = int(input('Eu pensei em qual número? '))
if inpUser == numEscolhido:
    print('Você venceu!')
else:
    print(f'Você perdeu!\nEu escolhi o número {numEscolhido}')
