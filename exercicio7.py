espaco_range = int(input('digite um numero de intervalos: '))
for n in range(1,espaco_range +1):
    count=0
    for i in range (1, n + 1 ):
        if n % i == 0 :
            count += 1
    print(f'{n} é  primo' if count == 2 else f'{n} Não é primo')
    print(f'realizou {n + 1} divisões')