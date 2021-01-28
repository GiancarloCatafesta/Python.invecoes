#Jogo de Par ou Impar
from random import randint
print('Jogo de Par ou Impar')
jogador = jogador1 = computador = vitorias = total = parimpar = 0
while jogador == parimpar:
    jogador = str(input('Escolha entre Impar[I] ou Par[P]:')).strip().upper()[0]
    if jogador not in 'IiPp':
        while True:
            jogador = str(input('Escolha entre Impar[I] ou Par[P]:')).strip().upper()[0]
            if jogador in 'IP':
                break
    jogador1 = int(input('Digite um numero: '))
    computador = randint(1,100)
    print(f'Computador digitou {computador}')
    total = jogador1 + computador
    print(f'O total disso foi {total}. Deu Par'if total % 2 == 0 else 'Deu Impar')
    if total % 2 == 0:
        parimpar = 'P'
    else:
        parimpar = 'I'
    if jogador == parimpar:
        print('Jogador Venceu')
    if jogador != parimpar:
        break
    vitorias += 1

print('Você perdeu. Game Over')
print(f'O jogador venceu {vitorias} vezes o computador ')