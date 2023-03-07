'''
Faça um programa que leia a ordem de uma matriz quadrada A (até 100),
posteriormente leia seus valores e escreva sua transposta AT, onde AT[i][j] = A[j][i]
'''

matrizA = []
matrizAT = []

for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input(f'Coloque o valor de [{i}][{j}]: ')))
    matrizA.append(linha)

for i in range(3):
    linha = []
    for j in range(3):
        linha.append(matrizA[j][i])
    matrizAT.append(linha)

print('Matriz:')
for i in range(3):
    print(matrizA[i])

print('Transposta:')
for i in range(3):
    print(matrizAT[i])