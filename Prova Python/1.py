'''
Dizemos que dois números são amigos se cada um deles é igual a soma dos divisores próprios do outro.
Os divisores próprios de um número positivo N são todos os divisores inteiros positivos de N exceto o próprio N.
Um exemplo de números amigos são 284 e 220, pois os divisores próprios de 220 são 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 e 110. Efetuando a soma destes números obtemos o resultado 284.
1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110 = 284
Os divisores próprios de 284 são 1, 2, 4, 71 e 142, efetuando a soma destes números obtemos o resultado 220.
1 + 2 + 4 + 71 + 142 = 220
'''

n1 = int(input('Coloque um numero qualquer: '))
n2 = int(input('Coloque um numero qualquer: '))

c1 = 0
c2 = 0

for i in range(1, n1):
    if n1%i == 0:
        c1 += i 

for i in range(1, n2):
    if n2%i == 0:
        c2 += i 

if c1 == n2 and c2 == n1:
    print(f'os numeros {n1} e {n2} são amigos')

else:
    print(f'os numeros {n1} e {n2} não são amigos')