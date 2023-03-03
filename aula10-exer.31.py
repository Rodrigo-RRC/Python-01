distancia = float(input('Qual é a distãncia da viagem em Km que você irá fazer? '))
preço1 = distancia * 0.50
preco2 = distancia * 0.45
if distancia <=220:
    print(' Sua viajem irá custar R$ {:.2f}'.format(preço1))
else:
    print('Sua viagem irá custar R$ {:.2f}'.format(preco2))