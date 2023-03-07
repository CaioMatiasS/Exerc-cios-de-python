# -*- coding: utf-8 -*-
"""

Faça um programa que leia dois números inteiros e imprima o dividendo, o divisor, o resto e o quociente.

"""

dividendo = int(input('Coloque o dividendo:'))
divisor = int(input('Coloque o divisor:'))

quociente = dividendo // divisor
resto = dividendo % divisor

print(f'{dividendo} dividido {divisor} é {quociente} e resto {resto}.') 