'''
2. Estenda o exemplo do cadastro para considerar também a altura da pessoa
'''
import random
from random import randint

nome = ['Caio', 'Marcos', 'Joao', 'Mateus', 'Gabriel']
sobrenome = ['Silva', 'Santos', 'Matias', 'Andrade', 'Filho']

arquivo = open('txt_arq/2.txt', 'x')

for i in range(5):
    idade = randint(1, 99)
    altura = 1 + random.uniform(0, 1)   
    arquivo.write(f'{nome[i]} {sobrenome[i]}, {str(idade)}, {altura:.2f}\n')

arquivo.close()









