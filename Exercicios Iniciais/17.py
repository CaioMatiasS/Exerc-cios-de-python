# -*- coding: utf-8 -*-
"""

Faça um programa que leia o ano atual e quantos anos uma pessoa fez ou fará nesse ano,
em seguida, calcule o ano em que a pessoa nasceu 

"""

ano = int(input('Coloque o ano em que estamos:'))
idade = int(input('Coloque a idade que voce tem ou fará nesse ano:'))

nascimento = ano - idade 

print(f'O ano em que voce nasceu é {nascimento}.')