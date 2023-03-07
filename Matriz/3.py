'''
Faça um programa que leia as dimensões de duas matrizes A e B, e depois leia as duas matrizes.
Se as matrizes forem de tamanhos compatíveis para multiplicação, multiplique as matrizes.
Imprima as matrizes A, B e a matriz resultante da multiplicação.
'''

dimA1 = int(input('Coloque o valor da dimenção A1: '))
dimA2 = int(input('Coloque o valor da dimenção A2: '))
dimB1 = int(input('Coloque o valor da dimenção B1: '))
dimB2 = int(input('Coloque o valor da dimenção B2: '))

matrizA = []
matrizB = []
matrizC = []
for i in range(dimA1):
    linha = []
    for j in range(dimA2):
        linha.append(int(input(f'Coloque um valor para matrizA [{i}][{j}]: ')))
    matrizA.append(linha)

for i in range(dimB1):
    linha = []
    for j in range(dimB2):
        linha.append(int(input(f'Coloque um valor para matrizB [{i}][{j}]: ')))
    matrizB.append(linha)

if dimA1 == dimB1 and dimA2 == dimB2:
    for i in range(dimA1):
        linha = []
        for i in range(dimA2):
            linha.append(matrizA[i][j] * matrizB[i][j])
        matrizC.append(linha)


    print('Matriz A:')
    for i in range(dimA1):
        print(matrizA[i])

    print('Matriz B:')
    for i in range(dimA1):
        print(matrizB[i])

    print('Matriz C:')
    for i in range(dimA1):
        print(matrizC[i])

else:
    print('Matriz A:')
    for i in range(dimA1):
        print(matrizA[i])

    print('Matriz B:')
    for i in range(dimA1):
        print(matrizB[i])

    print('Não houve multiplicação.')





