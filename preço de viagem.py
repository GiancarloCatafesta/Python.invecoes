#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
kmrodado = float(input('DIgite quantos km foram percorridos: '))
diaspercorrids = int(input('Quantos dias ele foi alugado: '))
pagarkm = kmrodado * 0.15
pagardias = diaspercorrids * 60
total = pagarkm + pagardias
print(f'Você percorreu {kmrodado} km em {diaspercorrids} dias. Você deverá pagar R${pagarkm} pelos quilometros percorridos e R${pagardias} pelos dias de uso, que dá um total de R${total}')
