'''
Faça um programa que leia dois valores A e B e em seguida efetue a troca dos 
valores de forma que a variável A passe a ter o valor da variável B e vice e
versa.
'''

a = int(input('Digite um valor para A: '))
b = int(input('Digite um valor para B: '))

print(f'Valor de A = {a} e valor de B = {b}')

c = a
a = b
b = c

print(f'Novo valor de A = {a} e novo valor de B = {b}')


