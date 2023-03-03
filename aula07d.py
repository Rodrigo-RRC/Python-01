n=int(input('Digite um número inteiro ao lado: '))
#d=2*n
#t=3*n
#r2=n**(1/2)
#print('Considerando o número digitado {}, \nTemos que o dobro deste número é {}, \nO triplo é: {} \nE a raiz quadrada aproximada é {:.3f}'.format(n, d, t, r2))


# (1) Outra forma
#print('Considerando o número digitado {}.\nTemos que seu dobro vale: {}\nSeu triplo vale: {}\nE sua raiz quadrada aproximada é: {:.3f}'.format(n, n*2, n*3, n**(1/2)))

# (2) Outra forma
print('Considerando o número digitado {}.\nTemos que seu dobro vale; {}\nSeu triplo vale: {}\nE sua raiz quadrada aproximada é: {:.3f}'.format(n, n*2, n*3, pow(n,(1/2))))