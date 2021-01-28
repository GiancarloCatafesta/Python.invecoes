#Somatória de valores
soma = 0
total = 0
print('Digite quantos numeros quiser. Se quiser parar digite 999')
num = 0
num = int(input('Digite um numero: '))
while num != 999:
    soma += num
    total += 1
    num = int(input('Digite um numero: '))

print('Fim')
print(f'Foram digitados {total}')
print(f'O total dos termos dados foi de {soma}')
