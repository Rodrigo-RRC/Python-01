from random import randint
from time import sleep
computador = randint(0, 5) # Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar!')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei de 0 a 5: '))
print('PROCESSANDO....')
sleep(5)
if (computador == jogador):
    print('Parabéns! Você acertou! Me venceu!')
else:
    print('Ganhei!! Pensei no número {} e não no {}'.format(computador, jogador))
