'''
6. Dado um vetor de 100 elementos, determine o maior e o menor elemento do vetor.
(Utilize as funções min() e max() )

'''

tam = 5
vet = []

for i in range(tam):
    vet.append(int(input('Coloque um valor: ')))

print(min(vet))
print(max(vet))