#Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5
# e paça para o usuário tentar descobrir qual foi o número escolhido pelo computador
#O programa deverá escrever na tela se o usuário venceu ou perdeu.
computador = jogador = cont = 0
while True:
    import random
    import playsound
    print('Computador. Pense em um número.\nOk vou pensar.')
    computador = random.randint(1,10)
    jogad = int(input('Digite um valor de 1 a 10: '))
    cont += 1
    if jogad == computador:
        print(f'O computador pensou em {computador}. Você acertou ')
        if cont == 1: #Se acertar de primeira, tocar musica
            playsound.playsound('UltraInstinct.mp3')
        break
    else:
        print(f'O computador pensou em {computador}. Você errooou')