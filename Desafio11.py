a = float(input("Digite a altura da parede: "))
l = float(input("Digite a largura da parede: "))
area = a*l
print("A área da parede é {} metros".format(area))
print("O rendimento da tinta é 1l/2m2, a quantidade necessária de tinta para pintura é {:.2f} litros".format(area/2))