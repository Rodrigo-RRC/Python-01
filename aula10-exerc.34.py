salario = float(input('Qual o valor de seu salário? R$ '))

if salario > 1250:
    aumento = salario * 0.1
else:
    aumento = salario * 0.15

soma = salario + aumento
print('Seu aumento salarial será de : R$ {:.2f}'.format(aumento))
print('Seu novo salário será: R$ {:.2f} mais R$ {:.2f}'.format(salario, aumento))
print('Totalizando: R$ {:.2f}'.format(soma))
print('Parabéns! Você merece!')