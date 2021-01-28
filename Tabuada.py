num = int(input('Digite um numero de 1 até 10: '))
for tabuada in range(0,11):
    multi = num * tabuada
    print('{} * {} = {}'.format(num,tabuada,multi))
print('FIM')