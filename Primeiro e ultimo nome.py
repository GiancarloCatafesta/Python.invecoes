# Faça um programa que leia o nome completo de uma pessoa,mostrando em seguida o primeiro e o último nome separadamente
# Ex: Ana Maria de Souza
# primeiro = Ana
# ultimo = Souza
nome = str(input('Digite o nome completo: ')).split()
first = nome[0]
last = nome[-1]
print(f'O primeiro nome é {first} e o ultimo é {last}')