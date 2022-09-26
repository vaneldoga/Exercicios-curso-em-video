# Exercicio - Curso em vídeo - Exercício 008
# Função: ler um valor em metros e exibir este valor convertido em centímetros e milímetros

metros = float(input('Digite um valor em metros: '))

print('#' * 5, end='')
print(' Conversão de',metros,'m: ', end='')
print('#' * 5)
print(f'{metros}m corresponde a: {metros * 10:.0f}dm')
print(f'{metros}m corresponde a: {metros * 100:.0f}cm')
print(f'{metros}m corresponde a: {metros * 1000:.0f}mm')
print(f'{metros}m corresponde a: {metros / 10:.0f}dam')
print(f'{metros}m corresponde a: {metros / 100:.0f}hm')
print(f'{metros}m corresponde a: {metros / 1000:.0f}km')