'''
Faça um programa que leia uma matriz 3x3 de inteiros e retorne a linha de maior soma. Imprima na tela a matriz, a linha de maior soma e a soma. Obs.:
Em Python existe uma função sum() que efetua a soma dos elementos de uma lista. Faça a questão de duas maneiras: utilizando e não utilizando a função sum().
'''
'''
Utilizando
'''

matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input(f'Coloque o valor para [{i}][{j}]: ')))
    matriz.append(linha)

linhaid = -1 
somalinha = 0 

for i in range(3):
    soma = 0
    soma = sum(matriz[i])

    if soma > somalinha:
        somalinha = soma
        linhaid = i

print('Matriz:')
for i in range(3):
    print(matriz[i])

print('A linha de maior soma:')
print(matriz[linhaid])

print(f'A soma de {matriz[linhaid][0]} + {matriz[linhaid][1]} + {matriz[linhaid][2]} é {somalinha}')
