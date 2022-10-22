# Exercicio - Curso em vídeo - Exercício 026
'''
    Função: Faça um programa que leia uma frase pelo teclado
    e mostre: 

    * Quantas vezes aparece a letra "A"
    * Em que posição ela aparece a primeira vez
    * Em que posição ela aparece a última vez
'''

a = input('Digite alguma coisa: ')
aup = a.upper()
quantA = aup.count('A')
primA = aup.find('A')+1
ultA = aup.rfind('A')+1

print(f'''
    A letra "A":
    
    Aparece {quantA} vezes
    aparece pela primeira vez na posição: {primA}
    aparece pela última vez na posição: {ultA}
''')