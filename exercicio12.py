qnt_cd = int(input('digite a quantidade de CDs: '))
n = 0
total = 0
for x in range(qnt_cd):
    valor_CD = float(input('Digite o valor unitário do CD: '))
    total += valor_CD
    valor_medio = total/valor_CD
    n = n + 1

print('O valor total gasto é:', total)
print('o valor medio de cada CD é:', valor_medio)

