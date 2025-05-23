# sistema de média de notas


print('seja bem vindo(a) ao sistema de notas')

nome= input('digite o nome do aluno:')

nota_mat = float(input('digite a nota de matematica:'))
nota_por = float(input('digite a nota de portugues:'))
nota_ing = float(input('digite a nota de ingles:'))

media = (nota_mat + nota_por + nota_ing) / 3

print('o aluno',nome, ' esta com a media', media)

aprovado = media >= 7
reprovado = media <= 5
recuperacao = media >=5 and media < 7

print(f'''

O aluno {nome}
APROVADO - {aprovado}
REPROVADO - {reprovado}
RECUPERAÇÃO - {recuperacao}
''')