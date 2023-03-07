'''
Faça um programa que, dado uma figura geométrica que pode ser uma circunferência, triângulo ou retângulo, calcule a área e o perímetro da figura
•O programa deve primeiro perguntar qual o tipo da figura:
–(1) circunferência
–(2) triângulo
–(3) retângulo
•Dependendo do tipo de figura, ler o (1) tamanho do raio da circunferência; (2) tamanho de cada um dos lados do triângulo; (3) tamanho dos dois lados retângulo
•Usar funções sempre que possível
'''

def circA(r):
    return 3.14*(r**2)

def circP(r):
    return 2*r*3.14

def retA(a, b):
    return a*b

def retP(a, b):
    return (2*a) + (2*b)

def trianP (a, b, c):
    return a+b+c 

opcao = 0 

while opcao != 4:

    print('(1) Circunferência')
    print('(2) Triângulo')
    print('(3) Retângulo')
    print('(4) Encerrar Programa')

    opcao = int(input('Escolha uma opção:\n'))

    if opcao == 1:
        r = float(input('Coloque o valor do raio:\n '))
        print(f'O valor da area da circuferencia é {circA(r)} e o perimetro é {circP(r)}')

    if opcao == 2:
        a = float(input('Coloque o valor do lado A:\n'))
        b = float(input('Coloque o valor do lado B:\n'))
        c = float(input('Coloque o valor do lado C:\n'))

        print(f'O valor do perimetro do triangulo é {trianP(a, b, c)}')

    if opcao == 3:
        a = float(input('Coloque o valor do lado A:\n'))
        b = float(input('Coloque o valor do lado B:\n'))

        print(f'O valor da area do retangulo é {retA(a, b)} e o perimetro é {retP(a, b)}')

    if opcao == 4:
        print('Programa Encerrado')