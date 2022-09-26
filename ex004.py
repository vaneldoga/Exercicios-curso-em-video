# Exercicio - Curso em vídeo - Exercício 004
# Função: ler algo pelo teclado e mostrar na tela o seu tipo primitivo e todas as possíveis informações sobre ele

algo = input('Digite algo: ')

# Não precisa colocar o ".format()". Pode colocar "f" na frente das aspas e inserir os valores dentro dos colchetes
print('O tipo primitivo do valor digitado é', type(algo))
print(f'Você digitou um número? {algo.isnumeric()}')
print(f'Você digitou um número ou uma letra? {algo.isalnum()}')
print(f'Você digitou apenas letras? {algo.isalpha()}')
print(f'Você digitou apenas letras Maiúsculas? {algo.isupper()}')
print(f'Você digitou apenas letras Minúsculas? {algo.islower()}')
print(f'Está capitalizada? {algo.istitle()}')