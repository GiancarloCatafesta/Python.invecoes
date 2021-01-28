#Identificar quantos homens mais novos,quem tem mais de 18 anos e as mulheres com menos de 20
mais18 = homens = menos_de_20 = 0
cont = 1
while True:
    print(f'{cont}ª pessoa')
    print('='*25)
    sexo = str(input(f'Qual o sexo do {cont}º pessoa? Masculino[M]/Feminino[F]:')).strip().upper()[0]
    idade = int(input(f'Qual a idade da {cont}ª pessoa?:'))
    print('='*25)
    if sexo == 'M':
        homens += 1
    if idade >= 18:
        mais18 += 1
    if sexo == 'F' and idade < 20:
        menos_de_20 += 1
    sim_nao = ''
    sim_nao = str(input('Deseja continuar ?Sim[S]/Não[N]:')).strip().upper()[0]
    while sim_nao not in 'SN':
        sim_nao = str(input('Deseja continuar ?Sim[S]/Não[N]:')).strip().upper()[0]
    if sim_nao == 'N':
        break
    cont += 1
print('Fim')
print(f'Tem {homens} pessoas que são homens')
print(f'{mais18} tem mais de 18 anos')
print(f'{menos_de_20} mulheres tem menos de 20 anos')