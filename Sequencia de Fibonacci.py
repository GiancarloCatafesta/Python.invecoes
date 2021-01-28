#Sequencia de Fibonacci
print('Sequencia de Fibonacci')
seq = int(input('Quantos termos deseja ver, desconsiderando o 0: '))
fib = 0
pro = 0
ant = 0
while fib < seq:
    print(f'{pro}',end='')
    print(f' -> ' if fib < seq else '...',end='')
    pro = pro + ant
    ant = pro - ant
    fib += 1
    if pro == 0:
        pro = pro + 1
print('Fim')