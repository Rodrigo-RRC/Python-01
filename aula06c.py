n=input('Digite algo:')
print('O tipo primitivo do valor digitado é: ',type(n))
print('Só tem espaços?',n.isspace())
print('É um número?',n.isnumeric())
print('É alfabético?', n.isalpha())
print('É alfanumérico?', n.isalnum())
print('Está em maiúsculas?',n.isupper())
print('Esta em minúsculas?',n.islower())
print('Esta capitalizada (Minúsculas e Maiúsculas)?', n.istitle())
# a = Objeto - Todo o objeto tem características e realiza funcionalidades.
#Ou seja,tem atributos e métodos.
# o .is""""() = métodos ( Todo objeto string tem estes métodos)