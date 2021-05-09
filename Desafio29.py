v = int(input("Dgite a velocidade medida: "))
if v > 80:
    print("Excesso de velocidade, você será multado !!")
    multa = float(v - 80)*7
    print("O valor da multa é: R${:.2f}".format(multa))
else:
    print("Velocidade dentro do limite, obrigado por respeitar a velocidade.")
