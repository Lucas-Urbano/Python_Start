sal = int(input("Digite o salário do colaborador: "))
print("O salário informado é: {}".format(sal))
if sal > 1250.00:
    aumento = float(sal+(sal*10/100))
    print("O salário com reajuste de 10% ficará em: {}".format(aumento))
if sal <= 1250.00:
    aumento = float(sal+(sal*15/100))
    print(" O salário com reajuste de 15% ficará em: {}".format(aumento))
print("End")


