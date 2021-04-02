num = int(input("Digite um número: "))
contador = 0

for i in range(1, num + 1):
    if num % i == 0:
        contador += 1
print('O número é primo') if contador == 2 else print('O número não é primo')