votos_a = 0
votos_b = 0
votos_c = 0

eleitores = int(input('Digite o numero de eleitores: '))
for i in range(eleitores):
    print('eleitor',i+1, '(faltam', eleitores - i)
    voto = input('informe seu voto: a, b, ou c ?')
    if voto == 'a': votos_a = votos_a+1
    if voto == 'b': votos_b = votos_b+1
    if voto == 'c': votos_c = votos_c+1

print('O cantidado A obteve', votos_a,'votos')
print('O candidato B obteve', votos_b,'votos')
print('O candidato C obteve', votos_c,'votos')
