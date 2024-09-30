'''
Três massas m1, m2 e m3 estão separadas por distâncias r12, r13, r23, como mostra a figura.

(figura no pdf)

Se G é a constante de gravitação universal, a força de coesão para manter a massa das partículas juntas é dada pela fórmula
                                
                                F = G.[ (m1.m2)/r122 + (m1.m3)/r132 + (m2.m3)/r232 ]

Faça um programa para ler os valores das 3 massas e das 3 distâncias e em seguida calcule a força de coesão. 
Para massa em Kg e distância em metros, G=6,67.10-11Nm2/Kg2. 
Assumir que todos os valores são reais.
'''

G = 6.67*(10**-11)

m1 = float(input("Digite a massa m1 (Kg): "))
m2 = float(input("Digite a massa m2 (Kg): "))
m3 = float(input("Digite a massa m3 (Kg): "))
r12 = float(input("Digite a distância r12 (m): "))
r13 = float(input("Digite a distância r13 (m): "))
r23 = float(input("Digite a distância r23 (m): "))

FC = G*(((m1*m2)/r12**2)+((m1*m3)/r13**2)+((m2*m3)/r23**2))

print(f"A força de coesão entre as massas é {FC:.2e} N")
#O resultado é exibido em notação científica (usando o formato :.2e).