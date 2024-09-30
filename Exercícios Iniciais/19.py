'''
Faça um programa que leia o raio de uma circunferência e calcule o perímetro e a área da circunferência.
'''

raio = float(input('Digite o raio da circuferencia: '))

#Perimetro = 2*pi*r
#Area = pi*r^2
#pi =~ 3.14

perimetro = (2*3.14)*raio
area = (raio**2)*3.14

print(f'A circuferencia de raio: {raio}, possui o perimetro de {perimetro} e a area de {area}.')