# -*- coding: utf-8 -*-
"""

Faça um programa que leia 100 números e diga quantos estão acima de 1000, 
quantos são iguais a 1000 e quantos estão abaixo de 1000.

"""

i = 1 

menor = 0
maior = 0
igual = 0


while i <= 5:
    
    n = int(input('Coloque um numero inteiro:'))
    
    if n < 1000:
        menor += 1
    
    elif n > 1000:
        maior +=1
        
    else:
        igual += 1
    
    i += 1
        
    
print(f'maiores que mil = {maior}')
print(f'iguais que mil = {igual}')
print(f'menores que mil = {menor}')