mat = []

n = int(input('Coloque qualquer valor: '))

for i in range(n):
    linha = []
    for i in range(n):
        if n%2 == 0:
            linha.append('Par')
        else:
            linha.append('Impar')
    
    mat.append(linha)

for i in range(n):
    mat[i][i] = '*'

for i in range(n):
    print(mat[i])