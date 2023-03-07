'''
3. Faça um programa que preencha por leitura um vetor de 5 posições,
e informe a posição em que um valor x (lido do teclado) está no
vetor. Caso o valor x não seja encontrado, o programa deve imprimir
o valor -1. Faça a questão de duas formas: não utililizando o método
index() e utilizando o método index().
'''

'''
Não utilizando
'''
vetor = []
for i in range(5):
    vetor.append(int(input('Coloque o valor: ')))

a = int(input('Qual valor voce quer saber a posição: '))
local = -1

for i in range(5):
    if a == vetor[i]:
        local = i
        i = 4

if local != -1:
    print(f'O local de {a} é {local}.')
else:
    print(f'O local de {a} é -1, não foi encontrado.') 