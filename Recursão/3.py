'''
Faça uma função recursiva que calcule e retorne o valor de S, onde:S=1 + 1/1! + 1/2! + 1/3! + ...+ 1/n!
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



def s(n):
    if n == 1:
        return 1
    else:
        return s(n-1) / fat(fibo(n))



n = int(input('Coloqeu um valor: '))

print(s(n))
