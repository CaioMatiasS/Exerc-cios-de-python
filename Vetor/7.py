'''
7. Dado um vetor de 100 elementos, determine o maior e o menor elemento do vetor.
(Não utilize as funções min() e max() )

'''

tam = 5
vet = []

for i in range(tam):
    vet.append(int(input('Coloque um valor: ')))

max = vet[0]
min = vet[0]

for i in range(tam):
    if vet[i] > max:
        max = vet[i]
    if vet[i] < min:
        min = vet[i]

print(max)
print(min) 