d = float(input("Digite a distância da viagem: "))
print("Distância: {}".format(d))
if d <= 200:
    print("Preço R$ 0,55 o kilômetro")
    preço = d * 0.55
    print("O preço da viagem ficou em: {}".format(float(preço)))
else:
    print("Preço: R$ 0.45 o kilômetro")
    preço = d * 0.45
    print("O preço da viagem ficou em: {}".format(float(preço)))
