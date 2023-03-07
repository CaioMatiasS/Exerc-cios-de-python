'''
ado o programa abaixo, construa a função recursiva tab( ), para que apareça na tela a tabuada de 1 até 10 de um número inteiro qualquer.Exemplo:  
Se n=5 deverá aparecer na tela

1 x 5 = 5
2 x 5 = 10
3 x 5 = 15
4 x 5 = 20
5 x 5 = 25
6 x 5 = 30
7 x 5 = 35
8 x 5 = 40
9 x 5 = 45
10 x 5 = 50

'''

def tab(n, i):
    if i <= 10:
        print(f'{i} x {n} = {i*5}')
        tab(n, i+1)

n = int(input('Coloque o valor entre 1 e 10: '))
tab(n, 1)

