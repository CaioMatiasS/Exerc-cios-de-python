'''
Faça um programa que leia um total de segundos e transforme para hora, minuto e segundo
'''

segundos = int(input('Digite o valor em segundos: '))

minuto = segundos//60
segundos = segundos%60

hora = minuto//60
minuto = minuto%60

print(f'Horas: {hora}, minutos: {minuto}, segundos: {segundos}')

