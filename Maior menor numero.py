#Faça um programa que leia três números e mostre qual é o Maior e qual é o Menor:
a = float(input('Digite um numero: '))
b = float(input('Digite outro numero: '))
c = float(input('Digite mais outro numero: '))
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
if a == b or b == a or c == a or c == b:
    print('Não tem maior')
print(f'O maior é {maior}')
print(f'O menor é {menor}')