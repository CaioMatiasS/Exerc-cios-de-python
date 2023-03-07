'''
4. Um dado é lançado 50 vezes, e o valor correspondente é
armazenado em um vetor. Faça um programa que determine o
percentual de ocorrências de face 6 do dado dentre esses 50
lançamentos. Obs: utilize a função randint() para gerar os 50
lançamentos do dados. randint(1,6)  gera números inteiros
aleatórios de 1 a 6. Insira no seu programa:
from random import randint

'''

from random import randint

dado = []

for i in range(50):
    dado.append(randint(1,6))

qtd = dado.count(6)

percentual = (qtd/50)*100
print(dado)
print(f'O percentual de 6 foi de {percentual}% em 50 jogadas.')