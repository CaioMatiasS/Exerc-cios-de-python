'''
Construa uma função recursiva que calcule e retorne o valor de 
S.S = 1^1! + 2^1! + 3^2! + 4^3! + 5^5! + 6^8! + 7^13! + ...
'''

def fat(n):
    if(n==1):
        return 1
    else:
        return n * fat(n-1)

def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

def pot(n, x):
    if x == 1:
        return x
    else:
        return x*pot(n, x-1)

def s(n):
    if n == 1:
        return 1
    else:
        return s(n-1) + pot(n, fat(fibo(n)))



n = int(input('Coloqeu um valor: '))

print(s(n))