#Crie um programa que faça o computador jogar Jokenpô com você
import random
import time
print('Computador. Vamos jogar um jogo\n Ooookk')
computador = ['PEDRA','PAPEL','TESOURA']
esco_comp = random.choice(computador)
computador = esco_comp
jogador = str(input('Escolha: ')).strip().upper()
ordem = 'PEDRA' > 'TESOURA' and 'TESOURA' > 'PAPEL' and 'PAPEL' > 'PEDRA'
time.sleep(1)
print('Jo')
time.sleep(1)
print('Kên')
time.sleep(1)
print('Po')
if jogador == 'PEDRA' and computador == 'TESOURA':
    print(f'Jogador Ganhou. Você jogou {jogador} e o computador jogou {computador}')
elif jogador == 'PAPEL' and computador == 'PEDRA':
    print(f'Jogador Ganhou. Você jogou {jogador} e o computador jogou {computador}')
elif jogador == 'TESOURA' and computador == 'PAPEL':
    print(f'Jogador Ganhou. Você jogou {jogador} e o computador jogou {computador}')
elif computador == 'PEDRA' and jogador == 'TESOURA':
    print(f'Computador Ganhou. Você jogou {jogador} e o computador jogou {computador}')
elif computador == 'PAPEL' and jogador == 'PEDRA':
    print(f'Computador Ganhou. Você jogou {jogador} e o computador jogou {computador}')
elif computador == 'TESOURA' and jogador == 'PAPEL':
    print(f'Computador Ganhou. Você jogou {jogador} e o computador jogou {computador}')
elif computador == jogador:
    print('Empatou.')