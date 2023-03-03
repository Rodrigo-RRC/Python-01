print('Quer saber o valor em dólar que você tem na carteira incluindo cédulas e moedas?')
d=float(input('Então conte o valor e digite-o ao lado: R$  '))
# print("O valor R$ {} vale em dólar: U$ {}".format(d, d/4))

# Outra forma
conv=d/4
print('O valor de R$ {:.2f} em dólar é: U$ {:.2f}'.format(d, conv))