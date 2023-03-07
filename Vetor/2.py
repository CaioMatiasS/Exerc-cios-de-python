'''
Faça um programa que preencha por leitura um vetor de 10 posições, e conta quantos valores diferentes existem no vetor.
'''

tam = 10
vetor = []

for i in range(tam):
    vetor.append(int(input('Coloque um valor: ')))

a = 0
cont = 0

for i in range(tam):
    repetido = False
    for j in range (i+1, tam):
        if vetor[i] == vetor[j]:
            repetido = True
            j = tam
    if not repetido:
        cont += 1

print(f'Existe {cont} elementos repetidos.')