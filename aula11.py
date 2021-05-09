print('\033[0;31;42mOlá Mundo ')
print('\033[4;30;45mOlá Mundo\033[m ')
print('\033[7;34mOlá Mundo\033[m ')

nome = input('Digite seu primeiro nome: ')
meio = input('Digite o sobrenome do meio: ')
sobrenome = input('Digite seu sobrenome: ')
print('Seu nome completo é \033[1;31;40m{}\033[m \033[4;32;41m{}\033[m \033[7;34;45m{}\033[m'.format(nome, meio, sobrenome))
print('Olá, prazer em te conhecer {}{}{} !!!'.format('\033[4;34m', nome, '\033[m'))