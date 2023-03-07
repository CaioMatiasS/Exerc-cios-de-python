# -*- coding: utf-8 -*-
"""

Faça um programa que leia dois lados de um triângulo retângulo e calcule a hipotenusa

"""

import math

lado1 = float(input('Coloque o valor do cateto a:'))
lado2 = float(input('Coloque o valor do cateto b:'))

hipotenusa2 = lado1**2 + lado2**2 
hipotenusa = math.sqrt(hipotenusa2)

print(f'A hipotenusa do triangulo retangulo de cateto a = {lado1} e cateto b = {lado2} é {hipotenusa}.')