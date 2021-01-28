# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'
cidade = str(input('Digite o nome da cidade: ')).upper().split()
if 'SANTO' in cidade[0]:
    print('Tem Santo nessa cidade')
else:
    print('Essa cidade está perdida')