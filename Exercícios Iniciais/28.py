'''
Faça um programa que leia um número binário de 4 dígitos e diga
qual é o seu decimal correspondente.
'''

bin = int(input('Digite um valor em binario de 4 digitos: '))

dig1 = bin//1000
dig2 = (bin%1000)//100
dig3 = ((bin%1000)%100)//10
dig4 = (((bin%1000)%100)%10)//1

dec1 = dig1*(2**3)
dec2 = dig2*(2**2)
dec3 = dig3*(2**1)
dec4 = dig4*(2**0)

dec = dec1 + dec2 + dec3 + dec4

print(f"O valor em binario {bin} em decimal é {dec}")

