a = float(input("Informe o salário atual do colaborador (R$): "))
b = float(input("Informe a porcentagem de aumento (%): "))
print("O salário atual do colaborador é R$ {}, com o reajuste de {}%, ficará e R${:.2f}".format(a, b, a+(a*b/100)))
