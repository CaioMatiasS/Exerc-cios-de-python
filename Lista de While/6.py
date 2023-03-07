# -*- coding: utf-8 -*-
"""

Faça um programa que leia 10 números e imprima a raiz quadrada de cada número. 

"""
import math

i = 1 

while i <= 10:
    
    n = int(input('Coloque um numero inteiro:'))
    raiz = math.sqrt(n)
    print(raiz)
    
    i += 1