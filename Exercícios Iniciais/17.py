'''
Faça um programa que leia o ano atual e quantos anos uma pessoa fez ou fará nesse ano,
em seguida, calcule o ano em que a pessoa nasceu
'''

ano = int(input('Digite o ano atual: '))
idade = int(input('Digite sua idade desse ano: '))

nasc = ano - idade

print(f'Voce nasceu no ano de {nasc}.')