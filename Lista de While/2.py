# -*- coding: utf-8 -*-
"""

Faça um programa que imprima os 100 primeiros números pares positivos.

"""

i = 1

while i <=100:
    n = i*2
    
    if n%2 == 0:
        print(n)
    
    i += 1

