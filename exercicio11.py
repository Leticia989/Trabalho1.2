qnt_turmas = int(input('Quantas turmas serão registradas? '))
x = 0
soma = 0
while x < qnt_turmas:
    turma = int(input('turma {} digite quantos alunos tem nessa turma: '.format(x+1)))
    while turma < 0 or turma > 40:
        if turma < 0 :
            print('digite um valor maior ou igual a zero: ')
        elif turma > 40:
            print('a turma não pode ter mais de 40 alunos')
        turma = int(input('turma {} digite quantos alunos tem nessa turma: '.format(x + 1)))
    soma += turma
    x += 1
print('Numero de turmas', qnt_turmas)
print('Numero total de alunos', soma)
print('Media de alunos: %.2f'%(soma/qnt_turmas))
