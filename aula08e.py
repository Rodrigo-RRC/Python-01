#import random
from random import choice
a1=str(input('Digite o nome do aluno 1: '))
a2=str(input('Digite o nome do aluno 2: ' ))
a3=str(input('Digite o nome do aluno 3: '))
a4=str(input('Digite o nome do aluno 4: '))
lista=[a1, a2, a3, a4]
#escolhido=random.choice(lista)
escolhido=choice(lista)
print("O(A) aluno(a) escolhido(a) é {} ".format(escolhido))
#random choice=escolha aleatória