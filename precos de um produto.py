#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.
print('='*20)
print('Lojas Pipinha')
print('='*20)
preco = total = maismil = mais_barato = cont = 0
nome_barato = ''
while True:
    prod = str(input('Qual o produto?: '))
    preco = float(input('Qual seu preço?: '))
    total += preco
    cont += 1
    if preco >= 1000:
        maismil += 1
    if cont == 1: #or preco < mais_barato:
        nome_barato = prod
        mais_barato = preco
    else:
        if preco < mais_barato:
            mais_barato = preco #Essa opção é igual a condição de cima. Pode ser simplificada
            nome_barato = prod
    sim_nao = str(input('Deseja continuar? Sim[S]/Não[N]: ')).strip().upper()[0]
    while not sim_nao in 'SN':
        sim_nao = str(input('Deseja continuar ? Sim[S]/Não[N]: ')).strip().upper()[0]
        if sim_nao == 'N':
            break
    if sim_nao == 'N':
        break
print(f'O total gasto foi de R${total}')
print(f'Tem {maismil} produtos com mais de R$ 1000')
print(f'O produto mais barato foi {nome_barato} e custou {mais_barato}')
