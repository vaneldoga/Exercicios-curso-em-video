# Exercicio - Curso em vídeo - Exercício 033
'''
    Função: Faça um programa que leia três números e mostre
    qual é o maior e qual é o menor
'''

a = float(input('Digite um número: '))
b = float(input('Digite um número: '))
c = float(input('Digite um número: '))

# para achar o maior valor:
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

# para achar o menor valor:
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

print(f'''
    O maior valor digitado: {maior}
    O menor valor digitado: {menor}
''')