'''
O professor deseja dividir uma turma com N alunos em dois grupos: um com M alunos e outro com (N-M) alunos.
Faça o programa que lê o valor de N e M e informa o número de combinações possíveis
–Número de combinações é igual a N!/(M! * (N-M)!)
–Use funções para evitar repetição de código
'''

def combinacoes(m, n):
    
    fatM = 1
    fatN = 1
    fatNM = 1

    for i in range(1, m + 1 ):
        fatM *= i 
    
    for i in range(1, n + 1 ):
        fatN *= i 

    for i in range(1, (n-m) + 1 ):
        fatNM *= i 

    return (fatM*(fatNM)/fatN)

m = int(input('Coloque um valor de M: '))
n = int(input('Coloque um valor de N: '))

print(f'O numero de combinações possiveis é {combinacoes(m, n)}')