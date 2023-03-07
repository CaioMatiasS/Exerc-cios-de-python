'''
Os primeiros membros da associação de Pitágoras definiram números poligonais como sendo o número de pontos em determinadas configurações geométricas. 
Os primeiros números pentagonais  são 1, 5, 12, 22. 
Faça uma função recursiva que receba um número natural positivo e encontre o n-ésimonúmero pentagonal.

(n/2) (3n - 1)
'''

def pent(n):
    return (n/2)*(3*n -1)

n = int(input('Coloque um valor: '))
print(pent(n))