
velocidade = float(input('A velocidade conferida no pardal foi de:'))
velocidadeMáxima = 80
multa = (velocidade - velocidadeMáxima) * 7.00
if (velocidade > 80):
    print('A velocidade máxima permitida é de {:.2f} Km/h e a sua velocidade registrada foi de {:.2f} Km/h. '.format(velocidadeMáxima, velocidade))
    multa = (velocidade - velocidadeMáxima) * 7.00
    print('Por isso irá pagar uma multa de R${:.2f}'.format(multa))
else:
    print('Parabéns! Você não foi multado.Tenha um bom dia!')