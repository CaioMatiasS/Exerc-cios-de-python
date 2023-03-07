# -*- coding: utf-8 -*-
"""

Faça um programa que leia um número inteiro e  calcule o seu fatorial

"""

i = 1
fat = 1

n = int(input('Coloque um numero inteiro:'))

while i <= n:
    
    fat *= i 
    i += 1
    
print(f'{n}! = {fat}')
