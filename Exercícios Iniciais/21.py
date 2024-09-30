'''
Faça um programa que leia a temperatura em graus centígrados e a converta 
para graus Fahrenheit. A fórmula de conversão é F=(9.C+160)/5, onde F é a 
temperatura em Fahreinheit e C é a temperatura em centígrados.
'''

C = float(input('Digite a temperatura em Celsius (C): '))

F = ((9*C)+160)/5
print(f'A temperatura de {C}C em Fahreinheit é {F}F')