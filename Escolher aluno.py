#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.
import random
alun = ['João','Pedro','Juliana','Pipinha']
esco = random.choice(alun)
print(f'O aluno escolhido foi {esco}')