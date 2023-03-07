# -*- coding: utf-8 -*-
"""

Faça um programa que leia duas notas e imprima a média aritmética truncada.

"""



'''
nota1 = float(input('Coloque a nota 1:'))
nota2 = float(input('Coloque a nota 2:'))

media = (nota1 + nota2)//2

print(f'A media de {nota1} e {nota2} é {media}.')
'''

import math

nota1 = float(input('Coloque a nota 1:'))
nota2 = float(input('Coloque a nota 2:'))

media = math.trunc((nota1 + nota2)/2)

print(f'A media de {nota1} e {nota2} é {media}.')