print('Quer saber quantos litros de tinta vais gastar para pintar sua parede?\nEntão digite abaixo o que se pede!')
largura=float(input('Digite a largura de sua parede em metros: '))
altura=float(input('Digite a altura em metros de sua parede: '))
area=largura*altura
tinta=area/2
print('A área de sua parede mede: {:.2f} m² e a quantidade de tinta utilizada será: {:.2f}litros'.format(area, tinta))

