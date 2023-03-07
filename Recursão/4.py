'''
Faça uma função recursiva que calcule e retorne x elevado a z. Em seguida, apresente o passo a passo de execução do programa com x=2 e z=-2. 
Obs.: x é um número real e z é um número inteiro. Não use o operador **
                                                        
                                                        defpotencia(x,  z):0

'''

def pot(x, z):
    if z == 1:
        return z
    elif z < 0:
        return 1 / pot(x, (z * -1) )
    else:
        return x * pot(x, z-1)

x = int(input('Coloque um valor para x: (X^Y): '))
z = int(input('Coloque um valor para z: (X^Z): '))

print(pot(x, z))
    

#NAO FEITO.
