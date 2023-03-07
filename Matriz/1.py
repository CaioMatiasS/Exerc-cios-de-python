'''
Faça um programa que leia uma matriz 3x3 e multiplique os elementos da diagonal principal da matriz por um número k.
Imprima a matriz na tela antes e depois da multiplicação.
'''

matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input(f'Coloque um valor pra [{i}][{j}] : ')))
    matriz.append(linha)

k = int(input('Entre com o valor de k: '))

print('Matriz original:')
for i in range(3):
    print(matriz[i])

for i in range(3):
    matriz[i][i] = (matriz[i][i])*k

print('Matriz após a multiplicação:')
for i in range(3):
    print(matriz[i])