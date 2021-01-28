#Se forma um triângulo,acrescentando o recurso de mostrar que tipo de triângulo será formado:
#-Equilátero: todos os lados iguais
#-Isósceles:dois lados iguais
#-Escaleno:todos os lados diferentes
l1 = float(input('Digite um valor: '))
l2 = float(input('Digite outro valor: '))
l3 = float(input('Digite mais outro valor: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Ela forma um triangulo')
    if l1 == l2 == l3:
        print('Ele é um triangulo Equilatero')
    elif l1 == l2 != l3 or l1 == l3 != l2 or l2 == l3 != l1:
        print('Ele é um triangulo Isosceles')
    else:
        print('Ele é um triangulo Escaleno')
else:
    print('Ele não forma um triângulo')