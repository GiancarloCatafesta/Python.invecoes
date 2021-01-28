#Calcule qual o maior e o menor da media
media = total = soma = maior_num = menor_num = 0
sim_nao = 'S'
while sim_nao == 'S':
    num = int(input('Digite um numero: '))
    sim_nao = str(input('Deseja continuar digitando? Sim[S]/Não[N]: ')).upper()
    total += 1
    soma += num
    media = soma/total
    if total == 1:
        maior_num = menor_num = num
    else:
        if num > maior_num:
            maior_num = num
        if num < menor_num:
            menor_num = num
print(f'Foram digitados {total} termos \nA média deles deu {media}.\nO maior numero foi {maior_num} e o menor foi {menor_num}')
