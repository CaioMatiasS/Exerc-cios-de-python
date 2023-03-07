'''
6.Faça um programa que leia o nome do usuário e mostre o
nome de trás para frente, utilizando somente letras
maiúsculas.
Exemplo:
Nome = Vanessa
Resultado gerado pelo programa:
ASSENAV
'''

nome = input('Coloque o seu primeiro nome: ')

for i in range(len(nome)-1, -1, -1): 
    print(nome[i].upper(), end ='' )