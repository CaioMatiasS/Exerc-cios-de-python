'''
Faça um programa que entre com um número de 3 dígitos (em apenas uma variável) e o escreva na ordem inversa
em que foi digitado. Ex.: se o usuário digitar 379 terá que aparecer na tela 973.
'''

num = int(input('Digite um numero inteiro de 3 digitos: '))

centena = num//100
dezena = (num%100)//10
unidade = ((num%100)%10)//1

print(f'O numero {num} na ordem inversa fica: {unidade}{dezena}{centena}')