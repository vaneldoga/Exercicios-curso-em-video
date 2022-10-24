# Exercicio - Curso em vídeo - Exercício 036
'''
    Função: Escreva um programa para aprovar o empréstimo bancário
    para a compra de uma casa. O programa vai perguntar o valor da casa,
    o salário do comprador e em quantos anos ele vai pagar.

    Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do
    salário ou então, o empréstimo será negado.
'''

print('-'*35)
print('Programa para solicitar empréstimo\nbancário para a compra de uma casa')
print('-'*35)

valor_casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o valor do seu salário? R$'))
anos = int(input('Em quantos anos você pretende pagar a casa?'))

meses = anos * 12
lim = salario * 0.3
prest_mensal = valor_casa / meses

if prest_mensal > lim:
    print(f'''
        O empréstimo foi negado.
        A prestação mensal ultrapassa 30% do seu salário (R${lim}).
    ''')
else:
    print(f'''
        O empréstimo foi aprovado
        Prestação mensal: R${prest_mensal:.2f} 
    ''')

