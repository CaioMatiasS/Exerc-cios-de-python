# -*- coding: utf-8 -*-
"""

Faça um programa que mostre a tabuada de 1 até 10 de um número inteiro lido do teclado.

"""

n = int(input('Coloque um numero entre 1 e 10'))
i = 1

if n > 10 and n < 1:
    print('Erro.')
    
else:
    while i <= 10:
        print(f'{i} x {n} = {i*n}')
        i += 1