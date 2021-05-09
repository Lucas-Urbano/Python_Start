from random import choice
lista = [0, 1, 2, 3, 4, 5]
pc = choice(lista)
print("O computador pensou em um número, tentei descobrir.")
user = int(input("Digite um número: "))
if pc == user:
    print("Parabéns você acertou !!")
else:
    print('O computador ganhou !!')