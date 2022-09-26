# Exercicio - Curso em vídeo - Exercício 015
# Função: Escreva um programa que pergunte a quantidade de Km percorridos por um
# carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Quantos dias alugado? '))
kmRodado = float(input('Quantos Km rodados? '))

print('#'*17)
print('Valor a ser pago: ')
print('#'*17)
print(f'O carro foi alugado por {dias} dias. Valor a ser pago: R${dias * 60:.2f}')
print(f'O carro percorreu {kmRodado}Km. Valor a ser pago: R${0.15 * kmRodado:.2f}')
print(f'Valor total a ser pago: R${(dias * 60) + (0.15 * kmRodado):.2f}')