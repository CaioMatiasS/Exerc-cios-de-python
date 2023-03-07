'''
    Um anagrama é uma palavra que é feita a partir da transposição das letras de outra palavra ou frase. Por exemplo, “Iracema” é um anagrama para “America”.
    Escreva um programa que decida se uma string é um anagrama de outra string, ignorando os espaços em branco. O programa deve considerar maiúsculas e minúsculas como sendo
    caracteres iguais, ou seja, “a” = “A”. Obs.: utilize a função sorted() que transforma uma string em uma lista de caracteres em ordem crescente.
'''

palavra1 = input('Coloque uma palavra'). split()
palavra2 = input('Coloque uma palavra'). split()

aux1 = sorted(palavra1.lower())
aux2 = sorted(palavra2.lower())

if aux1 == aux2:
    print(f'{palavra1} e {palavra2} são anagramas.')
else:
    print(f'{palavra1} e {palavra2} não são anagramas.')