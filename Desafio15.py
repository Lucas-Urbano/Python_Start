dias = float(input("Quantos dias foi utilizado ? "))
km = float(input("Quantos km foi utilizado ? "))
diaria = 60
precokm = 0.15
print("Locação do carro {} dias, Valor da diária {} \nKilometragem rodada {}, Preço por kilometro rodado {}".format(dias, diaria, km, precokm))
print("Total de diárias R$ {:.2f}, Total de kilometragem rodada R$ {:.2f}, \nTotal geral R$ {:.2f}".format(diaria*dias, km*precokm, (diaria*dias+km*precokm)))