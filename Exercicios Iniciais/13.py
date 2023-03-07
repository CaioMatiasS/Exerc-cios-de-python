# -*- coding: utf-8 -*-
"""

Faça um programa que leia duas notas e imprima a média aritmética arredondada.

"""

nota1 = float(input('Coloque a nota 1:'))
nota2 = float(input('Coloque a nota 2:'))

media = round((nota1 + nota2)/2)

print(f'A media de {nota1} e {nota2} é {media}.')