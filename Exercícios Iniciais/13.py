'''
Faça um programa que leia duas notas e imprima a média aritmética arredondada.
'''

nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))

media = round((nota1 + nota2)/2)

print(f"A media arredonda de {nota1} e {nota2} é {media}")
