alunos = {
    
'nomes':['Ana','Pedro','Julia','Maria'],
'notas':[float(input('nota >')), float(input('nota >')), float(input('nota >')), float(input('nota >'))]

}

media_turma = (alunos['notas'][0] +  alunos['notas'][1] + alunos['notas'][2]+ alunos['notas'][3])/ len(alunos['notas'])

print('média', media_turma)