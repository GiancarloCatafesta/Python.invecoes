#Escreva um programa que leia Dois numeros inteiros e compare-os mostrando na tela uma mensagem:
#- O primeiro valor é Maior
#- O segundo valor é Maior
#- Não existe valor maior, os dois são Iguais.
n1 = int(input('Digite um numero inteiro: '))
n2 = int(input('Digite outro numero inteiro: '))
if n1 > n2:
    print(f'{n1} é maior')
elif n2 > n1:
    print(f'{n2} é maior')
else:
    print('Não existe valor maior, os dois são Iguais')