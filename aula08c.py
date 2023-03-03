#from math import sqrt
#from math import pow
#import math
from math import hypot
cat1=float(input('Digite o Cateto Oposto do triângulo: '))
cat2=float(input('Digite o Cateto Adjascente do triângulo: '))
hip=hypot(cat1, cat2)
#hip=math.hypot(cat1,cat2)
#hip=sqrt((cat1**2)+(cat2**2))
#hip=sqrt((pow(cat1,2))+pow(cat2,2))
print("A hipotenusa do triângulo retângulo é: {:.2f} ".format(hip))
