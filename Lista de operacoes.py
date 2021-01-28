from random import randint
n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero: '))
esco = 0
while esco < 5:
    print('[1]Somar\n'
          '[2]Multiplicar\n'
          '[3]Maior\n'
          '[4]Novos numeros\n'
          '[5]Sair do programa')
    esco = int(input('Escolha uma operação a ser realizada:'))
    if esco == 1:
        soma = n1 + n2
        print(f'A soma dos dois numeros é {soma}')
    elif esco == 2:
        multi = n1 * n2
        print(f'A multiplicação dos dois numeros dá {multi}')
    elif esco == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
        else:
            print(f'{n2} é maior que {n1}')
    elif esco == 4:
        opcao = str(input('Deseja digitar manualmente os valores: Sim[S]/Não[N]:')).upper()
        if opcao == 'S':
            n1 = float(input('Digite um novo valor:'))
            n2 = float(input('Digite um novo valor:'))
            print(n1)
            print(n2)
        else:
            n1 = randint(1,100)
            n2 = randint(1,100)
            print(n1)
            print(n2)
print('Fim')
