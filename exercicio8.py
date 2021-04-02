quantidade = int(input('Gogite quantas notas deseja calcular: '))
notas = [ float(input('Qual a {}ª nota? '.format(i + 1))) for i in range(quantidade) ]
print('A média é {:.2f}'.format(sum(notas) / len(notas)))