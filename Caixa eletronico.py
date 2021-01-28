#Crie um programa que simule o funcionamento de um caixa eletrônico.
# NO início, pergunte ao usuário qual será o valor a ser sacado (numero inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#OBS: considere que o caixa possui de R$50, R$20, R$10 e R$1.
print('='*30)
print('Bem Vindo ao Banco 123')
print('='*30)
conta = 1500
sacar = int(input('Quanto deseja sacar ? R$'))
total = sacar
ced = 50
total_ced = 0
while True:
    if total >= ced:
        total -= ced
        total_ced += 1
    else:
        if total_ced > 0:
            print(f'Total de {total_ced} notas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        total_ced = 0
        if total == 0:
            break
print('='*30)
print('Obrigado por usar o Banco 123')