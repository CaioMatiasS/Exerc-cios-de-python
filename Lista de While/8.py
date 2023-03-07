# -*- coding: utf-8 -*-
"""

Faça um programa que leia 100 números inteiros e diga quantos são ímpares.

"""

i = 1
cont = 0

while i <= 5:
    n = int(input('Coloque um numero inteiro:'))
    
    if n%2 == 1:
        cont += 1
        
    i += 1
    
print(f'A quantidade de numeros impares é {cont}')