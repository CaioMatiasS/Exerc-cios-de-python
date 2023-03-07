'''Faça um programa que decida se duas strings lidas do teclado são palíndromasmútuas, ou seja, se uma é igual à outra quando lida de traz para frente.
•Exemplo: amor e roma.'''

palavra1 = input('Coloque uma palavra qualquer: ').split()
palavra2 = input('Coloque outra palavra: ').split()
cont = 0
if len(palavra1) == len(palavra2):
    for i in range (len(palavra1)):
        if palavra1[i] == palavra2[len(palavra2)-1-i]:
            cont += 1
    
    if cont == len(palavra1):
        print('São palindromas')
    else:
        print('Não são palindromas')
else:
    print('Não são palindromas')


        