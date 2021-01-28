#Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com a sua idade:
#-Se ele Ainda vai se alistar ao serviço militar
#-Se é a Hora de se alistar
#-Se já passou do tempo de alistamento
from datetime import date
ano_atual = date.today().year
nasc = int(input('Ano de nascimento:'))
sexo = str(input('Qual seu sexo? [M/F]:')).upper()
idade = ano_atual - nasc
if sexo == 'M':
    if idade < 18:
        print(f'Você ainda não tem idade {idade}. Falta {18 - idade} para poder se alistar')
        saldo = 18 - idade
        ano = ano_atual + saldo
        print(f'Seu alistamento será em {ano}')
    elif idade == 18:
        print('Você já pode se alistar')
    else:
        print(f'Você já passou da idade de alistamento em {idade - 18} anos. Está preso')
        saldo = idade - 18
        ano = ano_atual - saldo
        print(f'Seu alistamento foi em {ano}')
elif sexo == 'F':
    print('Você não precisa se alistar obrigatoriamente')
else:
    print('Digite um valor valido')
