'''
5. Faça um programa que leia um vetor vet de 20 números inteiros. O
programa deve gerar, a partir do vetor lido, um outro vetor pos que
contenha apenas os valores inteiros positivos de vet. A partir do
vetor pos, deve ser gerado um outro vetor semdup que contenha
apenas uma ocorrência de cada valor de pos.

ex.:  
    
    vet = [-1, -1, -1, -1, -1, -1, -1, -1 ,-1, -1, 1, 1, 2, 2, 3, 3, 1, 2, 3, 1]
    
    pos = [1, 1, 2, 2, 3, 3, 1, 2, 3, 1]
    
    semdup = [] + [1] = [1]   
  
    semdup = [1, 2, 3]

i    j
1    0


'''

vet = []
pos = []
semdup = []

for i in range(5):
    vet.append(int(input('Coloque um valor: ')))

for i in range(5):
    if vet[i] > 0:
        pos.append(vet[i])



for i in range(len(pos)):
    repetido = False
    for j in range(i):
        if pos[i]==pos[j]:
            repetido = True
            j = i
    if not repetido:
        semdup.append(pos[i])

print(vet)
print(pos)
print(semdup)