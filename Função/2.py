'''
Faça uma função que receba um número inteiro e retorne True se o número for par e False se o número for ímpar
'''

def num(x):
    if x%2 == 0:
        return True
    
    else:
        return False

n = int(input('Coloque um valor: '))
print(num(n))