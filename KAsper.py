vetor =[]
for i in range (3):
    print("Digite o" ,i+1, "° coeficiente:")
    w = float(input())
    vetor.append(w)

delta = vetor[1]**2 - 4*vetor[0]*vetor[2]
print("O valor de delta é: ", delta)

x1 = (-vetor[1] - delta**0.5) / (2*vetor[0])
x2 = (-vetor[1] + delta**0.5) / (2*vetor[0])
print("O valor de X1 é: ", x1)
print("O valor de X2 é: ", x2)