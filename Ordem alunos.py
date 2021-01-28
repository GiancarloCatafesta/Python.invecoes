#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
aluns = ['João','Pedro','Juliana','Pipinha','Romeu','Rozé','Dumbo']
seque = random.shuffle(aluns)
print(f'A ordem das apresentações será {aluns}')