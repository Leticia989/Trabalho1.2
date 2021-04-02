num = int(input("Digite o tamanho do conjunto: "))

ma = None
me = None

for i in range(num):

   x = float(input("Digite um número: "))
   ma = ma if ma != None and ma > x else x
   me = me if me != None and me < x else x

print(f'O maior valor digitado foi {ma} e o menor foi {me}')

