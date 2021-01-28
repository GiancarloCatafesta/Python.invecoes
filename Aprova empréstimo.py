#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#O programa vai perguntar o Valor da casa, o Salário do comprador e em Quantos anos ele vai pagar
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado
print('\033[7;31;40mEmpréstimo Bancário\033[m')
valor_casa = float(input('Qual o valor da casa que quer comprar ?: '))
seu_salário = float(input('Qual o seu salário ?: '))
anos_pagar = int(input('Em quantos anos pretende pagar?: '))
prestacao_mensal = valor_casa/(anos_pagar*12)
emprestimo = seu_salário*0.30
print(f'Sua prestação é de {prestacao_mensal:.2f}')
if prestacao_mensal <= emprestimo:
    print('Você conseguiu o empréstimo')
else:
    print('A sua renda é insuficiente para uma prestação')'''