#Desenvolva uma lógica que leia o peso e a altura de uma pessoa,calcule seu IMC e mostre seu status,
#de acordo com a tabela abaixo:
#-Abaixo de 18.5:Abaixo do Peso
#-Entre 18.5 e 25:Peso ideial
#-25 até 30:Sobrepeso
#-30 até 40:Obesidade mórbida
peso = float(input('Qual o seu peso?: '))
altura = float(input('Qual a sua altura?: '))
imc = peso / (altura * altura)
print(f'Seu IMC é {imc:.2f}')
if imc < 18.5:
    print('Está Abaixo do Peso')
elif imc >= 18.5 and imc < 25:
    print('Seu Peso está ideal')
elif imc >= 25 and imc < 30:
    print('Está com Sobrepeso. Se cuide')
elif imc >= 30 and imc < 40:
    print('Está com Obesidade Morbida. Procure um médico')