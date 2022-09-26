# Exercicio - Curso em vídeo - Exercício 012
# Função: ler o preço de um produtor e exibir seu novo preço com 5% de desconto

preco = float(input('Informe o valor do produto: R$'))

print(f'O valor do produto com 5% de desconto será igual a: R${preco - (preco * 0.05):.2f}')