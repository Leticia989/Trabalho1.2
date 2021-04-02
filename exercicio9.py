numero_pessoas =int(input('Digite o numero de pessoas: '))
soma = 0
for i in range(numero_pessoas):
    idade = int(input('Digite sua idade: '))
    soma += idade
media = soma / numero_pessoas
if 0 >media<25:
    print('Turma de jovens pois a media de idade é:', media)
elif media <60:
    print('Turma de adultos pois a media é:', media)
else:
    print('Turma de idosos pois a media de idade é media:', media)