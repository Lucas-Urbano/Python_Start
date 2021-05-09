p1 = float(input("Digite o preço do produto: R$ "))
p2 = p1-(p1*5/100)
print("Preço do produto sem desconto: R$ {} \n"
      "Produto com desconto de 5%: R$ {:.2f}".format(p1, p2))