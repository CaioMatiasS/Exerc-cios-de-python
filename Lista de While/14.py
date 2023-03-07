# -*- coding: utf-8 -*-
"""

Faça um programa que leia um número inteiro n qualquer e mostre na tela a figura abaixo.

"""

n = int(input('Coloque um numero inteiro: '))

linha = 1

while linha <= n:
    cont = 1
    
    while cont <= linha:
        
        print('*', end = '')
        cont += 1
       
    print()
    linha += 1