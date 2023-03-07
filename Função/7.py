'''
Faça uma função que informe o status do aluno a partir da sua média de acordo com a tabela a seguir:
–Nota acima de 6   -> "Aprovado”
–Nota entre 4 e 6  -> “Verificação Suplementar”
–Nota abaixo de 4  -> “Reprovado”
'''

def status(a):
    if a >= 6:
        return "Aprovado"
    
    if a >= 4 and a < 6:
        return "Verificação Suplementar"

    if a < 4:
        return "Reprovado"

media = float(input('Coloque a media: '))
print(status(media))