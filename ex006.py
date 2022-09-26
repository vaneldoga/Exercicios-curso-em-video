# Exercicio - Curso em vídeo - Exercício 006
# Função: ler um número e exibir o seu dobro, triplo e raiz quadrada

num = int(input('Digite um número inteiro: '))

print(f'Dobro de ({num}): {num * 2}')
print(f'Triplo de ({num}): {num * 3}')
print(f'Raiz Quadrada de ({num}): {num ** 0.5:.2f}')

# "num ** 0.5" -> pode ser escrito da seguinte forma:
# pow(n, (1/2))