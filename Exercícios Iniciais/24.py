'''
Faça um programa que leia um valor inteiro representado uma certa 
quantidade em real (moeda), e diga qual é o número máximo de notas de dois 
reais e o mínimo de moedas de um real em que esse valor pode ser representado.
'''

moeda = int(input('Digite um valor inteiro de em real: '))

dois = moeda//2
um = moeda%2

print(f'Para o valor de R${moeda} podemos ter o maximo de {dois} notas de 2 reais e no minimo {um} moedas de 1 real.')