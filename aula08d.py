#import math
from math import radians, sin, cos, tan
a=float(input('Digite um ângulo, em graus, para saber seu seno, cosseno e tangente: '))
#sen=math.sin(math.radians(a))
#cos=math.cos(math.radians(a))
#ta=math.tan(math.radians(a))
sen=sin(radians(a))
cos=cos(radians(a))
ta=tan(radians(a))
print(' O seno do ângulo {} é: {:.2f}, seu cosseno é: {:.2f} e a tangente é: {:.2f}'.format(a, sen, cos, ta))

