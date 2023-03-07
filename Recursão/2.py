'''
Faça uma função recursiva que receba um número inteiro e calcule o n-ésimotermo da série de Fibonacci
'''

def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = int(input('Coloque um valor: '))
print(fib(n))