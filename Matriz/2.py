'''
Faça um programa que leia duas matrizes A e B 2x2 e imprima a matriz C que é a soma das matrizes A e B.
'''

matrizA = []
matrizB = []

for i in range(2):
    linhaA = []
    for j in range(2):
        linhaA.append(int(input(f'Coloque um valor para matriz A [{i}][{j}]: ')))
    matrizA.append(linhaA)

for i in range(2):
    linhaB = []
    for j in range(2):
        linhaB.append(int(input(f'Coloque um valor para matriz B [{i}][{j}]: ')))
    matrizB.append(linhaB)

matrizC = matrizA[:]

for i in range(2):
    for  j in range(2):
        matrizC[i][j] = matrizC[i][j] + matrizB[i][j]

for i in range(2):
    print(matrizC[i])
