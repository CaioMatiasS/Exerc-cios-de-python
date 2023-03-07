'''

8. Dado um vetor de 100 elementos, determine a diferença entre a soma dos elementos
de índice par e a soma dos elementos de índice ímpar.


a = [ 1,     2,     3,    4,     5,      1,     1,  ...   , 1]
     a[0]   a[1]   a[2]   a[3]   a[4]    a[5]  a[6]      a[99]
     
     
abs(-3)    ---> 3
abs(2)     ---> 2

i  soma_par         soma_impar
      0                 0
0     0+ 1 = 1 
1                     0 + 2 = 2
2     1 + 3 = 4
     
'''

tam = 5
vet = []

par = 0
impar = 0

for i in range(tam):
    vet.append(int(input('Coloque um valor: ')))

for i in range(5):
    if (i%2) == 0:
        par += vet[i]
    else:
        impar += vet[i]

diferença = abs(par - impar)

print(diferença)