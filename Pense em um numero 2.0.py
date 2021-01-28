#Adivinhar um numero
num = 1
from random import randint
sim_nao = str(input('Vamos jogar um joga humano?Sim[S]/Não[N]: ')).upper()
computador = randint(1,11)
if sim_nao == 'N':
    print('Talvez outra hora né ')
else:
    jogador = int(input('Ok. Pense em um numero de 1 até 10: '))
    while jogador != computador:
        print('Você errou. Tente novamente')
        jogador = int(input('Pense novamente: '))
        num += 1
    if jogador == computador:
        print('Computador jogou Você ganhou')
        if num == 1:
            print('Você acertou de primeira ')
        else:
            print(f'Você precisou de {num} vez para acertar')