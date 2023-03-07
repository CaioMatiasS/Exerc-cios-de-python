# -*- coding: utf-8 -*-
"""

Escreva um programa que lê uma frase, uma palavra antiga e uma palavra nova.
O programa deve imprimir a frase com as ocorrências da palavra antiga substituídas
pela palavra nova. Exemplo:
Frase: “Quem parte e reparte fica com a maior parte”
Palavra antiga: “parte”–Palavra nova: “parcela”
Saída: “Quem parcela e reparte fica com a maior parcela”

"""

frase = 'Quem parte e reparte fica com a maior parte'
frase = frase.replace('parte', 'parcela')
frase = frase.replace('reparcela', 'reparte')

print(frase)