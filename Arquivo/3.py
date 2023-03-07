'''
Escreva uma função que recebe dois nomes de arquivos e copia o conteúdo do primeiro arquivo para o segundo arquivo.
Considere que o conteúdo do arquivo de origem é um texto. 
Sua função não deve copiar linhas comentadas (que começam com //)
'''

arq1 = open('txt_arq/3a.txt', 'r')
arq2 = open('txt_arq/3b.txt', 'w')


for linha in range(arq1.readline()):
    if linha[0] != '/':
        arq2.write(linha) 
    
    

arq1.close()
arq2.close()