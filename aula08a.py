#import math
from math import sqrt
n=int(input('Digite um número: '))
cores = {'limpa': '\033[m',
         'verde':'\033[4;32m',
         'amarelo':'\033[4;33m',
         'pretoebranco': '\033[7;30m'}
#raiz=math.sqrt(n)
raiz=sqrt(n)
print('A {}raiz quadrada{} de {} é igual a {}'.format(cores['pretoebranco'], cores['limpa'],n, raiz))
#print('A raiz quadrada de {} é igual a {:.4f}'.format(n, raiz))