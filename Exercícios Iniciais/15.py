'''
Faça um programa que leia dois números inteiros e imprima o dividendo, o divisor, o resto e o quociente.
'''

num1 = int(input('Digite o numero 1: '))
num2 = int(input('Digite o numero 2: '))

quociente = num1//num2
resto = num1%num2

print(f'Dividendo: {num1}')
print(f'Divisor: {num2}')
print(f'Resto: {resto}')
print(f'Quociente: {quociente}')
