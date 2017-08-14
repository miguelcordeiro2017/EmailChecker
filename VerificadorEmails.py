# Desenvolvido por: scr1pter

from time import sleep
from sys import exit

print('-'*10 ,'Verificador de Emails 1.0', '-'*10)
print()

email = str(input('Insira o seu email -> '))
print()

print('Verificando Email...')
sleep(2)

caracteres_invalidos = ['|', '!', '"', '#', '£', '$', '%', '&', '/', '{', '(', '[', ')', ']', '=', '}', '?', '«', '»', '*', '+', '¨', '`', '´', 'ª', 'º', '^', '~', ';', ',', ':', '..', '__', '--']

# verificar se a string email têm mais de 35 caracteres
if len(email) >= 35:
    print()
    print('-' * 16, 'Email Inválido', '-' * 15)
    sleep(3)
    exit()
else:
    print('25% Completo!')
    sleep(2)

# verificar se existe algum @ dentro da string email
if not '@' in  email:
    print()
    print('-' * 16, 'Email Inválido', '-' * 15)
    sleep(3)
    exit()
else:
    print('50% Completo!')
    sleep(2)

# verificar se cada caracter esta dentro da string email
for i in range(len(caracteres_invalidos)):
    if caracteres_invalidos[i] in email:
        print()
        print('-' * 16, 'Email Inválido', '-' * 15)
        sleep(3)
        exit()
print('75% Completo!')
sleep(2)

# verificar se existe algum espaço na string email
if ' ' in email:
    print()
    print('-'*16, 'Email Inválido', '-'*15)
    sleep(3)
    exit()
else:
    print('100% Completo!')
    sleep(2)

print()
print('-'*17 ,'Email Válido', '-'*16)
sleep(3)