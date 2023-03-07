'''
Os primeiros membros da associação de Pitágoras definiram números poligonais como sendo o número de pontos em determinadas configurações geométricas.
Os primeiros números triangulares são 1, 3, 6, 10, 15. 
Faça uma função recursiva que receba um número natural positivo e encontre o n-ésimonúmero triangular.
'''

def pit(a):
    if a == 1:
        return 1
    else:
        return a + pit(a - 1)

n = int(input('Coloque um valor:'))
print(pit(n))