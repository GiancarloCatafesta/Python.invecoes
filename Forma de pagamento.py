#Elabore um programa que calcule o valor a ser pago por um produto,considerando o seu Preço normal e Condição de pagamento:
#-á vista Dinheiro/cheque: 10% de desconto
#-á vista no Cartão: 5% de desconto
#-em até 2x no cartão: preço normal
#-3x ou mais no cartão: 20% de juros
produt = float(input('Qual o valor do produto?: '))
pagar = int(input('Qual a forma de pagamento?:'
                  '\n1 - Á vista Dinheiro/Cheque\n'
                  '2 - Á vista no Cartão\n'
                  '3 - 2X no Cartão\n'
                  '4 - 3X ou mais no Cartão\n'))
if pagar == 1:
    pagar = produt - produt * 0.10
    print(f'Terá que pagar R${pagar:.2f}')
elif pagar == 2:
    pagar = produt - produt * 0.05
    print(f'Terá que pagar R${pagar:.2f}')
elif pagar == 3:
    parcela = produt/2
    print(f'Você terá que pagar 2x parcelas de {parcela}, que dá um total de R${produt}')
elif pagar == 4:
    pagar = produt * 0.20 + produt
    parce_produ = int(input('Quantas parcelas deseja pagar?: '))
    parcela = pagar/parce_produ
    print(f'Você terá que pagar {parce_produ}x de parcelas de {parcela}, que irá dar um total de R${pagar:.2f}')
else:
    print('\033[0;35mDigite um valor válido\033[m')