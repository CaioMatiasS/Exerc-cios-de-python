# -*- coding: utf-8 -*-
"""

Um número perfeito é um número natural para o qual a soma de todos os seus
divisores naturais próprios (excluindo ele mesmo) é igual ao próprio número. 
Exemplo 6 é um número perfeito, pois 6 = 1 + 2 +3. 28 é um número perfeito, pois
28 = 1+2+4+7+14. Faça um programa que leia um número e diga se ele é um número perfeito.

"""

n = int(input('Coloque um numero inteiro: '))
i = 1
a = 0 

while i < n:
    if n%i == 0:
        a += i
        
    i += 1
    
if a == n:
    print(f'{n} é um numero perfeito.')
    
else:
    print(f'{n} não é um numero perfeito.')
