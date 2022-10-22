# Exercicio - Curso em vídeo - Exercício 027
'''
    Função: Faça um programa que leia o nome completo de uma pessoa,
    mostrando em seguida o primeiro e o último nome separadamente.

    ex: Ana Maria De Souza
    primeiro = Ana
    Último = Souza
'''

nome = input('Qual o seu nome? ')
nomesep = nome.split()
indexult = len(nomesep)

print(f'''
    Seu nome completo: {nome}
    Seu primeiro nome: {nomesep[0]}
    seu último nome: {nomesep[indexult - 1]}
''')

'''
    outra forma de resolver;
    nome = input('Qual o seu nome?')
    nomesep = nome.split()
    print(f''
        primeiro nome: {nomesep[0]}
        último nome: {nomesep[-1]}
    
    '')
'''