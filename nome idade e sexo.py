#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
total = media = mulher_menos_vinte = homem_velho = mais_velho = 0
for dados in range(1,5):
    print('='*20)
    nome = str(input(f'Qual o nome da {dados}ª: '))
    idade = int(input(f'Qual a idade da {dados}ª pessoa: '))
    sexo = str(input(f'Qual a sexo: M/F: ')).upper()
    print('x'*20)
    total += idade
    media = total / 4
    if sexo == 'F' and idade < 18:
        mulher_menos_vinte += 1
    if sexo in 'M' and dados == 1:
        mais_velho = idade
        homem_velho = nome
    if sexo in 'M' and idade > mais_velho:
        mais_velho = idade
        homem_velho = nome

print(f'A média de idade do grupo é de {media}')
print(f'Tem {mulher_menos_vinte} menor(es) de idade')
print(f'O homem mais velho se chama {homem_velho} e tem {mais_velho}')
