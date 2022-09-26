# Exercicio - Curso em vídeo - Exercício 011
# Função: ler a largura e a altura de uma parede em metros, calcular a sua área
# e a quantidade necessária para pintá-la, sabendo que cada litro de tinta pinta
# uma área de 2m^2

largura = float(input('Digite o valor da largura da parede (em metros): '))
altura = float(input('Digite o valor da altura da parede (em metros): '))

print(f'Sua parede possui uma dimensão de: {largura}x{altura}')
print(f'A área é igual a: {largura*altura}m²')
print(f'Para pintar essa parede, você precisará de {largura * altura / 2} litros de tinta')
