num = int(input("Digite o tamanho do conjunto: "))

ma = None
me = None

for i in range(num):

   n = float(input("Digite um número: "))
   while not 0 < n < 1000:
       n = float(input(' Apenas numeros de 0 a 1000! '))
   ma = ma if ma != None and ma > n else n
   me = me if me != None and me < n else n

print(f'O maior valor digitado foi {ma} e o menor foi {me}')