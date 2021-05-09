'''co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adjacente: "))
h = (ca**2 + co**2)**(1/2)
print("O valor da hipotenusa é {:.4f}".format(h))'''


from math import hypot, ceil
co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adjacente: "))
h = hypot(co, ca)
print('A hipotenusa vai medir: {} '.format(ceil(h)))

