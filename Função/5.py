'''
Faça uma função que receba um caractere retorne Truese for consoante e False caso contrário
'''

def consoante(a):
    if a in ('a', 'e', 'i', 'o', 'u'):
        return False

    else: 
        return True

a = input('Coloque um caracter: ').lower()
print(consoante(a))