nome=input(str('Digite seu nome completo: ')).strip()
print(nome)
print('Seu nome escrito com todas as letras maiúsculas é: {}'.format(nome.upper()))
print('Seu nome escrito em letra minùscula é: {}'.format(nome.lower()))
print("A quantidade de letras de seu nome é: {}".format(len(nome) - nome.count(' ')))
#print('O número de letras de seu primeiro nome é: {}'.format(nome.find(" ")))
listaPrimeiro = nome.split()
print('Seu primeiro nome é {} e possui {} letras'.format(listaPrimeiro[0], len(listaPrimeiro[0])))



