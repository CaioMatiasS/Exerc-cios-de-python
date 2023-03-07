'''
3. Faça um programa que preencha por leitura um vetor de 5 posições,
e informe a posição em que um valor x (lido do teclado) está no
vetor. Caso o valor x não seja encontrado, o programa deve imprimir
o valor -1. Faça a questão de duas formas: não utililizando o método
index() e utilizando o método index().
'''

'''
Utilizando
'''

vetor = []

for i in range(5):
    vetor.append(int(input('Coloque os valores para o vetor: ')))

a = int(input('Qual valor voce quer saber a posicão: '))

if a in vetor:
    print(f'a posição do valor {a} é {vetor.index(a)}.')
else:
    print(f'a posição do valor {a} é -1, não foi encontrado.')