#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
ano = int(input('Digite um ano: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 and ano % 100 != 0:
    print('Ele é um ano Bissexo')
else:
    print('Ele é um ano hétero macho opressor ')