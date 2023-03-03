frase='Curso em vídeo Python'
# 21 caracteres ( Do zero ao 20).

#Fatiamento:

#frase[9]
#frase[9:13]#Pega do 9 ao 12 (exclui o 13. Caso queira pegar o "O", também, teria que colocar [9:14];
#frase[9:21]# Pega até o caractes 20.
#frase[9:21:2]# Pega até o caracter 20, pulando de 2 em 2.
#frase[:5]# Quando omito o início, começará do caracter 0;
#frase[15:]# Quando omito depois de :, pego do 15 até o final, ou seja, caratcter 20;
#frase[9::3]#Começa no caracter 9 e vai até o final pulando de 3 em 3;

#Análise

#Função len (comprimento) - Saber quantos caracteres;
#Função frase.cont() - Saber quantos caracteres existem de um mesmo tipo
#Exemplo: frase.cont("o") - Retorna o número de "o" existe na string do início ao fima da mesma;
#frase.cont('o',0,13)
#Faço uma contagem da letra 'o' já com o fatiamento (0 ao 12).
#frase.find('deo')
#Acho qual posição começa a palavra 'deo', ou seja, na posição 11.

#Transformação

#frase.replace() - Troca a primeira palavra pela segunda.
#frase.upper() - Troca as minúsculas por maiúsculas
#frase.lower() - Transforma as maiúsculas em minusculas
#frase.capitalize() - Joga os caracteres para minusculo exceto o primeiro caractere
#frase.title() - Todas as primeiras letras de cada palavra ficam maiúsculas
#frase.strip() - Elimina os espaços antes e depois da string
#frase.rstrip() - Elimina os espaços a direita
#frase.lstrip() - Elimina os espaços a esquerda

#Divisão

#frase.split() - Gera uma lista com todas as palvras de uma cadeia de caracteres
##Palavra 0 = Curso; Palavra 1= em, Palavra 2 = Video, Palavra 4 = Pytnhon

#Junção

#'-'.join(frase) = Junta as palavras de uma string e coloca os  tracinhos entre elas ou outro caracter entre aspas.


#-----------------------------------------------------------------------------------

frase='Curso em vídeo Python'
#frase='   Aprenda Python   '
print(len(frase))
print(frase.count('o'))
#print(frase.count('o',0,13))
print(frase.count('o',0,15))
#print(frase.find('deo'))
print(frase.find('deo'))
print(frase.find('Android')) # -1 significa que não foi encontrado.
print('Curso'in frase) # Para saber se a palavra existe na frase
print(frase.replace('Python','Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())
print('-'.join(frase))
print(''.join(frase))