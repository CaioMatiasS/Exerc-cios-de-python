'''
1. Faça um programa que gere um arquivo com 10 nomes e idades aleatórios 
• Faça uso de duas listas criadas na mão: uma que contenha 10 nomes e outra que contenha 10 sobrenomes 
• Cada linha do arquivo resultante deve conter um nome completo e a sua idade 
'''

from random import randint

nome = ['Caio', 'Marcos', 'Joao', 'Mateus', 'Gabriel']
sobrenome = ['Silva', 'Santos', 'Matias', 'Andrade', 'Filho']

arquivo = open('txt_arq/1.txt', 'x')

for i in range(5):
    idade = randint(1, 99)   
    arquivo.write(f'{nome[i]} {sobrenome[i]}, {str(idade)}\n')

arquivo.close()

