# -*- coding: utf-8 -*-
"""

Faça um programa que leia um número é verifique se ele é um número primo.

"""

n = int(input('Coloque um numero inteiro: '))

i = 1
primo = 0


while i <= n:
    if n%i == 0:
        primo += 1
        
    i += 1
    
if primo == 2:
    print(f'o numero {n} é primo')
    
else:
    print(f'o numero {n} não é primo')