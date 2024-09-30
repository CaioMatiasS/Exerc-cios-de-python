'''
Faça um programa que leia duas notas e imprima a média aritmética truncada.
'''

nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))

media = (nota1 + nota2)//2

print(f"A media arredonda de {nota1} e {nota2} é {media}")