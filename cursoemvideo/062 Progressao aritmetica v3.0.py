#Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. 
# O programa encerrará quando ele disser que quer mostrar 0 termos.

termo1 = int(input('Digite o 1º termo da PA: '))
razao = int(input('Digite a razão da PA: '))
n = 1
while n!= 10:
    an = termo1 + (n - 1) * razao
    n += 1
    print (an, end=' ')








