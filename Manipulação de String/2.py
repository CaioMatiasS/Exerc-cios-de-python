# -*- coding: utf-8 -*-
"""

Faça um programa que lê uma frase e retorna o número de palavras que a frase contém.

"""

frase = input('Coloque uma frase qualqer: ')

frase = frase.split()
aux = len(frase)

print(aux)

