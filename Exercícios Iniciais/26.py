'''
Faça um programa que leia hora, minuto e segundo e transforme
tudo para segundos
'''

hora = int(input('Digite a hora: '))
minuto = int(input('Digite o minuto: '))
segundo = int(input('Digite o segundo: '))

print(F'{hora}:{minuto}:{segundo}')

shora = (hora*60)*60
sminuto = minuto*60

segundo += shora
segundo += sminuto

print(f"O horario digitado somente em segundos: {segundo}s.")