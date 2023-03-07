'''
Faça um programa que leia uma matriz 6x3 com números reais, calcule e mostre:
(a) o maior elemento da matriz e sua respectiva posição (linha e coluna); 
(b) o menor elemento da matriz e sua respectiva posição.
'''


aux1 = 0
aux2 = 0 
aux3 = 0
aux4 = 0 

maior = 0
menor = 0
matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input('Coloque um valor: ')))
    matriz.append(linha)

for i in range(3):
    for j in range(3):
        if (i == 0) and (j == 0):
            maior = matriz[i][j]
            aux1 = i
            aux2 = j

        if maior > matriz[i][j]:
            maior = matriz[i][j]
            aux1 = i
            aux2 = j
        
for i in range(3):
    for j in range(3):
        if (i == 0) and (j == 0):
            menor = matriz[i][j]
            aux3 = i
            aux4 = j

        if menor < matriz[i][j]:
            menor = matriz[i][j]
            aux3 = i
            aux4 = j

print(f'O maior elemento é {maior} e esta na linha {aux1} e na coluna {aux2}')
print(f'O menor elemento é {menor} e esta na linha {aux3} e na coluna {aux4}')
