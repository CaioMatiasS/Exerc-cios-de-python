# -*- coding: utf-8 -*-
"""

Faça um programa que leia 100 números inteiros e diga qual é o menor. 

"""

i = 1

while i <= 5:
    
    n = int(input('Coloque um numero inteiro:'))
    
    if i == 1:
        menor = n
    else:
        if n < menor:
            menor = n
    i += 1
    
print(f'O menor numero é {menor}')