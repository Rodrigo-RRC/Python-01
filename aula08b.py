#1 from math import trunc
#2 import math
cores = {'azul':'\033[34m',
         'vermelho':'\033[31m',
         'lilas':'\033[35m',
         'limpa':'\033[m'}
n=float(input('Digite um número real qualquer: '))
#1 print(' A parte inteira do número {} é {}'.format(n, trun(n))
#2 print('A parte inteira do número {} é {}'.format(n, math.trunc(n)))

print('A parte inteira do número {}{}{} é {}{}{}'.format(cores['lilas'], n, cores['limpa'],cores['vermelho'], int(n), cores['limpa']))