while True:
 numero = int(input('A Fatorial é: '))
 while not 0 <= numero<= 16:
    numero = int(input('Válido apenas números entre 0 e 16!'))
else:
  resultado = 1

print(f'{numero}! = ', end='')

for i in range(numero, 0, -1):
    print(f'.{i}', end='')
    resultado = resultado * i

print(f' = {resultado}', end='')