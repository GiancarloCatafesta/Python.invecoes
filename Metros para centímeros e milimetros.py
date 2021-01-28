#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
metro = float(input('Digite quantos metros deseja converter: '))
cent = metro*(10**2)
mili = metro*(10**3)
conver = 0
while conver == 1 or 2:
    conver = int(input('Para qual valor deseja converter:\n'
                       'Centimetros:[1]\n'
                       'Milimetros:[2]\n'
                       ':'))
    if conver == 1:
        conver = cent
        print(f'{conver} centímetros')
    elif conver == 2:
        conver = mili
        print(f'{conver} milímetros')
    else:
        break
print('Fim')
print(f'Você digitou tantos {metro} metros, isso dá {cent} centímetros e {mili} milímetros ')