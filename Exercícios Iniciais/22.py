'''
Faça um programa para calcular o volume de uma lata de óleo, utilizando a fórmula volume=PIxR^2
xaltura. Seu programa deve ler o raio e a altura da lata.
'''

raio = float(input('Digite o raio da lata: '))
altura = float(input('Digite a altura da lata: '))

volume = 3.14*(raio**2)*altura

print(f'A lata de raio {raio} e altura {altura} tem o volume de {volume}.')