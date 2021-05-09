import random
A1 = input('Digite o nome do perimeiro aluno: ')
A2 = input('Digite o nome do segundo aluno: ')
A3 = input('Digite o nome do terceiro aluno: ')
A4 = input('Digite o nome do quarto aluno: ')
lista = [A1, A2, A3, A4]
Sorteado = random.choice(lista)
print('O aluno escolhido é {}'.format(Sorteado))

'''from random import choice
A1 = input('Digite o nome do perimeiro aluno: ')
A2 = input('Digite o nome do segundo aluno: ')
A3 = input('Digite o nome do terceiro aluno: ')
A4 = input('Digite o nome do quarto aluno: ')
lista = [A1, A2, A3, A4]
Sorteado = choice(lista)
print('O aluno escolhido é {}'.format(Sorteado)'''