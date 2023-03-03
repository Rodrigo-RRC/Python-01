km=float(input('Qual a quantidade em Km que você percorreu com o carro? '))
d=int(input('Quantos dias você ficou com o carro? '))
p=(60*d) + (0.15*km)
print('O preço total que você irá pagar será de R$ {:.2f}'.format(p))
