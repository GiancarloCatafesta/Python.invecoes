#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média
nota1 = float(input('Qual foi a nota da primeira prova: '))
nota2 = float(input('Qual a nota da segunda prova: '))
media = (nota1 + nota2)/2
print(f'Você tirou {nota1} e {nota2}, sua média é {media}')
if media >= 6:
    print('Você foi aprovado')
else:
    print('Você está de recuperação')