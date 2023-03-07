'''
Faça uma função que receba um caractere retorne True se for vogal e False caso contrário
'''

def vogal(a):
    if a in ('a', 'e', 'i', 'o', 'u'):
        return True

    else: 
        return False

a = input('Coloque um caracter: ').lower()
print(vogal(a))