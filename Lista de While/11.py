# -*- coding: utf-8 -*-
"""

Faça um programa que leia um número inteiro e calcule e mostre os n primeiros termos da série de Fibonacci

"""

n = int(input('Coloque um numero inteiro: '))

linha = 1
a = 0
b = 0 
c = 1

while linha <= n:
    
    print(c, end = ' ')
    a = b
    b = c
    c = a + b
        
    linha += 1