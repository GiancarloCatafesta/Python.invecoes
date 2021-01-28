#Maior e o menor peso
maiorpeso = 0
menorpeso = 0
for peso in range(1,6):
    peso_pessoa = float(input('Qual o peso da {} pessoa:'.format(peso)))
    if peso == 1:
        maiorpeso = peso_pessoa
        menorpeso = peso_pessoa
    else:
        if peso_pessoa > maiorpeso:
            maiorpeso = peso_pessoa
        if peso_pessoa < menorpeso:
            menorpeso = peso_pessoa
print('O maior peso lido foi de {} kg'.format(maiorpeso))
print('O menor peso foi de {} kg'.format(menorpeso))