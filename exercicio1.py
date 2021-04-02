numero = int(input('A Fatorial é: '))

resultado = 1

print(f'{numero}! = ', end='')

for i in range(numero, 0, -1):
    print(f'.{i}', end='')
    resultado = resultado * i

print(f' = {resultado}', end='')