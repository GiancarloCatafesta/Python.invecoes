#Desconto maior de 250 gasto
cont = 0
while True:
    produt = str(input('Qual o nome do produto:'))
    valor = float(input('Qual o valor do produto: '))
    continua = str(input('Deseja continuar? [S/N]:')).upper()
    cont += valor
    if continua == 'N':
        break
    while continua != 'S':
        continua = str(input('Deseja continuar? [S/N]:')).upper()
print(f'O total gasto foi {cont:.2f}')
if cont > 250:
    desc = cont * 0.20
    final = cont - desc
    print(f'E pelo valor ser de {cont:.2f} maior que R$100 você recebeu um desconto de 20%. Você irá pagar {final:.2f}')'''