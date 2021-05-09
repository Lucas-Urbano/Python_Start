ano = float(input("Digite o ano: "))
print("Verificar se esse ano é bissexto: ")
resultado = ano % 4
if resultado == 0:
    print("O ano informado é bissexto")
else:
    print("O ano informado não é bissexto")