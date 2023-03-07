# -*- coding: utf-8 -*-
"""

Faça um programa que leia seu nome, sua idade e sua altura e escreva na tela.

"""

nome = input('Coloque seu nome:')
idade = int(input('Coloque sua idade:'))
altura = float(input('Coloque sua altura:'))

print(f'{nome} tem {idade} anos e {altura:.2f}m de altura.')