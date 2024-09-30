'''
Faça um programa que leia dois lados de um triângulo retângulo e calcule a hipotenusa
'''

import math

cat1 = float(input(f'Digite o valor do cateto 1: '))
cat2 = float(input(f'Digite o valor do cateto 2: '))

sumcat = cat1**2 + cat2**2
hipotenusa = math.sqrt(sumcat)

print(f'A hipotenusa do triangulo retangulo de cateto a = {cat1} e cateto b = {cat2} é {hipotenusa}.')