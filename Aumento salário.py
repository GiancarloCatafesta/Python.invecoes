#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1.250,00 ,calcule um aumento de 10%
#Para os inferiores ou iguais, o aumento é de 15%
salar = float(input('Qual o seu salário?: '))
if salar <= 1250:
    novosalar = salar * 0.15
    print(f'Você teve um aumento de {novosalar}. Seu novo salário é de {novosalar+salar}')
else:
    novosalar = salar * 0.10
    print(f'Você teve um aumento de {novosalar}. Seu novo salário é de {novosalar+salar}')