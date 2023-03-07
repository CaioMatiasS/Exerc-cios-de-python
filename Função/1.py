'''
Faça uma função que retorne o valor absoluto de um número
'''

def valorabsoluto(x):
    if x >= 0:
        return x
    else:
        return x * -1 


n = int(input('Coloque um valor: '))
print(f'O valor absoluto de {n} é {valorabsoluto(n)}')
