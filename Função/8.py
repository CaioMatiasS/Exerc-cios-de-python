'''
Faça uma calculadora que forneça as seguintes opções para o usuário, usando funções sempre que necessário. 
Cada opção deve usar como operando um número lido do teclado e o valor atual da memória. 
Por exemplo, se o estado atual da memória é 5, e o usuário escolhe somar, ele deve informar um novo número (por exemplo, 3). 
Após a conclusão da soma, o novo estado da memória passa a ser 8.

Estado da memória: 0

Opções:

(1)Somar
(2)Subtrair
(3)Multiplicar
(4)Dividir
(5)Limpar memória
(6)Sair do programa

Qual opção você deseja?
'''

def soma (a, b):
    return a + b

def sub(a, b):
    return a - b

def multi(a, b):
    return a*b

def div(a, b):
    return a/b

def menu(a):
    print(f'Estado de mémoria = {a}')
    print()
    print('-' * 50)
    print()
    print('(1)Somar')
    print('(2)Subtrair')
    print('(3)Multiplicar')
    print('(4)Dividir')
    print('(5)Limpar memória')
    print('(6)Sair do programa')
    print()
    print('Qual opção você deseja?')
    print()
    print('-' * 50)

em = 0 #estado de memoria 
opcao = 0

while opcao != 6:
    menu(em)
    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        n = float(input('Coloque o numero que deseja somar:\n'))
        em = soma(em, n)
    
    if opcao == 2:
        n = float(input('Coloque o numero que deseja subtrair:\n'))
        em = sub(em, n)

    if opcao == 3:
        n = float(input('Coloque o numero que deseja multiplicar:\n'))
        em = multi(em, n)

    if opcao == 4:
        n = float(input('Coloque o numero que deseja dividir:\n'))
        em = div(em, n)
    
    if opcao == 5:
        em = 0
        print('Mémoria Limpa')

    if opcao == 6:
        print('Programa encerrado')

