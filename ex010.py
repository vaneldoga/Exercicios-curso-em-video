# Exercicio - Curso em vídeo - Exercício 010
# Função: ler quanto dinheiro uma pessoa possui e exibir quantos dólares ela pode comprar
# considerar: US$1.00 = R$3.27

n = float(input('Informe o valor que você possui: R$'))
print(f'Com o R${n:.2f} você pode comprar U${n / 3.27:.2f} (dolár)')
print(f'Com o R${n:.2f} você pode comprar €{n / 5.14:.2f} (euro)')