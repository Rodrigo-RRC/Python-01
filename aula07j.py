print('Quer saber o valor do produto se você pagar a vista em dinheiro?\nEntão digite o valor abaixo!')
preço=float(input('Qual o valor do produto desejado:R$ '))
desconto=0.95*preço
print('O valor do produto com deconto é: R$ {:.2f}'.format(desconto))
