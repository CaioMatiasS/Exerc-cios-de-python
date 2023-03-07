'''
Faça uma função que receba dois valores e retorne a média aritmética
'''

def media(a, b):
    return (a+b)/2

a = int(input('Coloque um valor: '))
b = int(input('Coloque um valor: '))

print(f'A media de {a} e {b} é {media(a, b)}')