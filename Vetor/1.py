'''
1. Faça um programa que leia dois vetores de 3 posições, que
representam forças sobre um ponto no espaço 3D, e escreva a força
resultante. Dica: força resultante é obtida pela soma dos valores das
coordenadas correspondentes nos dois vetores: (x1 + x2), (y1+ y2),
(z1 + z2)

'''
resultante = []
vetor1 = []
vetor2 = []

for i in range(3):
    vetor1.append(float(input('Coloque um valor para o vetor 1: ')))
    vetor2.append(float(input('Coloque um valor para o vetor 2: ')))

for i in range(3):
    resultante.append(vetor1[i] + vetor2[i])

print(resultante)

