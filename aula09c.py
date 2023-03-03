num = int(input('Escreva um número: '))
n = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analisando o número: {} '.format(num))
print('O número que representa a unidade é: {}'.format(n))
print('O número que representa a dezena é: {}'.format(d))
print('O número que representa a centena é: {}'.format(c))
print('O número que represnta o milhar é: {} '.format(m))